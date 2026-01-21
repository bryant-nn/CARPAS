from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and {coo_name}, Chief Operating Officer.

Before we begin, I would like to remind you that some of the statements we make today may be forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed discussion of these risks.

I will now turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. {company_name} delivered solid results in {quarter}, driven by strong operational performance and favorable commodity prices. We achieved {aspect_1_details}. I'm particularly pleased with our progress on {aspect_2_details}. We are focused on {aspect_3_details}. Finally, we are taking steps to {aspect_4_details}.

Now, I'll turn the call over to {cfo_name} to discuss our financial results in more detail.

{cfo_name}: Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Our revenue was {revenue_amount}, up {revenue_percentage}% year-over-year. Operating income was {operating_income_amount}, and net income was {net_income_amount}. We generated {cash_flow_amount} in free cash flow and returned {capital_returned_amount} to shareholders through dividends and share repurchases. Our balance sheet remains strong, with {debt_amount} in debt and {cash_amount} in cash.

I will now turn the call over to {coo_name} for an operational update.

{coo_name}: Thank you, {cfo_name}. On the operational front, we continue to execute our strategy effectively. Our production averaged {production_volume} barrels of oil equivalent per day. We successfully brought {new_well_name} online, which is expected to contribute significantly to our production growth in the coming quarters. We are also making progress on our cost reduction initiatives.

Operator, we are now ready to open the line for questions.

Operator: [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you provide more detail on {analyst_1_question}?

{ceo_name}: {ceo_answer_1}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Good morning. What are your expectations for {analyst_2_question}?

{cfo_name}: {cfo_answer_2}

Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}: Could you please provide more color on {analyst_3_question}?

{coo_name}: {coo_answer_3}

