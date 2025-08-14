# Gesamtbericht: Modell-Ergebnisse, statistische Tests und menschliche Evaluation

Der Bericht bündelt die finalen Ergebnisdateien, die Comparison-Notebooks und die menschliche Evaluation.

## 0. Eckdaten

| Kennzahl | Wert |
|---|---:|
| Final statistisch ausgewertete Modell-/Ergebniskategorien | 19 |
| davon Video-Kategorien im finalen Merge | 15 |
| davon Text-/Kommentar-Kategorien | 4 |
| Comparison-Notebooks | 23 |
| finale Video-Ergebnisdateien | 15 |
| finale Kommentar-/Text-Ergebnisdateien | 9 |
| Videos im finalen Video-Merge | 500 |
| VI-Videos / RI-Videos | 250 / 250 |
| Long-Format-Zeilen für Video-Metriken | 22500 |
| Video-Untermetriken im Long-Format | 45 |
| numerische Video-Untermetriken mit VI-vs.-RI-Test | 38 |
| signifikante VI-vs.-RI-Unterschiede, p < .05 | 29 / 38 |
| Richtung aller VI-vs.-RI-Unterschiede | RI höher: 31, VI höher: 7 |
| Richtung signifikanter VI-vs.-RI-Unterschiede | RI höher: 24, VI höher: 5 |
| Video-Engagement-Korrelationen | 38 |
| signifikante Video-Engagement-Korrelationen, p < .05 | 17 / 38 |
| positive/negative Video-Engagement-Korrelationen | 28 positiv, 10 negativ |
| signifikante positive/negative Video-Engagement-Korrelationen | 14 positiv, 3 negativ |
| Regressions-/Hauptmodell-Variablen | 10 |
| standardisierte Betas positiv/negativ | 5 positiv, 5 negativ |
| Chi2-Labelverteilungstests aus Comparison-Notebooks | 6 / 8 signifikant |
| kategoriale Engagementtests, ANOVA/Kruskal | 4 / 6 signifikant |
| Kommentar-Topics mit Engagementbezug | 10 / 15 signifikant |
| Richtung Topic-Engagement-Korrelationen | 0 positiv, 15 negativ |
| signifikante Topic-Engagement-Korrelationen | 0 positiv, 10 negativ |
| Human-Evaluation-Stichprobe | 50 Videos, davon 25 VI und 25 RI |
| Human-Evaluation Likert-Merkmale | 10 |
| Human-Evaluation kategoriale Merkmale | 6 |
| mittlere Human-vs.-Modell Exact-Match-Rate, Likert | 21.8% |
| mittlere Human-vs.-Modell Off-by-1-Rate, Likert | 52.2% |
| mittlere Human-vs.-Modell Accuracy, kategorial | 45% |

Interpretation der Eckdaten: Die Videoanalyse ist auf 15 finalen Kategorien aufgebaut. Für die numerischen Video-Untermetriken zeigen 29 von 38 VI-vs.-RI-Tests signifikante Unterschiede. Engagement-Korrelationen sind seltener signifikant: 17 von 38, davon deutlich mehr positiv als negativ. Bei Kommentar-Topics sind alle 15 Topic-Korrelationen negativ; 10 davon sind signifikant.

## 1. Welche statistischen Tests wurden verwendet?

| Test/Analyse | Wo verwendet | Zweck | Signifikanzregel |
|---|---|---|---|
| Mann-Whitney-U | finale Video-Gruppenunterschiede, viele Video-Comparison-Notebooks, Kommentar-Sentiment/-Emotion/-Topics | Nichtparametrischer VI-vs.-RI-Vergleich numerischer Metriken | `p < .05` |
| Welch-/t-Test | einzelne Comparison-Notebooks, z. B. Helligkeit, Beauty, Aesthetic, Legacy-Notebooks | Parametrischer Mittelwertvergleich als Zusatztest | `p < .05` |
| Cohen's d | Accumulate-Notebook und mehrere Comparison-Notebooks | Effektgröße für VI-vs.-RI-Unterschiede; im Accumulate-Notebook positiv = RI höher, negativ = VI höher | deskriptiv, keine eigene Signifikanz |
| Spearman-Rho | finale Engagement-Korrelationen, Video- und Kommentar-Comparison-Notebooks | Monotone Korrelation zwischen Metrik und Engagement | `p < .05` |
| Chi-Quadrat-Test | Labelverteilungen bei Sentiment, Emotion, Topic, Kameradistanz, Szene, Face Emotion, Body Pose | Testet, ob kategoriale Labelverteilungen zwischen VI und RI verschieden sind | `p < .05` |
| ANOVA/f_oneway | kategoriale Video-Labels vs. Engagement in Kamera/Szene/Emotion/Pose | Testet Engagementunterschiede zwischen Labelgruppen | `p < .05` |
| Kruskal-Wallis | dominante Kommentar-Emotion und dominante Kommentar-Topics vs. Engagement | Nichtparametrischer Engagementvergleich zwischen mehreren Kategorien | `p < .05` |
| Dummy-Regression | ausgewählte kategoriale Video-Comparison-Notebooks | Deskriptive Modellierung kategorialer Labels als Dummies; R2 wird berichtet | nicht als Hauptsignifikanz genutzt |
| Hauptmodell mit standardisierten Betas | `data/05_notebooks/03_accumulate_results.ipynb` | relative Bedeutung ausgewählter signifikanter Engagement-Prädiktoren | p-Werte stammen aus vorheriger univariater Spearman-Auswahl, nicht aus multivariaten Beta-Tests |

## 2. Ergebnisübersicht nach finaler Video-Kategorie

| Kategorie | getestete Untermetriken | signifikante VI-vs.-RI-Unterschiede | signifikante Engagement-Korrelationen |
|---|---:|---:|---:|
| `aesthetic_quality` | 2 | 2 | 1 |
| `angle_face_orientation` | 3 | 1 | 2 |
| `beauty_scoring` | 3 | 2 | 0 |
| `body_pose` | 1 | 1 | 1 |
| `brightness_contrast` | 2 | 0 | 0 |
| `camera_distance` | 1 | 1 | 0 |
| `camera_stability` | 3 | 3 | 0 |
| `cuts` | 6 | 6 | 3 |
| `face_emotion` | 2 | 2 | 1 |
| `saturation` | 1 | 1 | 0 |
| `scene_classification` | 1 | 1 | 1 |
| `skin_smoothness` | 6 | 3 | 5 |
| `structural_personen_anzahl` | 3 | 2 | 1 |
| `visual_filter` | 2 | 2 | 1 |
| `visual_sharpness` | 2 | 2 | 1 |

## 3. Comparison-Notebooks: Tests und gespeicherte Befunde

Die folgende Tabelle fasst alle gefundenen Comparison-Notebooks zusammen. Legacy-Notebooks aus früheren Testdaten sind bewusst mit aufgeführt, aber die finalen `data/04_analysis_results/visual_features/99_*`-Tabellen sind für den Hauptbericht maßgeblich.

