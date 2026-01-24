"""
Company Categories Configuration for Multi-Industry Synthetic Data Generation

This module defines 20 diverse company categories with industry-specific attributes
for generating realistic earnings call transcripts across different sectors.
"""

from collections import OrderedDict

# Each category contains:
# - key: unique identifier for the category
# - name: human-readable display name
# - sector: broader sector grouping
# - key_metrics: industry-specific financial metrics
# - executive_roles: typical executive titles for this industry
# - aspects: industry-specific financial aspects to discuss in earnings calls

COMPANY_CATEGORIES = OrderedDict([
    # ========== TECHNOLOGY SECTOR ==========
    ("software_saas", {
        "name": "Software / SaaS",
        "sector": "Technology",
        "key_metrics": [
            "Annual Recurring Revenue (ARR)",
            "Monthly Recurring Revenue (MRR)",
            "Net Revenue Retention (NRR)",
            "Customer Acquisition Cost (CAC)",
            "Lifetime Value (LTV)",
            "Churn Rate",
            "Gross Margin",
            "Rule of 40"
        ],
        "executive_roles": ["CEO", "CFO", "CTO", "Chief Revenue Officer"],
        "aspects": [
            "ARR and MRR growth, QoQ and YoY changes, new customer additions",
            "Net Revenue Retention and expansion revenue from existing customers",
            "Customer acquisition cost trends and sales efficiency metrics",
            "Gross margin results and cost of revenue breakdown",
            "Operating expenses by category (R&D, S&M, G&A) and operating margin",
            "Free cash flow and cash runway commentary",
            "Product roadmap updates and new feature launches",
            "Enterprise vs SMB customer mix and average contract value trends",
            "Geographic revenue breakdown and international expansion",
            "Guidance for next quarter ARR and full-year revenue"
        ]
    }),

    ("cloud_computing", {
        "name": "Cloud Computing",
        "sector": "Technology",
        "key_metrics": [
            "Total Revenue",
            "Cloud Services Revenue",
            "Remaining Performance Obligations (RPO)",
            "Infrastructure Utilization",
            "Data Center Capacity",
            "Gross Margin"
        ],
        "executive_roles": ["CEO", "CFO", "CTO", "Chief Product Officer"],
        "aspects": [
            "Cloud services revenue growth, QoQ and YoY changes with driver analysis",
            "Remaining Performance Obligations (RPO) and backlog commentary",
            "Data center expansion and capital expenditure for infrastructure",
            "Compute and storage capacity utilization rates",
            "Gross margin trends and cost optimization initiatives",
            "AI/ML workload growth and new service launches",
            "Enterprise customer wins and large deal commentary",
            "Multi-cloud and hybrid cloud partnership updates",
            "Security and compliance certifications achieved",
            "Revenue guidance for cloud segment and full company"
        ]
    }),

    ("ecommerce", {
        "name": "E-Commerce / Online Retail",
        "sector": "Technology",
        "key_metrics": [
            "Gross Merchandise Value (GMV)",
            "Take Rate",
            "Active Buyers/Sellers",
            "Average Order Value (AOV)",
            "Customer Acquisition Cost",
            "Fulfillment Cost per Order"
        ],
        "executive_roles": ["CEO", "CFO", "COO", "Chief Marketing Officer"],
        "aspects": [
            "GMV and revenue growth, QoQ and YoY changes with seasonality analysis",
            "Active buyer and seller count growth and engagement metrics",
            "Average order value trends and basket size analysis",
            "Take rate changes and marketplace fee structure updates",
            "Fulfillment and logistics cost per order and efficiency gains",
            "Advertising and marketing spend efficiency and ROAS",
            "Mobile app engagement and conversion rate improvements",
            "Seller services and value-added services revenue",
            "International market expansion and cross-border commerce",
            "Holiday season preparation and inventory management"
        ]
    }),

    ("cybersecurity", {
        "name": "Cybersecurity",
        "sector": "Technology",
        "key_metrics": [
            "Annual Recurring Revenue (ARR)",
            "Billings",
            "Net Dollar Retention",
            "Platform Adoption Rate",
            "Customers over $100K ARR"
        ],
        "executive_roles": ["CEO", "CFO", "CTO", "Chief Security Officer"],
        "aspects": [
            "ARR growth and billings performance, QoQ and YoY trends",
            "Net dollar retention and upsell/cross-sell momentum",
            "Platform vs point product adoption rates",
            "Number of customers with ARR over $100K and average deal size",
            "Threat landscape commentary and new threat detection capabilities",
            "Cloud security and SASE adoption trends",
            "Channel partner performance and go-to-market strategy",
            "R&D investment and new product/feature launches",
            "Competitive win rates and market share gains",
            "Next quarter billings guidance and full-year outlook"
        ]
    }),

    # ========== ENERGY SECTOR ==========
    ("oil_gas", {
        "name": "Oil & Gas",
        "sector": "Energy",
        "key_metrics": [
            "Production Volume (BOE/day)",
            "Realized Price per Barrel",
            "Finding and Development Cost",
            "Lifting Cost",
            "EBITDA",
            "Proved Reserves"
        ],
        "executive_roles": ["CEO", "CFO", "COO", "VP of Exploration"],
        "aspects": [
            "Production volumes in BOE/day, oil vs gas split, QoQ and YoY changes",
            "Realized prices per barrel/MCF and hedging program commentary",
            "Lifting costs and operating expenses per BOE",
            "Capital expenditure breakdown: drilling, completion, facilities",
            "Exploration and drilling activity updates and well results",
            "Proved reserves additions and reserve replacement ratio",
            "Refining and midstream segment performance",
            "ESG initiatives and emissions reduction progress",
            "Debt levels and capital allocation priorities",
            "Production guidance for next quarter and full year"
        ]
    }),

    ("renewable_energy", {
        "name": "Renewable Energy / Clean Tech",
        "sector": "Energy",
        "key_metrics": [
            "Generation Capacity (MW/GW)",
            "Capacity Factor",
            "Power Purchase Agreement (PPA) Price",
            "Levelized Cost of Energy",
            "Development Pipeline"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Development Officer", "Chief Sustainability Officer"],
        "aspects": [
            "Operating capacity in MW and generation output in GWh",
            "Capacity factor performance by technology (solar, wind, storage)",
            "PPA pricing trends and contract extensions",
            "Development pipeline additions and project milestones",
            "Construction progress and commercial operation dates",
            "Capital recycling and asset sale transactions",
            "Tax equity financing and project-level financing",
            "Storage deployment and hybrid project updates",
            "Policy and regulatory environment commentary",
            "Capacity addition guidance and pipeline targets"
        ]
    }),

    ("utilities", {
        "name": "Utilities / Power Generation",
        "sector": "Energy",
        "key_metrics": [
            "Rate Base",
            "Earned ROE",
            "Customer Count",
            "O&M Expense",
            "Capital Investment",
            "Reliability Metrics"
        ],
        "executive_roles": ["CEO", "CFO", "COO", "Chief Strategy Officer"],
        "aspects": [
            "Revenue and earnings breakdown by regulated vs unregulated segments",
            "Rate base growth and regulatory rate case updates",
            "Authorized vs earned ROE and regulatory lag commentary",
            "Customer growth and usage per customer trends",
            "O&M expense management and efficiency programs",
            "Capital investment plan and grid modernization projects",
            "Generation fleet transition and clean energy goals",
            "Reliability metrics (SAIDI, SAIFI) and storm response",
            "Dividend policy and payout ratio",
            "Earnings guidance and rate base growth outlook"
        ]
    }),

    # ========== FINANCIAL SECTOR ==========
    ("banking", {
        "name": "Banking / Financial Services",
        "sector": "Financial",
        "key_metrics": [
            "Net Interest Income (NII)",
            "Net Interest Margin (NIM)",
            "Fee Income",
            "Provision for Credit Losses",
            "Efficiency Ratio",
            "CET1 Ratio"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Risk Officer", "Chief Credit Officer"],
        "aspects": [
            "Net interest income and net interest margin trends",
            "Loan growth by segment: commercial, consumer, mortgage",
            "Deposit growth and mix, and cost of deposits",
            "Fee income breakdown: wealth management, investment banking, cards",
            "Provision for credit losses and reserve build/release",
            "Credit quality metrics: NPL ratio, charge-offs, delinquencies",
            "Operating expenses and efficiency ratio progress",
            "Capital ratios (CET1, Tier 1) and capital return plans",
            "Digital banking adoption and technology investments",
            "NII and earnings guidance for next quarter"
        ]
    }),

    ("insurance", {
        "name": "Insurance",
        "sector": "Financial",
        "key_metrics": [
            "Gross Written Premiums",
            "Combined Ratio",
            "Loss Ratio",
            "Investment Income",
            "Book Value per Share"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Underwriting Officer", "Chief Investment Officer"],
        "aspects": [
            "Gross and net written premiums by line of business",
            "Combined ratio, loss ratio, and expense ratio analysis",
            "Catastrophe losses and reinsurance recoveries",
            "Policy retention rates and new business production",
            "Investment portfolio performance and asset allocation",
            "Reserve development and actuarial assumptions",
            "Underwriting profitability by segment",
            "Capital position and statutory surplus",
            "Share repurchase and dividend activity",
            "Premium growth and combined ratio guidance"
        ]
    }),

    ("asset_management", {
        "name": "Asset Management / Investment",
        "sector": "Financial",
        "key_metrics": [
            "Assets Under Management (AUM)",
            "Net Flows",
            "Management Fee Revenue",
            "Performance Fees",
            "Operating Margin"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Investment Officer", "Head of Distribution"],
        "aspects": [
            "AUM growth and breakdown by asset class and geography",
            "Net flows by channel: institutional, retail, alternatives",
            "Management fee revenue and average fee rate trends",
            "Performance fees realized and performance vs benchmarks",
            "Operating expenses and compensation ratio",
            "New product launches and fund performance rankings",
            "Distribution partnerships and channel expansion",
            "Technology and digital platform investments",
            "Organic growth rate and market share commentary",
            "AUM and flow guidance for upcoming periods"
        ]
    }),

    # ========== HEALTHCARE SECTOR ==========
    ("pharma_biotech", {
        "name": "Pharmaceuticals / Biotech",
        "sector": "Healthcare",
        "key_metrics": [
            "Product Revenue by Drug",
            "R&D Expense",
            "Pipeline Milestone Updates",
            "Patent Expiry Timeline",
            "Gross Margin"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Medical Officer", "Chief Scientific Officer"],
        "aspects": [
            "Product revenue by key drug franchise with volume and price analysis",
            "New product launch updates and market share gains",
            "R&D expense and pipeline investment priorities",
            "Clinical trial updates: phase progression, data readouts, regulatory milestones",
            "Regulatory approvals and label expansions achieved",
            "Patent cliff exposure and life cycle management strategies",
            "Business development: licensing deals, acquisitions, partnerships",
            "Gross margin trends and manufacturing efficiency",
            "Geographic revenue breakdown and emerging market growth",
            "Revenue guidance and key upcoming catalysts"
        ]
    }),

    ("medical_devices", {
        "name": "Medical Devices",
        "sector": "Healthcare",
        "key_metrics": [
            "Organic Revenue Growth",
            "Procedure Volume",
            "New Product Revenue",
            "Gross Margin",
            "R&D as % of Revenue"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Technology Officer", "Chief Commercial Officer"],
        "aspects": [
            "Organic revenue growth by segment and geography",
            "Procedure volume trends and market recovery commentary",
            "New product launches and contribution to growth",
            "FDA approvals and CE marks obtained",
            "Gross margin trends and supply chain commentary",
            "R&D investment and innovation pipeline",
            "Capital equipment vs consumables mix",
            "Hospital and ambulatory surgery center adoption",
            "Competitive dynamics and market share trends",
            "Revenue and margin guidance"
        ]
    }),

    ("healthcare_services", {
        "name": "Healthcare Services / Hospitals",
        "sector": "Healthcare",
        "key_metrics": [
            "Admissions",
            "Revenue per Admission",
            "Patient Days",
            "Payer Mix",
            "Operating Margin",
            "Same-Facility Growth"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Medical Officer", "Chief Operating Officer"],
        "aspects": [
            "Admissions and patient day volumes, same-facility trends",
            "Revenue per admission and acuity mix changes",
            "Payer mix shifts: Medicare, Medicaid, commercial, self-pay",
            "Labor costs and staffing levels, contract labor usage",
            "Operating margin by segment and improvement initiatives",
            "Outpatient and ambulatory care growth",
            "Value-based care contracts and quality metrics",
            "Capital expenditure for facility modernization",
            "Acquisition and divestitures activity",
            "Same-facility volume and revenue growth guidance"
        ]
    }),

    # ========== CONSUMER SECTOR ==========
    ("consumer_goods", {
        "name": "Consumer Goods / CPG",
        "sector": "Consumer",
        "key_metrics": [
            "Organic Sales Growth",
            "Volume vs Price/Mix",
            "Gross Margin",
            "Market Share",
            "A&P Spend"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Marketing Officer", "Chief Supply Chain Officer"],
        "aspects": [
            "Organic sales growth decomposition: volume, price, mix",
            "Performance by category and key brand updates",
            "Geographic segmentation: developed vs emerging markets",
            "Gross margin progression and commodity cost headwinds/tailwinds",
            "Pricing actions taken and elasticity observations",
            "A&P (advertising & promotion) investment and ROI",
            "Innovation pipeline and new product launches",
            "Market share trends by category and region",
            "Supply chain optimization and productivity savings",
            "Organic sales growth and margin guidance"
        ]
    }),

    ("retail", {
        "name": "Retail / Brick-and-Mortar",
        "sector": "Consumer",
        "key_metrics": [
            "Comparable Store Sales",
            "Store Traffic",
            "Average Transaction Value",
            "Inventory Turnover",
            "Sales per Square Foot"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Merchandising Officer", "Chief Stores Officer"],
        "aspects": [
            "Comparable store sales growth with traffic vs ticket breakdown",
            "E-commerce and omnichannel sales growth",
            "Gross margin and shrink/theft impact",
            "Inventory levels and markdown activity",
            "Store opening and closing plans",
            "Labor costs and store payroll leverage",
            "Private label penetration and margin contribution",
            "Loyalty program membership and engagement",
            "Supply chain and distribution center investments",
            "Comp sales and earnings guidance"
        ]
    }),

    ("food_beverage", {
        "name": "Food & Beverage",
        "sector": "Consumer",
        "key_metrics": [
            "Organic Revenue Growth",
            "Volume Growth",
            "Price Realization",
            "Gross Margin",
            "EBITDA Margin"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Growth Officer", "Chief Supply Chain Officer"],
        "aspects": [
            "Organic revenue growth by region and category",
            "Volume trends and price/mix contribution",
            "Key brand performance and innovation launches",
            "Gross margin trends and input cost inflation",
            "Pricing actions and revenue growth management",
            "Channel performance: retail, foodservice, convenience",
            "Marketing investment and brand health metrics",
            "Sustainability initiatives and packaging updates",
            "M&A and portfolio reshaping activity",
            "Organic sales and EPS guidance"
        ]
    }),

    # ========== INDUSTRIAL SECTOR ==========
    ("automotive", {
        "name": "Automotive / EV",
        "sector": "Industrial",
        "key_metrics": [
            "Vehicle Deliveries",
            "Average Selling Price",
            "Gross Margin per Vehicle",
            "Production Capacity",
            "Order Backlog"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Manufacturing Officer", "Chief Technology Officer"],
        "aspects": [
            "Vehicle production and delivery volumes by model",
            "Average selling price trends and mix effects",
            "Gross margin per vehicle and cost reduction initiatives",
            "EV-specific metrics: battery costs, range improvements",
            "Production capacity expansion and factory utilization",
            "Order backlog and reservation trends",
            "Autonomous driving and software update revenue",
            "Charging network expansion and energy business",
            "Supply chain and raw material sourcing",
            "Delivery volume and margin guidance"
        ]
    }),

    ("aerospace_defense", {
        "name": "Aerospace & Defense",
        "sector": "Industrial",
        "key_metrics": [
            "Backlog",
            "Book-to-Bill Ratio",
            "Program Margin",
            "Aftermarket Revenue",
            "Free Cash Flow"
        ],
        "executive_roles": ["CEO", "CFO", "COO", "Chief Technology Officer"],
        "aspects": [
            "Revenue by segment: commercial aerospace, defense, services",
            "Backlog growth and book-to-bill ratio",
            "Major program updates and contract awards",
            "Commercial aircraft delivery rates and recovery trajectory",
            "Defense budget outlook and priority programs",
            "Aftermarket and services revenue growth",
            "Program margins and cost performance",
            "R&D investment in next-gen platforms",
            "Free cash flow and capital deployment",
            "Revenue and earnings guidance by segment"
        ]
    }),

    ("manufacturing", {
        "name": "Manufacturing / Industrial Equipment",
        "sector": "Industrial",
        "key_metrics": [
            "Order Intake",
            "Revenue",
            "Operating Margin",
            "Backlog",
            "Aftermarket Revenue"
        ],
        "executive_roles": ["CEO", "CFO", "COO", "Chief Technology Officer"],
        "aspects": [
            "Order intake and book-to-bill trends by end market",
            "Revenue growth organic vs inorganic breakdown",
            "Operating margin by segment and price-cost dynamics",
            "Backlog and lead times commentary",
            "End market demand: construction, mining, agriculture, manufacturing",
            "Aftermarket parts and services revenue",
            "Automation and digital offerings growth",
            "Supply chain and component availability",
            "Capital allocation: M&A, dividends, buybacks",
            "Order, revenue, and margin guidance"
        ]
    }),

    # ========== TELECOM SECTOR ==========
    ("telecom", {
        "name": "Telecommunications / Media",
        "sector": "Telecom",
        "key_metrics": [
            "Service Revenue",
            "ARPU",
            "Net Subscriber Additions",
            "Churn Rate",
            "EBITDA Margin"
        ],
        "executive_roles": ["CEO", "CFO", "Chief Network Officer", "Chief Commercial Officer"],
        "aspects": [
            "Service revenue growth: wireless, broadband, enterprise",
            "Subscriber additions and churn by segment",
            "ARPU trends and pricing/bundling strategy",
            "Network investment: 5G deployment, fiber buildout",
            "Spectrum assets and capital allocation",
            "Content and media segment performance",
            "Enterprise and B2B growth initiatives",
            "Operating expense management and EBITDA margin",
            "Free cash flow and dividend sustainability",
            "Subscriber and revenue growth guidance"
        ]
    }),
])


def get_category_keys():
    """Returns a list of all category keys."""
    return list(COMPANY_CATEGORIES.keys())


def get_category_by_key(key):
    """Returns category configuration by key, or None if not found."""
    return COMPANY_CATEGORIES.get(key)


def get_categories_by_sector(sector):
    """Returns all categories belonging to a specific sector."""
    return {k: v for k, v in COMPANY_CATEGORIES.items() if v["sector"] == sector}


def get_all_sectors():
    """Returns a list of unique sectors."""
    return list(set(cat["sector"] for cat in COMPANY_CATEGORIES.values()))


if __name__ == "__main__":
    # Print summary of all categories
    print("=" * 60)
    print("COMPANY CATEGORIES SUMMARY")
    print("=" * 60)
    
    for sector in get_all_sectors():
        print(f"\n{sector.upper()} SECTOR:")
        for key, cat in get_categories_by_sector(sector).items():
            print(f"  - {key}: {cat['name']} ({len(cat['aspects'])} aspects)")
    
    print(f"\nTotal categories: {len(COMPANY_CATEGORIES)}")
