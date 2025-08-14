from pathlib import Path
import numpy as np
import pandas as pd
import cv2
from tqdm import tqdm


# -------------------------------
# Configuration
# -------------------------------
DATA_DIR = Path('../../data')

COMBINED_CSV = DATA_DIR / '03_datasets/influencer_balanced/01_AI_AND_REAL_TIKTOK_VIDEOS_stratified_per_influencer_50.csv'
OUTPUT_CSV = DATA_DIR / '04_analysis_results' / 'visual_features' / '09_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_beauty_scoring.csv'
FRAME_ROOT = DATA_DIR / '02_media/stratified_sample/frames'
SOURCE_FILTER = None
DEFAULT_MAX_FRAMES_PER_VIDEO = 60

MODEL_PROTOTXT = Path(__file__).with_name('resnext50_deploy.prototxt')
MODEL_WEIGHTS = Path(__file__).with_name('resnext50.caffemodel')
INPUT_SIZE = 224
MEAN_BGR = np.array([104.0, 117.0, 123.0], dtype=np.float32)


if not MODEL_PROTOTXT.exists() or not MODEL_WEIGHTS.exists():
    raise FileNotFoundError('Missing model files: resnext50_deploy.prototxt / resnext50.caffemodel')


def load_data() -> pd.DataFrame:
    df = pd.read_csv(COMBINED_CSV)
    if 'influencer_type' not in df.columns and 'source' in df.columns:
        df['influencer_type'] = df['source']
    return df


def get_video_id(row, video_id_col: str) -> str:
    value = row.get(video_id_col, None)
    if pd.isna(value):
        return ''
    return str(value)


def get_duration_seconds(row):
    for col in ('video_duration_seconds', 'duration_seconds', 'duration', 'video_duration'):
        if col in row.index:
            value = row.get(col, np.nan)
            if pd.notna(value):
                return value
    return np.nan


def has_frames(video_id: str) -> bool:
    return (FRAME_ROOT / video_id).is_dir()


def sample_frame_paths(video_id: str, duration_seconds=None, default_max_frames: int = DEFAULT_MAX_FRAMES_PER_VIDEO):
    folder = FRAME_ROOT / video_id
    if not folder.is_dir():
        return []

    frame_files = sorted(folder.glob('*.jpeg'))
    if not frame_files:
        frame_files = sorted(folder.glob('*.jpg'))
    if not frame_files:
        frame_files = sorted(folder.glob('*.png'))
    if not frame_files:
        return []

    try:
        duration_value = float(duration_seconds)
    except (TypeError, ValueError):
        duration_value = np.nan

    if pd.notna(duration_value) and duration_value > 0:
        target_frames = int(np.ceil(duration_value))
    else:
        target_frames = default_max_frames

    target_frames = max(1, min(target_frames, len(frame_files)))
    step = max(1, len(frame_files) // target_frames)
    return frame_files[::step][:target_frames]


def preprocess_bgr(img_bgr: np.ndarray):
    img = cv2.resize(img_bgr, (INPUT_SIZE, INPUT_SIZE), interpolation=cv2.INTER_AREA).astype(np.float32)
    img -= MEAN_BGR
    blob = np.transpose(img, (2, 0, 1))[np.newaxis, ...]
    return blob


def load_net():
    net = cv2.dnn.readNetFromCaffe(str(MODEL_PROTOTXT), str(MODEL_WEIGHTS))
    return net


def predict_beauty_score(img_bgr: np.ndarray, net):
    blob = preprocess_bgr(img_bgr)
    net.setInput(blob)
    out = net.forward()
    return float(np.mean(out))


def crop_largest_face_bgr(img_bgr: np.ndarray, haar, margin: float = 0.2):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    if len(faces) == 0:
        return None

    areas = [(w * h) for (_, _, w, h) in faces]
    idx = int(np.argmax(areas))
    x, y, w, h = faces[idx]

    H, W = img_bgr.shape[:2]
    xm = max(0, int(x - margin * w))
    ym = max(0, int(y - margin * h))
    x2m = min(W, int(x + w + margin * w))
    y2m = min(H, int(y + h + margin * h))

    crop = img_bgr[ym:y2m, xm:x2m]
    return crop if crop.size else None


def main():
    df = load_data()

    if SOURCE_FILTER:
        df = df[df['influencer_type'].isin(SOURCE_FILTER)].copy()

    video_id_col = 'video_id' if 'video_id' in df.columns else 'id'

    video_ids = df[video_id_col].astype(str)
    df['has_frames'] = [has_frames(video_id) for video_id in video_ids]
    df = df[df['has_frames']].reset_index(drop=True)

    haar = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    net = load_net()

    beauty_score_mean = []
    beauty_score_std = []
    detected_face_frames = []

    for _, row in tqdm(df.iterrows(), total=len(df), desc='Processing videos'):
        vid = get_video_id(row, video_id_col)
        duration_seconds = get_duration_seconds(row)
        frame_paths = sample_frame_paths(vid, duration_seconds=duration_seconds)

        scores = []
        faces_seen = 0

        for fp in frame_paths:
            img = cv2.imread(str(fp))
            if img is None:
                continue

            face = crop_largest_face_bgr(img, haar=haar, margin=0.2)
            if face is None:
                continue

            faces_seen += 1
            try:
                score = predict_beauty_score(face, net)
                scores.append(score)
            except Exception:
                continue

        if scores:
            beauty_score_mean.append(float(np.mean(scores)))
            beauty_score_std.append(float(np.std(scores)))
        else:
            beauty_score_mean.append(np.nan)
            beauty_score_std.append(np.nan)

        detected_face_frames.append(int(faces_seen))

    df['beauty_score_mean'] = beauty_score_mean
    df['beauty_score_std'] = beauty_score_std
    df['beauty_detected_face_frames'] = detected_face_frames

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f'Saved: {OUTPUT_CSV}')


if __name__ == '__main__':
    main()