| Notebook | erkannte Tests/Analysen | gespeicherte Kernaussagen |
|---|---|---|
| `comments/01_sentiment_caption/01_sentiment_caption_comparison.ipynb` | Mann-Whitney-U, Spearman, Chi-Quadrat, Cohen d | - Deskriptive Kennwerte<br>- Gruppenunterschied: U = 111769.00, p = 0.6112. Der Unterschied ist nicht signifikant. Effektgröße: vernachlässigbar klein (d = 0.112).<br>- Label-Verteilung: chi2 = 5.77, df = 2, p = 0.0560. Die Verteilung ist nicht signifikant unterschiedlich.<br>- Zusammenhang mit Engagement gesamt: rho = 0.019, p = 0.5530. Der Befund ist nicht signifikant und entspricht praktisch kein Zusammenhang.<br>- Zusammenhang mit Engagement nur VI: rho = -0.018, p = 0.7615.<br>- Zusammenhang mit Engagement nur RI: rho = 0.044, p = 0.2347. |
| `comments/02_sentiment_comments/02_sentiment_comments_comparison.ipynb` | Mann-Whitney-U, Spearman, Chi-Quadrat, Cohen d | - Kommentar-Level<br>- Gruppenunterschied: U = 177660744.00, p = 0.0000. Der Unterschied ist signifikant. Effektgröße: vernachlässigbar klein (d = -0.080).<br>- Label-Verteilung: chi2 = 740.92, df = 2, p = 0.0000. Die Verteilung ist signifikant unterschiedlich.<br>- Video-Level<br>- Gruppenunterschied: U = 84418.00, p = 0.0166. Der Unterschied ist signifikant. Effektgröße: vernachlässigbar klein (d = -0.171).<br>- Zusammenhang mit Engagement gesamt: rho = 0.183, p = 0.0000. Der Befund ist signifikant und entspricht schwacher Zusammenhang.<br>- Zusammenhang mit Engagement nur VI: rho = 0.228, p = 0.0011.<br>- Zusammenhang mit Engagement nur RI: rho = 0.095, p = 0.0185. |
| `comments/03_comment_emotion/03_comment_emotion_comparison.ipynb` | Mann-Whitney-U, Spearman, Chi-Quadrat, Kruskal-Wallis, Cohen d | - Kommentar-Level VI: n = 15090, M = 1.967, Md = 2.000<br>- Kommentar-Level RI: n = 24525, M = 2.142, Md = 2.000<br>- Emotionsvielfalt auf Kommentar-Level: U = 167279342.00, p = 0.0000. Der Unterschied ist signifikant. Effektgröße: vernachlässigbar klein (d = -0.178).<br>- Verteilung der dominanten Emotionslabels: chi2 = 1843.69, df = 26, p = 0.0000. Die Verteilung ist signifikant unterschiedlich.<br>- Emotionsvielfalt und Engagement: rho = 0.004, p = 0.9204. Der Befund ist nicht signifikant und entspricht praktisch kein Zusammenhang.<br>- Dominante Kommentar-Emotion und Engagement: H = 43.23, p = 0.0007. Der Unterschied zwischen den Emotionskategorien ist signifikant. |
| `comments/04_comment_topic_analysis/04_comment_topic_analysis_comparison.ipynb` | Mann-Whitney-U, Chi-Quadrat, Kruskal-Wallis, Cohen d | - signifikant  videos_n<br>- Video-Level VI: Videos = 272, M = 5.732, Md = 5.000<br>- Video-Level RI: Videos = 689, M = 4.624, Md = 4.000<br>- Themenverteilung: chi2 = 12478.71, df = 14, p = 0.0000. Die Verteilung ist signifikant unterschiedlich.<br>- Thematische Vielfalt pro Video: U = 109525.00, p = 0.0000. Der Unterschied ist signifikant. Effektgröße: klein (d = 0.322).<br>- Dominantes Thema und Engagement: H = 66.59, p = 0.0000. Der Befund ist signifikant. |
| `models/01_visual_brightness_contrast/01_visual_brightness_contrast_comparison.ipynb` | Mann-Whitney-U, Welch/t-Test, Spearman, Cohen d | Kurzinterpretation:<br>- Beleuchtung (brightness_index): t-Test ist signifikant (p=0.0217), Mann-Whitney ist nicht signifikant (p=0.2374). Interpretation: Mittelwert/Median zeigen, welche Gruppe heller ist (höher bei RI).<br>- Kontrast (contrast_index): t-Test ist nicht signifikant (p=0.5814), Mann-Whitney ist nicht signifikant (p=0.3924). Interpretation: Unterschied in der Farb-/Helligkeitsabstufung zwischen VI und RI (höher bei RI).<br>- Engagement (Helligkeitsindex): Spearman ist nicht signifikant (rho=-0.067, p=0.1374). Interpretation: negativer Zusammenhang zwischen Metrik und Engagement.<br>- Engagement (Kontrastindex): Spearman ist nicht signifikant (rho=0.044, p=0.3228). Interpretation: positiver Zusammenhang zwischen Metrik und Engagement. |
| `models/02_visual_saturation/02_saturation_comparison.ipynb` | Mann-Whitney-U, Spearman | Kurzinterpretation:<br>- Farbsättigung (saturation_index): Mann-Whitney ist signifikant (p=0.0000). Interpretation: Signifikanter Gruppenunterschied bedeutet systematisch unterschiedliche Farbgestaltung (höher bei VI).<br>- Engagement-Zusammenhang: Spearman ist nicht signifikant (rho=0.063, p=0.1606). Interpretation: positiver Zusammenhang; positives Vorzeichen deutet auf stärkere Performance bei höhere Sättigung hin. |
| `models/03_visual_cuts/03_visual_cuts_comparison.ipynb` | Mann-Whitney-U, Spearman | Kurzinterpretation:<br>- Schnittdynamik (cut_count): Mann-Whitney ist signifikant (p=0.0000). Interpretation: Höherer Median/Mittelwert zeigt dynamischere Videobearbeitung (höher bei RI).<br>- Zeit bis zum nächsten Schnitt (seconds_per_cut): Mann-Whitney ist signifikant (p=0.0019). Interpretation: Kleinere Werte bedeuten schnellere Schnitte (kürzer bei RI).<br>- Videolänge (video_duration_seconds): Mann-Whitney ist signifikant (p=0.0000). Interpretation: Unterschiede in der Länge zwischen VI- und RI-Videos (höher bei RI).<br>- Engagement ~ cut_count (Spearman): nicht signifikant (rho=0.052, p=0.2488). Interpretation: positiver Zusammenhang von Schnitthäufigkeit und Engagement.<br>- Engagement ~ seconds_per_cut (Spearman + Regression): nicht signifikant (rho=0.012, p=0.8452). Interpretation: Ein negativer Zusammenhang würde bedeuten, dass schnellere Schnitte tendenziell mit höherem Engagement einhergehen.<br>- Engagement ~ Videolänge (Spearman + Regression): signifikant (rho=0.139, p=0.0018). Interpretation: Positiver Effekt bedeutet längere Inhalte mit tendenziell mehr Interaktion. |
| `models/04_visual_angle_face_orientation/04_angle_face_orientation_comparison.ipynb` | Welch/t-Test, Spearman | Kurzinterpretation:<br>- face_pitch_mean (t-Test): nicht signifikant (p=0.1557). Interpretation: Unterschiedliche Mittelwerte deuten auf unterschiedliche Kameraposition/Blickwinkel hin (höherer Mittelwert bei VI).<br>- face_yaw_mean (t-Test): nicht signifikant (p=0.8907). Interpretation: Unterschiedliche Mittelwerte deuten auf unterschiedliche Kameraposition/Blickwinkel hin (höherer Mittelwert bei RI).<br>- Engagement ~ Durchschnittlicher Face Pitch (Spearman): signifikant (rho=-0.219, p=0.0000). Interpretation: negativer monotoner Zusammenhang mit Engagement.<br>- Engagement ~ Durchschnittlicher Face Yaw (Spearman): nicht signifikant (rho=-0.085, p=0.0602). Interpretation: negativer monotoner Zusammenhang mit Engagement. |
| `models/05_visual_camera_distance/02_camera_distance_comparison.ipynb` | Mann-Whitney-U, Spearman, Chi-Quadrat, ANOVA/f_oneway, Dummy-Regression | - 0     camera_distance_confidence  Mann-Whitney-U   250     250   0.7702<br>- 1  camera_distance_unique_labels  Mann-Whitney-U   250     250   1.9440<br>- Kurzinterpretation:<br>- camera_distance_confidence (Mann-Whitney): nicht signifikant (p=0.2323). Interpretation: höher bei VI.<br>- camera_distance_unique_labels (Mann-Whitney): signifikant (p=< 1e-308). Interpretation: höher bei RI.<br>- Camera-Distance-Label (Chi2): nicht signifikant (chi2=13.47, p=0.0614). Interpretation: Label-Verteilungen unterscheiden sich zwischen VI und RI.<br>- Engagement ~ camera_distance_confidence (Spearman): nicht signifikant (rho=-0.063, p=0.1614). Interpretation: negativer Zusammenhang.<br>- Engagement ~ Camera-Distance-Label (ANOVA): nicht signifikant (F=1.96, p=0.0593). |
| `models/06_scene_classification/06_scene_classification_comparison.ipynb` | Mann-Whitney-U, Spearman, Chi-Quadrat, ANOVA/f_oneway, Dummy-Regression | - 0  scene_unique_labels  Mann-Whitney-U   250     250    3.952      7.192<br>- Kurzinterpretation:<br>- Szenenvielfalt (scene_unique_labels, Mann-Whitney): signifikant (p=0.0000). Interpretation: Höhere Vielfalt kann auf abwechslungsreichere Inszenierung hindeuten (höher bei RI).<br>- Szenenlabel (scene_top1_label, Chi2): signifikant (chi2=185.68, p=0.0000). Interpretation: Bestimmte Szenentypen treten je Gruppe unterschiedlich häufig auf.<br>- Engagement ~ scene_unique_labels (Spearman): signifikant (rho=0.139, p=0.0018). Interpretation: positiver Zusammenhang; positive Werte sprechen für besseren Output bei hoher Vielfalt.<br>- Engagement ~ scene_top1_label (ANOVA): signifikant (F=1.58, p=0.0105). |
| `models/07_visual_skin_smoothness/07_skin_smoothness_comparison.ipynb` | Mann-Whitney-U, Spearman | Kurzinterpretation:<br>- Skin Smoothness (skin_smoothness_highpass_index, Mann-Whitney): nicht signifikant (p=0.3531). Interpretation: Höhere Werte deuten auf stärkere Glättung/bearbeitete Haut hin (höher bei RI). |
| `models/08_aesthetic_beauty_scoring/09_aesthetic_beauty_scoring_comparison.ipynb` | Mann-Whitney-U, Welch/t-Test, Spearman, Cohen d | - 1   beauty_score_std  mann-whitney-u   244     243   4.8223     5.1695<br>- Kurzinterpretation:<br>- Beauty Score Mean (t-Test): nicht signifikant (p=0.1195). Interpretation: Höhere Mittelwerte bedeuten höhere wahrgenommene Attraktivität (höher bei VI).<br>- Beauty Score Std (Mann-Whitney): signifikant (p=0.0017). Interpretation: Höhere Varianz kann heterogene Bildqualität anzeigen (höher bei RI).<br>- Engagement ~ beauty_score_mean (Spearman): nicht signifikant (rho=0.019, p=0.6676). Interpretation: positiver Zusammenhang mit Engagement.<br>- Engagement ~ beauty_score_std (Spearman): nicht signifikant (rho=0.039, p=0.3898). Interpretation: positiver Zusammenhang mit Engagement. |
| `models/09_aesthetic_aesthetic_quality/08_aesthetic_quality_comparison.ipynb` | Welch/t-Test, Spearman, Cohen d | Kurzinterpretation:<br>- Ästhetische Qualität (t-Test): signifikant (p=0.0000). Interpretation: Höhere Werte stehen für höhere visuelle Qualität (höher bei VI).<br>- Engagement ~ aesthetic_quality_score (Spearman + Regression): nicht signifikant (rho=0.038, p=0.3999). Interpretation: positiver Effekt visueller Qualität auf Engagement. |
| `models/10_face_emotion/10_face_emotion_comparison.ipynb` | Mann-Whitney-U, Spearman, Chi-Quadrat, ANOVA/f_oneway, Dummy-Regression | - 0  emotion_major_beit_confidence  Mann-Whitney-U   250     250   0.5727<br>- Kurzinterpretation:<br>- Sicherheit der dominanten Emotion (Mann-Whitney): signifikant (p=0.0315). Interpretation: Höhere Werte deuten auf eine sicherere dominante Emotion hin (höher bei RI).<br>- Dominante Emotionskategorie (Chi2): signifikant (chi2=28.03, p=0.0001). Interpretation: Die Verteilung der dominanten Emotionen unterscheidet sich zwischen VI und RI.<br>- Engagement ~ emotion_major_beit_confidence (Spearman): signifikant (rho=0.134, p=0.0028). Interpretation: positiver Zusammenhang mit Engagement.<br>- Engagement ~ emotion_unique_labels (Spearman): nicht signifikant (rho=-0.066, p=0.1391). Interpretation: negativer Zusammenhang mit Engagement.<br>- Engagement ~ dominante Emotionskategorie (ANOVA): nicht signifikant (F=2.07, p=0.0550). |
| `models/11_body_pose/02_body_pose_comparison.ipynb` | Mann-Whitney-U, Spearman, Chi-Quadrat, ANOVA/f_oneway, Dummy-Regression | - 0  pose_confidence  Mann-Whitney-U   250     250   0.6387      0.583<br>- Kurzinterpretation:<br>- Pose Confidence (Mann-Whitney): signifikant (p=0.0011). Interpretation: Positiver Zusammenhang zeigt Einfluss von Bewegungsdynamik (höher bei VI).<br>- Pose Label (Chi2): signifikant (chi2=42.85, p=0.0001). Interpretation: Körperposen treten je Gruppe unterschiedlich häufig auf.<br>- Engagement ~ pose_confidence (Spearman): nicht signifikant (rho=-0.083, p=0.0653). Interpretation: negativer Zusammenhang mit Engagement.<br>- Engagement ~ pose_label (ANOVA): signifikant (F=2.04, p=0.0138). |
| `models/12_structural_personen_zahl/02_structural_personen_anzahl_comparison.ipynb` | Mann-Whitney-U, Spearman | Kurzinterpretation:<br>- Personenanzahl (personen_anzahl): Mann-Whitney ist signifikant (p=0.0090). Interpretation: Ein signifikanter Gruppenunterschied weist auf unterschiedlich viele sichtbare Personen hin (höher bei VI).<br>- Engagement-Zusammenhang: Spearman ist nicht signifikant (rho=-0.055, p=0.2210). Interpretation: negativer Zusammenhang zwischen Personenanzahl und Engagement. |
| `models/13_visual_sharpness/12_visual_sharpness_comparison.ipynb` | Mann-Whitney-U, Spearman | Kurzinterpretation:<br>- Sharpness (sharpness_laplacian_mean): Mann-Whitney ist signifikant (p=0.0005). Interpretation: Ein signifikanter Gruppenunterschied weist auf systematisch unterschiedliche technische Schärfe hin (höher bei RI).<br>- Engagement-Zusammenhang: Spearman ist nicht signifikant (rho=0.035, p=0.4420). Interpretation: positiver Zusammenhang; positives Vorzeichen deutet auf bessere Performance bei höherer Schärfe hin. |
| `models/14_visual_camera_stability/14_camera_stability_comparison.ipynb` | Mann-Whitney-U, Spearman | Kurzinterpretation:<br>- Kamerastabilität (stability_index): Mann-Whitney ist signifikant (p=0.0000). Interpretation: Ein signifikanter Gruppenunterschied weist auf systematisch unterschiedliche Kameraruhe hin (höher bei VI).<br>- Engagement-Zusammenhang: Spearman ist nicht signifikant (rho=-0.029, p=0.5196). Interpretation: negativer Zusammenhang; positives Vorzeichen deutet auf mehr Engagement bei höherer Kamerastabilität hin. |
| `models/15_visual_filter/15_visual_filter_comparison.ipynb` | Mann-Whitney-U, Spearman | Kurzinterpretation:<br>- Visuelle Filter (filter_strength_prob): Mann-Whitney ist signifikant (p=0.0067). Interpretation: Ein signifikanter Gruppenunterschied weist auf systematisch unterschiedliche Nachbearbeitung hin (höher bei VI).<br>- Engagement-Zusammenhang: Spearman ist signifikant (rho=0.103, p=0.0213). Interpretation: positiver Zusammenhang; positives Vorzeichen deutet auf mehr Engagement bei höherer Filterwahrscheinlichkeit hin. |

