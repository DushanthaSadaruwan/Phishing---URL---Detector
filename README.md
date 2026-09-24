# AI-Based Phishing URL Detection System Using Machine Learning

## Project Overview

This project presents a machine-learning-based approach for detecting potentially phishing URLs using measurable characteristics extracted directly from URL strings.

The system converts each URL into a numerical feature set and uses supervised machine-learning models to classify URLs as either **Phishing** or **Legitimate**.

The project was developed as a cybersecurity and machine-learning project to demonstrate a practical workflow covering data preparation, data cleaning, feature engineering, exploratory data analysis, model training, model evaluation, and URL prediction.

---

## Project Objectives

The main objectives of this project are to:

- Analyze a labelled phishing URL dataset.
- Perform data-quality checking and duplicate removal.
- Extract numerical features from URL strings.
- Explore differences between phishing and legitimate URLs.
- Train supervised machine-learning classification models.
- Evaluate model performance using standard classification metrics.
- Develop a reusable phishing URL classification prototype.
- Establish a foundation for future cybersecurity and machine-learning research.

---

## Dataset

The project uses a labelled URL dataset containing **549,346 initial records**.

### Dataset Summary

| Measure | Result |
|---|---:|
| Initial records | 549,346 |
| Missing URL values | 0 |
| Missing Label values | 0 |
| Duplicate records | 42,150 |
| Records after duplicate removal | 507,196 |

### Dataset Classes

| Label | Meaning |
|---|---|
| `good` | Legitimate URL |
| `bad` | Phishing URL |

For machine-learning purposes, the labels were encoded as:

```text
good → 0
bad  → 1
```

### Initial Class Distribution

| Class | Records |
|---|---:|
| Good | 392,924 |
| Bad | 156,422 |

The dataset is therefore imbalanced, with more legitimate URLs than phishing URLs. This is an important consideration when interpreting model performance.

---

## Features Used

The final model uses five lexical URL features extracted directly from the URL string.

| Feature | Description |
|---|---|
| `url_length` | Total number of characters in the URL |
| `num_dots` | Number of `.` characters in the URL |
| `num_hyphens` | Number of `-` characters in the URL |
| `num_at` | Number of `@` characters in the URL |
| `num_digits` | Number of numeric digits in the URL |

These features are extracted without visiting the destination webpage.

This makes the feature-extraction stage lightweight and suitable for demonstrating a URL-level phishing detection approach.

---

## Project Workflow

```text
Dataset
   ↓
Data Quality Checking
   ↓
Duplicate Removal
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
Train/Test Split
   ↓
Machine Learning
   ↓
Model Evaluation
   ↓
URL Prediction
   ↓
Model Saving
```

---

## Data Preparation

The dataset was first inspected to understand its size, structure, missing values, and duplicate records.

The analysis identified:

- 549,346 initial records.
- No missing values in the `URL` and `Label` columns.
- 42,150 duplicate records.

Duplicate records were removed before the main modelling experiment.

After duplicate removal, the dataset contained:

```text
507,196 records
```

---

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the characteristics of the dataset and investigate whether the extracted URL features showed useful differences between the two classes.

The analysis included:

- Class distribution
- URL length analysis
- Number of dots
- Number of hyphens
- Number of `@` symbols
- Number of digits
- Feature comparison
- Correlation analysis
- Distribution analysis using boxplots

---

## Average Feature Values

The recorded mean values for the extracted features were:

| Feature | Bad URLs | Good URLs |
|---|---:|---:|
| URL length | 63.2176 | 45.7675 |
| Number of dots | 2.7668 | 1.7819 |
| Number of hyphens | 0.6095 | 1.3323 |
| Number of `@` symbols | 0.0119 | 0.0007 |
| Number of digits | 8.8789 | 3.1334 |

These values are descriptive observations from the dataset. They should not be interpreted as standalone rules for determining whether a URL is malicious.

---

## Correlation Analysis

The recorded correlations with the numerical target label were:

