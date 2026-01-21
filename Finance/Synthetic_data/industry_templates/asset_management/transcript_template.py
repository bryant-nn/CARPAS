from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and {cio_name}, Chief Investment Officer.

    Before we begin, I'd like to remind you that some of the statements made today may be forward-looking. Please refer to our SEC filings for a discussion of the risks and uncertainties that could cause actual results to differ materially.

    With that, I'll turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us. I'm pleased to report on our performance for {quarter}. We achieved solid results this quarter, driven by {aspect_1_details}.

    {cfo_name}: Thank you, {ceo_name}. From a financial perspective, {company_name} delivered strong results in {quarter}. Our revenue was {revenue_amount}, representing a {revenue_growth_percentage}% increase year-over-year. This growth was primarily driven by {aspect_2_details}. Our expenses were {expense_amount}, resulting in net income of {net_income_amount}. We continue to manage our expenses prudently while investing in key growth initiatives.

    {cio_name}: Thank you, {cfo_name}. On the investment front, we continue to focus on delivering strong risk-adjusted returns for our clients.  Our key strategies performed well, particularly in {asset_class}. We are navigating the current market environment by {aspect_3_details}.

    {ceo_name}: In summary, we are confident in our ability to continue delivering value to our shareholders. We are focused on executing our strategic priorities and capitalizing on the opportunities ahead.  This includes {aspect_4_details}.

    Operator: Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Can you provide more details on {analyst_question_1}?

    {ceo_name}: [Response to Analyst Question 1]

    [Analyst Name]: Thank you. And a follow-up on {analyst_question_2}?

    {cfo_name}: [Response to Analyst Question 2]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Could you elaborate on the performance of {specific_fund}?

    {cio_name}: [Response to Analyst Question 3]

    Operator: Thank you. There are no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}: Thank you for joining us today. We appreciate your interest in {company_name}. We look forward to speaking with you again next quarter.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("5", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cio_name}, Chief Investment Officer; and {head_of_distribution_name}, Head of Distribution.

    Before we begin, I'd like to remind you that some of the statements made today may be forward-looking. Please refer to our SEC filings for a discussion of the risks and uncertainties that could cause actual results to differ materially.

    With that, I'll turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us. I'm pleased to report on our performance for {quarter}. We achieved solid results this quarter, driven by {aspect_1_details}. Our AUM grew to {aum_amount}.

    {cfo_name}: Thank you, {ceo_name}. From a financial perspective, {company_name} delivered strong results in {quarter}. Our revenue was {revenue_amount}, representing a {revenue_growth_percentage}% increase year-over-year. This growth was primarily driven by {aspect_2_details}. Our expenses were {expense_amount}, resulting in net income of {net_income_amount}. We continue to manage our expenses prudently.

    {cio_name}: Thank you, {cfo_name}. On the investment front, we continue to focus on delivering strong risk-adjusted returns for our clients. Our key strategies performed well, particularly in {asset_class}. We are navigating the current market environment by {aspect_3_details}. We launched {new_product} this quarter, and the early reception has been positive, with {impact_of_product}.

    {head_of_distribution_name}: Thank you, {cio_name}.  From a distribution perspective, we saw strong inflows into our {fund_type} funds.  Our efforts to expand our reach in {geographic_region} are paying off, as evidenced by {aspect_4_details}.

    {ceo_name}: In summary, we are confident in our ability to continue delivering value to our shareholders. We are focused on executing our strategic priorities and capitalizing on the opportunities ahead.  This includes {aspect_5_details}.

    Operator: Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Can you provide more details on {analyst_question_1}?

    {ceo_name}: [Response to Analyst Question 1]

    [Analyst Name]: Thank you. And a follow-up on {analyst_question_2}?

    {cfo_name}: [Response to Analyst Question 2]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Could you elaborate on the performance of {specific_fund}?

    {cio_name}: [Response to Analyst Question 3]

    [Analyst Name]: And how is the new product {new_product} performing relative to expectations?

    {head_of_distribution_name}: [Response to Analyst Question 4]

    Operator: Thank you. There are no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}: Thank you for joining us today. We appreciate your interest in {company_name}. We look forward to speaking with you again next quarter.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("6", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cio_name}, Chief Investment Officer; {head_of_distribution_name}, Head of Distribution; and {head_of_operations_name}, Head of Operations.

    Before we begin, I'd like to remind you that some of the statements made today may be forward-looking. Please refer to our SEC filings for a discussion of the risks and uncertainties that could cause actual results to differ materially.

    With that, I'll turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us. I'm pleased to report on our performance for {quarter}. We achieved solid results this quarter, driven by {aspect_1_details}. Our AUM grew to {aum_amount}.

    {cfo_name}: Thank you, {ceo_name}. From a financial perspective, {company_name} delivered strong results in {quarter}. Our revenue was {revenue_amount}, representing a {revenue_growth_percentage}% increase year-over-year. This growth was primarily driven by {aspect_2_details}. Our expenses were {expense_amount}, resulting in net income of {net_income_amount}. Our expense ratio improved due to {expense_ratio_improvement}.

    {cio_name}: Thank you, {cfo_name}. On the investment front, we continue to focus on delivering strong risk-adjusted returns for our clients. Our key strategies performed well, particularly in {asset_class}. We are navigating the current market environment by {aspect_3_details}. We launched {new_product} this quarter, and the early reception has been positive, with {impact_of_product}.

    {head_of_distribution_name}: Thank you, {cio_name}. From a distribution perspective, we saw strong inflows into our {fund_type} funds. Our efforts to expand our reach in {geographic_region} are paying off, as evidenced by {aspect_4_details}.

    {head_of_operations_name}: Thank you, {head_of_distribution_name}. Operationally, we've made significant progress in improving our technology infrastructure.  This has resulted in increased efficiency and reduced operational risk.  We are also focused on {aspect_5_details}.

    {ceo_name}: In summary, we are confident in our ability to continue delivering value to our shareholders. We are focused on executing our strategic priorities and capitalizing on the opportunities ahead. This includes {aspect_6_details}.

    Operator: Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Can you provide more details on {analyst_question_1}?

    {ceo_name}: [Response to Analyst Question 1]

    [Analyst Name]: Thank you. And a follow-up on {analyst_question_2}?

    {cfo_name}: [Response to Analyst Question 2]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Could you elaborate on the performance of {specific_fund}?

    {cio_name}: [Response to Analyst Question 3]

    [Analyst Name]: And how is the new product {new_product} performing relative to expectations?

    {head_of_distribution_name}: [Response to Analyst Question 4]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Can you provide more color on the operational efficiencies you've gained?

    {head_of_operations_name}: [Response to Analyst Question 5]

    Operator: Thank you. There are no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}: Thank you for joining us today. We appreciate your interest in {company_name}. We look forward to speaking with you again next quarter.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("7", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cio_name}, Chief Investment Officer; {head_of_distribution_name}, Head of Distribution; {head_of_operations_name}, Head of Operations; and {head_of_risk_management_name}, Head of Risk Management.

    Before we begin, I'd like to remind you that some of the statements made today may be forward-looking. Please refer to our SEC filings for a discussion of the risks and uncertainties that could cause actual results to differ materially.

    With that, I'll turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us. I'm pleased to report on our performance for {quarter}. We achieved solid results this quarter, driven by {aspect_1_details}. Our AUM grew to {aum_amount}.

    {cfo_name}: Thank you, {ceo_name}. From a financial perspective, {company_name} delivered strong results in {quarter}. Our revenue was {revenue_amount}, representing a {revenue_growth_percentage}% increase year-over-year. This growth was primarily driven by {aspect_2_details}. Our expenses were {expense_amount}, resulting in net income of {net_income_amount}. Our expense ratio improved due to {expense_ratio_improvement}.

    {cio_name}: Thank you, {cfo_name}. On the investment front, we continue to focus on delivering strong risk-adjusted returns for our clients. Our key strategies performed well, particularly in {asset_class}. We are navigating the current market environment by {aspect_3_details}. We launched {new_product} this quarter, and the early reception has been positive, with {impact_of_product}.

    {head_of_distribution_name}: Thank you, {cio_name}. From a distribution perspective, we saw strong inflows into our {fund_type} funds. Our efforts to expand our reach in {geographic_region} are paying off, as evidenced by {aspect_4_details}.

    {head_of_operations_name}: Thank you, {head_of_distribution_name}. Operationally, we've made significant progress in improving our technology infrastructure. This has resulted in increased efficiency and reduced operational risk. We are also focused on {aspect_5_details}.

    {head_of_risk_management_name}: Thank you, {head_of_operations_name}. From a risk management perspective, we continue to maintain a robust framework to identify, assess, and mitigate risks across the organization.  We have enhanced our monitoring of {risk_area} and are taking steps to address potential vulnerabilities.  This includes {aspect_6_details}.

    {ceo_name}: In summary, we are confident in our ability to continue delivering value to our shareholders. We are focused on executing our strategic priorities and capitalizing on the opportunities ahead. This includes {aspect_7_details}.

    Operator: Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Can you provide more details on {analyst_question_1}?

    {ceo_name}: [Response to Analyst Question 1]

    [Analyst Name]: Thank you. And a follow-up on {analyst_question_2}?

    {cfo_name}: [Response to Analyst Question 2]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Could you elaborate on the performance of {specific_fund}?

    {cio_name}: [Response to Analyst Question 3]

    [Analyst Name]: And how is the new product {new_product} performing relative to expectations?

    {head_of_distribution_name}: [Response to Analyst Question 4]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Can you provide more color on the operational efficiencies you've gained?

    {head_of_operations_name}: [Response to Analyst Question 5]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: What are your thoughts on the current regulatory environment and its impact on your risk profile?

    {head_of_risk_management_name}: [Response to Analyst Question 6]

    Operator: Thank you. There are no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}: Thank you for joining us today. We appreciate your interest in {company_name}. We look forward to speaking with you again next quarter.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("8", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cio_name}, Chief Investment Officer; {head_of_distribution_name}, Head of Distribution; {head_of_operations_name}, Head of Operations; {head_of_risk_management_name}, Head of Risk Management; and {head_of_technology_name}, Head of Technology.

    Before we begin, I'd like to remind you that some of the statements made today may be forward-looking. Please refer to our SEC filings for a discussion of the risks and uncertainties that could cause actual results to differ materially.

    With that, I'll turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us. I'm pleased to report on our performance for {quarter}. We achieved solid results this quarter, driven by {aspect_1_details}. Our AUM grew to {aum_amount}.

    {cfo_name}: Thank you, {ceo_name}. From a financial perspective, {company_name} delivered strong results in {quarter}. Our revenue was {revenue_amount}, representing a {revenue_growth_percentage}% increase year-over-year. This growth was primarily driven by {aspect_2_details}. Our expenses were {expense_amount}, resulting in net income of {net_income_amount}. Our expense ratio improved due to {expense_ratio_improvement}.

    {cio_name}: Thank you, {cfo_name}. On the investment front, we continue to focus on delivering strong risk-adjusted returns for our clients. Our key strategies performed well, particularly in {asset_class}. We are navigating the current market environment by {aspect_3_details}. We launched {new_product} this quarter, and the early reception has been positive, with {impact_of_product}.

    {head_of_distribution_name}: Thank you, {cio_name}. From a distribution perspective, we saw strong inflows into our {fund_type} funds. Our efforts to expand our reach in {geographic_region} are paying off, as evidenced by {aspect_4_details}.

    {head_of_operations_name}: Thank you, {head_of_distribution_name}. Operationally, we've made significant progress in streamlining our middle and back office functions. This has resulted in increased efficiency and reduced operational risk. We are also focused on {aspect_5_details}.

    {head_of_risk_management_name}: Thank you, {head_of_operations_name}. From a risk management perspective, we continue to maintain a robust framework to identify, assess, and mitigate risks across the organization. We have enhanced our monitoring of {risk_area} and are taking steps to address potential vulnerabilities. This includes {aspect_6_details}.

    {head_of_technology_name}: Thank you, {head_of_risk_management_name}. On the technology front, we are investing in advanced analytics and AI to enhance our investment decision-making process and improve client service. We are also focused on strengthening our cybersecurity posture. Specifically, {aspect_7_details}.

    {ceo_name}: In summary, we are confident in our ability to continue delivering value to our shareholders. We are focused on executing our strategic priorities and capitalizing on the opportunities ahead. This includes {aspect_8_details}.

    Operator: Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Can you provide more details on {analyst_question_1}?

    {ceo_name}: [Response to Analyst Question 1]

    [Analyst Name]: Thank you. And a follow-up on {analyst_question_2}?

    {cfo_name}: [Response to Analyst Question 2]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Good morning. Could you elaborate on the performance of {specific_fund}?

    {cio_name}: [Response to Analyst Question 3]

    [Analyst Name]: And how is the new product {new_product} performing relative to expectations?

    {head_of_distribution_name}: [Response to Analyst Question 4]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: Can you provide more color on the operational efficiencies you've gained?

    {head_of_operations_name}: [Response to Analyst Question 5]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: What are your thoughts on the current regulatory environment and its impact on your risk profile?

    {head_of_risk_management_name}: [Response to Analyst Question 6]

    Operator: Our next question comes from [Analyst Name] with [Analyst Firm].

    [Analyst Name]: How are you leveraging technology to improve investment performance?

    {head_of_technology_name}: [Response to Analyst Question 7]

    Operator: Thank you. There are no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

    {ceo_name}: Thank you for joining us today. We appreciate your interest in {company_name}. We look forward to speaking with you again next quarter.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """)
])