## 4. Finale Video-Gruppenunterschiede VI vs. RI

Quelle: `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_group_differences.csv`. Test: Mann-Whitney-U pro numerischer Untermetrik; Effektgröße `Cohen's d` ist im Accumulate-Notebook als RI minus VI definiert.

| Kategorie | Gruppe | Metrik | VI M | RI M | VI Md | RI Md | p | d | Richtung | signifikant |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| Schnittdynamik \| Absolute Anzahl der Schnitte | `cuts` | `cut_count` | 3.9 | 14.952 | 0 | 6 | < .001 | 0.466 | RI höher | True |
| Schnittdynamik \| Analysierte Frames | `cuts` | `frames_scanned` | 523.74 | 1266.336 | 357.5 | 719.5 | < .001 | 0.676 | RI höher | True |
| Schnittdynamik \| Schnittdichte pro Sekunde | `cuts` | `cuts_per_second` | 0.182 | 0.524 | 0 | 0.229 | < .001 | 0.443 | RI höher | True |
| Ästhetische Gesamtwirkung \| Anteil ästhetisch bewerteter Frames | `aesthetic_quality` | `aesthetic_quality_scored_frames` | 18.564 | 43.156 | 12 | 25 | < .001 | 0.669 | RI höher | True |
| Emotionale Gesichtswirkung \| Anteil emotional auswertbarer Frames | `face_emotion` | `detected_emotion_frames` | 18.564 | 43.156 | 12 | 25 | < .001 | 0.669 | RI höher | True |
| Körperhaltung und Pose \| Anteil erkannter Pose-Frames | `body_pose` | `detected_pose_frames` | 18.564 | 43.156 | 12 | 25 | < .001 | 0.669 | RI höher | True |
| Schnittdynamik \| Schnittdichte pro Frame | `cuts` | `cuts_per_frame` | 0.006 | 0.018 | 0 | 0.008 | < .001 | 0.431 | RI höher | True |
| Schnittdynamik \| Geschätzte Videodauer | `cuts` | `video_duration_seconds_est` | 18.125 | 42.777 | 11.563 | 24.683 | < .001 | 0.67 | RI höher | True |
| Bildschärfe \| Streuung der Bildschärfe | `visual_sharpness` | `sharpness_laplacian_std` | 127.82 | 215.576 | 71.338 | 150.742 | < .001 | 0.408 | RI höher | True |
| Szenerischer Kontext \| Vielfalt erkannter Szenen | `scene_classification` | `scene_unique_labels` | 3.952 | 7.192 | 2.5 | 5 | < .001 | 0.527 | RI höher | True |
| Kamerastabilität \| Durchschnittliche Bewegungsstärke | `camera_stability` | `optical_flow_magnitude_mean` | 0.006 | 0.011 | 0.003 | 0.009 | < .001 | 0.589 | RI höher | True |
| Kamerastabilität \| Stabilitätsindex | `camera_stability` | `stability_index` | 0.729 | 0.581 | 0.763 | 0.532 | < .001 | -0.646 | VI höher | True |
| Kamerastabilität \| Streuung der Bewegungsstärke | `camera_stability` | `optical_flow_magnitude_std` | 0.008 | 0.014 | 0.004 | 0.012 | < .001 | 0.51 | RI höher | True |
| Sichtbare Personenzahl \| Anteil erkannter Personenframes | `structural_personen_anzahl` | `detected_person_frames` | 13.476 | 17.144 | 12 | 19 | < .001 | 0.576 | RI höher | True |
| Hauttextur und Hautglätte \| Feinstruktur der Hauttextur | `skin_smoothness` | `skin_texture_laplacian_var` | 435.137 | 584.883 | 240.504 | 410.27 | < .001 | 0.219 | RI höher | True |
| Emotionale Gesichtswirkung \| Vielfalt erkannter Emotionen | `face_emotion` | `emotion_unique_labels` | 2.748 | 3.504 | 3 | 4 | < .001 | 0.507 | RI höher | True |
| Farbliche Intensitaet \| Farbsättigung | `saturation` | `saturation_index` | 83.861 | 66.769 | 77.489 | 65.03 | < .001 | -0.573 | VI höher | True |
| Ästhetische Gesamtwirkung \| Ästhetische Qualitätsbewertung | `aesthetic_quality` | `aesthetic_quality_score` | 4.684 | 4.363 | 4.697 | 4.315 | < .001 | -0.416 | VI höher | True |
| Kameradistanz \| Vielfalt erkannter Kameradistanzen | `camera_distance` | `camera_distance_unique_labels` | 1.944 | 2.428 | 2 | 2 | < .001 | 0.372 | RI höher | True |
| Filtereinsatz \| Streuung der Filterstärke | `visual_filter` | `filter_strength_std` | 0.01 | 0.015 | 0.00098 | 0.002 | < .001 | 0.122 | RI höher | True |
| Schnittdynamik \| Bildrate des Videos | `cuts` | `video_fps` | 28.695 | 29.468 | 30 | 30 | < .001 | 0.262 | RI höher | True |
| Hauttextur und Hautglätte \| Anteil auswertbarer Hautframes | `skin_smoothness` | `detected_skin_face_frames` | 16.132 | 36 | 11 | 17 | < .001 | 0.566 | RI höher | True |
| Bildschärfe \| Durchschnittliche Bildschärfe | `visual_sharpness` | `sharpness_laplacian_mean` | 505.223 | 625.707 | 397.573 | 483.079 | < .001 | 0.267 | RI höher | True |
| Gesichtsorientierung \| Anteil erkannter Gesichtsframes | `angle_face_orientation` | `detected_face_frames` | 15.904 | 33.8 | 11 | 15 | < .001 | 0.537 | RI höher | True |
| Attraktivitätsbewertung \| Anteil bewertbarer Gesichtsframes | `beauty_scoring` | `beauty_detected_face_frames` | 14.1 | 30.224 | 9 | 13 | 0.0013 | 0.509 | RI höher | True |
| Hauttextur und Hautglätte \| Hochfrequente Hauttextur | `skin_smoothness` | `skin_texture_highpass_var` | 127.861 | 155.165 | 84.432 | 108.708 | 0.0015 | 0.165 | RI höher | True |
| Attraktivitätsbewertung \| Streuung der Attraktivitätsbewertung | `beauty_scoring` | `beauty_score_std` | 4.822 | 5.169 | 3.297 | 4.573 | 0.0017 | 0.087 | RI höher | True |
| Filtereinsatz \| Wahrscheinlichkeit für Filtereinsatz | `visual_filter` | `filter_strength_prob` | 0.992 | 0.989 | 0.997 | 0.996 | 0.0067 | -0.144 | VI höher | True |
| Sichtbare Personenzahl \| Durchschnittliche Personenzahl | `structural_personen_anzahl` | `personen_anzahl` | 2.332 | 1.931 | 2 | 1.792 | 0.009 | -0.313 | VI höher | True |
| Gesichtsorientierung \| Mittlere vertikale Gesichtsausrichtung | `angle_face_orientation` | `face_pitch_mean` | 6.948 | 6.226 | 7.549 | 6.767 | 0.1627 | -0.129 | VI höher | False |
| Visuelle Beleuchtung \| Durchschnittliche Helligkeit | `brightness_contrast` | `brightness_index` | 114.907 | 120.949 | 120.803 | 122.409 | 0.2374 | 0.206 | RI höher | False |
| Attraktivitätsbewertung \| Mittlere Attraktivitätsbewertung | `beauty_scoring` | `beauty_score_mean` | 32.273 | 31.184 | 31.286 | 30.058 | 0.2665 | -0.141 | VI höher | False |
| Hauttextur und Hautglätte \| Hautglätte (Highpass) | `skin_smoothness` | `skin_smoothness_highpass_index` | 0.019 | 0.019 | 0.014 | 0.014 | 0.3531 | 0.008 | RI höher | False |
| Hauttextur und Hautglätte \| Hautglätte (DoG) | `skin_smoothness` | `skin_smoothness_dog_index` | 0.058 | 0.061 | 0.047 | 0.053 | 0.3891 | 0.087 | RI höher | False |
| Visuelle Beleuchtung \| Bildkontrast | `brightness_contrast` | `contrast_index` | 59.556 | 60.027 | 59.281 | 60.071 | 0.3924 | 0.049 | RI höher | False |
| Sichtbare Personenzahl \| Maximale Personenzahl | `structural_personen_anzahl` | `personen_anzahl_max` | 4.44 | 4.668 | 4 | 4 | 0.5271 | 0.059 | RI höher | False |
| Gesichtsorientierung \| Mittlere horizontale Gesichtsausrichtung | `angle_face_orientation` | `face_yaw_mean` | -0.718 | -0.559 | 0.268 | 0.557 | 0.8549 | 0.012 | RI höher | False |
| Hauttextur und Hautglätte \| Texturkontrast der Haut | `skin_smoothness` | `skin_texture_dog_var` | 27.116 | 27.79 | 23.319 | 24.33 | 0.866 | 0.035 | RI höher | False |