| Feature | Correlation with Target |
|---|---:|
| `num_dots` | 0.293474 |
| `num_hyphens` | -0.134541 |
| `num_at` | 0.074363 |
| `num_digits` | 0.224053 |
| `url_length` | 0.177295 |

The strongest feature-to-feature correlation observed in the recorded correlation matrix was:

```text
num_digits ↔ url_length = 0.772517
```

Correlation represents statistical association and does not establish causation.

---

# Machine Learning

## Supervised Classification

This project is formulated as a supervised binary classification problem.

The model receives five numerical URL features as input and learns to predict one of two classes:

```text
0 → Legitimate
1 → Phishing
```

---

## Train/Test Split

The cleaned dataset was divided into training and testing subsets using an 80/20 split.

```text
Training data → 80%
Testing data  → 20%
```

A fixed `random_state=42` was used to improve reproducibility.

For the cleaned 507,196-row dataset, the recorded split corresponds to:

```text
Training set: 405,756 records
Test set:     101,440 records
```

For future experiments involving the imbalanced dataset, stratified splitting should also be considered.

---

## Models Evaluated

Two primary machine-learning approaches were evaluated:

1. Logistic Regression
2. Random Forest

A separate experiment was also performed using a class-balanced Random Forest.

---

# Logistic Regression

Logistic Regression was used as a baseline classification model.

It estimates the probability of a binary outcome using a weighted combination of the input features.

### Recorded Results

| Metric | Result |
|---|---:|
| Accuracy | 82.55% |
| Phishing Precision | 82% |
| Phishing Recall | 28% |
| Phishing F1-score | 42% |

The model achieved reasonable overall accuracy, but the phishing-class recall was comparatively low.

This means that a significant number of phishing examples were not detected by the baseline model.

---

# Random Forest

Random Forest was used as a non-linear tree-based classification model.

A Random Forest combines predictions from multiple decision trees to produce a final classification.

The model can capture non-linear relationships and interactions between features.

### Recorded Results

The following results were obtained on the same 101,440-row test experiment used for the main Logistic Regression comparison:

| Metric | Result |
|---|---:|
| Accuracy | 85% |
| Phishing Precision | 79% |
| Phishing Recall | 46% |
| Phishing F1-score | 58% |

---

## Random Forest Classification Results

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good | 0.86 | 0.97 | 0.91 | 78,736 |
| Bad | 0.79 | 0.46 | 0.58 | 22,704 |
| Accuracy | — | — | 0.85 | 101,440 |
| Macro Average | 0.83 | 0.71 | 0.75 | 101,440 |
| Weighted Average | 0.85 | 0.85 | 0.84 | 101,440 |

---

## Confusion Matrix

The recorded Random Forest confusion matrix was:

```text
                 Predicted
              Good      Bad

Actual Good   76043     2693

Actual Bad    12279     10425
```

This corresponds to:

| Measure | Value |
|---|---:|
| True Negatives (TN) | 76,043 |
| False Positives (FP) | 2,693 |
| False Negatives (FN) | 12,279 |
| True Positives (TP) | 10,425 |

### Interpretation

- **True Negative:** A legitimate URL correctly classified as legitimate.
- **False Positive:** A legitimate URL incorrectly classified as phishing.
- **False Negative:** A phishing URL incorrectly classified as legitimate.
- **True Positive:** A phishing URL correctly classified as phishing.

In a phishing-detection context, false negatives are particularly important because they represent phishing URLs that were missed by the classifier.

---

# Balanced Random Forest

A separate Random Forest experiment was performed using:

```python
class_weight="balanced"
```

This approach gives greater importance to the minority class during model training.

### Recorded Results

| Metric | Result |
|---|---:|
| Accuracy | 79% |
| Phishing Precision | 64% |
| Phishing Recall | 64% |
| Phishing F1-score | 64% |

This experiment used a different test-set composition after the dataset was reloaded. Therefore, these results should be treated as a separate experiment rather than a directly controlled comparison with the standard Random Forest result.

---

# Model Comparison

The main recorded experiments can be summarized as follows:

| Model | Test Size | Accuracy | Phishing Recall | Phishing F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 101,440 | 82.55% | 28% | 42% |
| Random Forest | 101,440 | 85% | 46% | 58% |
| Balanced Random Forest | 109,870 | 79% | 64% | 64% |

