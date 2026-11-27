# StudentScope — Student Lifestyle & Performance Explorer

**SkillMe Data Science Virtual Internship | Four-Week End-to-End Data Science Project**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Internship-Completed-success)

## Project Overview

**StudentScope** is an end-to-end Data Science and Machine Learning project developed during the four-week Data Science Virtual Internship at SkillMe.

The project explores relationships between student lifestyle, study habits, home resources, and academic performance using the UCI Student Performance Dataset.

It covers the complete data science lifecycle, from exploratory data analysis and preprocessing to statistical analysis, predictive modeling, and interactive dashboard development using Streamlit.

## Project Objectives

- Explore and analyze real-world student performance data.
- Identify patterns in study habits and academic performance.
- Perform data cleaning, feature engineering, and data validation.
- Conduct statistical comparisons and hypothesis testing.
- Develop and evaluate machine learning classifiers.
- Present analytical insights through an interactive dashboard.
- Understand model limitations and responsible machine learning practices.

## Dataset Information

| Attribute | Description |
|---|---|
| Dataset | UCI Student Performance |
| Course | Portuguese Language |
| Total Records | 649 |
| Original Features | 33 |
| Cleaned Dataset Columns | 35 |
| Missing Values | 0 |
| Main Analysis Variable | G3 – Final Grade |
| Grade Range | 0–20 |
| Dataset Coverage | Two Portuguese schools |

**Dataset Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/320/student+performance)

**Dataset Authors:** Paulo Cortez and Alice Silva

**DOI:** 10.24432/C5TG7T

## Project Workflow

```text
Raw Dataset
     ↓
Exploratory Data Analysis
     ↓
Data Cleaning & Feature Engineering
     ↓
Statistical Analysis & Hypothesis Testing
     ↓
Machine Learning & Model Evaluation
     ↓
Interactive Streamlit Dashboard
```

## Internship Progress

| Week | Module | Status |
|---|---|---|
| Week 1 | Exploratory Data Analysis | Completed |
| Week 2 | Data Cleaning & Feature Engineering | Completed |
| Week 3 | Statistical Analysis & Machine Learning | Completed |
| Week 4 | Interactive Streamlit Dashboard | Completed |

## Week 1 — Exploratory Data Analysis (EDA)

Focused on understanding the dataset, exploring student characteristics, and identifying academic performance patterns.

### Work Completed

- Dataset loading and inspection using Pandas.
- Descriptive statistical analysis.
- Categorical and numerical variable analysis.
- Missing-value identification.
- Grouped student performance comparisons.
- Data visualization using Matplotlib and Seaborn.
- Cross-tabulation and heatmap analysis.

### Key Findings

| Metric | Result |
|---|---:|
| Student records | 649 |
| Original columns | 33 |
| GP school students | 423 |
| MS school students | 226 |
| Average final grade | 11.91/20 |
| Highest mean grade by study-time category | 13.23/20 |
| Missing values | 0 |

Study-time category 3 recorded the highest average final grade among the four study-time categories.

## Week 2 — Data Cleaning & Feature Engineering

Focused on preparing a reliable and structured dataset for further statistical analysis and machine learning.

### Work Completed

- Standardized categorical values using Pandas string methods.
- Applied mapping dictionaries for categorical grouping.
- Documented missing-value handling strategies.
- Created `Mjob_group` to group mother's occupation categories.
- Created `AgeGroup` using `pd.cut()`.
- Applied one-hot encoding using `pd.get_dummies()`.
- Repeated grouped comparisons using cleaned data.
- Implemented data-quality validation checks.
- Exported cleaned and encoded datasets.

### Key Results

| Metric | Result |
|---|---:|
| Original records | 649 |
| Cleaned records | 649 |
| Original columns | 33 |
| Cleaned dataset columns | 35 |
| New engineered features | 2 |
| Missing values after cleaning | 0 |

### Generated Outputs

