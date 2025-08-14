# Dokumentation der menschlichen Evaluation und des Modellabgleichs

Der Bericht dokumentiert den Prozess der manuellen Re-Annotation, die Übersetzung der menschlichen Annotationsschemata in die maschinellen Modelloutputs und die berechneten Vergleichsergebnisse.

## Kurzüberblick

- Stichprobe: 50 Videos aus dem influencer-balancierten 500er Videodatensatz, davon 25 VI und 25 RI.
- Sampling-Run: `sample_20260402_173603`.
- Konsolidierte Human-Annotationen: `data/06_human_evaluation_reannotation/human_evaluation_ai_2_annotators.csv` und `data/06_human_evaluation_reannotation/human_evaluation_real_2_annotators.csv`.
- Optionaler Sample-Export: `data/06_human_evaluation_reannotation/reannotation_samples/sample_20260402_173603/` (wird vom Sampling-Notebook erzeugt und ist in dieser Arbeitskopie nicht versioniert).
- Modellvergleich: `data/04_analysis_results/visual_features/99_AI_AND_REAL_TIKTOK_VIDEOS_all_results_merged.csv`.
- Vergleichslogik: 10 graduelle Merkmale als 1-5-Likert-Abgleich, 6 kategoriale Merkmale als Label-Abgleich nach Mapping auf ein gemeinsames Schema.

## 1. Auswahl der Videos

Die Stichprobe wurde im Notebook `data/05_notebooks/04_sample_reannotation_videos.ipynb` erzeugt. Ausgangspunkt war der influencer-balancierte Videodatensatz:

- Metadaten: `data/03_datasets/influencer_balanced/01_AI_AND_REAL_TIKTOK_VIDEOS_stratified_per_influencer_50.csv`
- Videoordner: `data/02_media/stratified_sample/videos`
- Gruppenspalte: `influencer_type`
- Zielgruppen: `ai` und `real`
- Stichprobengröße: `25` Videos pro Gruppe
- Zufallsseed: `42`

Das Notebook hat zuerst geprüft, ob für alle CSV-Zeilen eine lokale Videodatei existiert. Laut Notebook-Output waren 500 von 500 Zeilen mit Videodatei vorhanden. Anschließend wurde pro Gruppe eine Zufallsstichprobe gezogen und in einen neuen Sample-Ordner kopiert. Der Sample-Exportordner ist ein generierter Arbeitsstand; die aktuell versionierten Human-Evaluation-Eingabedaten liegen als konsolidierte CSV-Dateien in `data/06_human_evaluation_reannotation/`.

### Sample-Output (generierbar)

- Gesamtmanifest: `data/06_human_evaluation_reannotation/reannotation_samples/sample_20260402_173603/selected_videos_manifest.csv`
- VI-Manifest: `data/06_human_evaluation_reannotation/reannotation_samples/sample_20260402_173603/selected_videos_manifest_ai.csv`
- RI-Manifest: `data/06_human_evaluation_reannotation/reannotation_samples/sample_20260402_173603/selected_videos_manifest_real.csv`
- VI-Videos: `data/06_human_evaluation_reannotation/reannotation_samples/sample_20260402_173603/ai/`
- RI-Videos: `data/06_human_evaluation_reannotation/reannotation_samples/sample_20260402_173603/real/`

### Verteilung der Stichprobe

| Gruppe | Videos |
|---|---:|
| ai | 25 |
| real | 25 |

| Gruppe | Engagement-Bin | Videos |
|---|---|---:|
| ai | High | 8 |
| ai | Low | 9 |
| ai | Medium | 8 |
| real | High | 8 |
| real | Low | 9 |
| real | Medium | 8 |

### Ausgewählte Videos

Die konkrete Auswahl ist in den generierbaren Manifest-Dateien des Sample-Exports dokumentiert. In der versionierten Arbeitskopie werden die konsolidierten Human-Annotationen verwendet; die kopierten MP4-Dateien des Sample-Exports sind nicht Bestandteil des versionierten Datenstands.

## 2. Manuelles Annotationsschema

Die Annotation wurde über das Label-Studio-Interface `labelstudio/video_labeling_interface.xml` vorbereitet. Annotiert wurde auf Videoebene. Das Interface zeigte Video-ID, Typ, Caption und das Video selbst an. Danach wurden strukturelle, visuelle und qualitative Merkmale vergeben.

### Kategoriale Annotationen

