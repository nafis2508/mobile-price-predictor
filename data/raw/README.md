# Data Dictionary — Mobile Price Classification

Dataset: **Mobile Price Classification**  
Source: [Kaggle](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)  
Author: Abhishek Sharma  
Files: `train.csv` (2,000 rows), `test.csv` (1,000 rows)

---

## Files

| File | Rows | Columns | Description |
|------|------|---------|-------------|
| `train.csv` | 2,000 | 21 | Training data with target label `price_range` |
| `test.csv` | 1,000 | 20 | Test data (no `price_range`; used for predictions) |

---

## Column Descriptions

| # | Column | Type | Description |
|---|--------|------|-------------|
| 1 | `battery_power` | int | Total energy a battery can store (mAh) |
| 2 | `blue` | bool | Has Bluetooth (1 = yes, 0 = no) |
| 3 | `clock_speed` | float | Processor speed (GHz) |
| 4 | `dual_sim` | bool | Supports dual SIM (1 = yes, 0 = no) |
| 5 | `fc` | int | Front camera megapixels |
| 6 | `four_g` | bool | Has 4G (1 = yes, 0 = no) |
| 7 | `int_memory` | int | Internal memory (GB) |
| 8 | `m_dep` | float | Mobile depth (cm) |
| 9 | `mobile_wt` | int | Mobile weight (grams) |
| 10 | `n_cores` | int | Number of processor cores |
| 11 | `pc` | int | Primary camera megapixels |
| 12 | `px_height` | int | Pixel resolution height |
| 13 | `px_width` | int | Pixel resolution width |
| 14 | `ram` | int | RAM (MB) |
| 15 | `sc_h` | int | Screen height (cm) |
| 16 | `sc_w` | int | Screen width (cm) |
| 17 | `talk_time` | int | Longest single battery charge talk time (hours) |
| 18 | `three_g` | bool | Has 3G (1 = yes, 0 = no) |
| 19 | `touch_screen` | bool | Has touch screen (1 = yes, 0 = no) |
| 20 | `wifi` | bool | Has WiFi (1 = yes, 0 = no) |
| 21 | `price_range` | int | **Target** — price category (0, 1, 2, 3); only in `train.csv` |

---

## Data Quality Notes

- **No missing values** in either file.
- All boolean features are encoded as `0` / `1`.
- All features are numeric — no categorical strings.
- Pixel resolution (`px_height`, `px_width`) can be combined into total pixels if needed.
- Feature scaling is recommended for distance-based algorithms (k-NN, SVM).

---

## Target Distribution (train.csv)

| `price_range` | Meaning | Count |
|---------------|---------|-------|
| 0 | Low cost | ~500 |
| 1 | Medium cost | ~500 |
| 2 | High cost | ~500 |
| 3 | Very high cost | ~500 |

Balanced dataset — ~25% per class.
