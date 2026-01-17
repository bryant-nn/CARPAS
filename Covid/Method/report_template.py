from collections import OrderedDict

from collections import OrderedDict

epidemic_report_template_dict = OrderedDict([
    ("Epidemic Statistics Overview for the Day", [
    "Total confirmed cases (local and imported), Day-over-Day or Week-over-Week changes with context",
    "Total deaths and recovered cases, breakdown by age or comorbidity where applicable",
    "Testing numbers (e.g. PCR, antigen), positivity rate trends"
    ]),

    ("Regional or City-Level Updates", [
        "Regional case breakdown and major outbreak hotspots",
        "Containment zones or lockdowns initiated or lifted",
        "Cross-city or cross-county policy differences explained"
    ]),

    ("Healthcare System Capacity and Burden", [
        "Hospital bed occupancy rate, ICU utilization, ventilator availability",
        "Medical staff workload, burnout reports, and government response",
        "Quarantine facility or shelter hospital capacity updates"
    ]),

    ("Vaccination Progress and Plans", [
        "Daily/weekly vaccination numbers, coverage rates by age group",
        "Updates on booster doses or new vaccine arrivals",
        "Comments on vaccine supply, procurement, and logistics"
    ]),

    ("Public Health Policy Updates", [
        "Changes to mask mandates, social distancing, gathering limits",
        "Border control measures: entry rules, quarantine requirements",
        "Changes to public health alert levels (e.g., from level 3 to 2)"
    ]),

    ("Economic and Social Impact Briefs", [
        "Unemployment rates, support subsidies, small business reliefs",
        "School closures, remote learning implementation, reopening plans",
        "Impact on travel, entertainment, and event industries"
    ]),

    ("Rumor Clarifications and Public Concerns", [
        "Official responses to misinformation or viral social media claims",
        "Clarification of vaccine side effects or variant transmission"
    ]),

    ("Variant and Mutation Monitoring", [
        "New variants detected and their potential impact",
        "Genomic surveillance efforts and variant distribution data",
        "Comparison with international variant trends"
    ]),

    ("International Collaboration and Comparisons", [
        "Updates on cross-border medical support or vaccine exchange",
        "Comparison of outbreak control with neighboring countries",
        "Statements from WHO or international health bodies"
    ])
])