| Menschliche Variable | Schema | Hinweis |
|---|---|---|
| `scene_context` | `home_living_room`, `bathroom_dressing_room`, `beauty_cosmetics_retail`, `studio_set_indoor`, `hospitality_bar_restaurant`, `transport_vehicle_interior`, `urban_outdoor`, `nature_outdoor`, `event_stage_public_venue`, `other_unclear` | Manuelles Oberkategorieschema statt komplettes Places365-Labelset. |
| `face_orientation` | `Frontal`, `Left`, `Right`, `Up`, `Down`, `Unbestimmt` | Dominante Gesichtsrichtung der Hauptperson. |
| `camera_distance` | `closeUp`, `mediumCloseUp`, `mediumShot`, `fullShot`, `longShot`, `extremeLongShot`, `detail`, `ambiguous`, `Unbestimmt` | Dominante Einstellungsgröße. |
| `face_emotion` | `Angry`, `Disgust`, `Fear`, `Happy`, `Neutral`, `Sad`, `Surprise`, `Unbestimmt` | Dominante sichtbare Gesichtsemotion. |
| `body_pose` | `sitting`, `laughing`, `eating`, `listening_to_music`, `calling`, `dancing`, `hugging`, `running`, `clapping`, `drinking`, `sleeping`, `using_laptop`, `fighting`, `texting`, `cycling`, `Unbestimmt` | Dominante körperliche Aktivitaet oder Pose. |
| `personen_anzahl` | `0`, `1`, `2`, `3_plus` | Typische gleichzeitig sichtbare Personenzahl. |

### Likert-Annotationen

Die folgenden graduellen Merkmale wurden auf 5-stufigen Skalen annotiert. `Unbestimmt` war jeweils als gültige Kategorie möglich, wenn das Merkmal nicht belastbar beurteilbar war.

| Menschliche Variable | Bedeutung der Skala |
|---|---|
| `aesthetic_quality_likert` | 1 = sehr niedrige ästhetische Qualität, 5 = sehr hochwertig |
| `beauty_score_likert` | 1 = sehr geringe Attraktivitätsinszenierung, 5 = sehr hoch |
| `brightness_likert` | 1 = sehr dunkel, 5 = sehr hell/überbelichtet |
| `contrast_likert` | 1 = sehr flach/gering, 5 = sehr hoher Hell-Dunkel-Kontrast |
| `camera_stability_likert` | 1 = sehr instabil/wackelig, 5 = sehr stabil/ruhig |
| `cuts_dynamik_likert` | 1 = sehr ruhig/kaum Schnitte, 5 = sehr dynamisch/hektisch |
| `filter_stärke_likert` | 1 = keine Filterwirkung, 5 = sehr starke/stilpraegende Filterwirkung |
| `saturation_likert` | 1 = fast farblos, 5 = sehr bunt/übersättigt |
| `sharpness_likert` | 1 = sehr unscharf, 5 = sehr scharf/klar |
| `skin_smoothness_likert` | 1 = sehr natuerlich/texturiert, 5 = sehr glatt/porenlos |

## 3. Zusammenführung von Human- und Modelldaten

Der Abgleich wurde im Notebook `data/05_notebooks/05_evaluate_human_annotation.ipynb` umgesetzt. Die beiden Human-CSV-Dateien wurden zusammengeführt und über `video_id` mit der finalen Modell-Merge-Datei verbunden.

| Datenquelle | Zeilen | Spalten |
|---|---:|---:|
| Human VI | 25 | 71 |
| Human RI | 25 | 71 |
| Human gesamt | 50 | 71 |
| Modell gesamt | 500 | 114 |

Alle 50 human annotierten Videos konnten mit Modellwerten gematcht werden; es gab 0 Zeilen ohne Modellwerte.

## 4. Übersetzung der Schemas für den Modellvergleich

Die Modelle liefern teils kontinuierliche Scores, teils andere oder feinere Labelsets als die menschliche Annotation. Deshalb wurden die Outputs vor dem Vergleich in ein gemeinsames Evaluationsschema übersetzt.

### Likert-Mapping für kontinuierliche Modellwerte

Für jede kontinuierliche Modellspalte wurde der Minimum- und Maximumwert aus dem gesamten 500er Modell-Datensatz genommen. Der Modellscore wurde linear auf eine 1-5-Skala abgebildet und auf den nächsten ganzzahligen Likert-Wert gerundet:

