# StudentScope — Week 1: Exploratory Data Analysis (EDA)

**Student Lifestyle & Performance Explorer | SkillMe Data Science Virtual Internship**

**Author:** Dinesh Kumar Pulagalla

## Project Overview

StudentScope is a data science project designed to explore the relationships between student lifestyle, study habits, home resources, and academic performance.

Week 1 focuses on Exploratory Data Analysis (EDA) using Python to understand the dataset, identify patterns, summarize student characteristics, and visualize academic performance.

## Dataset Information

| Attribute | Description |
|---|---|
| Dataset | UCI Student Performance |
| Course | Portuguese Language |
| File | `student-por.csv` |
| Total Records | 649 |
| Original Columns | 33 |
| Missing Values | 0 |
| Main Analysis Variable | G3 – Final Grade |
| Grade Range | 0–20 |

**Dataset Source:** [UCI Machine Learning Repository – Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance)

## Project Objectives

- Load and explore a real-world public dataset.
- Understand dataset structure and data types.
- Analyze categorical and numerical variables.
- Identify missing values.
- Perform grouped statistical comparisons.
- Visualize student performance patterns.
- Extract meaningful insights from the dataset.

## Tasks Completed

### 1. Data Loading and Inspection

- Imported the dataset using Pandas.
- Inspected the first five records using `head()`.
- Examined data types using `info()`.
- Generated descriptive statistics using `describe()`.
- Identified dataset dimensions and column names.

### 2. Categorical Data Analysis

Analyzed the frequency and percentage distributions of five categorical variables:

- School (`school`)
- Sex (`sex`)
- Address type (`address`)
- Internet availability (`internet`)
- Family size (`famsize`)

### 3. Missing Value Analysis

- Identified missing values using `isnull().sum()`.
- Calculated missing-value percentages.
- Confirmed that the dataset contains no missing values.

### 4. Grouped Statistical Analysis

Used `groupby()` to compare final grades across weekly study-time categories.

Calculated:

- Student count
- Mean final grade
- Median final grade

### 5. Data Visualization

Created four visualizations:

- **Bar Chart:** Number of students by school.
- **Box Plot:** Final grade distribution by study-time category.
- **Histogram:** Distribution of final grades.
- **Heatmap:** Relationship between home internet access and final-grade categories.

### 6. Stretch Goal — Cross-Tabulation

Used `pd.crosstab()` to compare internet availability with two project-defined final-grade categories:

- Below 10
- 10 or above

Calculated row-normalized percentages to compare groups of different sizes.

## Key Findings

| Finding | Result |
|---|---:|
| Total student records | 649 |
| Original dataset columns | 33 |
| GP school students | 423 |
| MS school students | 226 |
| Female student records | 383 |
| Overall average final grade | 11.91/20 |
| Highest-performing study-time category by mean grade | Category 3 |
| Average grade of study-time category 3 | 13.23/20 |
| Total missing values | 0 |

The analysis shows an association between study-time categories and academic performance. However, these observations do not establish a causal relationship.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab
- GitHub

## Project Structure

```text
Week-1-Exploratory-Data-Analysis/
│
├── README.md
├── StudentScope_Week1.ipynb
└── student-por.csv
```

## How to Run

1. Clone or download the project repository.
2. Open `StudentScope_Week1.ipynb` in Google Colab.
3. Upload `student-por.csv` when prompted.
4. Run all notebook cells sequentially.
5. Explore the generated statistics, charts, and findings.

The original CSV uses a semicolon separator (`sep=';'`).

## Learning Outcomes

- Exploratory Data Analysis using Python.
- Dataset inspection and descriptive statistics.
- Categorical and numerical data analysis.
- Missing-value identification.
- Grouped analysis using Pandas.
- Data visualization and interpretation.
- Extracting meaningful insights from real-world datasets.

## Limitations

- The dataset represents students from two Portuguese schools.
- Study-time categories represent time bands rather than exact hours.
- Group differences indicate associations, not causation.
- This exploratory analysis does not predict individual student performance.

## Conclusion

Week 1 established the foundation for the StudentScope project by exploring student performance data, identifying patterns, and generating meaningful visualizations.

The findings provide a foundation for subsequent data cleaning, feature engineering, statistical analysis, machine learning, and interactive dashboard development.

## Next Steps

- Week 2 — Data Cleaning & Feature Engineering
- Week 3 — Statistical Analysis & Machine Learning
- Week 4 — Interactive Streamlit Dashboard

---

**Author:** Dinesh Kumar Pulagalla

**Internship:** SkillMe Data Science Virtual Internship

**GitHub:** https://github.com/dk0009-pv

**Project Repository:** https://github.com/dk0009-pv/StudentScope-Student-Performance-Analysis/tree/main/Week-1-Explore
