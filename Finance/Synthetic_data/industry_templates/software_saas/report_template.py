from collections import OrderedDict

report_template_dict = OrderedDict([
    ("Revenue & Recurring Revenue", [
        "ARR growth (YoY and QoQ): Report actual ARR and percentage growth.",
        "MRR trends: Discuss MRR growth, highlighting significant changes.",
        "New customer acquisition: Number of new customers added, and impact on ARR/MRR."
    ]),
    ("Net Revenue Retention (NRR)", [
        "NRR performance: Report NRR and explain drivers (expansion, contraction, churn).",
        "Expansion revenue: Detail revenue growth from existing customers.",
        "Churn analysis: Discuss reasons for customer churn and mitigation strategies."
    ]),
    ("Customer Acquisition & Sales Efficiency", [
        "CAC trends: Report Customer Acquisition Cost and trends.",
        "Sales efficiency: Discuss sales cycle length and conversion rates.",
        "LTV/CAC ratio: Report the Lifetime Value to Customer Acquisition Cost ratio."
    ]),
    ("Gross Margin & Cost of Revenue", [
        "Gross margin: Report gross margin and explain changes from prior periods.",
        "Cost of revenue breakdown: Detail key components of cost of revenue (hosting, support, etc.)."
    ]),
    ("Operating Expenses & Profitability", [
        "Operating expense breakdown: Discuss trends in R&D, Sales & Marketing, and G&A expenses.",
        "Operating margin: Report operating margin and explain drivers.",
        "Rule of 40: Report the Rule of 40 metric (Revenue Growth + Profit Margin)."
    ]),
    ("Cash Flow & Financial Position", [
        "Free cash flow: Report free cash flow and explain key drivers.",
        "Cash runway: Discuss cash position and expected cash runway.",
        "Capital allocation: Discuss capital allocation strategy (investments, acquisitions, etc.)."
    ]),
    ("Product & Market", [
        "Product roadmap: Provide updates on key product initiatives and feature launches.",
        "Customer mix: Discuss trends in enterprise vs. SMB customer mix.",
        "Average contract value (ACV): Report and explain trends in average contract value."
    ]),
    ("Guidance", [
        "Next quarter ARR guidance: Provide ARR guidance for the next quarter.",
        "Full-year revenue guidance: Provide revenue guidance for the full fiscal year.",
        "Key assumptions: Outline key assumptions underlying guidance."
    ])
])