## 5. Finale Video-Engagement-Korrelationen

Quelle: `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_engagement_correlations.csv`. Test: Spearman-Rho zwischen numerischer Untermetrik und `video_engagement_rate`.

| Kategorie | Gruppe | Metrik | rho | p | Richtung | signifikant |
|---|---|---|---:|---:|---|---|
| Gesichtsorientierung \| Mittlere vertikale Gesichtsausrichtung | `angle_face_orientation` | `face_pitch_mean` | -0.219 | < .001 | negativ | True |
| Schnittdynamik \| Bildrate des Videos | `cuts` | `video_fps` | 0.186 | < .001 | positiv | True |
| Schnittdynamik \| Analysierte Frames | `cuts` | `frames_scanned` | 0.156 | < .001 | positiv | True |
| Ästhetische Gesamtwirkung \| Anteil ästhetisch bewerteter Frames | `aesthetic_quality` | `aesthetic_quality_scored_frames` | 0.143 | 0.0014 | positiv | True |
| Körperhaltung und Pose \| Anteil erkannter Pose-Frames | `body_pose` | `detected_pose_frames` | 0.143 | 0.0014 | positiv | True |
| Emotionale Gesichtswirkung \| Anteil emotional auswertbarer Frames | `face_emotion` | `detected_emotion_frames` | 0.143 | 0.0014 | positiv | True |
| Schnittdynamik \| Geschätzte Videodauer | `cuts` | `video_duration_seconds_est` | 0.139 | 0.0018 | positiv | True |
| Szenerischer Kontext \| Vielfalt erkannter Szenen | `scene_classification` | `scene_unique_labels` | 0.139 | 0.0018 | positiv | True |
| Hauttextur und Hautglätte \| Anteil auswertbarer Hautframes | `skin_smoothness` | `detected_skin_face_frames` | 0.113 | 0.0112 | positiv | True |
| Hauttextur und Hautglätte \| Hautglätte (DoG) | `skin_smoothness` | `skin_smoothness_dog_index` | -0.112 | 0.0126 | negativ | True |
| Sichtbare Personenzahl \| Anteil erkannter Personenframes | `structural_personen_anzahl` | `detected_person_frames` | 0.11 | 0.0142 | positiv | True |
| Bildschärfe \| Streuung der Bildschärfe | `visual_sharpness` | `sharpness_laplacian_std` | 0.104 | 0.02 | positiv | True |
| Filtereinsatz \| Wahrscheinlichkeit für Filtereinsatz | `visual_filter` | `filter_strength_prob` | 0.103 | 0.0213 | positiv | True |
| Hauttextur und Hautglätte \| Hautglätte (Highpass) | `skin_smoothness` | `skin_smoothness_highpass_index` | -0.103 | 0.0215 | negativ | True |
| Gesichtsorientierung \| Anteil erkannter Gesichtsframes | `angle_face_orientation` | `detected_face_frames` | 0.099 | 0.0267 | positiv | True |
| Hauttextur und Hautglätte \| Texturkontrast der Haut | `skin_smoothness` | `skin_texture_dog_var` | 0.097 | 0.0311 | positiv | True |
| Hauttextur und Hautglätte \| Feinstruktur der Hauttextur | `skin_smoothness` | `skin_texture_laplacian_var` | 0.091 | 0.0437 | positiv | True |
| Gesichtsorientierung \| Mittlere horizontale Gesichtsausrichtung | `angle_face_orientation` | `face_yaw_mean` | -0.085 | 0.0602 | negativ | False |
| Hauttextur und Hautglätte \| Hochfrequente Hauttextur | `skin_smoothness` | `skin_texture_highpass_var` | 0.084 | 0.0622 | positiv | False |
| Attraktivitätsbewertung \| Anteil bewertbarer Gesichtsframes | `beauty_scoring` | `beauty_detected_face_frames` | 0.074 | 0.0967 | positiv | False |
| Visuelle Beleuchtung \| Durchschnittliche Helligkeit | `brightness_contrast` | `brightness_index` | -0.067 | 0.1374 | negativ | False |
| Emotionale Gesichtswirkung \| Vielfalt erkannter Emotionen | `face_emotion` | `emotion_unique_labels` | -0.066 | 0.1391 | negativ | False |
| Farbliche Intensitaet \| Farbsättigung | `saturation` | `saturation_index` | 0.063 | 0.1606 | positiv | False |
| Sichtbare Personenzahl \| Durchschnittliche Personenzahl | `structural_personen_anzahl` | `personen_anzahl` | -0.055 | 0.221 | negativ | False |
| Kameradistanz \| Vielfalt erkannter Kameradistanzen | `camera_distance` | `camera_distance_unique_labels` | 0.052 | 0.2474 | positiv | False |
| Schnittdynamik \| Absolute Anzahl der Schnitte | `cuts` | `cut_count` | 0.052 | 0.2488 | positiv | False |
| Schnittdynamik \| Schnittdichte pro Sekunde | `cuts` | `cuts_per_second` | 0.051 | 0.2544 | positiv | False |
| Filtereinsatz \| Streuung der Filterstärke | `visual_filter` | `filter_strength_std` | -0.049 | 0.2779 | negativ | False |
| Schnittdynamik \| Schnittdichte pro Frame | `cuts` | `cuts_per_frame` | 0.048 | 0.2803 | positiv | False |
| Visuelle Beleuchtung \| Bildkontrast | `brightness_contrast` | `contrast_index` | 0.044 | 0.3228 | positiv | False |
| Attraktivitätsbewertung \| Streuung der Attraktivitätsbewertung | `beauty_scoring` | `beauty_score_std` | 0.039 | 0.3898 | positiv | False |
| Ästhetische Gesamtwirkung \| Ästhetische Qualitätsbewertung | `aesthetic_quality` | `aesthetic_quality_score` | 0.038 | 0.3999 | positiv | False |
| Bildschärfe \| Durchschnittliche Bildschärfe | `visual_sharpness` | `sharpness_laplacian_mean` | 0.034 | 0.442 | positiv | False |
| Kamerastabilität \| Streuung der Bewegungsstärke | `camera_stability` | `optical_flow_magnitude_std` | 0.033 | 0.4636 | positiv | False |
| Kamerastabilität \| Durchschnittliche Bewegungsstärke | `camera_stability` | `optical_flow_magnitude_mean` | 0.029 | 0.5196 | positiv | False |
| Kamerastabilität \| Stabilitätsindex | `camera_stability` | `stability_index` | -0.029 | 0.5196 | negativ | False |
| Attraktivitätsbewertung \| Mittlere Attraktivitätsbewertung | `beauty_scoring` | `beauty_score_mean` | 0.02 | 0.6676 | positiv | False |
| Sichtbare Personenzahl \| Maximale Personenzahl | `structural_personen_anzahl` | `personen_anzahl_max` | -0.006 | 0.8896 | negativ | False |

