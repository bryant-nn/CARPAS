from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, everyone, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please also note, today's event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. Joining me on today’s call are {ceo_name}, Chief Executive Officer; and {cfo_name}, Chief Financial Officer.

    Before we begin, I would like to remind you that this call contains forward-looking statements, which are subject to risks and uncertainties. Please refer to our SEC filings for a complete discussion of these risks.

    With that, I’ll turn the call over to {ceo_name}.

    **{ceo_name}, Chief Executive Officer:**
    Thank you, {ir_name}. Good morning, everyone.  Thank you for joining us today. I’m pleased to report {company_name}'s performance for the {quarter}. We continued to execute on our strategic priorities and delivered solid results despite the challenging macroeconomic environment.

    Today I will cover four key aspects of our performance:

    1.  **Overall Performance:** {aspect_1_details}
    2.  **E-Commerce Growth:** {aspect_2_details}
    3.  **Store Performance:** {aspect_3_details}
    4.  **Marketing Initiatives:** {aspect_4_details}

    We are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

    Now, I'll turn the call over to {cfo_name} to provide more details on our financial results.

    **{cfo_name}, Chief Financial Officer:**
    Thank you, {ceo_name}. Good morning. I'll provide a more detailed review of our financial performance for the {quarter}.

    *   **Revenue:** Our total revenue for the quarter was {revenue_amount}, a {revenue_growth_percent}% increase/decrease compared to the same period last year.
    *   **Gross Margin:** Gross margin was {gross_margin_percent}%, primarily driven by {gross_margin_drivers}.
    *   **Operating Expenses:** Operating expenses were {operating_expenses_amount}, representing {operating_expenses_percent}% of revenue.
    *   **Net Income:** Net income was {net_income_amount}, or {earnings_per_share} per share.
    *   **Cash Flow:** We generated {cash_flow_amount} in cash flow from operations.
    *   **Inventory:** Inventory levels are currently {inventory_levels_description}.

    We are maintaining a strong balance sheet and are well positioned to invest in our growth initiatives.

    Now, let's open the line for questions.

    **Operator:**
    Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name} ({analyst_1_firm}):**
    Good morning. Can you provide more color on the impact of {specific_market_trend} on your sales?

    **{ceo_name}:**
    {response_to_analyst_1}

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name} ({analyst_2_firm}):**
    What are your expectations for same-store sales growth in the next quarter?

    **{cfo_name}:**
    {response_to_analyst_2}

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, Chief Executive Officer:**
    Thank you for your questions. In closing, we are pleased with our progress this quarter and remain focused on executing our long-term strategy. Thank you for your continued support.

    **{ir_name}, {ir_title}:**
    This concludes today's call. Thank you for joining us.
    """),
    ("5", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, everyone, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please also note, today's event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. Joining me on today’s call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and {chief_merchandising_officer_name}, Chief Merchandising Officer.

    Before we begin, I would like to remind you that this call contains forward-looking statements, which are subject to risks and uncertainties. Please refer to our SEC filings for a complete discussion of these risks.

    With that, I’ll turn the call over to {ceo_name}.

    **{ceo_name}, Chief Executive Officer:**
    Thank you, {ir_name}. Good morning, everyone.  Thank you for joining us today. I’m pleased to report {company_name}'s performance for the {quarter}. We continued to execute on our strategic priorities and delivered solid results despite the challenging macroeconomic environment.

    Today I will cover five key aspects of our performance:

    1.  **Overall Performance:** {aspect_1_details}
    2.  **E-Commerce Growth:** {aspect_2_details}
    3.  **Store Performance:** {aspect_3_details}
    4.  **Marketing Initiatives:** {aspect_4_details}
    5.  **Supply Chain Optimization:** {aspect_5_details}

    We are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

    Now, I'll turn the call over to {cfo_name} to provide more details on our financial results.

    **{cfo_name}, Chief Financial Officer:**
    Thank you, {ceo_name}. Good morning. I'll provide a more detailed review of our financial performance for the {quarter}.

    *   **Revenue:** Our total revenue for the quarter was {revenue_amount}, a {revenue_growth_percent}% increase/decrease compared to the same period last year.
    *   **Gross Margin:** Gross margin was {gross_margin_percent}%, primarily driven by {gross_margin_drivers}.
    *   **Operating Expenses:** Operating expenses were {operating_expenses_amount}, representing {operating_expenses_percent}% of revenue.
    *   **Net Income:** Net income was {net_income_amount}, or {earnings_per_share} per share.
    *   **Cash Flow:** We generated {cash_flow_amount} in cash flow from operations.
    *   **Inventory:** Inventory levels are currently {inventory_levels_description}.

    We are maintaining a strong balance sheet and are well positioned to invest in our growth initiatives.

    Now, I'd like to hand it over to {chief_merchandising_officer_name}, our Chief Merchandising Officer, to discuss our new product lines.

    **{chief_merchandising_officer_name}, Chief Merchandising Officer:**
    Thank you, {cfo_name}. This quarter, we launched our {new_product} line, which has seen {impact_of_product}. We are excited about the potential of this new product and other upcoming launches.

    Now, let's open the line for questions.

    **Operator:**
    Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name} ({analyst_1_firm}):**
    Good morning. Can you provide more color on the impact of {specific_market_trend} on your sales?

    **{ceo_name}:**
    {response_to_analyst_1}

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name} ({analyst_2_firm}):**
    What are your expectations for same-store sales growth in the next quarter?

    **{cfo_name}:**
    {response_to_analyst_2}

    **Operator:**
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    **{analyst_3_name} ({analyst_3_firm}):**
    Can you elaborate on the supply chain improvements?

    **{ceo_name}:**
    {response_to_analyst_3}

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, Chief Executive Officer:**
    Thank you for your questions. In closing, we are pleased with our progress this quarter and remain focused on executing our long-term strategy. Thank you for your continued support.

    **{ir_name}, {ir_title}:**
    This concludes today's call. Thank you for joining us.
    """),
    ("6", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, everyone, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please also note, today's event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. Joining me on today’s call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_merchandising_officer_name}, Chief Merchandising Officer; and {chief_stores_officer_name}, Chief Stores Officer.

    Before we begin, I would like to remind you that this call contains forward-looking statements, which are subject to risks and uncertainties. Please refer to our SEC filings for a complete discussion of these risks.

    With that, I’ll turn the call over to {ceo_name}.

    **{ceo_name}, Chief Executive Officer:**
    Thank you, {ir_name}. Good morning, everyone.  Thank you for joining us today. I’m pleased to report {company_name}'s performance for the {quarter}. We continued to execute on our strategic priorities and delivered solid results despite the challenging macroeconomic environment.

    Today I will cover six key aspects of our performance:

    1.  **Overall Performance:** {aspect_1_details}
    2.  **E-Commerce Growth:** {aspect_2_details}
    3.  **Store Performance:** {aspect_3_details}
    4.  **Marketing Initiatives:** {aspect_4_details}
    5.  **Supply Chain Optimization:** {aspect_5_details}
    6.  **Loyalty Program Update:** {aspect_6_details}

    We are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

    Now, I'll turn the call over to {cfo_name} to provide more details on our financial results.

    **{cfo_name}, Chief Financial Officer:**
    Thank you, {ceo_name}. Good morning. I'll provide a more detailed review of our financial performance for the {quarter}.

    *   **Revenue:** Our total revenue for the quarter was {revenue_amount}, a {revenue_growth_percent}% increase/decrease compared to the same period last year.
    *   **Gross Margin:** Gross margin was {gross_margin_percent}%, primarily driven by {gross_margin_drivers}.
    *   **Operating Expenses:** Operating expenses were {operating_expenses_amount}, representing {operating_expenses_percent}% of revenue.
    *   **Net Income:** Net income was {net_income_amount}, or {earnings_per_share} per share.
    *   **Cash Flow:** We generated {cash_flow_amount} in cash flow from operations.
    *   **Inventory:** Inventory levels are currently {inventory_levels_description}.

    We are maintaining a strong balance sheet and are well positioned to invest in our growth initiatives.

    Now, I'd like to hand it over to {chief_merchandising_officer_name}, our Chief Merchandising Officer, to discuss our new product lines, and after that to {chief_stores_officer_name} to discuss store operations.

    **{chief_merchandising_officer_name}, Chief Merchandising Officer:**
    Thank you, {cfo_name}. This quarter, we launched our {new_product} line, which has seen {impact_of_product}. We are excited about the potential of this new product and other upcoming launches.

    **{chief_stores_officer_name}, Chief Stores Officer:**
    Thank you, {chief_merchandising_officer_name}. We continue to focus on improving the customer experience in our stores. We have implemented {new_store_initiative} and are seeing positive results.

    Now, let's open the line for questions.

    **Operator:**
    Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name} ({analyst_1_firm}):**
    Good morning. Can you provide more color on the impact of {specific_market_trend} on your sales?

    **{ceo_name}:**
    {response_to_analyst_1}

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name} ({analyst_2_firm}):**
    What are your expectations for same-store sales growth in the next quarter?

    **{cfo_name}:**
    {response_to_analyst_2}

    **Operator:**
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    **{analyst_3_name} ({analyst_3_firm}):**
    Can you elaborate on the supply chain improvements?

    **{ceo_name}:**
    {response_to_analyst_3}

    **Operator:**
    Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

    **{analyst_4_name} ({analyst_4_firm}):**
    What is the impact from the loyalty program?

    **{ceo_name}:**
    {response_to_analyst_4}

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, Chief Executive Officer:**
    Thank you for your questions. In closing, we are pleased with our progress this quarter and remain focused on executing our long-term strategy. Thank you for your continued support.

    **{ir_name}, {ir_title}:**
    This concludes today's call. Thank you for joining us.
    """),
    ("7", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, everyone, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please also note, today's event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. Joining me on today’s call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_merchandising_officer_name}, Chief Merchandising Officer; {chief_stores_officer_name}, Chief Stores Officer; and {chief_marketing_officer_name}, Chief Marketing Officer.

    Before we begin, I would like to remind you that this call contains forward-looking statements, which are subject to risks and uncertainties. Please refer to our SEC filings for a complete discussion of these risks.

    With that, I’ll turn the call over to {ceo_name}.

    **{ceo_name}, Chief Executive Officer:**
    Thank you, {ir_name}. Good morning, everyone.  Thank you for joining us today. I’m pleased to report {company_name}'s performance for the {quarter}. We continued to execute on our strategic priorities and delivered solid results despite the challenging macroeconomic environment.

    Today I will cover seven key aspects of our performance:

    1.  **Overall Performance:** {aspect_1_details}
    2.  **E-Commerce Growth:** {aspect_2_details}
    3.  **Store Performance:** {aspect_3_details}
    4.  **Marketing Initiatives:** {aspect_4_details}
    5.  **Supply Chain Optimization:** {aspect_5_details}
    6.  **Loyalty Program Update:** {aspect_6_details}
    7.  **Sustainability Initiatives:** {aspect_7_details}

    We are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

    Now, I'll turn the call over to {cfo_name} to provide more details on our financial results.

    **{cfo_name}, Chief Financial Officer:**
    Thank you, {ceo_name}. Good morning. I'll provide a more detailed review of our financial performance for the {quarter}.

    *   **Revenue:** Our total revenue for the quarter was {revenue_amount}, a {revenue_growth_percent}% increase/decrease compared to the same period last year.
    *   **Gross Margin:** Gross margin was {gross_margin_percent}%, primarily driven by {gross_margin_drivers}.
    *   **Operating Expenses:** Operating expenses were {operating_expenses_amount}, representing {operating_expenses_percent}% of revenue.
    *   **Net Income:** Net income was {net_income_amount}, or {earnings_per_share} per share.
    *   **Cash Flow:** We generated {cash_flow_amount} in cash flow from operations.
    *   **Inventory:** Inventory levels are currently {inventory_levels_description}.

    We are maintaining a strong balance sheet and are well positioned to invest in our growth initiatives.

    Now, I'd like to hand it over to {chief_merchandising_officer_name}, our Chief Merchandising Officer, to discuss our new product lines, followed by {chief_stores_officer_name} to discuss store operations, and then {chief_marketing_officer_name} to discuss marketing initiatives.

    **{chief_merchandising_officer_name}, Chief Merchandising Officer:**
    Thank you, {cfo_name}. This quarter, we launched our {new_product} line, which has seen {impact_of_product}. We are excited about the potential of this new product and other upcoming launches.

    **{chief_stores_officer_name}, Chief Stores Officer:**
    Thank you, {chief_merchandising_officer_name}. We continue to focus on improving the customer experience in our stores. We have implemented {new_store_initiative} and are seeing positive results.

    **{chief_marketing_officer_name}, Chief Marketing Officer:**
    Thank you, {chief_stores_officer_name}. Our new marketing campaign, {marketing_campaign_name}, has increased brand awareness by {brand_awareness_increase}%.

    Now, let's open the line for questions.

    **Operator:**
    Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name} ({analyst_1_firm}):**
    Good morning. Can you provide more color on the impact of {specific_market_trend} on your sales?

    **{ceo_name}:**
    {response_to_analyst_1}

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name} ({analyst_2_firm}):**
    What are your expectations for same-store sales growth in the next quarter?

    **{cfo_name}:**
    {response_to_analyst_2}

    **Operator:**
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    **{analyst_3_name} ({analyst_3_firm}):**
    Can you elaborate on the supply chain improvements?

    **{ceo_name}:**
    {response_to_analyst_3}

    **Operator:**
    Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

    **{analyst_4_name} ({analyst_4_firm}):**
    What is the impact from the loyalty program?

    **{ceo_name}:**
    {response_to_analyst_4}

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, Chief Executive Officer:**
    Thank you for your questions. In closing, we are pleased with our progress this quarter and remain focused on executing our long-term strategy. Thank you for your continued support.

    **{ir_name}, {ir_title}:**
    This concludes today's call. Thank you for joining us.
    """),
    ("8", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, everyone, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please also note, today's event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. Joining me on today’s call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_merchandising_officer_name}, Chief Merchandising Officer; {chief_stores_officer_name}, Chief Stores Officer; {chief_marketing_officer_name}, Chief Marketing Officer; and {chief_technology_officer_name}, Chief Technology Officer.

    Before we begin, I would like to remind you that this call contains forward-looking statements, which are subject to risks and uncertainties. Please refer to our SEC filings for a complete discussion of these risks.

    With that, I’ll turn the call over to {ceo_name}.

    **{ceo_name}, Chief Executive Officer:**
    Thank you, {ir_name}. Good morning, everyone.  Thank you for joining us today. I’m pleased to report {company_name}'s performance for the {quarter}. We continued to execute on our strategic priorities and delivered solid results despite the challenging macroeconomic environment.

    Today I will cover eight key aspects of our performance:

    1.  **Overall Performance:** {aspect_1_details}
    2.  **E-Commerce Growth:** {aspect_2_details}
    3.  **Store Performance:** {aspect_3_details}
    4.  **Marketing Initiatives:** {aspect_4_details}
    5.  **Supply Chain Optimization:** {aspect_5_details}
    6.  **Loyalty Program Update:** {aspect_6_details}
    7.  **Sustainability Initiatives:** {aspect_7_details}
    8.  **Technology Investments:** {aspect_8_details}

    We are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

    Now, I'll turn the call over to {cfo_name} to provide more details on our financial results.

    **{cfo_name}, Chief Financial Officer:**
    Thank you, {ceo_name}. Good morning. I'll provide a more detailed review of our financial performance for the {quarter}.

    *   **Revenue:** Our total revenue for the quarter was {revenue_amount}, a {revenue_growth_percent}% increase/decrease compared to the same period last year.
    *   **Gross Margin:** Gross margin was {gross_margin_percent}%, primarily driven by {gross_margin_drivers}.
    *   **Operating Expenses:** Operating expenses were {operating_expenses_amount}, representing {operating_expenses_percent}% of revenue.
    *   **Net Income:** Net income was {net_income_amount}, or {earnings_per_share} per share.
    *   **Cash Flow:** We generated {cash_flow_amount} in cash flow from operations.
    *   **Inventory:** Inventory levels are currently {inventory_levels_description}.

    We are maintaining a strong balance sheet and are well positioned to invest in our growth initiatives.

    Now, I'd like to hand it over to {chief_merchandising_officer_name}, our Chief Merchandising Officer, to discuss our new product lines, followed by {chief_stores_officer_name} to discuss store operations, {chief_marketing_officer_name} to discuss marketing initiatives, and {chief_technology_officer_name} to talk about technology advancements.

    **{chief_merchandising_officer_name}, Chief Merchandising Officer:**
    Thank you, {cfo_name}. This quarter, we launched our {new_product} line, which has seen {impact_of_product}. We are excited about the potential of this new product and other upcoming launches.

    **{chief_stores_officer_name}, Chief Stores Officer:**
    Thank you, {chief_merchandising_officer_name}. We continue to focus on improving the customer experience in our stores. We have implemented {new_store_initiative} and are seeing positive results.

    **{chief_marketing_officer_name}, Chief Marketing Officer:**
    Thank you, {chief_stores_officer_name}. Our new marketing campaign, {marketing_campaign_name}, has increased brand awareness by {brand_awareness_increase}%.

    **{chief_technology_officer_name}, Chief Technology Officer:**
    Thank you, {chief_marketing_officer_name}. We have invested in {technology_investment_area} which has improved our {technology_improvement}.

    Now, let's open the line for questions.

    **Operator:**
    Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name} ({analyst_1_firm}):**
    Good morning. Can you provide more color on the impact of {specific_market_trend} on your sales?

    **{ceo_name}:**
    {response_to_analyst_1}

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name} ({analyst_2_firm}):**
    What are your expectations for same-store sales growth in the next quarter?

    **{cfo_name}:**
    {response_to_analyst_2}

    **Operator:**
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    **{analyst_3_name} ({analyst_3_firm}):**
    Can you elaborate on the supply chain improvements?

    **{ceo_name}:**
    {response_to_analyst_3}

    **Operator:**
    Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

    **{analyst_4_name} ({analyst_4_firm}):**
    What is the impact from the loyalty program?

    **{ceo_name}:**
    {response_to_analyst_4}

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, Chief Executive Officer:**
    Thank you for your questions. In closing, we are pleased with our progress this quarter and remain focused on executing our long-term strategy. Thank you for your continued support.

    **{ir_name}, {ir_title}:**
    This concludes today's call. Thank you for joining us.
    """)
])