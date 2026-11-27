"""StudentScope: interactive exploration of the Portuguese-course dataset."""
import streamlit as st
import pandas as pd
from analysis_core import (ROOT, LABELS, STUDY, TRAVEL, load_data, filter_data,
                           grade_distribution, grouped_stats, train_week3, compare_study_time, predict_grade)

st.set_page_config(page_title='StudentScope | Performance Explorer', page_icon='📚', layout='wide')

@st.cache_data
def get_data():
    return load_data()

@st.cache_resource
def get_model():
    return train_week3(get_data())

df = get_data()
model, metrics, report, cm = get_model()
st.title('📚 StudentScope')
st.markdown('**Student Lifestyle & Performance Explorer · Week 4**')
st.write('Explore academic outcomes across school and home contexts, revisit study-time statistics, and try the Week 3 grade-band classifier.')
a,b,c,d = st.columns(4)
a.metric('Student records', f'{len(df):,}')
b.metric('Original variables', '33')
c.metric('Schools', df.school.nunique())
d.metric('Overall mean grade', f'{df.G3.mean():.2f}/20')
st.caption('UCI Student Performance · Portuguese language course · 649 records from two schools. Grade bands are analytical categories, not official promotion rules.')

st.sidebar.header('Explore the sample')
school = st.sidebar.multiselect('School', sorted(df.school.unique()), default=sorted(df.school.unique()), format_func=str.upper)
address = st.sidebar.multiselect('Home address type', sorted(df.address.unique()), default=sorted(df.address.unique()), format_func=lambda x: {'u':'Urban','r':'Rural'}[x])
internet = st.sidebar.multiselect('Home internet access', sorted(df.internet.unique()), default=sorted(df.internet.unique()), format_func=str.capitalize)
selected = filter_data(df, {'school':school,'address':address,'internet':internet})
st.sidebar.caption('All values are selected initially. An empty selection returns no records. Filters affect exploration only, not the trained model.')

explore, evidence, prediction = st.tabs(['Explore grades', 'Week 3 evidence', 'Try a prediction'])
with explore:
    st.subheader('Filtered academic outcomes')
    x,y,z = st.columns(3)
    x.metric('Matching records', f'{len(selected):,}')
    y.metric('Mean final grade', f'{selected.G3.mean():.2f}/20' if len(selected) else '—')
    z.metric('Grade ≥ 10', f'{(selected.G3>=10).mean():.1%}' if len(selected) else '—')
    if selected.empty:
        st.warning('No students match these selections. Choose at least one value in every filter.')
    else:
        left,right = st.columns(2)
        with left:
            st.markdown('**Final grade-band distribution**')
            st.bar_chart(grade_distribution(selected).to_frame())
            st.dataframe(grade_distribution(selected).to_frame(), use_container_width=True)
        with right:
            st.markdown('**Mean final grade by study-time band**')
            stats = grouped_stats(selected)
            chart = stats[['mean']].rename(index=STUDY, columns={'mean':'Mean grade'})
            st.bar_chart(chart)
            st.dataframe(stats.rename(index=STUDY).round(2), use_container_width=True)
        st.markdown('**Full final-grade distribution (0–20)**')
        st.bar_chart(selected.G3.value_counts().reindex(range(21),fill_value=0).sort_index().rename('Students').to_frame())
    st.download_button('Export filtered records (CSV)', selected.drop(columns=['grade_band']).to_csv(index=False).encode('utf-8'), 'studentscope_filtered.csv', 'text/csv', disabled=selected.empty)

with evidence:
    st.subheader('Study time and final grades · Full dataset')
    comparison = compare_study_time(df)
    a,b,c = st.columns(3)
    a.metric('Lowest study band', f"{comparison['lowest_mean']:.2f}")
    b.metric('Higher study bands', f"{comparison['higher_mean']:.2f}")
    c.metric('Mean difference', f"{comparison['gap']:.2f} points")
    st.write(f"Welch’s t-test p-value: {comparison['p_value']:.3g}. This is an association, not evidence that additional study time causes higher grades.")
    st.dataframe(grouped_stats(df).rename(index=STUDY).round(2),use_container_width=True)
    st.subheader('Logistic Regression · Held-out evaluation')
    a,b,c = st.columns(3)
    a.metric('Test accuracy',f"{metrics['accuracy']:.2%}")
    b.metric('Majority baseline',f"{metrics['baseline']:.2%}")
    c.metric('Balanced accuracy',f"{metrics['balanced_accuracy']:.2%}")
    st.caption(f"Training: {metrics['train']} records · Testing: {metrics['test']} records · Same stratified split and features as Week 3.")
    l,r = st.columns(2)
    with l:
        st.markdown('**Confusion matrix**')
        st.dataframe(cm.rename_axis('Actual ↓ / Predicted →'),use_container_width=True)
        st.caption('Rows are actual categories; columns are predictions.')
    with r:
        st.markdown('**Precision, recall and F1 by class**')
        st.dataframe(report.loc[LABELS,['precision','recall','f1-score','support']].round(3),use_container_width=True)
    st.warning(f"Below-10 recall: {report.loc['Below 10','recall']:.2%}. The baseline classifier is not suitable for identifying at-risk students or making academic decisions.")
    st.markdown('**Week 3 optional model comparison (saved results)**')
    st.dataframe(pd.read_csv(ROOT/'outputs'/'model_comparison.csv').round(3),use_container_width=True)

with prediction:
    st.subheader('Estimate a final grade band')
    st.write('Select the same five input features used in Week 3. Earlier grades and the final grade are not model inputs.')
    with st.form('student_prediction'):
        l,r = st.columns(2)
        with l:
            study = st.selectbox('Weekly study time', list(STUDY), index=1, format_func=STUDY.get)
            failures = st.selectbox('Previous class failures (recorded code)', [0,1,2,3])
            travel = st.selectbox('Travel time to school', list(TRAVEL), format_func=TRAVEL.get)
        with r:
            access = st.selectbox('Home internet', sorted(df.internet.unique()), index=1, format_func=str.capitalize)
            job = st.selectbox('Mother’s job group', sorted(df.Mjob_group.unique()))
        submitted = st.form_submit_button('Predict grade band', type='primary')
    if submitted:
        result, probs = predict_grade(model, study, failures, travel, access, job)
        st.info(f'Predicted category: {result}')
        st.dataframe(pd.DataFrame({'Model probability (not calibrated)':pd.Series(probs).reindex(LABELS).map(lambda x: f'{x:.1%}')}),use_container_width=True)
    st.caption('Educational demonstration only. The model has low minority-class recall and is not a reliable personal assessment. No real-world decisions should be based on this output.')

st.divider()
st.caption('Data source: UCI Student Performance (https://archive.ics.uci.edu/dataset/320/student+performance). Results describe this historical sample only.')