- `survey_clean.csv`
- `survey_encoded.csv`

## Week 3 — Statistical Analysis & Machine Learning

Focused on identifying statistically meaningful patterns and developing supervised machine learning classifiers.

### Work Completed

- Calculated grouped means, medians, and student counts.
- Applied Welch's t-test for statistical significance.
- Selected five relevant input features.
- Created a binary classification target.
- Applied feature scaling and categorical encoding.
- Implemented a stratified 80/20 train-test split.
- Trained Logistic Regression and Random Forest classifiers.
- Evaluated models using accuracy, precision, recall, F1-score, and confusion matrices.
- Analyzed class imbalance and model limitations.

### Statistical Analysis Results

| Metric | Result |
|---|---:|
| Lowest study-time band mean grade | 10.84 |
| Higher study-time bands mean grade | 12.42 |
| Mean grade difference | 1.58 |
| Welch p-value | 7.015 × 10⁻⁹ |
| Significance level | 0.05 |

The results indicate a statistically significant difference between the study-time groups. However, statistical association does not establish causation.

### Machine Learning Features

| Feature | Description |
|---|---|
| `studytime` | Weekly study-time category |
| `failures` | Previous class failures |
| `traveltime` | Home-to-school travel-time category |
| `internet` | Internet availability at home |
| `Mjob_group` | Grouped mother's occupation |

### Classification Target

- **Below 10:** Final grade below 10.
- **10 or above:** Final grade greater than or equal to 10.

The grade columns `G1`, `G2`, and `G3` were excluded from predictors to prevent target leakage.

### Model Configuration

| Parameter | Value |
|---|---|
| Training split | 80% |
| Testing split | 20% |
| Training records | 519 |
| Testing records | 130 |
| Random state | 42 |
| Stratification | Enabled |

### Model Performance

| Model | Test Accuracy |
|---|---:|
| Logistic Regression | 83.85% |
| Random Forest | 83.08% |
| Majority-Class Baseline | 84.62% |

### Model Interpretation

Although Logistic Regression achieved 83.85% test accuracy, it recorded 0.00% recall for the Below-10 category.

Both classifiers performed below the majority-class baseline, demonstrating that accuracy alone is insufficient when evaluating imbalanced classification problems.

## Week 4 — Interactive Streamlit Dashboard

Transformed the previous three weeks of data analysis, statistical findings, and machine learning results into an interactive data science application.

### Dashboard Features

**Interactive Filters**

- School selection — GP/MS.
- Address type — Urban/Rural.
- Internet availability — Yes/No.
- Dynamic summary metrics and visualizations.
- Empty-selection validation.

**Student Performance Analysis**

- Grade distribution charts.
- Grouped statistical comparisons.
- Student performance summary metrics.
- Filtered dataset exploration.

**Statistical Evidence**

- Grouped mean and median results.
- Welch's hypothesis test results.
- Statistical significance interpretation.

**Machine Learning Evaluation**

- Logistic Regression evaluation.
- Random Forest comparison.
- Classification metrics.
- Confusion matrix.
- Majority-class baseline comparison.

**Interactive Prediction Form**

- Five selectable input features.
- Predicted grade-band category.
- Estimated model probabilities.

**Data Export**

- Download filtered student records as a CSV file.

**Automated Validation**

- Filter logic validation.
- Full and empty selection checks.
- Week 3 metric reproduction.
- Prediction validation covering all 512 selectable input combinations.

The analytical calculations and validation notebook were executed locally. Browser-level Streamlit interaction testing remains to be confirmed.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Statistical Analysis | SciPy |
| Machine Learning | Scikit-learn |
| Data Visualization | Matplotlib, Seaborn |
| Dashboard Development | Streamlit |
| Development Tools | Google Colab, Jupyter Notebook, VS Code |
| Testing | Python Automated Validation |
| Version Control | Git, GitHub |

