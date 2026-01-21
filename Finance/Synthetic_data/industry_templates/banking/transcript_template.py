from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
    Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today to review {company_name}'s results for the {quarter}. With me this morning are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cro_name}, Chief Risk Officer.

    Before we begin, let me remind you that some of the statements we will be making today are forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties. Please refer to our SEC filings for a discussion of these factors.

    I will now turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} delivered solid performance in the {quarter}, demonstrating the strength of our diversified business model and our commitment to serving our customers.

    Our key priorities for this year remain focused on:
    1.  Enhancing customer experience
    2.  Driving operational efficiency
    3.  Investing in strategic growth initiatives
    4.  Maintaining strong capital levels.

    Now, I'd like to provide some highlights on:
    {aspect_1_details}
    {aspect_2_details}
    {aspect_3_details}
    {aspect_4_details}

    I will now turn the call over to {cfo_name} to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}, and good morning. {company_name} reported net income of {net_income} for the {quarter}, or {earnings_per_share} per share. Our results reflect strong revenue growth, disciplined expense management, and a healthy credit environment.

    Net interest income increased {nii_increase} driven by higher interest rates and loan growth. Non-interest income was impacted by {non_interest_income_impact}. We continue to maintain a strong capital position with a CET1 ratio of {cet1_ratio}. We are pleased with the progress we are making on our strategic initiatives, and we remain confident in our ability to deliver sustainable value for our shareholders.

    Operator, we are now ready to open the line for questions.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}. Please go ahead.

    {analyst_1_name}:
    Good morning. Can you provide some color on {analyst_1_question}?

    {ceo_name}:
    [Response to analyst_1_question]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_company}. Please go ahead.

    {analyst_2_name}:
    Good morning. What is your outlook for {analyst_2_question}?

    {cfo_name}:
    [Response to analyst_2_question]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_company}. Please go ahead.

    {analyst_3_name}:
    Good morning. Can you discuss the impact of {analyst_3_question} on your loan portfolio?

    {cro_name}:
    [Response to analyst_3_question]

    Operator:
    There are no further questions at this time. I'd like to turn the conference back over to {ceo_name} for any closing remarks.

    {ceo_name}:
    Thank you for your interest in {company_name}. We appreciate you joining us today. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("5", """
    Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today to review {company_name}'s results for the {quarter}. With me this morning are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cro_name}, Chief Risk Officer; and {cco_name}, Chief Credit Officer.

    Before we begin, let me remind you that some of the statements we will be making today are forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties. Please refer to our SEC filings for a discussion of these factors.

    I will now turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} delivered strong performance in the {quarter}, driven by our commitment to customer service and operational excellence.

    Our key priorities for this year remain focused on:
    1.  Growing our core businesses
    2.  Investing in technology and innovation
    3.  Managing risk effectively
    4.  Optimizing our capital allocation
    5.  Enhancing our employee engagement.

    Now, I'd like to provide some highlights on:
    {aspect_1_details}
    {aspect_2_details}
    {aspect_3_details}
    {aspect_4_details}
    {aspect_5_details}

    I will now turn the call over to {cfo_name} to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}, and good morning. {company_name} reported net income of {net_income} for the {quarter}, or {earnings_per_share} per share. Our results reflect strong revenue growth, disciplined expense management, and a healthy credit environment.

    Net interest income increased {nii_increase} due to loan growth and improved net interest margin. Non-interest income was {non_interest_income_performance}. Key performance indicators include {kpi_1}, {kpi_2}. We are confident in our ability to achieve our financial goals for the year.

    {cro_name}:
    Thank you, {cfo_name}. As Chief Risk Officer, I would like to briefly discuss our risk management framework. We continue to prioritize proactive risk identification and mitigation. Our key focus areas include {risk_area_1}, {risk_area_2}. We remain vigilant in monitoring emerging risks and adapting our strategies accordingly.

    Operator, we are now ready to open the line for questions.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}. Please go ahead.

    {analyst_1_name}:
    Good morning. Can you provide more detail on {analyst_1_question}?

    {ceo_name}:
    [Response to analyst_1_question]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_company}. Please go ahead.

    {analyst_2_name}:
    What are your expectations for {analyst_2_question}?

    {cfo_name}:
    [Response to analyst_2_question]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_company}. Please go ahead.

    {analyst_3_name}:
    Can you comment on the credit quality of {analyst_3_question}?

    {cco_name}:
    [Response to analyst_3_question]

    Operator:
    There are no further questions at this time. I'd like to turn the conference back over to {ceo_name} for any closing remarks.

    {ceo_name}:
    Thank you for your interest in {company_name}. We appreciate you joining us today. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("6", """
    Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today to review {company_name}'s results for the {quarter}. With me this morning are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cro_name}, Chief Risk Officer; {cco_name}, Chief Credit Officer; and {cto_name}, Chief Technology Officer.

    Before we begin, let me remind you that some of the statements we will be making today are forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties. Please refer to our SEC filings for a discussion of these factors.

    I will now turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} delivered excellent results in the {quarter}, demonstrating the strength of our franchise and our ability to navigate a dynamic market environment.

    Our key priorities for this year remain focused on:
    1.  Expanding our market share
    2.  Improving our efficiency ratio
    3.  Strengthening our balance sheet
    4.  Investing in our people
    5.  Driving innovation
    6.  Meeting our ESG goals.

    Now, I'd like to provide some highlights on:
    {aspect_1_details}
    {aspect_2_details}
    {aspect_3_details}
    {aspect_4_details}
    {aspect_5_details}
    {aspect_6_details}

    I will now turn the call over to {cfo_name} to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}, and good morning. {company_name} reported net income of {net_income} for the {quarter}, or {earnings_per_share} per share. Our results reflect strong revenue growth, disciplined expense management, and a healthy credit environment.

    Net interest income increased {nii_increase} due to {nii_drivers}. Non-interest income was {non_interest_income_performance} driven by {non_interest_income_drivers}. Our efficiency ratio improved to {efficiency_ratio}. We are on track to achieve our financial targets for the year.

    {cro_name}:
    Thank you, {cfo_name}.  From a risk perspective, we are closely monitoring {risk_factor_1} and {risk_factor_2}. We are taking proactive steps to mitigate these risks and maintain a strong risk profile.

    {cco_name}:
    Good morning. Our credit quality remains strong with {credit_quality_metric_1} at {credit_quality_value_1} and {credit_quality_metric_2} at {credit_quality_value_2}. We are actively managing our loan portfolio and remain confident in our ability to navigate the current economic environment.

    Operator, we are now ready to open the line for questions.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}. Please go ahead.

    {analyst_1_name}:
    Good morning. Can you elaborate on {analyst_1_question}?

    {ceo_name}:
    [Response to analyst_1_question]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_company}. Please go ahead.

    {analyst_2_name}:
    What is your strategy for {analyst_2_question}?

    {cfo_name}:
    [Response to analyst_2_question]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_company}. Please go ahead.

    {analyst_3_name}:
    How are you addressing {analyst_3_question}?

    {cro_name}:
    [Response to analyst_3_question]

    Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_company}. Please go ahead.

    {analyst_4_name}:
    Can you update us on {analyst_4_question}?

    {cco_name}:
    [Response to analyst_4_question]

    Operator:
    There are no further questions at this time. I'd like to turn the conference back over to {ceo_name} for any closing remarks.

    {ceo_name}:
    Thank you for your interest in {company_name}. We appreciate you joining us today. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("7", """
    Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today to review {company_name}'s results for the {quarter}. With me this morning are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cro_name}, Chief Risk Officer; {cco_name}, Chief Credit Officer; {cto_name}, Chief Technology Officer; and {coo_name}, Chief Operating Officer.

    Before we begin, let me remind you that some of the statements we will be making today are forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties. Please refer to our SEC filings for a discussion of these factors.

    I will now turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} delivered exceptional results in the {quarter}, exceeding expectations and demonstrating the strength of our diversified business model.

    Our key priorities for this year remain focused on:
    1.  Accelerating revenue growth
    2.  Improving profitability
    3.  Managing risk effectively
    4.  Investing in technology and innovation
    5.  Enhancing customer experience
    6.  Strengthening our brand
    7.  Delivering value to our shareholders.

    Now, I'd like to provide some highlights on:
    {aspect_1_details}
    {aspect_2_details}
    {aspect_3_details}
    {aspect_4_details}
    {aspect_5_details}
    {aspect_6_details}
    {aspect_7_details}

    I will now turn the call over to {cfo_name} to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}, and good morning. {company_name} reported net income of {net_income} for the {quarter}, or {earnings_per_share} per share. Our results reflect strong revenue growth, disciplined expense management, and a healthy credit environment.

    Net interest income increased {nii_increase} driven by {nii_driver_1} and {nii_driver_2}. Non-interest income was {non_interest_income_performance}, reflecting strong performance in {non_interest_income_segment_1} and {non_interest_income_segment_2}. Our capital ratios remain strong, and we are well-positioned to support future growth.

    {cro_name}:
    Thank you, {cfo_name}. From a risk management perspective, we are closely monitoring {risk_area_1}, {risk_area_2}, and {risk_area_3}. We are taking proactive steps to mitigate these risks and maintain a strong risk profile.

    {cco_name}:
    Good morning. Our credit quality remains exceptionally strong with {credit_quality_metric_1} at {credit_quality_value_1} and {credit_quality_metric_2} at {credit_quality_value_2}. We are actively managing our loan portfolio and remain confident in our ability to navigate the current economic environment. Specifically, the performance of our {loan_segment} portfolio has been strong.

    {cto_name}:
    Thank you. I'd like to provide an update on our technology initiatives. We are making significant progress on our digital transformation, including the launch of {new_product} which has seen {impact_of_product} in terms of customer adoption and efficiency gains.

    {coo_name}:
    Good morning. We are focused on operational excellence and driving efficiency across the organization. Key initiatives include {operational_initiative_1} and {operational_initiative_2}, which are contributing to improved productivity and cost savings.

    Operator, we are now ready to open the line for questions.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}. Please go ahead.

    {analyst_1_name}:
    Good morning. Can you provide further insights into {analyst_1_question}?

    {ceo_name}:
    [Response to analyst_1_question]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_company}. Please go ahead.

    {analyst_2_name}:
    What are your plans for {analyst_2_question}?

    {cfo_name}:
    [Response to analyst_2_question]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_company}. Please go ahead.

    {analyst_3_name}:
    How are you managing {analyst_3_question}?

    {cro_name}:
    [Response to analyst_3_question]

    Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_company}. Please go ahead.

    {analyst_4_name}:
    Can you discuss the performance of {analyst_4_question}?

    {cco_name}:
    [Response to analyst_4_question]

    Operator:
    There are no further questions at this time. I'd like to turn the conference back over to {ceo_name} for any closing remarks.

    {ceo_name}:
    Thank you for your interest in {company_name}. We appreciate you joining us today. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("8", """
    Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today to review {company_name}'s results for the {quarter}. With me this morning are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cro_name}, Chief Risk Officer; {cco_name}, Chief Credit Officer; {cto_name}, Chief Technology Officer; {coo_name}, Chief Operating Officer; {chief_marketing_officer}, Chief Marketing Officer; and {chief_compliance_officer}, Chief Compliance Officer.

    Before we begin, let me remind you that some of the statements we will be making today are forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties. Please refer to our SEC filings for a discussion of these factors.

    I will now turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} delivered record results in the {quarter}, exceeding all previous benchmarks and solidifying our position as a leader in the financial services industry.

    Our key priorities for this year remain focused on:
    1.  Sustaining strong revenue growth
    2.  Driving operational efficiency
    3.  Managing risk effectively
    4.  Investing in technology and innovation
    5.  Enhancing customer experience
    6.  Strengthening our brand reputation
    7.  Promoting a diverse and inclusive culture
    8.  Delivering superior returns to our shareholders.

    Now, I'd like to provide some highlights on:
    {aspect_1_details}
    {aspect_2_details}
    {aspect_3_details}
    {aspect_4_details}
    {aspect_5_details}
    {aspect_6_details}
    {aspect_7_details}
    {aspect_8_details}

    I will now turn the call over to {cfo_name} to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}, and good morning. {company_name} reported net income of {net_income} for the {quarter}, or {earnings_per_share} per share. Our results reflect strong revenue growth, disciplined expense management, and a healthy credit environment.

    Net interest income increased {nii_increase}, driven by growth in our loan portfolio and improved net interest margin. Non-interest income was {non_interest_income_performance}, reflecting strong performance in our investment banking and wealth management businesses. We are generating strong returns on equity and are committed to delivering value to our shareholders.

    {cro_name}:
    Thank you, {cfo_name}. From a risk management perspective, we are closely monitoring {risk_area_1}, {risk_area_2}, {risk_area_3}, and {risk_area_4}. We are implementing enhanced controls and monitoring to mitigate these risks and maintain a strong risk profile.

    {cco_name}:
    Good morning. Our credit quality remains excellent with {credit_quality_metric_1} at {credit_quality_value_1} and {credit_quality_metric_2} at {credit_quality_value_2}. We are actively managing our loan portfolio and remain confident in our ability to navigate the current economic environment.

    {cto_name}:
    Thank you. I'd like to provide an update on our technology initiatives. We are leveraging technology to enhance customer experience, improve efficiency, and drive innovation. Our investments in {technology_area_1} and {technology_area_2} are yielding significant results.

    {coo_name}:
    Good morning. We are focused on operational excellence and driving efficiency across the organization. Key initiatives include streamlining our processes, optimizing our infrastructure, and leveraging data analytics to improve decision-making.

    {chief_marketing_officer}:
    Thank you. From a marketing perspective, we are focused on strengthening our brand reputation and enhancing customer engagement. Our recent marketing campaigns have been highly successful in driving customer acquisition and retention.

    {chief_compliance_officer}:
    Good morning. We are committed to maintaining the highest standards of compliance and ethical conduct. We are continuously strengthening our compliance programs and working closely with regulators to ensure we are meeting all applicable requirements.

    Operator, we are now ready to open the line for questions.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}. Please go ahead.

    {analyst_1_name}:
    Good morning. Could you please provide more detail on {analyst_1_question}?

    {ceo_name}:
    [Response to analyst_1_question]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_company}. Please go ahead.

    {analyst_2_name}:
    What is your outlook for {analyst_2_question}?

    {cfo_name}:
    [Response to analyst_2_question]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_company}. Please go ahead.

    {analyst_3_name}:
    Can you discuss the impact of {analyst_3_question}?

    {cro_name}:
    [Response to analyst_3_question]

    Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_company}. Please go ahead.

    {analyst_4_name}:
    What are your plans for {analyst_4_question}?

    {cto_name}:
    [Response to analyst_4_question]

    Operator:
    There are no further questions at this time. I'd like to turn the conference back over to {ceo_name} for any closing remarks.

    {ceo_name}:
    Thank you for your interest in {company_name}. We appreciate you joining us today. We look forward to speaking with you again next quarter.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """)
])