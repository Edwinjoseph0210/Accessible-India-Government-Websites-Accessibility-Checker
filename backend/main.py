from crawler import WebCrawler
from accessibility_audit import AccessibilityAuditor
from gpt_enhancer import GPTEnhancer
from report_generator import generate_report
import os

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py <base_url>")
        exit(1)
    base_url = sys.argv[1]
    crawler = WebCrawler(base_url)
    print(f"Crawling {base_url}...")
    crawler.crawl()
    pages = crawler.get_pages()
    auditor = AccessibilityAuditor()
    enhancer = GPTEnhancer()
    audit_results = []
    for page in pages:
        url = page['url']
        print(f"Auditing {url}...")
        audit = auditor.audit_url(url)
        issues = audit if audit else []
        # Enhance alt text suggestions (example: for missing alt)
        for issue in issues:
            if 'alt' in issue.get('message', '').lower():
                # Use some context from the page for better suggestions
                suggestion = enhancer.suggest_alt_text(f"Page: {url}")
                issue['gpt_suggestion'] = suggestion
        audit_results.append({'url': url, 'issues': issues})
    generate_report(audit_results, output_file='report.csv')
    print("Done. Report generated as report.csv.") 