`Likert = round(((score - min) / (max - min)) * 4 + 1)`, begrenzt auf `1..5`.

| Menschliche Variable | Modellspalte | Modell-Min | Modell-Max |
|---|---|---:|---:|
| `aesthetic_quality_likert` | `aesthetic_quality__aesthetic_quality_score` | 2.051 | 7.528 |
| `beauty_score_likert` | `beauty_scoring__beauty_score_mean` | 14.698 | 85.219 |
| `brightness_likert` | `brightness_contrast__brightness_index` | 15.892 | 199.457 |
| `contrast_likert` | `brightness_contrast__contrast_index` | 33.659 | 88.945 |
| `camera_stability_likert` | `camera_stability__stability_index` | 0.176 | 1 |
| `cuts_dynamik_likert` | `cuts__cuts_per_second` | 0 | 8.45 |
| `filter_stärke_likert` | `visual_filter__filter_strength_prob` | 0.682 | 1 |
| `saturation_likert` | `saturation__saturation_index` | 24.461 | 225.816 |
| `sharpness_likert` | `visual_sharpness__sharpness_laplacian_mean` | 44.93 | 3327.96 |
| `skin_smoothness_likert` | `skin_smoothness__skin_smoothness_highpass_index` | 0.000645 | 0.258 |

### Kategoriales Mapping der Modelllabels

| Menschliche Kategorie | Modellspalte | Mapping-Logik |
|---|---|---|
| `body_pose` | `body_pose__pose_orientation` | `sitting`, `dancing`, `eating` bleiben erhalten; alle anderen Modellposes werden zu `Unbestimmt`. |
| `camera_distance` | `camera_distance__camera_distance_label` | `closeUp` wird zu `mediumCloseUp`; `extremeLongShot` wird zu `longShot`; alle anderen Labels bleiben erhalten. |
| `face_emotion` | `face_emotion__emotion_major_beit_readable` | `Happy`, `Neutral`, `Sad` bleiben erhalten; alle anderen Emotionen werden zu `Unbestimmt`. |
| `face_orientation` | `angle_face_orientation__angle_face_orientation` | `Frontal` und `Left` bleiben erhalten; alle anderen Orientierungen werden zu `Unbestimmt`. |
| `personen_anzahl` | `structural_personen_anzahl__personen_anzahl` | numerisch gebinnt: `<0.5` -> `0`, `<1.5` -> `1`, `<2.5` -> `2`, sonst `3_plus`. |
| `scene_context` | `scene_classification__scene_top1_label` | Places365-Labels werden auf manuelle Oberkategorien gemappt; nicht abgedeckte Szenen werden `other_unclear`. |

### Scene-Context-Mapping im Detail

| Modell-Places365-Labels | Manuelle Kategorie |
|---|---|
| living_room, kitchen, pantry, shower, dressing_room, playroom, berth | `home_living_room` |
| park, forest/broadleaf, desert/sand | `nature_outdoor` |
| racecourse, raceway, runway, boat_deck | `urban_outdoor` |
| stage/indoor, stage/outdoor, discotheque | `event_stage_public_venue` |
| beauty_salon, florist_shop/indoor, ice_cream_parlor | `beauty_cosmetics_retail` |
| art_studio, airplane_cabin, car_interior, laundromat | `studio_set_indoor` |
| alle anderen Labels | `other_unclear` |

## 5. Datenqualität und Missing Values

`Unbestimmt` wurde als gültige Annotation behandelt und nicht als Missing Value. Die folgende Tabelle zeigt echte leere Werte und die Anzahl der nutzbaren Zeilen je Vergleich.

