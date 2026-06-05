# Mobile Price Prediction

This repository contains code for predicting the price range of mobile phones based on their hardware features using machine learning. It covers data exploration, feature analysis, model training, and evaluation.

## Dataset

The dataset contains specifications of mobile phones — battery power, RAM, camera, display resolution, connectivity, etc. The target variable `price_range` has four classes:

| Class | Meaning        |
|-------|----------------|
| 0     | Low cost       |
| 1     | Medium cost    |
| 2     | High cost      |
| 3     | Very high cost |

The dataset is provided in two forms inside `data/`:
- `data/raw/` — original Kaggle files (`train.csv`, `test.csv`)
- `data/cleaned/` — preprocessed version used for modeling

See [`data/raw/README.md`](data/raw/README.md) for the full feature dictionary.
**Source:** [Kaggle — Mobile Price Classification](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)

## Project Structure

```
mobile-price-prediction/
├── data/
│   ├── raw/                     # Original Kaggle CSVs
│   └── cleaned/                 # Preprocessed data
├── notebooks/
│   ├── data_analysis.ipynb      # EDA, visualization, correlation
│   └── model_training.ipynb     # Model training & evaluation
├── src/                         # Optional reusable modules
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Contents

- **`data_analysis.ipynb`** — data exploration, visualization, and correlation analysis.
- **`model_training.ipynb`** — training and evaluation of Logistic Regression and K-Nearest Neighbors models.
- **`requirements.txt`** — Python dependencies.
- **`README.md`** — project overview (this file).

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mobile-price-prediction.git
   cd mobile-price-prediction
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # macOS / Linux
   .venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add the dataset**
   Download `train.csv` and `test.csv` from the [Kaggle dataset page](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification) and place them in `data/raw/`.

## Usage

Launch Jupyter and run the notebooks in order:

```bash
jupyter notebook
```

1. `notebooks/data_analysis.ipynb` — explore the data and analyze feature correlations.
2. `notebooks/model_training.ipynb` — train models and evaluate performance.

Modify the code as needed for further analysis or experimentation with different models and parameters.

## Results

### Logistic Regression
- **Training accuracy:** ~96.25%
- **Test accuracy:** ~97.25%
- **Top 5 features positively correlated with price range:** RAM, battery power, display width, display height, internal memory.

### K-Nearest Neighbors (KNN)
- **Training accuracy:** ~95.44%
- **Test accuracy:** ~94.50%
- **Best K (via grid search):** 11, with cross-validated accuracy of ~93.12%.

## Future Improvements

- Explore additional features or transformations to better capture underlying patterns.
- Experiment with other algorithms (SVM, Random Forest, XGBoost) or more complex models.
- Fine-tune hyperparameters for further optimization.
- Handle class imbalance if present in the target variable.
- Report additional metrics such as precision, recall, F1-score, and ROC-AUC for a more comprehensive evaluation.

## Contributors

- **Muntasir Md Nafis**

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