## 6. Hauptmodell mit standardisierten Betas

Quelle: `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_regression_betas.csv`. Das Accumulate-Notebook verwendet numerische Variablen mit signifikantem Spearman-Zusammenhang zum Engagement, entfernt stark redundante Variablen (`r > .85`) und berechnet standardisierte Betas per Pseudo-Inverse. Wichtig: Die p-Werte in dieser Tabelle sind die vorherigen univariaten Engagement-p-Werte, keine multivariaten Koeffizienten-p-Werte.

| Kategorie | beta_std | p aus Engagement-Korrelation | Richtung |
|---|---:|---:|---|
| Gesichtsorientierung \| Mittlere vertikale Gesichtsausrichtung | -0.152 | < .001 | negativ |
| Bildschärfe \| Streuung der Bildschärfe | -0.046 | 0.02 | negativ |
| Hauttextur und Hautglätte \| Feinstruktur der Hauttextur | -0.033 | 0.0437 | negativ |
| Hauttextur und Hautglätte \| Hautglätte (DoG) | -0.016 | 0.0126 | negativ |
| Filtereinsatz \| Wahrscheinlichkeit für Filtereinsatz | -0.008 | 0.0213 | negativ |
| Schnittdynamik \| Analysierte Frames | 0.007 | < .001 | positiv |
| Sichtbare Personenzahl \| Anteil erkannter Personenframes | 0.008 | 0.0142 | positiv |
| Hauttextur und Hautglätte \| Texturkontrast der Haut | 0.056 | 0.0311 | positiv |
| Szenerischer Kontext \| Vielfalt erkannter Szenen | 0.073 | 0.0018 | positiv |
| Schnittdynamik \| Bildrate des Videos | 0.12 | < .001 | positiv |