## How to Run the Streamlit Dashboard

### Prerequisites

Python 3.10–3.12 is recommended.

Open a terminal in the Week 4 dashboard directory.

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Run Automated Tests

```bash
python test_dashboard_logic.py
```

### Launch the Application

```bash
python -m streamlit run app.py
```

Open the application in your browser:

http://localhost:8501

Windows users can alternatively launch the application using `RUN_WEEK4.bat`.

The dataset is bundled with the application. No external API key or additional dataset download is required.

## Project Screenshots

### Week 1 — Exploratory Data Analysis

Dataset exploration, descriptive statistics, and student performance visualizations.

### Week 2 — Data Cleaning & Feature Engineering

Categorical standardization, engineered features, and data-quality validation.

### Week 3 — Statistical Analysis & Machine Learning

Statistical comparisons, classification reports, and confusion matrices.

### Week 4 — Interactive Streamlit Dashboard

Interactive filters, dynamic visualizations, model evaluation, and grade-band prediction form.

## Key Project Achievements

- Completed all four weeks of the Data Science Virtual Internship.
- Analyzed 649 real-world student records across 33 original features.
- Prepared a cleaned dataset containing 35 columns with zero missing values.
- Identified a 1.58-point mean grade difference between study-time groups.
- Implemented statistical hypothesis testing.
- Developed and evaluated two supervised machine learning classifiers.
- Developed an interactive Streamlit dashboard.
- Implemented automated validation covering 512 prediction input combinations.
- Identified class imbalance and limitations of accuracy-based model evaluation.

## Skills Developed

- Python Programming
- Exploratory Data Analysis
- Data Cleaning and Preprocessing
- Feature Engineering
- Statistical Analysis
- Hypothesis Testing
- Supervised Machine Learning
- Classification Model Evaluation
- Data Visualization
- Interactive Dashboard Development
- Software Testing and Validation
- Git and GitHub
- Technical Documentation

## Limitations

- The dataset represents students from only two Portuguese schools.
- The historical dataset may not represent current student populations.
- Study-time categories represent time bands rather than exact hours.
- Statistical associations do not establish causation.
- Class imbalance affects minority-class prediction performance.
- Model probabilities are not calibrated.
- The models are educational baselines and are unsuitable for high-stakes academic decisions.

## Future Enhancements

- Implement class-weighted classification models.
- Improve minority-class recall.
- Apply cross-validation and hyperparameter tuning.
- Explore additional machine learning algorithms.
- Introduce model explainability techniques such as SHAP.
- Enhance dashboard visualizations and interactive features.
- Validate models using additional datasets.
- Deploy the dashboard after completing browser-level testing.

## Conclusion

StudentScope demonstrates the complete data science lifecycle, from raw data exploration and preprocessing to statistical analysis, predictive modeling, and interactive application development.

Through this four-week internship, I gained practical experience in transforming real-world data into meaningful insights, developing machine learning models, and building an interactive dashboard.

The project also highlights the importance of data quality, reproducibility, responsible machine learning, and critical evaluation of model performance.

## Acknowledgements

- **SkillMe** — for providing the Data Science Virtual Internship and hands-on learning opportunity.
- **UCI Machine Learning Repository** — for providing the Student Performance Dataset.
- **Paulo Cortez and Alice Silva** — for the original dataset.

## Author

**Dinesh Kumar Pulagalla**

B.Tech — Artificial Intelligence & Data Science

- **GitHub:** [dk0009-pv](https://github.com/dk0009-pv)
- **LinkedIn:** [Dinesh Kumar Pulagalla](https://www.linkedin.com/in/dinesh-kumar-pulagalla-670bb2345/)
- **Project:** [StudentScope](https://github.com/dk0009-pv/StudentScope-Student-Performance-Analysis)

---

**Internship Status:** Completed — All Four Weeks

*Exploring Data. Discovering Insights. Building Intelligent Solutions.*