| Typ | Kategorie | n gesamt | Human leer | Modell leer | Zeilen für Klassenmetriken | Zeilen für numerische Fehlermaße |
|---|---|---:|---:|---:|---:|---:|
| likert | `aesthetic_quality_likert` | 50 | 0 | 0 | 50 | 50 |
| likert | `beauty_score_likert` | 50 | 0 | 2 | 50 | 42 |
| likert | `brightness_likert` | 50 | 0 | 0 | 50 | 50 |
| likert | `contrast_likert` | 50 | 0 | 0 | 50 | 50 |
| likert | `camera_stability_likert` | 50 | 0 | 0 | 50 | 50 |
| likert | `cuts_dynamik_likert` | 50 | 0 | 0 | 50 | 50 |
| likert | `filter_stärke_likert` | 50 | 0 | 0 | 50 | 49 |
| likert | `saturation_likert` | 50 | 0 | 0 | 50 | 50 |
| likert | `sharpness_likert` | 50 | 0 | 0 | 50 | 50 |
| likert | `skin_smoothness_likert` | 50 | 0 | 1 | 50 | 45 |
| categorical | `body_pose` | 50 | 0 | 0 | 50 |  |
| categorical | `camera_distance` | 50 | 0 | 0 | 50 |  |
| categorical | `face_emotion` | 50 | 0 | 0 | 50 |  |
| categorical | `face_orientation` | 50 | 0 | 0 | 50 |  |
| categorical | `personen_anzahl` | 50 | 0 | 0 | 50 |  |
| categorical | `scene_context` | 50 | 0 | 0 | 50 |  |

## 6. Ergebnisse: Likert-Merkmale

Für Likert-Merkmale sind zwei Übereinstimmungswerte zentral: `Exact Match` bedeutet exakt gleicher Likert-Wert; `Off-by-1` zählt auch als Übereinstimmung, wenn Human und Modell höchstens eine Likert-Stufe auseinanderliegen. Spearman bezieht sich auf die menschliche Likert-Zahl und den rohen Modellscore.

| Merkmal | n | n numerisch | Spearman | Exact Match | Off-by-1 | MAE Likert | MAE norm. Modellskala |
|---|---:|---:|---:|---:|---:|---:|---:|
| Helligkeit | 50 | 50 | 0.2 | 28% | 86% | 0.86 | 0.202 |
| Kontrast | 50 | 50 | 0.127 | 40% | 86% | 0.76 | 0.196 |
| Aesthetic Quality | 50 | 50 | -0.046 | 18% | 84% | 1.02 | 0.257 |
| Schnittdynamik | 50 | 50 | 0.809 | 60% | 68% | 0.96 | 0.227 |
| Kamerastabilität | 50 | 50 | 0.498 | 32% | 64% | 1.14 | 0.305 |
| Filterstärke | 50 | 49 | 0.312 | 28% | 62% | 1.327 | 0.329 |
| Sättigung | 50 | 50 | 0.317 | 10% | 54% | 1.38 | 0.354 |
| Bildschärfe | 50 | 50 | -0.099 | 0% | 14% | 2.42 | 0.586 |
| Skin Smoothness | 50 | 45 | 0.069 | 2% | 4% | 3.711 | 0.878 |
| Beauty Score | 50 | 42 | 0.235 | 0% | 0% | 2.619 | 0.673 |

### Likert-Ergebnisse nach Gruppe

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

### Interpretation der Likert-Ergebnisse

- Höchste tolerante Übereinstimmung (Off-by-1): Helligkeit (86%), Kontrast (86%), Aesthetic Quality (84%).
- Niedrigste tolerante Übereinstimmung (Off-by-1): Beauty Score (0%), Skin Smoothness (4%), Bildschärfe (14%).
- Exact-Match-Werte sind deutlich strenger, weil schon eine Abweichung um eine Likert-Stufe als Fehler zählt. Für graduelle visuelle Merkmale ist daher Off-by-1 meist die interpretierbarere Kennzahl.

## 7. Ergebnisse: kategoriale Merkmale

| Merkmal | Modellspalte | n | Accuracy | Human-Labels | Modelllabels nach Mapping |
|---|---|---:|---:|---:|---:|
| Gesichtsorientierung | `angle_face_orientation__angle_face_orientation` | 50 | 66% | 3 | 3 |
| Kameradistanz | `camera_distance__camera_distance_label` | 50 | 62% | 6 | 4 |
| Body Pose | `body_pose__pose_orientation` | 50 | 54% | 4 | 4 |
| Gesichtsemotion | `face_emotion__emotion_major_beit_readable` | 50 | 38% | 4 | 4 |
| Szenenkontext | `scene_classification__scene_top1_label` | 50 | 26% | 7 | 6 |
| Personenanzahl | `structural_personen_anzahl__personen_anzahl` | 50 | 24% | 4 | 4 |

### Kategoriale Ergebnisse nach Gruppe

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

### Interpretation der kategorialen Ergebnisse