Operator: There are no further questions at this time. I would like to turn the conference back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you, Operator. In summary, we are pleased with our performance in {quarter}. We remain focused on executing our strategy and delivering value to our shareholders. Thank you for joining us today.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("5", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; and {vp_exploration_name}, VP of Exploration.

Before we begin, I would like to remind you that some of the statements we make today may be forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed discussion of these risks.

I will now turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. {company_name} delivered solid results in {quarter}, driven by strong operational performance and favorable commodity prices. We achieved {aspect_1_details}. I'm particularly pleased with our progress on {aspect_2_details}. We are focused on {aspect_3_details}. Further, we are working on {aspect_4_details}. Finally, we are taking steps to {aspect_5_details}.

Now, I'll turn the call over to {cfo_name} to discuss our financial results in more detail.

{cfo_name}: Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Our revenue was {revenue_amount}, up {revenue_percentage}% year-over-year. Operating income was {operating_income_amount}, and net income was {net_income_amount}. We generated {cash_flow_amount} in free cash flow and returned {capital_returned_amount} to shareholders through dividends and share repurchases. Our balance sheet remains strong, with {debt_amount} in debt and {cash_amount} in cash.

I will now turn the call over to {coo_name} for an operational update.

{coo_name}: Thank you, {cfo_name}. On the operational front, we continue to execute our strategy effectively. Our production averaged {production_volume} barrels of oil equivalent per day. We successfully brought {new_well_name} online, which is expected to contribute significantly to our production growth in the coming quarters. We are also making progress on our cost reduction initiatives.

Now I will turn it over to {vp_exploration_name} for an update on our exploration activities.

{vp_exploration_name}: Thank you, {coo_name}. We are excited about the potential of our exploration program. We recently completed a successful seismic survey in {exploration_area} and are planning to drill {number_of_wells} exploration wells in the next year. We believe these wells have the potential to add significant reserves to our portfolio.

Operator, we are now ready to open the line for questions.

Operator: [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you provide more detail on {analyst_1_question}?

{ceo_name}: {ceo_answer_1}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Good morning. What are your expectations for {analyst_2_question}?

{cfo_name}: {cfo_answer_2}

Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}: Could you please provide more color on {analyst_3_question}?

{coo_name}: {coo_answer_3}

Operator: Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

{analyst_4_name}: How will the results of the exploration program affect the company's future strategy?

{vp_exploration_name}: {vp_exploration_answer_4}

Operator: There are no further questions at this time. I would like to turn the conference back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you, Operator. In summary, we are pleased with our performance in {quarter}. We remain focused on executing our strategy and delivering value to our shareholders. Thank you for joining us today.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("6", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; {vp_exploration_name}, VP of Exploration; and {vp_marketing_name}, VP of Marketing.

Before we begin, I would like to remind you that some of the statements we make today may be forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed discussion of these risks.

I will now turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. {company_name} delivered solid results in {quarter}, driven by strong operational performance and favorable commodity prices. We achieved {aspect_1_details}. I'm particularly pleased with our progress on {aspect_2_details}. We are focused on {aspect_3_details}. Further, we are working on {aspect_4_details}. We continue to adjust to {aspect_5_details}. Finally, we are taking steps to {aspect_6_details}.

Now, I'll turn the call over to {cfo_name} to discuss our financial results in more detail.

{cfo_name}: Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Our revenue was {revenue_amount}, up {revenue_percentage}% year-over-year. Operating income was {operating_income_amount}, and net income was {net_income_amount}. We generated {cash_flow_amount} in free cash flow and returned {capital_returned_amount} to shareholders through dividends and share repurchases. Our balance sheet remains strong, with {debt_amount} in debt and {cash_amount} in cash.

I will now turn the call over to {coo_name} for an operational update.

{coo_name}: Thank you, {cfo_name}. On the operational front, we continue to execute our strategy effectively. Our production averaged {production_volume} barrels of oil equivalent per day. We successfully brought {new_well_name} online, which is expected to contribute significantly to our production growth in the coming quarters. We are also making progress on our cost reduction initiatives.

Now I will turn it over to {vp_exploration_name} for an update on our exploration activities.

{vp_exploration_name}: Thank you, {coo_name}. We are excited about the potential of our exploration program. We recently completed a successful seismic survey in {exploration_area} and are planning to drill {number_of_wells} exploration wells in the next year. We believe these wells have the potential to add significant reserves to our portfolio.

Finally, I'll turn it over to {vp_marketing_name} to discuss our marketing strategy.

{vp_marketing_name}: Thank you, {vp_exploration_name}. We are focused on optimizing our marketing strategy to maximize the value of our production. We are seeing strong demand for {new_product} in {market_area}, and we are working to expand our customer base and strengthen our relationships with existing customers. The {impact_of_product} is significant.

Operator, we are now ready to open the line for questions.

Operator: [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you provide more detail on {analyst_1_question}?

{ceo_name}: {ceo_answer_1}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Good morning. What are your expectations for {analyst_2_question}?

{cfo_name}: {cfo_answer_2}

Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}: Could you please provide more color on {analyst_3_question}?

{coo_name}: {coo_answer_3}

Operator: Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

{analyst_4_name}: How will the results of the exploration program affect the company's future strategy?

{vp_exploration_name}: {vp_exploration_answer_4}

Operator: Our next question comes from {analyst_5_name} with {analyst_5_firm}. Please go ahead.

{analyst_5_name}: What is the outlook for the new product in the coming years?

{vp_marketing_name}: {vp_marketing_answer_5}

Operator: There are no further questions at this time. I would like to turn the conference back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you, Operator. In summary, we are pleased with our performance in {quarter}. We remain focused on executing our strategy and delivering value to our shareholders. Thank you for joining us today.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("7", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; {vp_exploration_name}, VP of Exploration; {vp_marketing_name}, VP of Marketing; and {chief_sustainability_officer_name}, Chief Sustainability Officer.

Before we begin, I would like to remind you that some of the statements we make today may be forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed discussion of these risks.

I will now turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. {company_name} delivered solid results in {quarter}, driven by strong operational performance and favorable commodity prices. We achieved {aspect_1_details}. I'm particularly pleased with our progress on {aspect_2_details}. We are focused on {aspect_3_details}. Further, we are working on {aspect_4_details}. We continue to adjust to {aspect_5_details}. We are advancing {aspect_6_details}. Finally, we are taking steps to {aspect_7_details}.

Now, I'll turn the call over to {cfo_name} to discuss our financial results in more detail.

{cfo_name}: Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Our revenue was {revenue_amount}, up {revenue_percentage}% year-over-year. Operating income was {operating_income_amount}, and net income was {net_income_amount}. We generated {cash_flow_amount} in free cash flow and returned {capital_returned_amount} to shareholders through dividends and share repurchases. Our balance sheet remains strong, with {debt_amount} in debt and {cash_amount} in cash.

I will now turn the call over to {coo_name} for an operational update.

{coo_name}: Thank you, {cfo_name}. On the operational front, we continue to execute our strategy effectively. Our production averaged {production_volume} barrels of oil equivalent per day. We successfully brought {new_well_name} online, which is expected to contribute significantly to our production growth in the coming quarters. We are also making progress on our cost reduction initiatives.

Now I will turn it over to {vp_exploration_name} for an update on our exploration activities.

{vp_exploration_name}: Thank you, {coo_name}. We are excited about the potential of our exploration program. We recently completed a successful seismic survey in {exploration_area} and are planning to drill {number_of_wells} exploration wells in the next year. We believe these wells have the potential to add significant reserves to our portfolio.

Finally, I'll turn it over to {vp_marketing_name} to discuss our marketing strategy.

{vp_marketing_name}: Thank you, {vp_exploration_name}. We are focused on optimizing our marketing strategy to maximize the value of our production. We are seeing strong demand for {new_product} in {market_area}, and we are working to expand our customer base and strengthen our relationships with existing customers. The {impact_of_product} is significant.

I will now turn it over to {chief_sustainability_officer_name} to discuss our sustainability efforts.

{chief_sustainability_officer_name}: Thank you, {vp_marketing_name}. We are committed to reducing our environmental footprint and operating in a sustainable manner. We have made significant progress on reducing our greenhouse gas emissions and are investing in renewable energy projects. We are also working to improve our water management practices and protect biodiversity.

Operator, we are now ready to open the line for questions.

Operator: [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you provide more detail on {analyst_1_question}?

{ceo_name}: {ceo_answer_1}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Good morning. What are your expectations for {analyst_2_question}?

{cfo_name}: {cfo_answer_2}

Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}: Could you please provide more color on {analyst_3_question}?

{coo_name}: {coo_answer_3}

Operator: Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

{analyst_4_name}: How will the results of the exploration program affect the company's future strategy?

{vp_exploration_name}: {vp_exploration_answer_4}

Operator: Our next question comes from {analyst_5_name} with {analyst_5_firm}. Please go ahead.

{analyst_5_name}: What is the outlook for the new product in the coming years?

{vp_marketing_name}: {vp_marketing_answer_5}

Operator: Our next question comes from {analyst_6_name} with {analyst_6_firm}. Please go ahead.

{analyst_6_name}: Could you elaborate on your sustainability targets?

{chief_sustainability_officer_name}: {chief_sustainability_officer_answer_6}

Operator: There are no further questions at this time. I would like to turn the conference back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you, Operator. In summary, we are pleased with our performance in {quarter}. We remain focused on executing our strategy and delivering value to our shareholders. Thank you for joining us today.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("8", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; {vp_exploration_name}, VP of Exploration; {vp_marketing_name}, VP of Marketing; {chief_sustainability_officer_name}, Chief Sustainability Officer; and {chief_technology_officer_name}, Chief Technology Officer.

Before we begin, I would like to remind you that some of the statements we make today may be forward-looking. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed discussion of these risks.

I will now turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. {company_name} delivered solid results in {quarter}, driven by strong operational performance and favorable commodity prices. We achieved {aspect_1_details}. I'm particularly pleased with our progress on {aspect_2_details}. We are focused on {aspect_3_details}. Further, we are working on {aspect_4_details}. We continue to adjust to {aspect_5_details}. We are advancing {aspect_6_details}. We are evaluating {aspect_7_details}. Finally, we are taking steps to {aspect_8_details}.

Now, I'll turn the call over to {cfo_name} to discuss our financial results in more detail.

{cfo_name}: Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Our revenue was {revenue_amount}, up {revenue_percentage}% year-over-year. Operating income was {operating_income_amount}, and net income was {net_income_amount}. We generated {cash_flow_amount} in free cash flow and returned {capital_returned_amount} to shareholders through dividends and share repurchases. Our balance sheet remains strong, with {debt_amount} in debt and {cash_amount} in cash.

I will now turn the call over to {coo_name} for an operational update.

{coo_name}: Thank you, {cfo_name}. On the operational front, we continue to execute our strategy effectively. Our production averaged {production_volume} barrels of oil equivalent per day. We successfully brought {new_well_name} online, which is expected to contribute significantly to our production growth in the coming quarters. We are also making progress on our cost reduction initiatives.

Now I will turn it over to {vp_exploration_name} for an update on our exploration activities.

{vp_exploration_name}: Thank you, {coo_name}. We are excited about the potential of our exploration program. We recently completed a successful seismic survey in {exploration_area} and are planning to drill {number_of_wells} exploration wells in the next year. We believe these wells have the potential to add significant reserves to our portfolio.

Finally, I'll turn it over to {vp_marketing_name} to discuss our marketing strategy.

{vp_marketing_name}: Thank you, {vp_exploration_name}. We are focused on optimizing our marketing strategy to maximize the value of our production. We are seeing strong demand for {new_product} in {market_area}, and we are working to expand our customer base and strengthen our relationships with existing customers. The {impact_of_product} is significant.

I will now turn it over to {chief_sustainability_officer_name} to discuss our sustainability efforts.

{chief_sustainability_officer_name}: Thank you, {vp_marketing_name}. We are committed to reducing our environmental footprint and operating in a sustainable manner. We have made significant progress on reducing our greenhouse gas emissions and are investing in renewable energy projects. We are also working to improve our water management practices and protect biodiversity.

I will now turn the call over to {chief_technology_officer_name} to discuss our technology initiatives.

{chief_technology_officer_name}: Thank you, {chief_sustainability_officer_name}. We are leveraging technology to improve our operational efficiency, reduce costs, and enhance safety. We are investing in automation, data analytics, and artificial intelligence to optimize our operations. We are also exploring new technologies such as carbon capture and storage.

Operator, we are now ready to open the line for questions.

Operator: [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you provide more detail on {analyst_1_question}?

{ceo_name}: {ceo_answer_1}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Good morning. What are your expectations for {analyst_2_question}?

{cfo_name}: {cfo_answer_2}

Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}: Could you please provide more color on {analyst_3_question}?

{coo_name}: {coo_answer_3}

Operator: Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

{analyst_4_name}: How will the results of the exploration program affect the company's future strategy?

{vp_exploration_name}: {vp_exploration_answer_4}

Operator: Our next question comes from {analyst_5_name} with {analyst_5_firm}. Please go ahead.

{analyst_5_name}: What is the outlook for the new product in the coming years?

{vp_marketing_name}: {vp_marketing_answer_5}

Operator: Our next question comes from {analyst_6_name} with {analyst_6_firm}. Please go ahead.

{analyst_6_name}: Could you elaborate on your sustainability targets?

{chief_sustainability_officer_name}: {chief_sustainability_officer_answer_6}

Operator: Our next question comes from {analyst_7_name} with {analyst_7_firm}. Please go ahead.

{analyst_7_name}: What are the key technology initiatives you are focused on?

{chief_technology_officer_name}: {chief_technology_officer_answer_7}

Operator: There are no further questions at this time. I would like to turn the conference back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you, Operator. In summary, we are pleased with our performance in {quarter}. We remain focused on executing our strategy and delivering value to our shareholders. Thank you for joining us today.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """)
])