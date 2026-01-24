from collections import OrderedDict

report_template_dict = OrderedDict([
    ("Revenue & Billings", [
        "ARR growth rate (QoQ and YoY)",
        "Billings performance vs. guidance",
        "Impact of currency fluctuations on revenue"
    ]),
    ("Customer Acquisition & Retention", [
        "Net Dollar Retention rate",
        "Number of new customers acquired",
        "Churn rate and reasons for churn"
    ]),
    ("Platform Adoption & Product Performance", [
        "Platform adoption rate vs. point products",
        "Performance of key product lines (e.g., cloud security, SASE)",
        "Customer feedback on new products/features"
    ]),
    ("Large Customer Growth", [
        "Number of customers with ARR over $100K",
        "Average deal size for new and existing customers",
        "Expansion within existing large accounts"
    ]),
    ("Market & Competition", [
        "Competitive win rates",
        "Market share trends",
        "Commentary on the evolving threat landscape"
    ]),
    ("Strategic Initiatives & R&D", [
        "R&D investment as a percentage of revenue",
        "Progress on key strategic initiatives",
        "Details on recent product/feature launches"
    ]),
    ("Go-to-Market & Channel", [
        "Channel partner performance and contribution to revenue",
        "Effectiveness of go-to-market strategy",
        "Marketing spend efficiency"
    ]),
    ("Financial Outlook", [
        "Next quarter billings guidance",
        "Full-year revenue and profitability outlook",
        "Assumptions underlying the guidance"
    ])
])