## 7. Kommentar-, Text- und Topic-Ergebnisse

### Caption-Sentiment

- Mann-Whitney-U für den Sentiment-Index: `p = 0.6112`, nicht signifikant.
- Chi2 für die Caption-Sentiment-Labelverteilung: `p = 0.0560`, nicht signifikant.
- Spearman Sentiment-Index vs. Engagement gesamt: `rho = 0.019`, `p = 0.5530`, nicht signifikant.
- Subgruppen: VI `rho = -0.018`, `p = 0.7615`; RI `rho = 0.044`, `p = 0.2347`.

### Kommentar-Sentiment

- Kommentar-Level: Mann-Whitney-U signifikant, `p < .001`, aber Effekt vernachlässigbar klein (`d = -0.080`).
- Kommentar-Level Labelverteilung: Chi2 signifikant, `chi2 = 740.92`, `df = 2`, `p < .001`.
- Video-Level: Mann-Whitney-U signifikant, `p = 0.0166`, Effekt vernachlässigbar klein (`d = -0.171`).
- Engagement-Korrelation Video-Level: gesamt `rho = 0.183`, `p < .001`; VI `rho = 0.228`, `p = 0.0011`; RI `rho = 0.095`, `p = 0.0185`.

### Kommentar-Emotion

- Emotionsvielfalt auf Kommentar-Level: Mann-Whitney-U signifikant, `p < .001`, Effekt vernachlässigbar klein (`d = -0.178`).
- Dominante Emotionslabels: Chi2 signifikant, `chi2 = 1843.69`, `df = 26`, `p < .001`.
- Emotionsvielfalt vs. Engagement: `rho = 0.004`, `p = 0.9204`, nicht signifikant.
- Dominante Kommentar-Emotion vs. Engagement: Kruskal-Wallis signifikant, `H = 43.23`, `p = 0.0007`.

