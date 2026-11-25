# StudentScope – Week 2: Data Cleaning & Feature Engineering

**SkillMe Data Science Virtual Internship**  
**Week:** 2 – Data Cleaning and Feature Engineering  
**Author:** Dinesh Kumar Pulagalla

## Project Overview

This project focuses on cleaning and preparing the Student Performance dataset for analysis. It builds on the Week 1 Exploratory Data Analysis (EDA) work by standardizing categorical data, handling missing values, creating new features, and encoding categorical variables.

## Dataset Information

- **Dataset:** UCI Student Performance Dataset
- **File:** `student-por.csv`
- **Records:** 649
- **Original Features:** 33
- **Target Variable:** `G3` (Final Grade)

## Tasks Completed

### 1. Data Inspection
- Examined dataset structure and data types.
- Checked unique values in categorical columns.
- Identified missing values.

### 2. Categorical Data Cleaning
- Created a `clean_categories(df)` function.
- Used `.str.strip()` and `.str.lower()` to standardize text.
- Applied mapping dictionaries where required.
- Compared category values before and after cleaning.

### 3. Missing Value Handling
- Checked missing values across the dataset.
- Applied an appropriate missing-value strategy where necessary.
- Validated the cleaned data.

*Note: The original dataset contains no missing values, so no artificial missing values were introduced.*

### 4. Feature Engineering
Created additional analytical features, including:
- `Mjob_group` – grouped mother's job categories.
- `AgeGroup` – grouped students into age categories using `pd.cut()`.

### 5. Categorical Encoding
Used `pd.get_dummies()` to convert selected categorical columns into numerical features for analysis and machine learning.

### 6. Group Comparisons
Repeated group-based comparisons using the cleaned dataset to understand student performance patterns.

### 7. Data Validation
- Checked the cleaned dataset shape.
- Verified missing-value counts.
- Compared category values before and after cleaning.
- Reloaded exported CSV files to verify successful saving.

## Project Structure

```text
Week-2-Data-Cleaning/
│
├── Readme.md
├── StudentScope_Week2.ipynb
├── student-por.csv
│
└── data/
    ├── survey_clean.csv
    └── survey_encoded.csv
```

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab

## Learning Outcomes

- Learned how to clean and standardize categorical data.
- Practiced handling missing values.
- Created new features using feature engineering.
- Applied one-hot encoding.
- Performed group-based comparisons.
- Validated and exported cleaned datasets.

## Output Files

The notebook generates:

- `survey_clean.csv` – cleaned dataset.
- `survey_encoded.csv` – encoded dataset.

These files are created inside the `data/` directory when the corresponding export cells are executed.

## Conclusion

Week 2 strengthened my understanding of data preprocessing, categorical data cleaning, missing-value validation, and feature engineering. These techniques help prepare reliable datasets for further analysis and machine learning.

---

**Author:** Dinesh Kumar Pulagalla  
**GitHub:** https://github.com/dk0009-pv
