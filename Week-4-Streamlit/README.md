# StudentScope — Week 4: Streamlit Dashboard

**Student Lifestyle & Performance Explorer | SkillMe Data Science Virtual Internship**

An interactive exploration of study habits, home resources and academic performance. Continues the same StudentScope project from Weeks 1–3 using the Portuguese-course dataset rather than introducing a new dataset.

## Run locally (Windows, macOS or Linux)

Install Python 3.10–3.12 (recommended). Extract the ZIP and open `Week-4-StudentScope-Dashboard` in a terminal or VS Code. Run:

```bash
python -m venv .venv
```

Activate on Windows PowerShell: `.\.venv\Scripts\Activate.ps1` (or use `RUN_WEEK4.bat` if PowerShell blocks activation). On macOS/Linux: `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python test_dashboard_logic.py
python -m streamlit run app.py
```

The app opens at `http://localhost:8501`. First installation requires internet access; the dataset is bundled and no data download or API key is required. On Windows, double-click `RUN_WEEK4.bat` for automatic environment creation, installation, tests and launch. Stop the server with Ctrl+C.

To inspect the calculation notebook, open `StudentScope_Week4_Dashboard.ipynb` in VS Code/Jupyter from this directory and select the same virtual environment. The supplied notebook has saved outputs. It does not launch the Streamlit server.

## Data story

- Week 1: inspected 649 student records, 33 original variables, missingness, school distribution and final grades by study time.
- Week 2: normalized text categories, grouped mother's job and engineered age bands; the cleaned dataset has 35 columns and no missing values.
- Week 3: compared grade distributions and trained a Logistic Regression classifier to predict **Below 10** versus **10 or above** (a project-defined grade threshold).
- Week 4: made the findings explorable with three filters, dynamic grade distributions, grouped comparisons, model results, an interactive prediction form and CSV export.

**Dataset:** UCI Student Performance, Portuguese language course. Source: https://archive.ics.uci.edu/dataset/320/student+performance (DOI 10.24432/C5TG7T). The original `student-por.csv` and the exact cleaned Week 3 `survey_clean.csv` are bundled in `data/`. Data represent two Portuguese schools. Credit: Paulo Cortez and Alice Silva; see the UCI dataset page for attribution and license information.

## Results from Week 3

| Finding | Value |
|---|---:|
| Records | 649 |
| Lowest study-time band mean final grade | 10.84 |
| Higher study-time bands mean final grade | 12.42 |
| Mean grade difference | 1.58 |
| Welch p-value | 7.015e-09 |
| Logistic Regression test accuracy | 83.85% |
| Majority-class baseline | 84.62% |
| Below-10 recall | 0.00% |
| Random Forest accuracy (Week 3 optional comparison) | 83.08% |

The five model features are studytime, failures, traveltime, internet and Mjob_group. The train/test split is stratified (80/20, random_state=42; 519/130). Scaling and encoding are fitted on training data only; G1, G2 and G3 are excluded from predictors. The model is recreated using the Week 3 pipeline rather than trained on filtered subsets. The high apparent accuracy masks poor performance on the minority category; the model is only an educational baseline.

## Dashboard guide

**Explore grades:** use the sidebar school (GP/MS), address type (urban/rural), and internet (yes/no) multiselect filters. The charts, summary cards and CSV export use the current selection. Empty selections show a warning instead of misleading averages.

**Week 3 evidence:** see full-dataset grouped mean/median results, Welch significance test, held-out accuracy, confusion matrix and per-class metrics. Filtering does not change the held-out model evaluation.

**Try a prediction:** choose the five feature values and click Predict grade band. The form returns one of the two categories and estimated model probabilities. These probabilities are not calibrated and should not be used for decisions about actual students.

## Verification and demo checklist

Automated tests compare three filtered slices with independently calculated masks, validate full and empty selections, reproduce Week 3 metrics, and check predictions for all 512 possible combinations of selectable feature values. The notebook records the filter and example prediction results in `outputs/`.

In the browser, try these exact combinations in Explore grades and confirm that the matching-record count and charts change:

1. GP / Urban / Yes
2. MS / Rural / No
3. Both schools / Rural / Yes

Then open Week 3 evidence and check that the test metrics remain unchanged. Open Try a prediction, select five values, click Predict grade band, and confirm a result appears. Try the CSV download. Record a 30–60 second demo: briefly introduce the dashboard, change filters, show Week 3 results and make a live prediction. The demo recording is not included in this repository.

The calculations and notebook were executed locally; Streamlit was not available in the build environment, so actual browser interaction must be confirmed after installing it. No claim of completed browser testing is made.

## Limitations

Study-time categories are self-reported bands, not exact hours. Group differences are observational, not causal. The sample is historical and limited to two schools. The classifier is unsuitable for identifying at-risk students, admissions or other high-stakes academic decisions.

## Repository files

- `app.py` — Streamlit dashboard.
- `analysis_core.py` — loading, filters, Week 3 model and predictions.
- `test_dashboard_logic.py` — automated checks.
- `StudentScope_Week4_Dashboard.ipynb` — executed validation notebook.
- `data/` — original and cleaned datasets.
- `outputs/` — Week 3 results and Week 4 validation artifacts.
- `requirements.txt`, `.streamlit/config.toml`, `RUN_WEEK4.bat` — reproducible setup and launch.
