# 🫁 Asthma Prediction — Synthetic Health Dataset

**Author:** Eric Inkoom Ayitey  
**Tools:** Python, Streamlit, Scikit-learn, Pandas, Matplotlib  
**Tags:** Machine Learning · Healthcare Analytics · Feature Engineering · Data Visualization · Deployment

---

## 📌 Overview

This project leverages a synthetic health dataset to build and deploy a predictive model for asthma risk estimation. It demonstrates end-to-end data science workflows that are reproducible, clinically interpretable, and deployable via an interactive web app.

Built with scalability and clarity in mind, the project showcases modular preprocessing pipelines, intelligent input handling, and visual storytelling — ideal for health data prototyping in real-world contexts.

---

## 📊 Dataset Summary

The dataset simulates 15 features spanning:

- **Demographic:** Age, Gender, BMI, Family History  
- **Clinical:** FeNO Level, Peak Expiratory Flow, Medication Adherence, Comorbidities  
- **Behavioral:** Physical Activity Level, Smoking Status  
- **Environmental:** Air Pollution Level, Allergies  
- **Utilization & Outcome:** ER Visits, Asthma Control Level, Has_Asthma (target)

---

## 🔍 Exploratory Insights

- **Asthma prevalence:** Imbalanced classes — majority of records show absence of asthma
- **FeNO levels & ER visits:** Top correlates with asthma incidence
- **Environmental influence:** Air pollution and physical activity levels impact asthma control trends
- **Categorical imputation:** Mode-based fill strategy for robustness and simplicity

---

## 🧠 Modeling Highlights

- ✅ **Pipeline-based training** using `ColumnTransformer` + `RandomForestClassifier`
- 🔁 **Automatic encoding/scaling** of inputs within pipeline for consistent inference
- 🔍 **Feature importance visualization** with teal-themed horizontal bar plots and crisp value labels

---

## 🔢 Evaluation Metrics

| Metric               | Value  |
|----------------------|--------|
| Accuracy             | 0.947  |
| Precision (Class 0)  | 0.96   |
| Recall (Class 0)     | 0.98   |
| F1 Score (Class 0)   | 0.97   |
| Precision (Class 1)  | 0.92   |
| Recall (Class 1)     | 0.86   |
| F1 Score (Class 1)   | 0.89   |
| ROC AUC Score        | 0.9909 |

🧮 **Confusion Matrix**  
      [[1467 37]
      [ 69 427]]


📊 These results show strong overall accuracy with balanced precision and recall across classes. Class 1 (asthma-positive) predictions have high precision, making the model suitable for cautious clinical screening applications.

---

## 🖼️ Visual Snapshot

This section features a curated selection of visuals that explore demographic, behavioral, and environmental patterns linked to asthma risk:

1. 🧑‍🤝‍🧑 Gender Distribution & Asthma Prevalence
Alt Text: Grouped bar chart showing asthma prevalence by gender Caption: Female and male groups show similar asthma rates, with a lower prevalence among nonbinary/other individuals. Embed Code:

![Asthma vs Gender: Grouped bar chart showing asthma prevalence by gender](image1.png)


2. 🚬 Smoking Status vs Asthma Risk
Alt Text: Bar chart comparing asthma occurrence across smoking categories Caption: Current smokers exhibit the highest asthma prevalence, underscoring the health impact of smoking behavior. Embed Code:

![Smoking Status vs Asthma: Bar chart comparing asthma occurrence across smoking categories](image2.png)


3. 🌾 Allergy Types & Asthma Correlation
Alt Text: Bar chart showing asthma cases linked to different allergy types Caption: Dust and pollen allergies lead the way in asthma association — key factors in environmental risk modeling. Embed Code:

![Allergy Type vs Asthma: Bar chart showing asthma cases linked to different allergy types](image3.png)


4. 📈 Target Variable Distribution
Alt Text: Bar chart illustrating the number of asthma-positive vs asthma-negative cases Caption: Dataset imbalance with more negative cases informs model evaluation strategy and handling of precision-recall trade-offs. Embed Code:

![Has Asthma Distribution: Bar chart illustrating the number of asthma-positive vs asthma-negative cases](image4.png)

---

## 🌐 Deployment

The app is deployed via **Streamlit Community Cloud** and accepts 14 patient features. It uses a trained ML pipeline to dynamically encode and scale user inputs, returning predicted asthma likelihood in real time.

### Access:

👉 [Live App](https://asthma-prediction-app-edksy83arxrfajqyzfnmtv.streamlit.app/)  

### Files Included:

- `app.py`: Streamlit interface  
- `asthma_prediction_pipeline.pkl`: Serialized ML pipeline  
- `asthma_banner.png`: Custom banner image  
- `requirements.txt`: Environment dependencies

---

## 🌍 Real-World Value

- A prototype for asthma screening and education tools  
- Supports community-level analytics in the Global South  
- Provides a reusable foundation for deploying disease models

---

## 📂 Artifacts

| File                          | Description                                  |
|------------------------------|----------------------------------------------|
| `Asthma_Prediction.ipynb`    | Clean analysis notebook with modeling flow   |
| `Asthma_Visuals.html`        | Exported standalone HTML report              |
| `README.md`                  | Project overview and technical guide         |
| `uvfExsgG4VNtcLH513brr.png`  | Feature importance plot for visual impact    |
| `F4YCi1T5sJFQYUefMPiLj.png`  | Evaluation matrix and confusion insights     |

---

### 🧪 Future Additions

- SHAP-based interpretability  
- Real-world data validation  
- Model comparison (e.g., XGBoost vs RandomForest)  
- GitHub Actions for CI/CD

---

🚀 Built for scalable health intelligence — from notebook to user-facing app.  
Made with clarity, impact, and reproducibility in mind.
