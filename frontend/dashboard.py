import streamlit as st
import pandas as pd
import os

def load_report(report_path):
    if os.path.exists(report_path):
        return pd.read_csv(report_path)
    return pd.DataFrame()

st.title('Accessible India: Government Websites Accessibility Checker')

uploaded_file = st.file_uploader('Upload report CSV', type='csv')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = load_report('backend/report.csv')

if not df.empty:
    st.dataframe(df)
    st.download_button('Download Report', df.to_csv(index=False), 'accessibility_report.csv')
    st.bar_chart(df['WCAG Level'].value_counts())
else:
    st.info('No report loaded. Please upload a report or run an audit.') 