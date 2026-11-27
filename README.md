# Tractor Engine Health Monitoring and Fault Detection Using Machine Learning

## Project Overview

This project applies machine learning to tractor engine condition monitoring. It uses operating and sensor-related measurements to classify an engine's **health status** and identify its **fault type**. The aim is to explore how data-driven models can support early identification of abnormal engine behaviour and make condition information easier to interpret.

The dataset used in the project is `tractor.csv`, a **synthetic dataset** containing 500 records. Its origin beyond the project file is not documented; it should not be described as measurements collected from physical tractor tests.

## Project Objective

**To predict tractor engine health status and identify the associated fault type using machine learning models trained on engine operating and sensor data.**

## Dataset

- **Source file:** `tractor.csv`
- **Records:** 500
- **Inputs:** `brand` and `engine_model` (categorical), plus 11 numerical engine operating/sensor readings
- **Prediction targets:** engine health status and fault type
- **Dataset type:** synthetic

### Engine health status distribution

| Health status | Records | Percentage |
|---|---:|---:|
| Healthy | 320 | 64% |
| Abnormal | 180 | 36% |
| **Total** | **500** | **100%** |

### Fault type distribution

| Fault type | Records | Percentage |
|---|---:|---:|
| None | 320 | 64.0% |
| General anomaly | 110 | 22.0% |
| High exhaust temperature | 59 | 11.8% |
| Excessive vibration | 10 | 2.0% |
| Overheating | 1 | 0.2% |
| **Total** | **500** | **100%** |

**Important:** Fault categories are strongly imbalanced. In particular, a single overheating record is insufficient for a reliable assessment of overheating detection.

## Problem Formulation

The project involves two related classification tasks:

1. **Engine health classification:** predict whether an engine is **Healthy** or **Abnormal**.
2. **Fault classification:** predict one of the five fault categories: **None**, **General anomaly**, **High exhaust temperature**, **Excessive vibration**, or **Overheating**.

These outputs are related, but they represent different questions: *Is the engine operating normally?* and *What type of fault does the record indicate?*

## Methodology

### 1. Data exploration

Load `tractor.csv` and inspect the available columns, data types, class counts, descriptive statistics and distributions of numerical readings. Examine the relationship between the operating measurements and the two target labels.

### 2. Data preparation

Separate the input variables from the two targets. Encode categorical inputs (`brand` and `engine_model`) using an appropriate method, and handle any missing or invalid values if present. Where scaling is needed, fit preprocessing transformations only on training data to prevent data leakage.

### 3. Model development

Develop supervised classification models for the health-status and fault-type tasks. The two tasks may be handled by separate classifiers or a suitable multi-output approach, depending on the implementation. The exact algorithms and saved model filenames should be confirmed against the project code before listing them as completed implementations.

### 4. Model evaluation

Evaluate performance using held-out data and suitable classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Per-class support

Because the classes are imbalanced, **macro-averaged F1-score and per-class recall** are especially important. Overall accuracy alone can hide poor performance on rare faults. Use stratified evaluation where feasible, but note that a class with only one observation cannot be meaningfully split between training and testing.

### 5. Prediction workflow

A new engine record supplies the same input features used during training. The record is transformed with the saved preprocessing configuration, passed to the trained classifier(s), and converted into readable outputs:

```text
Tractor brand + engine model + 11 numerical readings
                         |
                         v
                 Data preprocessing
                         |
                         v
                Trained ML model(s)
                         |
              +----------+----------+
              |                     |
              v                     v
       Engine health status      Fault type
       Healthy / Abnormal        Fault category
```

## Understanding the Outputs

| Output | Meaning |
|---|---|
| Healthy | The record is classified as normal by the model |
| Abnormal | The record is classified as indicating an abnormal engine condition |
| None | No fault category is assigned by the fault classifier |
| General anomaly | Abnormal behaviour not assigned to a more specific listed fault |
| High exhaust temperature | The record is classified into the high-exhaust-temperature fault category |
| Excessive vibration | The record is classified into the excessive-vibration fault category |
| Overheating | The record is classified into the overheating fault category |

These are **model predictions**, not confirmed mechanical diagnoses. In a production system, contradictory combinations (such as Healthy together with a specific fault) should be flagged or resolved through a documented consistency rule.

## Technologies

- **Python:** project implementation
- **Pandas and NumPy:** dataset manipulation and numerical analysis
- **Scikit-learn:** classification modelling and evaluation, where used in the project code
- **Matplotlib / Seaborn:** exploratory plots and model visualizations, where used
- **Jupyter Notebook:** exploratory development, where used

## Suggested Repository Layout

The following is a **recommended structure**, not a claim about the existing repository:

```text
tractor-engine-health/
├── README.md
├── data/
│   └── tractor.csv
├── notebooks/
│   └── engine_health_analysis.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
├── models/
│   └── [trained model and preprocessing files]
└── requirements.txt
```

Replace placeholder paths and filenames with the actual project files before publishing.

## How to Run

The exact execution command depends on the final project structure. A typical Python workflow is:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
pip install -r requirements.txt
```

On Windows, activate the environment using `.venv\Scripts\activate`.

Then run the actual training notebook or Python entry point supplied in the repository. Do not assume the suggested `src/train.py` exists unless it has been added.

## Key Findings and Interpretation

The dataset contains substantially more healthy records than abnormal records (320 versus 180). The fault-type distribution is even more uneven: general anomaly and high exhaust temperature account for most abnormal records, while excessive vibration and overheating are rare. This makes fault-specific evaluation essential and limits confidence in predictions for minority fault classes.

Numerical accuracy and F1-score results are intentionally omitted because verified results from the final model have not been supplied here.

## Limitations

1. The dataset is synthetic; it has not been established as real-world tractor sensor data.
2. There are only 500 records, which may limit generalization.
3. Fault classes are severely imbalanced, particularly overheating.
4. The model may learn patterns specific to the synthetic data-generation process.
5. Real-world performance across different engines, loads, operating environments and maintenance conditions has not been demonstrated.
6. A predicted fault label is not a substitute for physical inspection or diagnostic testing.

## Future Scope

- Collect real sensor readings from tractors under documented operating conditions.
- Increase the number of observations for rare fault categories.
- Evaluate models on independent tractors and operating sessions.
- Add time-series information to detect developing faults.
- Calibrate prediction confidence and investigate false alarms.
- Build or refine an interactive dashboard for monitoring engine condition.
- Validate predictions against inspection records and confirmed fault events.

## Conclusion

This project demonstrates a machine-learning workflow for predicting tractor engine health status and fault type from engine operating and sensor-related data. It frames engine monitoring as two connected classification tasks and highlights the importance of careful preprocessing, class-aware evaluation and realistic validation. The current synthetic dataset makes the work suitable for methodological exploration, while real-world deployment would require additional representative data and testing.

---

**Domain:** Agricultural Engineering · Tractor Engines · Machine Learning · Condition Monitoring

**Dataset:** `tractor.csv` · 500 synthetic observations

**Targets:** Engine health status and fault type
