from collections import OrderedDict

report_template_dict = OrderedDict([

    ("P&L highlights for this quarter", [
        "Revenue: this quarter's result, QoQ and YoY trends with reasons, and comparison to last quarter's guidance",
        "Gross margin: result, QoQ and YoY changes with explanations, and deviation from guidance",
        "Operating margin: result and margin expansion/shrinkage trends with interpretation",
        "Net margin and EPS: reported net profit margin and diluted EPS"
    ]),

    ("Business segment and customer highlights", [
        "Sales breakdown by business segment or platform and respective margins",
        "Management comments or outlook by segment",
        "New customer design wins and key customer updates",
        "LTA (Long-Term Agreement) or supply agreement changes and underutilization charges"
    ]),

    ("Production and pricing commentary", [
        "Wafer shipments and ASP (Average Selling Price) breakdown by volume and unit price",
        "Overall wafer ASP trend and ASP by node or product line",
        "Utilization rate for this quarter and next quarter's outlook"
    ]),

    ("Inventory and capital expenditure", [
        "Inventory or Days of Inventory (DOI) commentary for this quarter",
        "CapEx for this quarter and recent changes",
        "CapEx guidance for the full year or long-term and changes from prior guidance"
    ]),

    ("Capacity expansion and government incentives", [
        "New fab construction progress and capacity ramp-up milestones (e.g., tool move-in, pilot run)",
        "Expansion plans for existing fabs",
        "Government grants, tax credits, loans, or other local incentives"
    ]),

    ("Forward guidance and management outlook", [
        "P&L guidance (revenue and gross margin) for next quarter",
        "Segment-level sales forecast or annual trend"
    ])
])