### Kommentar-Topics

- Themenverteilung VI vs. RI: Chi2 signifikant, `chi2 = 12478.71`, `df = 14`, `p < .001`.
- Thematische Vielfalt pro Video: Mann-Whitney-U signifikant, `p < .001`, kleiner Effekt (`d = 0.322`).
- Dominantes Thema vs. Engagement: Kruskal-Wallis signifikant, `H = 66.59`, `p < .001`.
- Topic-Anteile vs. Engagement: 10 von 15 Topics signifikant; alle 15 Rhos sind negativ.

#### Topic-Engagement-Korrelationen

| topic_id | topic_label | rho | p | signifikant | Videos n |
|---|---|---:|---:|---|---:|
| 8 | like \| people \| don | -0.121 | 0.0301 | True | 324 |
| 2 | like \| girl \| know | -0.146 | 0.0027 | True | 422 |
| 10 | feel \| just \| ve | -0.223 | < .001 | True | 223 |
| 0 | yes \| hi \| early | -0.257 | < .001 | True | 397 |
| 7 | filter \| like \| pink | -0.274 | < .001 | True | 332 |
| 3 | real \| look \| fake | -0.288 | < .001 | True | 132 |
| 11 | try \| almond \| use | -0.345 | < .001 | True | 330 |
| 6 | janet \| girl \| like | -0.403 | < .001 | True | 214 |
| 5 | philippines \| europe \| country | -0.442 | < .001 | True | 89 |
| 4 | robot \| ai \| janet | -0.463 | < .001 | True | 116 |
| 14 | love \| voice \| girl | -0.023 | 0.6246 | False | 443 |
| 1 | beautiful \| love \| amazing | -0.066 | 0.1997 | False | 383 |
| 13 | beautiful \| janet \| super | -0.102 | 0.1939 | False | 165 |
| 9 | pay \| like \| just | -0.129 | 0.0579 | False | 217 |
| 12 | skin \| kids \| acne | -0.129 | 0.1469 | False | 128 |

## 8. Menschliche Evaluation: Prozess

Die menschliche Evaluation wurde als separate Re-Annotation einer Stichprobe umgesetzt.

| Schritt | Dokumentation |
|---|---|
| Stichprobe | 50 Videos aus dem influencer-balancierten 500er Datensatz, davon 25 VI und 25 RI |
| Sampling-Notebook | `data/05_notebooks/04_sample_reannotation_videos.ipynb` |
| Sampling-Seed | `42` |
| Sample-Exportordner | `data/06_human_evaluation_reannotation/reannotation_samples/sample_20260402_173603` (vom Sampling-Notebook generierbar, nicht versioniert) |
| Human VI CSV | `data/06_human_evaluation_reannotation/human_evaluation_ai_2_annotators.csv` |
| Human RI CSV | `data/06_human_evaluation_reannotation/human_evaluation_real_2_annotators.csv` |
| Modellvergleich | `data/05_notebooks/05_evaluate_human_annotation.ipynb` und `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_all_results_merged.csv` |
| Join-Schluessel | `video_id`; 0 von 50 Zeilen ohne Modellwerte |

Die graduellen Human-Labels wurden als 1-5-Likert annotiert. Kontinuierliche Modellwerte wurden linear über den Min-/Max-Bereich des gesamten 500er Modell-Datensatzes auf 1-5 gemappt und gerundet. `Unbestimmt` wurde als gültige Klasse behandelt, nicht als Missing Value.

### Human-Evaluation-Stichprobe

| Gruppe | Engagement-Bin | Videos |
|---|---|---:|
| ai | High | 8 |
| ai | Low | 9 |
| ai | Medium | 8 |
| real | High | 8 |
| real | Low | 9 |
| real | Medium | 8 |

### Human-Evaluation: Likert-Ergebnisse

| Merkmal | n | Spearman Human-Likert vs. Modellscore | Exact Match | Off-by-1 | MAE Likert |
|---|---:|---:|---:|---:|---:|
| Helligkeit | 50 | 0.2 | 28% | 86% | 0.86 |
| Kontrast | 50 | 0.127 | 40% | 86% | 0.76 |
| Aesthetic Quality | 50 | -0.046 | 18% | 84% | 1.02 |
| Schnittdynamik | 50 | 0.809 | 60% | 68% | 0.96 |
| Kamerastabilität | 50 | 0.498 | 32% | 64% | 1.14 |
| Filterstärke | 50 | 0.312 | 28% | 62% | 1.327 |
| Sättigung | 50 | 0.317 | 10% | 54% | 1.38 |
| Bildschärfe | 50 | -0.099 | 0% | 14% | 2.42 |
| Skin Smoothness | 50 | 0.069 | 2% | 4% | 3.711 |
| Beauty Score | 50 | 0.235 | 0% | 0% | 2.619 |

### Human-Evaluation: Likert nach Gruppe

| Gruppe | Merkmal | n | Exact Match | Off-by-1 |
|---|---|---:|---:|---:|
| AI | Aesthetic Quality | 25 | 20% | 88% |
| AI | Beauty Score | 25 | 0% | 0% |
| AI | Bildschärfe | 25 | 0% | 16% |
| AI | Filterstärke | 25 | 44% | 88% |
| AI | Helligkeit | 25 | 32% | 84% |
| AI | Kamerastabilität | 25 | 36% | 84% |
| AI | Kontrast | 25 | 36% | 80% |
| AI | Sättigung | 25 | 4% | 36% |
| AI | Schnittdynamik | 25 | 76% | 92% |
| AI | Skin Smoothness | 25 | 0% | 0% |
| RI | Aesthetic Quality | 25 | 16% | 80% |
| RI | Beauty Score | 25 | 0% | 0% |
| RI | Bildschärfe | 25 | 0% | 12% |
| RI | Filterstärke | 25 | 12% | 36% |
| RI | Helligkeit | 25 | 24% | 88% |
| RI | Kamerastabilität | 25 | 28% | 44% |
| RI | Kontrast | 25 | 44% | 92% |
| RI | Sättigung | 25 | 16% | 72% |
| RI | Schnittdynamik | 25 | 44% | 44% |
| RI | Skin Smoothness | 25 | 4% | 8% |

### Human-Evaluation: kategoriale Ergebnisse

| Merkmal | n | Accuracy |
|---|---:|---:|
| Gesichtsorientierung | 50 | 66% |
| Kameradistanz | 50 | 62% |
| Body Pose | 50 | 54% |
| Gesichtsemotion | 50 | 38% |
| Szenenkontext | 50 | 26% |
| Personenanzahl | 50 | 24% |

### Human-Evaluation: kategorial nach Gruppe

| Gruppe | Merkmal | n | Accuracy |
|---|---|---:|---:|
| AI | Body Pose | 25 | 44% |
| AI | Gesichtsemotion | 25 | 48% |
| AI | Gesichtsorientierung | 25 | 72% |
| AI | Kameradistanz | 25 | 64% |
| AI | Personenanzahl | 25 | 16% |
| AI | Szenenkontext | 25 | 40% |
| RI | Body Pose | 25 | 64% |
| RI | Gesichtsemotion | 25 | 28% |
| RI | Gesichtsorientierung | 25 | 60% |
| RI | Kameradistanz | 25 | 60% |
| RI | Personenanzahl | 25 | 32% |
| RI | Szenenkontext | 25 | 12% |

