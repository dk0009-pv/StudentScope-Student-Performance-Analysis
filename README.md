# 📊 StudentScope – Student Performance Analysis

### SkillMe Data Science Virtual Internship · Week 1 · Exploratory Data Analysis (EDA)

**Author:** Dinesh Kumar Pulagalla

---

## 📌 About the Project

StudentScope is an Exploratory Data Analysis (EDA) project developed as part of the **SkillMe Data Science Virtual Internship – Week 1**.

This project explores the UCI Student Performance dataset to understand student backgrounds, study habits, school-related factors, and academic performance using Python data analysis libraries.

The objective is to develop practical skills in data loading, data inspection, categorical analysis, missing-value detection, grouping, and data visualization.

## 🎯 Project Objectives

- Load a public dataset using Pandas.
- Understand dataset structure and data types.
- Analyse categorical variables and response distributions.
- Identify missing values.
- Compare academic performance using GroupBy operations.
- Create meaningful charts and visualizations.
- Extract insights from student performance data.

## 📂 Dataset

**Dataset:** UCI Student Performance – Portuguese Language Course (`student-por.csv`)

**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/320/student+performance)

- Total Records: 649
- Original Columns: 33
- Target Variable: `G3` (Final Grade)

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab / Jupyter Notebook

## 🔍 Analysis Performed

1. **Data Loading:** Imported the CSV dataset using `pandas.read_csv()`.
2. **Data Inspection:** Used `.head()`, `.info()`, and `.describe()`.
3. **Categorical Analysis:** Explored school, sex, address, internet access, and family size.
4. **Missing Value Analysis:** Used `.isnull().sum()` to identify missing data.
5. **GroupBy Analysis:** Compared average final grades across study-time categories.
6. **Data Visualization:** Created bar charts, box plots, and histograms.
7. **Heatmap Analysis:** Explored the relationship between internet access and final-grade categories.

## 📊 Key Findings

- The dataset contains 649 student records.
- The dataset has 33 original columns.
- The average final grade is approximately 11.91 out of 20.
- No missing values were found in the dataset.
- Students in different study-time categories showed differences in average final grades.

## 📁 Repository Structure

```text
StudentScope-Student-Performance-Analysis/
│
├── StudentScope_Week1.ipynb
├── README.md
└── student-por.csv
```

## ▶️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/dk0009-pv/StudentScope-Student-Performance-Analysis.git
   ```

2. Open the notebook in Google Colab or Jupyter Notebook.

3. Install the required libraries if needed:

   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

4. Download `student-por.csv` from the UCI dataset source.

5. Upload the CSV file when prompted by the notebook.

6. Run all cells to reproduce the analysis and visualizations.

## 📚 Learning Outcomes

Through this project, I practised:

- Exploratory Data Analysis using Pandas.
- Working with real-world public datasets.
- Handling and inspecting missing data.
- Grouping and summarising data.
- Creating visualizations with Matplotlib and Seaborn.
- Communicating insights from data.

## 👨‍💻 Author

**Dinesh Kumar Pulagalla**

---

### 🏅 Internship

**SkillMe Data Science Virtual Internship**

**Week 1:** Exploratory Data Analysis (EDA)

---

*Learning, analysing, and building with data! 🚀*
