from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Thank you, operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; and {coo_name}, COO.

    Before we begin, I would like to remind you that this call may contain forward-looking statements, including our expectations for future financial performance, business strategies, and market trends. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete list of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. We are pleased to report a strong {quarter} performance, driven by {aspect_1_details}, and {aspect_2_details}.

    Our focus remains on {aspect_3_details}. We are also excited about the initial traction we are seeing with our {new_product}, which we believe will significantly {impact_of_product}.

    Finally, we are committed to {aspect_4_details}.

    Now, I'll turn the call over to {cfo_name}, our CFO, to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}. Our {quarter} revenue was {revenue}, an increase of {revenue_growth}% year-over-year. Gross margin was {gross_margin}%, driven by {gross_margin_drivers}. Operating expenses were {operating_expenses}, representing {operating_expenses_percent}% of revenue.

    Our net income for the quarter was {net_income}, or {earnings_per_share} per share. We ended the quarter with {cash_balance} in cash and cash equivalents. We are reaffirming our full-year guidance of {full_year_guidance}.

    Operator, we are now ready for questions.

    Operator:
    [Operator instructions for Q&A session]. Our first question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}:
    [Analyst 1 Question]

    {ceo_name}:
    [CEO Response to Analyst 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}:
    [Analyst 2 Question]

    {cfo_name}:
    [CFO Response to Analyst 2]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}:
    [Analyst 3 Question]

    {coo_name}:
    [COO Response to Analyst 3]

    Operator:
    There are no further questions at this time. I would now like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}:
    Thank you for joining us today. We are confident in our ability to continue to execute our strategy and deliver long-term value for our shareholders. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("5", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Thank you, operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {coo_name}, COO; and {chief_marketing_officer_name}, CMO.

    Before we begin, I would like to remind you that this call may contain forward-looking statements, including our expectations for future financial performance, business strategies, and market trends. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete list of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. We are pleased to report a strong {quarter} performance, driven by {aspect_1_details}, and {aspect_2_details}. We saw significant growth in {key_metrics}.

    Our focus remains on {aspect_3_details}. We are also excited about the initial traction we are seeing with our {new_product}, which we believe will significantly {impact_of_product}.

    We are investing heavily in {aspect_4_details}

    Finally, we are committed to {aspect_5_details}.

    Now, I'll turn the call over to {cfo_name}, our CFO, to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}. Our {quarter} revenue was {revenue}, an increase of {revenue_growth}% year-over-year. Gross margin was {gross_margin}%, driven by {gross_margin_drivers}. Operating expenses were {operating_expenses}, representing {operating_expenses_percent}% of revenue. {marketing_spend_details}

    Our net income for the quarter was {net_income}, or {earnings_per_share} per share. We ended the quarter with {cash_balance} in cash and cash equivalents. We are reaffirming our full-year guidance of {full_year_guidance}.

    Now I'll turn it over to {coo_name} to discuss operations.

    {coo_name}:
    Thanks, {cfo_name}. Operationally, we focused on {operational_focus_1} and {operational_focus_2}. Our shipping times improved by {shipping_improvement}%. Fulfillment costs were {fulfillment_cost_improvement}%. We are implementing {new_technology_implementation}.

    Now I'll turn it over to {chief_marketing_officer_name}.

    {chief_marketing_officer_name}:
    Thanks, {coo_name}. From a marketing perspective, we saw strong results from {marketing_campaign_1} and {marketing_campaign_2}. Customer acquisition costs were {customer_acquisition_cost}. Our brand awareness increased by {brand_awareness_increase}%. We are focusing on {marketing_focus}.

    Operator, we are now ready for questions.

    Operator:
    [Operator instructions for Q&A session]. Our first question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}:
    [Analyst 1 Question]

    {ceo_name}:
    [CEO Response to Analyst 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}:
    [Analyst 2 Question]

    {cfo_name}:
    [CFO Response to Analyst 2]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}:
    [Analyst 3 Question]

    {coo_name}:
    [COO Response to Analyst 3]

    Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_firm}.

    {analyst_4_name}:
    [Analyst 4 Question]

    {chief_marketing_officer_name}:
    [CMO Response to Analyst 4]

    Operator:
    There are no further questions at this time. I would now like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}:
    Thank you for joining us today. We are confident in our ability to continue to execute our strategy and deliver long-term value for our shareholders. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("6", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Thank you, operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {coo_name}, COO; {chief_marketing_officer_name}, CMO; and {chief_technology_officer_name}, CTO.

    Before we begin, I would like to remind you that this call may contain forward-looking statements, including our expectations for future financial performance, business strategies, and market trends. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete list of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. We are pleased to report a strong {quarter} performance, driven by {aspect_1_details}, and {aspect_2_details}. We saw significant growth in {key_metrics}.

    Our focus remains on {aspect_3_details}. We are also excited about the initial traction we are seeing with our {new_product}, which we believe will significantly {impact_of_product}.

    We are investing heavily in {aspect_4_details}

    We are focused on improving {aspect_5_details}.

    Finally, we are committed to {aspect_6_details}.

    Now, I'll turn the call over to {cfo_name}, our CFO, to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}. Our {quarter} revenue was {revenue}, an increase of {revenue_growth}% year-over-year. Gross margin was {gross_margin}%, driven by {gross_margin_drivers}. Operating expenses were {operating_expenses}, representing {operating_expenses_percent}% of revenue. {marketing_spend_details}

    Our net income for the quarter was {net_income}, or {earnings_per_share} per share. We ended the quarter with {cash_balance} in cash and cash equivalents. We are reaffirming our full-year guidance of {full_year_guidance}.

    Now I'll turn it over to {coo_name} to discuss operations.

    {coo_name}:
    Thanks, {cfo_name}. Operationally, we focused on {operational_focus_1} and {operational_focus_2}. Our shipping times improved by {shipping_improvement}%. Fulfillment costs were {fulfillment_cost_improvement}%. We are implementing {new_technology_implementation}.

    Now I'll turn it over to {chief_marketing_officer_name}.

    {chief_marketing_officer_name}:
    Thanks, {coo_name}. From a marketing perspective, we saw strong results from {marketing_campaign_1} and {marketing_campaign_2}. Customer acquisition costs were {customer_acquisition_cost}. Our brand awareness increased by {brand_awareness_increase}%. We are focusing on {marketing_focus}.

    Now I'll turn it over to {chief_technology_officer_name}.

    {chief_technology_officer_name}:
    Thanks, {chief_marketing_officer_name}. On the technology front, we've been focused on {technology_focus_1} and {technology_focus_2}. Our website uptime was {website_uptime}%. Mobile app usage increased by {mobile_app_usage_increase}%. We're investing in {new_tech_investment}.

    Operator, we are now ready for questions.

    Operator:
    [Operator instructions for Q&A session]. Our first question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}:
    [Analyst 1 Question]

    {ceo_name}:
    [CEO Response to Analyst 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}:
    [Analyst 2 Question]

    {cfo_name}:
    [CFO Response to Analyst 2]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}:
    [Analyst 3 Question]

    {coo_name}:
    [COO Response to Analyst 3]

    Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_firm}.

    {analyst_4_name}:
    [Analyst 4 Question]

    {chief_marketing_officer_name}:
    [CMO Response to Analyst 4]

    Operator:
    Our next question comes from {analyst_5_name} with {analyst_5_firm}.

    {analyst_5_name}:
    [Analyst 5 Question]

    {chief_technology_officer_name}:
    [CTO Response to Analyst 5]

    Operator:
    There are no further questions at this time. I would now like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}:
    Thank you for joining us today. We are confident in our ability to continue to execute our strategy and deliver long-term value for our shareholders. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("7", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Thank you, operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {coo_name}, COO; {chief_marketing_officer_name}, CMO; {chief_technology_officer_name}, CTO; and {chief_data_officer_name}, CDO.

    Before we begin, I would like to remind you that this call may contain forward-looking statements, including our expectations for future financial performance, business strategies, and market trends. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete list of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. We are pleased to report a strong {quarter} performance, driven by {aspect_1_details}, and {aspect_2_details}. We saw significant growth in {key_metrics}.

    Our focus remains on {aspect_3_details}. We are also excited about the initial traction we are seeing with our {new_product}, which we believe will significantly {impact_of_product}.

    We are investing heavily in {aspect_4_details}

    We are focused on improving {aspect_5_details}.

    We are expanding our presence in {aspect_6_details}.

    Finally, we are committed to {aspect_7_details}.

    Now, I'll turn the call over to {cfo_name}, our CFO, to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}. Our {quarter} revenue was {revenue}, an increase of {revenue_growth}% year-over-year. Gross margin was {gross_margin}%, driven by {gross_margin_drivers}. Operating expenses were {operating_expenses}, representing {operating_expenses_percent}% of revenue. {marketing_spend_details}

    Our net income for the quarter was {net_income}, or {earnings_per_share} per share. We ended the quarter with {cash_balance} in cash and cash equivalents. We are reaffirming our full-year guidance of {full_year_guidance}.

    Now I'll turn it over to {coo_name} to discuss operations.

    {coo_name}:
    Thanks, {cfo_name}. Operationally, we focused on {operational_focus_1} and {operational_focus_2}. Our shipping times improved by {shipping_improvement}%. Fulfillment costs were {fulfillment_cost_improvement}%. We are implementing {new_technology_implementation}.

    Now I'll turn it over to {chief_marketing_officer_name}.

    {chief_marketing_officer_name}:
    Thanks, {coo_name}. From a marketing perspective, we saw strong results from {marketing_campaign_1} and {marketing_campaign_2}. Customer acquisition costs were {customer_acquisition_cost}. Our brand awareness increased by {brand_awareness_increase}%. We are focusing on {marketing_focus}.

    Now I'll turn it over to {chief_technology_officer_name}.

    {chief_technology_officer_name}:
    Thanks, {chief_marketing_officer_name}. On the technology front, we've been focused on {technology_focus_1} and {technology_focus_2}. Our website uptime was {website_uptime}%. Mobile app usage increased by {mobile_app_usage_increase}%. We're investing in {new_tech_investment}.

    Now I'll turn it over to {chief_data_officer_name}.

    {chief_data_officer_name}:
    Thanks, {chief_technology_officer_name}. Data science is a key focus for us. We've seen a {conversion_rate_improvement}% improvement in conversion rates because of {data_science_initiative}. We are also focusing on {data_privacy_initiative}.

    Operator, we are now ready for questions.

    Operator:
    [Operator instructions for Q&A session]. Our first question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}:
    [Analyst 1 Question]

    {ceo_name}:
    [CEO Response to Analyst 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}:
    [Analyst 2 Question]

    {cfo_name}:
    [CFO Response to Analyst 2]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}:
    [Analyst 3 Question]

    {coo_name}:
    [COO Response to Analyst 3]

    Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_firm}.

    {analyst_4_name}:
    [Analyst 4 Question]

    {chief_marketing_officer_name}:
    [CMO Response to Analyst 4]

    Operator:
    Our next question comes from {analyst_5_name} with {analyst_5_firm}.

    {analyst_5_name}:
    [Analyst 5 Question]

    {chief_technology_officer_name}:
    [CTO Response to Analyst 5]

    Operator:
    Our next question comes from {analyst_6_name} with {analyst_6_firm}.

    {analyst_6_name}:
    [Analyst 6 Question]

    {chief_data_officer_name}:
    [CDO Response to Analyst 6]

    Operator:
    There are no further questions at this time. I would now like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}:
    Thank you for joining us today. We are confident in our ability to continue to execute our strategy and deliver long-term value for our shareholders. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("8", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Thank you, operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {coo_name}, COO; {chief_marketing_officer_name}, CMO; {chief_technology_officer_name}, CTO; {chief_data_officer_name}, CDO; and {chief_sustainability_officer_name}, CSO.

    Before we begin, I would like to remind you that this call may contain forward-looking statements, including our expectations for future financial performance, business strategies, and market trends. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete list of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. We are pleased to report a strong {quarter} performance, driven by {aspect_1_details}, and {aspect_2_details}. We saw significant growth in {key_metrics}.

    Our focus remains on {aspect_3_details}. We are also excited about the initial traction we are seeing with our {new_product}, which we believe will significantly {impact_of_product}.

    We are investing heavily in {aspect_4_details}

    We are focused on improving {aspect_5_details}.

    We are expanding our presence in {aspect_6_details}.

    We are enhancing our customer experience through {aspect_7_details}.

    Finally, we are committed to {aspect_8_details}.

    Now, I'll turn the call over to {cfo_name}, our CFO, to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}. Our {quarter} revenue was {revenue}, an increase of {revenue_growth}% year-over-year. Gross margin was {gross_margin}%, driven by {gross_margin_drivers}. Operating expenses were {operating_expenses}, representing {operating_expenses_percent}% of revenue. {marketing_spend_details}

    Our net income for the quarter was {net_income}, or {earnings_per_share} per share. We ended the quarter with {cash_balance} in cash and cash equivalents. We are reaffirming our full-year guidance of {full_year_guidance}.

    Now I'll turn it over to {coo_name} to discuss operations.

    {coo_name}:
    Thanks, {cfo_name}. Operationally, we focused on {operational_focus_1} and {operational_focus_2}. Our shipping times improved by {shipping_improvement}%. Fulfillment costs were {fulfillment_cost_improvement}%. We are implementing {new_technology_implementation}.

    Now I'll turn it over to {chief_marketing_officer_name}.

    {chief_marketing_officer_name}:
    Thanks, {coo_name}. From a marketing perspective, we saw strong results from {marketing_campaign_1} and {marketing_campaign_2}. Customer acquisition costs were {customer_acquisition_cost}. Our brand awareness increased by {brand_awareness_increase}%. We are focusing on {marketing_focus}.

    Now I'll turn it over to {chief_technology_officer_name}.

    {chief_technology_officer_name}:
    Thanks, {chief_marketing_officer_name}. On the technology front, we've been focused on {technology_focus_1} and {technology_focus_2}. Our website uptime was {website_uptime}%. Mobile app usage increased by {mobile_app_usage_increase}%. We're investing in {new_tech_investment}.

    Now I'll turn it over to {chief_data_officer_name}.

    {chief_data_officer_name}:
    Thanks, {chief_technology_officer_name}. Data science is a key focus for us. We've seen a {conversion_rate_improvement}% improvement in conversion rates because of {data_science_initiative}. We are also focusing on {data_privacy_initiative}.

    Now I'll turn it over to {chief_sustainability_officer_name}.

    {chief_sustainability_officer_name}:
    Thanks, {chief_data_officer_name}. Sustainability is very important to us. We reduced our carbon footprint by {carbon_reduction_percentage}%. We are committed to {sustainability_initiative_1} and {sustainability_initiative_2}.

    Operator, we are now ready for questions.

    Operator:
    [Operator instructions for Q&A session]. Our first question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}:
    [Analyst 1 Question]

    {ceo_name}:
    [CEO Response to Analyst 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}:
    [Analyst 2 Question]

    {cfo_name}:
    [CFO Response to Analyst 2]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}:
    [Analyst 3 Question]

    {coo_name}:
    [COO Response to Analyst 3]

    Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_firm}.

    {analyst_4_name}:
    [Analyst 4 Question]

    {chief_marketing_officer_name}:
    [CMO Response to Analyst 4]

    Operator:
    Our next question comes from {analyst_5_name} with {analyst_5_firm}.

    {analyst_5_name}:
    [Analyst 5 Question]

    {chief_technology_officer_name}:
    [CTO Response to Analyst 5]

    Operator:
    Our next question comes from {analyst_6_name} with {analyst_6_firm}.

    {analyst_6_name}:
    [Analyst 6 Question]

    {chief_data_officer_name}:
    [CDO Response to Analyst 6]

    Operator:
    Our next question comes from {analyst_7_name} with {analyst_7_firm}.

    {analyst_7_name}:
    [Analyst 7 Question]

    {chief_sustainability_officer_name}:
    [CSO Response to Analyst 7]

    Operator:
    There are no further questions at this time. I would now like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}:
    Thank you for joining us today. We are confident in our ability to continue to execute our strategy and deliver long-term value for our shareholders. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """)
])