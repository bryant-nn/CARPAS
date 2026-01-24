from collections import OrderedDict

report_template_dict = OrderedDict([
    ("Revenue Performance", [
        "Service revenue growth: wireless, broadband, enterprise (YoY % change)",
        "ARPU trends and impact of pricing and bundling strategies (YoY % change, $ value)",
        "Revenue mix analysis: contribution by segment (percentage breakdown)"
    ]),
    ("Subscriber Metrics", [
        "Net subscriber additions by segment (residential, business) (Number)",
        "Churn rate analysis: trends and drivers (percentage)",
        "Subscriber acquisition cost (SAC) trends ($ value)"
    ]),
    ("Profitability and Cost Management", [
        "EBITDA margin: analysis of key drivers and trends (percentage)",
        "Operating expense management initiatives and impact on profitability ($ value)",
        "Cost of revenue analysis: trends and drivers ($ value)"
    ]),
    ("Network and Infrastructure", [
        "Network investment: 5G deployment progress and capital expenditure ($ value)",
        "Fiber buildout: progress, coverage expansion, and customer adoption (Number of homes passed, subscribers)",
        "Spectrum assets: utilization and future allocation plans"
    ]),
    ("Capital Allocation and Cash Flow", [
        "Free cash flow generation and utilization ($ value)",
        "Dividend sustainability and shareholder returns ($ value)",
        "Debt levels and leverage ratios (Debt/EBITDA)"
    ]),
    ("Strategic Initiatives and Growth", [
        "Enterprise and B2B growth initiatives: progress and key wins ($ value)",
        "Content and media segment performance: revenue, profitability, and subscriber metrics ($ value, percentage, Number)",
        "New product and service launches: impact on revenue and subscriber growth ($ value, Number)"
    ]),
    ("Guidance and Outlook", [
        "Subscriber and revenue growth guidance for next quarter/year (percentage, $ value)",
        "EBITDA margin guidance for next quarter/year (percentage)",
        "Capital expenditure guidance for network investments ($ value)"
    ])
])