The Balanced Random Forest result should not be interpreted as a direct head-to-head comparison because it was evaluated using a different test-set composition.

---

# URL Prediction

After training, the model can receive a new URL and calculate the same five features used during training.

Example:

```text
https://example.com
```

The system extracts:

```text
num_dots
num_hyphens
num_at
num_digits
url_length
```

These values are then passed to the trained classifier.

### Recorded Example

```text
Input URL:
https://example.com

Prediction:
Legitimate
```

The prediction demonstrates the complete flow from raw URL input to machine-learning classification.

---

# Model Saving

The trained model was serialized using Joblib so that it can be reused later without retraining from the beginning.

The model file is kept private and is intentionally not included in the public repository.

```text
phishing_url_detector.pkl
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Jupyter Notebook
- Visual Studio Code

---

# Project Structure

The public repository is intentionally kept lightweight.

```text
phishing-url-detector/
│
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
│
└── docs/
    └── PROJECT_DOCUMENTATION.md
```

Private project files such as the complete source code, dataset, notebook, and trained model are maintained separately.

---

# Repository Privacy

The public GitHub repository contains project documentation and selected project information.

The following project assets are intentionally kept private:

- Complete source code
- Full Jupyter Notebook
- Dataset
- Trained machine-learning model
- Local experimental files

This structure allows the project to be presented professionally on GitHub while keeping the complete implementation private.

> **Note:** Files that are uploaded to a public GitHub repository should be considered public. `.gitignore` prevents future tracking of matching files but does not remove files that were already committed to Git history.

---

# Limitations

The current prototype has several limitations:

- It uses only five URL-level features.
- It does not inspect webpage content.
- It does not analyze JavaScript.
- It does not use DNS information.
- It does not use SSL/TLS certificate information.
- It does not use real-time threat intelligence.
- It does not perform webpage crawling.
- The dataset contains class imbalance.
- The current evaluation contains experiments with different dataset states.
- The saved model should be versioned clearly in future experiments.

Therefore, the current implementation should be considered a **machine-learning research and learning prototype**, rather than a production-ready phishing defence system.

---

# Future Improvements

Possible future improvements include:

### Feature Engineering

- Additional URL characteristics
- Suspicious keyword detection
- URL entropy
- Path depth
- Query-string analysis
- Domain-related features

### Security Intelligence

- DNS information
- Domain age
- SSL/TLS certificate information
- Redirect analysis
- Threat-intelligence feeds

### Machine Learning

- Stratified cross-validation
- Hyperparameter tuning
- Feature selection
- Ensemble optimization
- Probability calibration

### Advanced Research

- Explainable AI
- NLP-based phishing detection
- Transformer-based models
- Deep-learning approaches
- Behavioural analysis
- Automated security response

These improvements can help extend the project from a simple lexical URL classifier toward a more comprehensive cybersecurity detection framework.

---

# Project Significance

This project demonstrates how cybersecurity problems can be approached using machine learning.

The project connects several important technical areas:

```text
Cybersecurity
      +
Python Programming
      +
Data Analysis
      +
Feature Engineering
      +
Machine Learning
      +
Model Evaluation
```

The work also provides a practical foundation for future research into intelligent phishing detection and broader cyber-resilience systems.

---

# Documentation

Detailed technical documentation is maintained separately and covers:

- Project methodology
- Dataset analysis
- Data preparation
- Feature engineering
- Exploratory Data Analysis
- Machine-learning methodology
- Model evaluation
- Experimental results
- Limitations
- Future improvements

---

# Author

**Dushantha Sadaruwan**

IT Undergraduate | Cybersecurity & Network Engineering

### Project

**AI-Based Phishing URL Detection System Using Machine Learning**

---

## Disclaimer

This project is developed for educational, research, and cybersecurity learning purposes.

The system is a prototype and should not be considered a complete replacement for enterprise-grade phishing detection, threat intelligence, endpoint protection, secure web gateways, or other professional security controls.
