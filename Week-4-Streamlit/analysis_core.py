"""Reproduce the Week 3 model and provide reusable dashboard calculations."""
from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, balanced_accuracy_score

ROOT = Path(__file__).resolve().parent
LABELS = ['Below 10', '10 or above']
NUMERIC = ['studytime', 'failures', 'traveltime']
CATEGORICAL = ['internet', 'Mjob_group']
FEATURES = NUMERIC + CATEGORICAL
FILTERS = ['school', 'address', 'internet']
STUDY = {1: '<2 hours', 2: '2–5 hours', 3: '5–10 hours', 4: '>10 hours'}
TRAVEL = {1: '<15 min', 2: '15–30 min', 3: '30–60 min', 4: '>60 min'}

def load_data(path=ROOT / 'data' / 'survey_clean.csv'):
    df = pd.read_csv(path)
    if df.shape != (649, 35) or df.isna().any().any():
        raise ValueError('Expected the complete 649 x 35 cleaned Week 3 dataset.')
    df['grade_band'] = np.where(df.G3 >= 10, LABELS[1], LABELS[0])
    return df

def filter_data(df, selections):
    result = df
    for col, choices in selections.items():
        if col not in FILTERS:
            raise ValueError(f'Unknown filter: {col}')
        result = result[result[col].isin(choices)]
    return result.copy()

def grade_distribution(df):
    return df.grade_band.value_counts().reindex(LABELS, fill_value=0).rename('Students')

def grouped_stats(df):
    return df.groupby('studytime').G3.agg(['count','mean','median','std'])

def train_week3(df):
    X_train, X_test, y_train, y_test = train_test_split(
        df[FEATURES], df.grade_band, test_size=0.2, random_state=42, stratify=df.grade_band)
    prep = ColumnTransformer([('num', StandardScaler(), NUMERIC),
                              ('cat', OneHotEncoder(handle_unknown='ignore'), CATEGORICAL)])
    model = Pipeline([('prepare', prep), ('classifier', LogisticRegression(max_iter=1000, random_state=42))])
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    report = pd.DataFrame(classification_report(y_test, pred, labels=LABELS, output_dict=True, zero_division=0)).T
    cm = pd.DataFrame(confusion_matrix(y_test, pred, labels=LABELS), index=LABELS, columns=LABELS)
    metrics = {'accuracy': accuracy_score(y_test, pred), 'baseline': (y_test == y_train.mode().iloc[0]).mean(),
               'balanced_accuracy': balanced_accuracy_score(y_test, pred), 'train': len(X_train), 'test': len(X_test)}
    return model, metrics, report, cm

def compare_study_time(df):
    low = df.loc[df.studytime == 1, 'G3']; high = df.loc[df.studytime > 1, 'G3']
    test = ttest_ind(high, low, equal_var=False)
    return {'lowest_mean': low.mean(), 'higher_mean': high.mean(), 'gap': high.mean()-low.mean(), 'p_value': test.pvalue}

def predict_grade(model, studytime, failures, traveltime, internet, job):
    row = pd.DataFrame([[studytime, failures, traveltime, internet, job]], columns=FEATURES)
    prediction = model.predict(row)[0]
    probs = dict(zip(model.classes_, model.predict_proba(row)[0]))
    return prediction, probs