- Beste kategoriale Übereinstimmung: Gesichtsorientierung (66%), Kameradistanz (62%), Body Pose (54%).
- Schwaechste kategoriale Übereinstimmung: Personenanzahl (24%), Szenenkontext (26%), Gesichtsemotion (38%).
- Besonders bei Szenenkontext, Body Pose und Gesichtsemotion ist die Accuracy auch davon abhängig, wie stark das maschinelle Labelset für den Vergleich verengt wurde.

## 8. Verteilungen der Human-Annotationen

Diese Tabellen zeigen, welche Labels in der Handannotation tatsaechlich vorkamen. Sie helfen einzuschätzen, ob niedrige Übereinstimmungen aus echten Modellfehlern oder aus sehr unausgeglichenen/seltenen Klassen entstehen.

### `aesthetic_quality_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 4_eher_hoch | 32 | 64% |
| 3_mittel | 14 | 28% |
| 5_sehr_hoch | 4 | 8% |

### `beauty_score_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 5_sehr_hoch | 33 | 66% |
| 4_eher_hoch | 11 | 22% |
| Unbestimmt | 6 | 12% |

### `brightness_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 4_eher_hell | 32 | 64% |
| 5_sehr_hell | 10 | 20% |
| 3_mittel | 8 | 16% |

### `contrast_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 3_mittel | 25 | 50% |
| 4_eher_hoch | 22 | 44% |
| 2_eher_gering | 3 | 6% |

### `camera_stability_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 5_sehr_stabil | 29 | 58% |
| 4_eher_stabil | 11 | 22% |
| 3_mittel | 6 | 12% |
| 2_eher_instabil | 4 | 8% |

### `cuts_dynamik_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 1_sehr_ruhig | 30 | 60% |
| 4_dynamisch | 6 | 12% |
| 3_mittel | 6 | 12% |
| 2_eher_ruhig | 5 | 10% |
| 5_sehr_dynamisch | 3 | 6% |

### `filter_stärke_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 4_deutlich | 17 | 34% |
| 5_sehr_stark | 14 | 28% |
| 3_mittel | 9 | 18% |
| 1_keine_filterwirkung | 5 | 10% |
| 2_sehr_leicht | 4 | 8% |
| Unbestimmt | 1 | 2% |

### `saturation_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 3_mittel | 26 | 52% |
| 4_eher_hoch | 20 | 40% |
| 2_eher_gering | 3 | 6% |
| 5_sehr_hoch | 1 | 2% |

### `sharpness_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 4_eher_scharf | 38 | 76% |
| 5_sehr_scharf | 5 | 10% |
| 3_mittel | 5 | 10% |
| 2_eher_unscharf | 2 | 4% |

### `skin_smoothness_likert`

| Wert | n | Anteil |
|---|---:|---:|
| 5_sehr_hoch | 39 | 78% |
| Unbestimmt | 5 | 10% |
| 4_eher_hoch | 5 | 10% |
| 2_eher_niedrig | 1 | 2% |

### `body_pose`

| Wert | n | Anteil |
|---|---:|---:|
| Unbestimmt | 33 | 66% |
| sitting | 14 | 28% |
| dancing | 2 | 4% |
| eating | 1 | 2% |

### `camera_distance`

| Wert | n | Anteil |
|---|---:|---:|
| mediumCloseUp | 22 | 44% |
| mediumShot | 12 | 24% |
| fullShot | 6 | 12% |
| ambiguous | 5 | 10% |
| Unbestimmt | 4 | 8% |
| longShot | 1 | 2% |

### `face_emotion`

| Wert | n | Anteil |
|---|---:|---:|
| Neutral | 23 | 46% |
| Happy | 16 | 32% |
| Unbestimmt | 9 | 18% |
| Sad | 2 | 4% |

### `face_orientation`

| Wert | n | Anteil |
|---|---:|---:|
| Frontal | 31 | 62% |
| Unbestimmt | 13 | 26% |
| Left | 6 | 12% |

### `personen_anzahl`

| Wert | n | Anteil |
|---|---:|---:|
| 1 | 39 | 78% |
| 2 | 7 | 14% |
| 3_plus | 2 | 4% |
| 0 | 2 | 4% |

### `scene_context`

| Wert | n | Anteil |
|---|---:|---:|
| home_living_room | 17 | 34% |
| other_unclear | 16 | 32% |
| nature_outdoor | 7 | 14% |
| urban_outdoor | 4 | 8% |
| studio_set_indoor | 3 | 6% |
| event_stage_public_venue | 2 | 4% |
| beauty_cosmetics_retail | 1 | 2% |

