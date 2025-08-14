# Datenordner

Dieser Ordner enthält die Datengrundlage der Analyse. Die Struktur trennt Rohdaten, Verweise auf Mediendateien, aufbereitete Analysedatensätze, Ergebnisdaten und Human-Evaluation-Daten, damit die Datenaufbereitung nachvollziehbar bleibt.

Hinweis: Die eigentlichen Video- und Frame-Dateien sind aufgrund ihrer Dateigröße nicht im GitHub-Repository enthalten. Sie liegen auf dem beigefügten Datenträger. Im Repository verbleiben die Metadaten, Datensätze, Auswertungsergebnisse und Notebooks, über die die Medien eindeutig zugeordnet und die Analysen nachvollzogen werden können.

## Ordnerstruktur

| Pfad | Inhalt |
| --- | --- |
| `01_raw/` | Ursprüngliche Metadaten der TikTok-Videos und -Kommentare. |
| `01_raw/videos_metadata/` | Beschreibende Video-Metadaten, z. B. ID, Autorin, Caption, Zeitpunkt, Engagement-Metriken, URLs, Video- und Frame-Verfügbarkeit. |
| `01_raw/comments_metadata/` | Rohdaten der Kommentar-Metadaten. |
| `02_media/` | Ablageort der Videodateien und extrahierten Frames auf dem beigefügten Datenträger. Im GitHub-Repository sind diese großen Mediendateien nicht enthalten. |
| `02_media/ai_videos_2025/` | Videos und Frames der virtuellen Influencerinnen auf dem Datenträger. |
| `02_media/real_videos_2025/` | Videos und Frames der menschlichen Influencerinnen auf dem Datenträger. |
| `02_media/stratified_sample/` | Videos und Frames des finalen stratifizierten Samples auf dem Datenträger. |
| `03_datasets/` | Aufbereitete Analysedatensätze. |
| `03_datasets/influencer_balanced/` | Influencer-balanciertes Sample mit 500 Videos sowie zugehöriger Sampling-Logdatei und Kommentardaten. |
| `04_analysis_results/` | Zusammengeführte Analyseergebnisse, u. a. visuelle Merkmale und Human-Evaluation-Auswertungen. |
| `05_notebooks/` | Notebooks zur Datenaufbereitung, Stichprobenziehung, Analyse und Human-Evaluation-Auswertung. |
| `06_human_evaluation_reannotation/` | Rohdaten der manuellen Reannotation für die Human Evaluation. |

## Zuordnung von Videos, Frames und Metadaten

Die Videodateien in `02_media/**/videos/` und die Frame-Ordner in `02_media/**/frames/` liegen auf dem beigefügten Datenträger. Sie sind über die jeweilige TikTok-Video-ID benannt. Diese ID entspricht der Spalte `video_id` in den aufbereiteten Metadaten bzw. der Spalte `id` in den ursprünglichen AI- und Real-Rohdateien.

Für die Beschreibung der Medien werden folgende Metadatenquellen verwendet:

| Datei | Verwendung |
| --- | --- |
| `01_raw/videos_metadata/01_AI_TIKTOK_VIDEOS_DATASET_2025.csv` | Roh-Metadaten der AI-Videos. |
| `01_raw/videos_metadata/01_REAL_TIKTOK_VIDEOS_DATASET_2025.csv` | Roh-Metadaten der Real-Videos. |
| `01_raw/videos_metadata/01_AI_AND_REAL_TIKTOK_VIDEOS_DATASET_2025.csv` | Zusammengeführte und vereinheitlichte Video-Metadaten für AI und Real. |
| `03_datasets/influencer_balanced/01_AI_AND_REAL_TIKTOK_VIDEOS_stratified_per_influencer_50.csv` | Finale Metadaten des stratifizierten Analysesamples mit 500 Videos. |
| `03_datasets/influencer_balanced/01_AI_AND_REAL_TIKTOK_VIDEOS_stratified_per_influencer_50_LOG.csv` | Dokumentation der Stichprobenziehung pro Influencerin. |
| `03_datasets/influencer_balanced/02_AI_AND_REAL_TIKTOK_COMMENTS_FOR_STRATIFIED_VIDEOS.csv` | Kommentare zu den Videos des stratifizierten Samples. |

## Hinweis zur Ablage

Die beschreibenden Metadaten bleiben im Rohdaten- bzw. Datensatzordner und werden nicht zusätzlich nach `02_media/` kopiert. Dadurch gibt es eine eindeutige Quelle pro Datenstand. Die Verbindung zu den Medien auf dem Datenträger ist über die Video-ID reproduzierbar.

Für das finale Analysesample ist insbesondere die Datei `03_datasets/influencer_balanced/01_AI_AND_REAL_TIKTOK_VIDEOS_stratified_per_influencer_50.csv` relevant, da sie genau die 500 Videos beschreibt, die auf dem Datenträger im Ordner `02_media/stratified_sample/` als Videos und Frames vorliegen.
