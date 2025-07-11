# Accessible India: Government Websites Accessibility Checker

## Overview
An AI-powered accessibility checker for Indian government websites. It crawls websites, audits for WCAG compliance, suggests improvements, and visualizes issues in a dashboard.

## Features
- Crawl government websites for all internal pages
- Audit accessibility using Pa11y
- Suggest improved alt text using OpenAI GPT
- Score compliance (A, AA, AAA)
- Generate downloadable reports
- Visualize issues in a Streamlit dashboard

## Backend Setup
1. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
2. Install [Pa11y](https://github.com/pa11y/pa11y) globally (requires Node.js):
   ```bash
   npm install -g pa11y
   ```
3. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```
4. Run the crawler and audit scripts as needed.

## Frontend Setup
1. Install Streamlit:
   ```bash
   pip install streamlit
   ```
2. Run the dashboard:
   ```bash
   streamlit run frontend/dashboard.py
   ```

## Usage
- Use the backend to crawl and audit a website, then generate a report.
- Load the report in the Streamlit dashboard to visualize and download results.