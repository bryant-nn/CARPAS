from collections import OrderedDict

report_template_dict = OrderedDict([
    ("Executive Summary", [
        "Overview of key financial performance highlights",
        "Strategic priorities and outlook for the next quarter/year"
    ]),
    ("Admissions and Patient Volumes", [
        "Total admissions and patient days (YoY and QoQ)",
        "Same-facility admissions and patient day growth (YoY and QoQ)",
        "Trends in inpatient vs. outpatient volumes",
        "Impact of seasonality or external factors (e.g., flu season)"
    ]),
    ("Revenue Analysis", [
        "Net patient revenue (YoY and QoQ)",
        "Revenue per admission trends and drivers",
        "Impact of acuity mix changes on revenue",
        "Breakdown of revenue by service line (if applicable)"
    ]),
    ("Payer Mix and Reimbursement", [
        "Percentage of revenue from Medicare, Medicaid, commercial insurance, and self-pay",
        "Trends in payer mix shifts and their impact on revenue",
        "Average reimbursement rates by payer category",
        "Impact of value-based care contracts on reimbursement"
    ]),
    ("Operating Expenses", [
        "Labor costs as a percentage of revenue",
        "Trends in staffing levels and contract labor usage",
        "Supply costs and other operating expenses",
        "Impact of cost reduction initiatives"
    ]),
    ("Operating Margin and Profitability", [
        "Operating margin (YoY and QoQ)",
        "Operating margin by segment (if applicable)",
        "Factors affecting operating margin (e.g., revenue growth, cost control)",
        "Initiatives to improve operating margin"
    ]),
    ("Capital Allocation and M&A", [
        "Capital expenditures for facility modernization and expansion",
        "Status of ongoing or planned acquisitions and divestitures",
        "Impact of recent acquisitions on financial performance"
    ]),
    ("Guidance", [
        "Same-facility volume and revenue growth guidance for the next quarter/year",
        "Operating margin guidance for the next quarter/year",
        "Capital expenditure guidance for the next quarter/year"
    ])
])