from collections import OrderedDict

report_template_dict = OrderedDict([
    ("Premiums Analysis", [
        "Gross Written Premiums (GWP) growth by line of business (%)",
        "Net Written Premiums (NWP) growth by line of business (%)",
        "Impact of pricing changes on premium volume"
    ]),
    ("Underwriting Performance", [
        "Combined Ratio analysis (Overall and by segment)",
        "Loss Ratio trends and drivers (e.g., claims frequency, severity)",
        "Expense Ratio trends and drivers (e.g., commission expenses, operating costs)"
    ]),
    ("Catastrophe & Reinsurance", [
        "Total catastrophe losses impact (USD or % of GWP)",
        "Reinsurance recoveries received and expected",
        "Effectiveness of reinsurance program"
    ]),
    ("Business Growth & Retention", [
        "Policy retention rates by major product line (%)",
        "New business production volume (USD or # of policies)",
        "Customer acquisition cost trends"
    ]),
    ("Investment Portfolio", [
        "Investment income yield (%)",
        "Asset allocation overview (e.g., fixed income, equities, alternatives)",
        "Realized and unrealized gains/losses on investments"
    ]),
    ("Reserves & Capital", [
        "Reserve development trends (favorable/unfavorable)",
        "Changes in actuarial assumptions and their impact",
        "Capital position and statutory surplus levels"
    ]),
    ("Capital Allocation", [
        "Share repurchase activity (USD)",
        "Dividend payments (USD per share)",
        "Capital deployment plans (e.g., acquisitions, new products)"
    ]),
    ("Outlook & Guidance", [
        "Premium growth guidance for the next quarter/year (%)",
        "Combined ratio guidance for the next quarter/year (%)"
    ])
])