## 9. Kompakte Confusion-Auswertungen

Die folgenden Tabellen listen die häufigsten Human-vs.-Modell-Kombinationen. Die Modellwerte sind bereits auf das jeweilige Evaluationsschema gemappt.

### Likert: Aesthetic Quality

| Human | Modell | n |
|---|---|---:|
| 4 | 3 | 25 |
| 3 | 3 | 7 |
| 4 | 2 | 5 |
| 3 | 2 | 4 |
| 3 | 4 | 3 |
| 4 | 4 | 2 |
| 5 | 2 | 2 |
| 5 | 3 | 1 |
| 5 | 4 | 1 |

### Likert: Beauty Score

| Human | Modell | n |
|---|---|---:|
| 5 | 2 | 23 |
| 4 | 2 | 10 |
| 5 | 3 | 7 |
| Unbestimmt | 2 | 4 |
| 5 | Unbestimmt | 2 |
| Unbestimmt | 3 | 2 |
| 5 | 1 | 1 |
| 4 | 1 | 1 |

### Likert: Helligkeit

| Human | Modell | n |
|---|---|---:|
| 4 | 3 | 22 |
| 4 | 4 | 9 |
| 5 | 3 | 6 |
| 3 | 3 | 4 |
| 5 | 4 | 3 |
| 3 | 2 | 2 |
| 3 | 4 | 2 |
| 5 | 5 | 1 |
| 4 | 2 | 1 |

### Likert: Kamerastabilität

| Human | Modell | n |
|---|---|---:|
| 5 | 4 | 10 |
| 5 | 5 | 9 |
| 4 | 2 | 6 |
| 5 | 3 | 6 |
| 4 | 4 | 4 |
| 3 | 2 | 3 |
| 5 | 2 | 3 |
| 2 | 2 | 2 |
| 3 | 3 | 1 |
| 4 | 3 | 1 |
| 2 | 4 | 1 |
| 3 | 1 | 1 |

### Likert: Kontrast

| Human | Modell | n |
|---|---|---:|
| 3 | 3 | 12 |
| 4 | 3 | 11 |
| 3 | 4 | 7 |
| 4 | 4 | 6 |
| 3 | 2 | 4 |
| 4 | 2 | 4 |
| 2 | 2 | 2 |
| 3 | 1 | 1 |
| 4 | 1 | 1 |
| 3 | 5 | 1 |
| 2 | 3 | 1 |

### Likert: Schnittdynamik

| Human | Modell | n |
|---|---|---:|
| 1 | 1 | 29 |
| 3 | 1 | 6 |
| 2 | 1 | 4 |
| 4 | 1 | 4 |
| 5 | 1 | 3 |
| 4 | 2 | 2 |
| 2 | 2 | 1 |
| 1 | 5 | 1 |

### Likert: Filterstärke

| Human | Modell | n |
|---|---|---:|
| 4 | 5 | 17 |
| 5 | 5 | 14 |
| 3 | 5 | 9 |
| 2 | 5 | 4 |
| 1 | 5 | 3 |
| 1 | 4 | 2 |
| Unbestimmt | 5 | 1 |

### Likert: Sättigung

| Human | Modell | n |
|---|---|---:|
| 3 | 2 | 17 |
| 4 | 2 | 16 |
| 3 | 1 | 6 |
| 4 | 3 | 3 |
| 2 | 2 | 3 |
| 3 | 3 | 2 |
| 4 | 1 | 1 |
| 3 | 4 | 1 |
| 5 | 4 | 1 |

### Likert: Bildschärfe

| Human | Modell | n |
|---|---|---:|
| 4 | 1 | 19 |
| 4 | 2 | 16 |
| 5 | 1 | 4 |
| 3 | 1 | 3 |
| 4 | 3 | 3 |
| 3 | 2 | 2 |
| 2 | 1 | 2 |
| 5 | 2 | 1 |

### Likert: Skin Smoothness

| Human | Modell | n |
|---|---|---:|
| 5 | 1 | 34 |
| 5 | 2 | 5 |
| 4 | 1 | 5 |
| Unbestimmt | 1 | 4 |
| Unbestimmt | Unbestimmt | 1 |
| 2 | 1 | 1 |

### Kategorie: Body Pose

