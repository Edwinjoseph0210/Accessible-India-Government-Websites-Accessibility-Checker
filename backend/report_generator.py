import pandas as pd
import csv

def score_wcag(issues):
    # Simple scoring: A (few issues), AA (moderate), AAA (many)
    count = len(issues)
    if count < 5:
        return 'AAA'
    elif count < 15:
        return 'AA'
    else:
        return 'A'

def generate_report(audit_results, output_file='report.csv'):
    rows = []
    for page in audit_results:
        url = page['url']
        issues = page.get('issues', [])
        score = score_wcag(issues)
        for issue in issues:
            rows.append({
                'URL': url,
                'Issue': issue.get('message', ''),
                'Code': issue.get('code', ''),
                'Selector': issue.get('selector', ''),
                'WCAG Level': score
            })
    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)
    print(f"Report saved to {output_file}")

if __name__ == "__main__":
    # Example usage
    sample_results = [
        {'url': 'https://example.com', 'issues': [{'message': 'Missing alt', 'code': 'WCAG2A', 'selector': 'img'}]},
        {'url': 'https://example.com/page2', 'issues': []}
    ]
    generate_report(sample_results) 