### Interpretation Human-Evaluation

- Über die 10 Likert-Merkmale liegt die mittlere Exact-Match-Rate bei 21.8%; die mittlere Off-by-1-Rate liegt bei 52.2%.
- Über die 6 kategorialen Merkmale liegt die mittlere Accuracy bei 45%.
- Beste tolerante Likert-Übereinstimmungen: Helligkeit, Kontrast und Aesthetic Quality.
- Schwaechste Likert-Übereinstimmungen: Beauty Score, Skin Smoothness und Bildschärfe.
- Beste kategoriale Übereinstimmungen: Gesichtsorientierung, Kameradistanz und Body Pose.
- Schwaechste kategoriale Übereinstimmungen: Personenanzahl, Szenenkontext und Gesichtsemotion.

## 9. Quelleninventar

### Finale Video-Ergebnisdateien

- `data/04_analysis_results/visual_features/01_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_brightness_contrast.csv`: 500 Zeilen, 47 Spalten.
- `data/04_analysis_results/visual_features/02_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_saturation.csv`: 500 Zeilen, 46 Spalten.
- `data/04_analysis_results/visual_features/03_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_cuts.csv`: 500 Zeilen, 51 Spalten.
- `data/04_analysis_results/visual_features/04_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_angle_face_orientation.csv`: 500 Zeilen, 49 Spalten.
- `data/04_analysis_results/visual_features/05_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_camera_distance.csv`: 500 Zeilen, 49 Spalten.
- `data/04_analysis_results/visual_features/06_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_scene_classification.csv`: 500 Zeilen, 48 Spalten.
- `data/04_analysis_results/visual_features/07_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_skin_smoothness.csv`: 500 Zeilen, 52 Spalten.
- `data/04_analysis_results/visual_features/08_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_aesthetic_quality.csv`: 500 Zeilen, 47 Spalten.
- `data/04_analysis_results/visual_features/09_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_beauty_scoring.csv`: 500 Zeilen, 48 Spalten.
- `data/04_analysis_results/visual_features/10_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_face_emotion.csv`: 500 Zeilen, 50 Spalten.
- `data/04_analysis_results/visual_features/11_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_body_pose.csv`: 500 Zeilen, 48 Spalten.
- `data/04_analysis_results/visual_features/12_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_structural_personen_anzahl.csv`: 500 Zeilen, 49 Spalten.
- `data/04_analysis_results/visual_features/13_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_visual_sharpness.csv`: 500 Zeilen, 48 Spalten.
- `data/04_analysis_results/visual_features/14_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_camera_stability.csv`: 500 Zeilen, 49 Spalten.
- `data/04_analysis_results/visual_features/15_AI_AND_REAL_TIKTOK_VIDEOS_stratified_with_visual_filter.csv`: 500 Zeilen, 49 Spalten.
- `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_all_results_long.csv`: 22500 Zeilen, 51 Spalten.
- `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_all_results_merged.csv`: 500 Zeilen, 114 Spalten.
- `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_engagement_correlations.csv`: 38 Zeilen, 6 Spalten.
- `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_group_differences.csv`: 38 Zeilen, 12 Spalten.
- `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_regression_betas.csv`: 10 Zeilen, 3 Spalten.

### Finale Kommentar-/Text-Ergebnisdateien

- `comments/results/01_caption_sentiment_results.csv`: 1029 Zeilen, 18 Spalten.
- `comments/results/02_comment_sentiment_results.csv`: 39615 Zeilen, 20 Spalten.
- `comments/results/02_comment_sentiment_video_level.csv`: 961 Zeilen, 12 Spalten.
- `comments/results/03_comment_emotion_results.csv`: 39615 Zeilen, 43 Spalten.
- `comments/results/03_comment_emotion_video_level.csv`: 961 Zeilen, 7 Spalten.
- `comments/results/04_comment_topics_engagement_relations.csv`: 15 Zeilen, 6 Spalten.
- `comments/results/04_comment_topics_keywords.csv`: 15 Zeilen, 4 Spalten.
- `comments/results/04_comment_topics_results.csv`: 39593 Zeilen, 14 Spalten.
- `comments/results/04_comment_topics_video_level.csv`: 961 Zeilen, 7 Spalten.

### Comparison-Notebooks

- `comments/01_sentiment_caption/01_sentiment_caption_comparison.ipynb`
- `comments/02_sentiment_comments/02_sentiment_comments_comparison.ipynb`
- `comments/03_comment_emotion/03_comment_emotion_comparison.ipynb`
- `comments/04_comment_topic_analysis/04_comment_topic_analysis_comparison.ipynb`
- `models/01_visual_brightness_contrast/01_visual_brightness_contrast_comparison.ipynb`
- `models/02_visual_saturation/02_saturation_comparison.ipynb`
- `models/03_visual_cuts/03_visual_cuts_comparison.ipynb`
- `models/04_visual_angle_face_orientation/04_angle_face_orientation_comparison.ipynb`
- `models/05_visual_camera_distance/02_camera_distance_comparison.ipynb`
- `models/06_scene_classification/06_scene_classification_comparison.ipynb`
- `models/07_visual_skin_smoothness/07_skin_smoothness_comparison.ipynb`
- `models/08_aesthetic_beauty_scoring/09_aesthetic_beauty_scoring_comparison.ipynb`
- `models/09_aesthetic_aesthetic_quality/08_aesthetic_quality_comparison.ipynb`
- `models/10_face_emotion/10_face_emotion_comparison.ipynb`
- `models/11_body_pose/02_body_pose_comparison.ipynb`
- `models/12_structural_personen_zahl/02_structural_personen_anzahl_comparison.ipynb`
- `models/13_visual_sharpness/12_visual_sharpness_comparison.ipynb`
- `models/14_visual_camera_stability/14_camera_stability_comparison.ipynb`
- `models/15_visual_filter/15_visual_filter_comparison.ipynb`

## 10. Kurzfazit

- Der klarste Befund im Videoteil sind breite VI-vs.-RI-Unterschiede: 29 von 38 numerischen Untermetriken sind signifikant.
- Engagement-Zusammenhänge sind selektiver: 17 von 38 numerischen Video-Untermetriken korrelieren signifikant mit Engagement; die meisten signifikanten Zusammenhänge sind positiv.
- Text-/Kommentarbefunde zeigen besonders bei Kommentar-Sentiment, Kommentar-Emotionen und Topics deutliche Verteilungsunterschiede zwischen VI und RI.
- Die menschliche Evaluation stützt einige maschinelle Kategorien besser als andere: Wahrnehmungsnahe Helligkeit/Kontrast-Merkmale funktionieren deutlich plausibler als Beauty Score, Skin Smoothness oder Personenzahl.
- Für die Arbeit wird zwischen statistischer Signifikanz, Effektgröße und Validität gegenüber der Human-Annotation getrennt: Ein signifikanter Modellunterschied ist nicht automatisch eine hohe menschliche Übereinstimmung.
