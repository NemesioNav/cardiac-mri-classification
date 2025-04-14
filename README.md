# MRI Heart Classification Challenge

## Overview
This repository contains a solution to the MRI Heart Classification Challenge that classifies cardiac MRI exams as normal or pathological based on clinical data. The implemented model achieved 86% accuracy using cross-validation, exceeding previously reported results from challenge participants.

## Challenge Description
The challenge involves binary classification of cardiac MRI exams using:
- Clinical information only (first sub-challenge)
- Clinical information combined with Delayed-Enhancement MRI (DE-MRI) exams (second sub-challenge)

Dataset Information
- 100 training cases (67 pathological, 33 normal) with full ground truth
- 50 testing cases (33 pathological, 17 normal) with undisclosed ground truth

**Note:** Since challenge organizers did not release testing set labels, this project relies on cross-validation of the 100 labeled cases. The reported 86% accuracy reflects performance on these cases through cross-validation.

### Data Features
Clinical characteristics used for classification include:
- Demographics: sex, age
- Risk factors: tobacco use, overweight (BMI > 25), arterial hypertension, diabetes, family history
- Clinical measurements: ECG results, troponin values, Killip max score, left ventricle ejection fraction, NTproBNP values

## Methodology
1. **Data Preprocessing:** Loading, EDA, scaling and transformation
2. **Modeling:** Feature selection, model development, hyperparameter tuning, cross-validation

## Results
The implemented approach achieved 86% cross-validation accuracy, comparing favorably to previous results:
- Girum et al.*: 80%
- Shi et al.*: 76%
- Lourenco et al.: 72%

*Teams with challenge organization members (not ranked)

## Project Structure
```
├── notebooks/
│   └── heart_classification.ipynb  # Main analysis notebook
├── scripts/
│   └── utils.py                    # Helper script
├── requirements.txt                # Dependencies
├── LICENSE
└── README.md
```

## Installation & Usage
```bash
git clone https://github.com/yourusername/cardiac-mri-classification.git
cd cardiac-mri-classification

# With conda
conda create -n heart-classification python=3.12.2
conda activate heart-classification
pip install -r requirements.txt

jupyter notebook notebooks/heart_classification.ipynb
```

## Future Work

- Implementation of the second sub-challenge (DE-MRI + clinical data)
- Advanced feature engineering approaches
- Ensemble methods for improved accuracy

## Disclaimer
This project was developed as part of thesis research to validate assumptions. The dataset was provided by the University Hospital of Dijon (France) for the original challenge. The dataset used in this project is available through the official challenge organizers' website.