| Human | Modell gemappt | n |
|---|---|---:|
| Unbestimmt | Unbestimmt | 25 |
| sitting | Unbestimmt | 13 |
| Unbestimmt | sitting | 6 |
| dancing | dancing | 1 |
| Unbestimmt | dancing | 1 |
| dancing | Unbestimmt | 1 |
| Unbestimmt | eating | 1 |
| sitting | sitting | 1 |
| eating | Unbestimmt | 1 |

### Kategorie: Kameradistanz

| Human | Modell gemappt | n |
|---|---|---:|
| mediumCloseUp | mediumCloseUp | 21 |
| mediumShot | mediumCloseUp | 6 |
| mediumShot | mediumShot | 6 |
| Unbestimmt | longShot | 4 |
| ambiguous | mediumShot | 4 |
| fullShot | fullShot | 3 |
| fullShot | mediumShot | 2 |
| mediumCloseUp | mediumShot | 1 |
| ambiguous | mediumCloseUp | 1 |
| longShot | longShot | 1 |
| fullShot | longShot | 1 |

### Kategorie: Gesichtsemotion

| Human | Modell gemappt | n |
|---|---|---:|
| Neutral | Neutral | 15 |
| Happy | Neutral | 11 |
| Unbestimmt | Neutral | 8 |
| Neutral | Sad | 5 |
| Neutral | Unbestimmt | 3 |
| Happy | Happy | 3 |
| Sad | Neutral | 2 |
| Happy | Sad | 1 |
| Happy | Unbestimmt | 1 |
| Unbestimmt | Unbestimmt | 1 |

### Kategorie: Gesichtsorientierung

| Human | Modell gemappt | n |
|---|---|---:|
| Frontal | Frontal | 23 |
| Frontal | Unbestimmt | 8 |
| Left | Left | 6 |
| Unbestimmt | Frontal | 6 |
| Unbestimmt | Unbestimmt | 4 |
| Unbestimmt | Left | 3 |

### Kategorie: Personenanzahl

| Human | Modell gemappt | n |
|---|---|---:|
| 1 | 2 | 20 |
| 1 | 3_plus | 10 |
| 1 | 1 | 9 |
| 2 | 3_plus | 3 |
| 2 | 2 | 2 |
| 2 | 1 | 2 |
| 3_plus | 2 | 2 |
| 0 | 0 | 1 |
| 0 | 1 | 1 |

### Kategorie: Szenenkontext

| Human | Modell gemappt | n |
|---|---|---:|
| home_living_room | beauty_cosmetics_retail | 11 |
| other_unclear | studio_set_indoor | 5 |
| nature_outdoor | nature_outdoor | 4 |
| home_living_room | home_living_room | 4 |
| other_unclear | home_living_room | 4 |
| other_unclear | beauty_cosmetics_retail | 4 |
| home_living_room | studio_set_indoor | 2 |
| other_unclear | event_stage_public_venue | 2 |
| event_stage_public_venue | event_stage_public_venue | 2 |
| urban_outdoor | urban_outdoor | 2 |
| nature_outdoor | urban_outdoor | 2 |
| studio_set_indoor | beauty_cosmetics_retail | 2 |
| urban_outdoor | beauty_cosmetics_retail | 1 |
| beauty_cosmetics_retail | beauty_cosmetics_retail | 1 |
| studio_set_indoor | home_living_room | 1 |

## 10. Zusammenfassung

- Über die 10 Likert-Merkmale liegt die mittlere Exact-Match-Rate bei 21.8%; die mittlere Off-by-1-Rate liegt bei 52.2%.
- Über die 6 kategorialen Merkmale liegt die mittlere Accuracy bei 45%.
- Der Abgleich ist für graduelle Scores methodisch konservativ: kontinuierliche Modellwerte werden aus dem globalen Wertebereich in 5 gleich breite Likert-Klassen übersetzt. Dadurch können Abweichungen entstehen, wenn menschliche Wahrnehmung nicht linear mit dem numerischen Modellscore skaliert.
- Bei kategorialen Merkmalen ist der Vergleich stark vom Mapping abhängig, weil mehrere Modelllabels zu `Unbestimmt` oder Oberkategorien zusammengefasst werden.
- Die Stichprobe ist für eine Validierung geeignet, aber mit 50 Videos bewusst klein; die Ergebnisse dienen als Plausibilitäts- und Reliabilitätscheck der Modellannotation, nicht als vollständige externe Validierung aller Modelle.
