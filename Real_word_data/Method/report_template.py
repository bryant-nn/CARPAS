from collections import OrderedDict

report_template_dict = OrderedDict([
    ("P&L (profit and loss statement) highlights result for this quarter", 
     ["Revenue results, QoQ changes, YoY changes with reasons, revenue results  v.s. guidance from last quarter with reasons",
      "wafer sales and the breakdown to wafer quanty and ASP for this quarter",
      "Gross margin results, QoQ changes, YoY changes with reasons, Gross margin results  v.s. guidance from last quarter with reasons",
      "Operating margin results, QoQ changes, YoY changes with reasons, Operating margin results  v.s. guidance from last quarter with reasons",
      "Net margin and Diluted EPS (earnings per share) results"]),

    ("Segment or Platform highlights for this quarter", 
     ["sales by segment or platforms, their respective margin levels, and their respective management comments",
      "sales guidance, forecast, or trend by segment next quarter or full year"]),

    ("Comments on inventory or DOI (Days of Inventory) for this quarter", ["comments on inventory or DOI (Days of Inventory) for this quarter"]),

    ("Utilization rate for this quarter", 
     ["utilization rate, and the utilization rate guidance for the next quarter and future outlook, and any comments in the Q&A session"]),

    ("Wafer ASP comments for this quarter", ["overall wafer ASP comments, and the by node or segment wafer ASP comments for this quarter"]),

    ("Foundry customer design win related topics for this quarter", ["foundry customer, and company's design win comment for this quarter"]),

    ("Customer LTA (Long Term Agreement) for this quarter", ["customer LTA (Long Term Agreement) or supply agreement update, and the underutilization charges for this quarter"]),

    ("Fab construction, expansion or capacity ramping progress for this quarter", 
     ["new fab construction progress (e.g., groundbreaking, tool move-in) for this quarter",
      "capacity expansion plan on the existing fabs for this quarter"]),

    ("Government grants, local grants, tax incentives, and loans for this quarter", 
     ["government grants, local grants, tax incentives, and loans (keywods: government grants, grants, tax credit, ITC, tax credit refund, tax refund for this quarter)"]),

    ("P&L (profit and loss statement) guidance", 
     ["P&L (revenue and gross margin) guidance for next quarter"]),

    ("CapEx or CapEx guidance", 
     ["CapEx, and the CapEx comments for this quarter", 
      "CapEx guidance for the full year or long term, the changes from the previous guidance, and the comments for this quarter"]),
])