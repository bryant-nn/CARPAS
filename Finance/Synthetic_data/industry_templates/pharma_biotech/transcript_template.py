from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s financial results for the {quarter}. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and {chief_medical_officer_name}, Chief Medical Officer.

    Before we begin, I would like to remind you that today's call will contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    **{ceo_name}, CEO:**
    Thank you, {ir_name}. Good morning, everyone.  {company_name} delivered a strong performance in the {quarter}, driven by [mention key drivers].  We continue to make significant progress on our key strategic priorities.

    Today, I will provide an overview of our performance and strategic initiatives, focusing on:
    *   {aspect_1_topic}: {aspect_1_details}
    *   {aspect_2_topic}: {aspect_2_details}
    *   {aspect_3_topic}: {aspect_3_details}
    *   {aspect_4_topic}: {aspect_4_details}

    We are particularly excited about {new_product} and its potential {impact_of_product}.

    Now, I will turn the call over to {cfo_name}, our CFO, to provide a more detailed review of our financial results.

    **{cfo_name}, CFO:**
    Thank you, {ceo_name}.  As {ceo_name} mentioned, we had a solid {quarter}. Revenue for the quarter was ${revenue} million, an increase of {revenue_growth}% compared to the same period last year. This increase was primarily driven by [explain increase].

    Our GAAP net income for the quarter was ${net_income} million, or ${earnings_per_share} per share. Non-GAAP net income was ${non_gaap_net_income} million, or ${non_gaap_earnings_per_share} per share.

    Our operating expenses were ${operating_expenses} million, reflecting [explain operating expenses]. We continue to invest in R&D to support our pipeline.  Our cash position remains strong at ${cash_position} million.

    For the full year, we are updating our guidance to [provide guidance].

    Now, I'll hand the call back to {ceo_name}.

    **{ceo_name}, CEO:**
    Thank you, {cfo_name}. We will now open the call for questions.

    **Operator:**
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name}, {analyst_1_firm}:**
    [Analyst Question 1]

    **{ceo_name}, CEO:**
    [Answer to Analyst Question 1]

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name}, {analyst_2_firm}:**
    [Analyst Question 2]

    **{cfo_name}, CFO:**
    [Answer to Analyst Question 2]

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, CEO:**
    Thank you for your questions.  In closing, I want to thank our employees for their hard work and dedication. We are confident in our ability to continue to execute on our strategic priorities and deliver long-term value for our shareholders.

    **{ir_name}, {ir_title}:**
    Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. Have a great day.

    **Operator:**
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
    ("5", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s financial results for the {quarter}. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_medical_officer_name}, Chief Medical Officer; and {chief_scientific_officer_name}, Chief Scientific Officer.

    Before we begin, I would like to remind you that today's call will contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    **{ceo_name}, CEO:**
    Thank you, {ir_name}. Good morning, everyone. {company_name} delivered a strong performance in the {quarter}, driven by [mention key drivers]. We continue to make significant progress on our key strategic priorities.

    Today, I will provide an overview of our performance and strategic initiatives, focusing on:
    *   {aspect_1_topic}: {aspect_1_details}
    *   {aspect_2_topic}: {aspect_2_details}
    *   {aspect_3_topic}: {aspect_3_details}
    *   {aspect_4_topic}: {aspect_4_details}
    *   {aspect_5_topic}: {aspect_5_details}

    We are particularly excited about {new_product} and its potential {impact_of_product}.

    Now, I will turn the call over to {cfo_name}, our CFO, to provide a more detailed review of our financial results.

    **{cfo_name}, CFO:**
    Thank you, {ceo_name}. As {ceo_name} mentioned, we had a solid {quarter}. Revenue for the quarter was ${revenue} million, an increase of {revenue_growth}% compared to the same period last year. This increase was primarily driven by [explain increase].

    Our GAAP net income for the quarter was ${net_income} million, or ${earnings_per_share} per share. Non-GAAP net income was ${non_gaap_net_income} million, or ${non_gaap_earnings_per_share} per share.

    Our operating expenses were ${operating_expenses} million, reflecting [explain operating expenses]. We continue to invest in R&D to support our pipeline. Our cash position remains strong at ${cash_position} million.

    For the full year, we are updating our guidance to [provide guidance].

    Now, I'll turn the call over to {chief_medical_officer_name}, our Chief Medical Officer, to discuss our clinical programs.

    **{chief_medical_officer_name}, Chief Medical Officer:**
    Thank you, {cfo_name}. We are very pleased with the progress of our clinical trials. Specifically, [discuss clinical trial updates].  We expect to [mention upcoming milestones].

    Now, I'll hand the call back to {ceo_name}.

    **{ceo_name}, CEO:**
    Thank you, {chief_medical_officer_name}. We will now open the call for questions.

    **Operator:**
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name}, {analyst_1_firm}:**
    [Analyst Question 1]

    **{ceo_name}, CEO:**
    [Answer to Analyst Question 1]

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name}, {analyst_2_firm}:**
    [Analyst Question 2]

    **{cfo_name}, CFO:**
    [Answer to Analyst Question 2]

    **Operator:**
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    **{analyst_3_name}, {analyst_3_firm}:**
    [Analyst Question 3]

    **{chief_medical_officer_name}, Chief Medical Officer:**
    [Answer to Analyst Question 3]

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, CEO:**
    Thank you for your questions. In closing, I want to thank our employees for their hard work and dedication. We are confident in our ability to continue to execute on our strategic priorities and deliver long-term value for our shareholders.

    **{ir_name}, {ir_title}:**
    Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. Have a great day.

    **Operator:**
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
    ("6", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s financial results for the {quarter}. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_medical_officer_name}, Chief Medical Officer; and {chief_scientific_officer_name}, Chief Scientific Officer; {head_of_commercial_name}, Head of Commercial.

    Before we begin, I would like to remind you that today's call will contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    **{ceo_name}, CEO:**
    Thank you, {ir_name}. Good morning, everyone. {company_name} delivered a strong performance in the {quarter}, driven by [mention key drivers]. We continue to make significant progress on our key strategic priorities.

    Today, I will provide an overview of our performance and strategic initiatives, focusing on:
    *   {aspect_1_topic}: {aspect_1_details}
    *   {aspect_2_topic}: {aspect_2_details}
    *   {aspect_3_topic}: {aspect_3_details}
    *   {aspect_4_topic}: {aspect_4_details}
    *   {aspect_5_topic}: {aspect_5_details}
    *   {aspect_6_topic}: {aspect_6_details}

    We are particularly excited about {new_product} and its potential {impact_of_product}.

    Now, I will turn the call over to {cfo_name}, our CFO, to provide a more detailed review of our financial results.

    **{cfo_name}, CFO:**
    Thank you, {ceo_name}. As {ceo_name} mentioned, we had a solid {quarter}. Revenue for the quarter was ${revenue} million, an increase of {revenue_growth}% compared to the same period last year. This increase was primarily driven by [explain increase].

    Our GAAP net income for the quarter was ${net_income} million, or ${earnings_per_share} per share. Non-GAAP net income was ${non_gaap_net_income} million, or ${non_gaap_earnings_per_share} per share.

    Our operating expenses were ${operating_expenses} million, reflecting [explain operating expenses]. We continue to invest in R&D to support our pipeline. Our cash position remains strong at ${cash_position} million.

    For the full year, we are updating our guidance to [provide guidance].

    Now, I'll turn the call over to {chief_medical_officer_name}, our Chief Medical Officer, to discuss our clinical programs.

    **{chief_medical_officer_name}, Chief Medical Officer:**
    Thank you, {cfo_name}. We are very pleased with the progress of our clinical trials. Specifically, [discuss clinical trial updates]. We expect to [mention upcoming milestones].

    Next, {chief_scientific_officer_name} will provide an update on our research pipeline.

    **{chief_scientific_officer_name}, Chief Scientific Officer:**
    Thank you, {chief_medical_officer_name}. We are making significant strides in our early-stage research. [Discuss research pipeline updates and advancements].

    Now I'll turn the call over to {head_of_commercial_name}, Head of Commercial, to discuss product sales and marketing.

    **{head_of_commercial_name}, Head of Commercial:**
    Thank you, {chief_scientific_officer_name}. Our sales performance this quarter was [state sales performance]. We are seeing strong uptake in [mention specific products and market segments]. Our marketing campaigns are proving effective in [explain marketing effectiveness].

    Now, I'll hand the call back to {ceo_name}.

    **{ceo_name}, CEO:**
    Thank you, {head_of_commercial_name}. We will now open the call for questions.

    **Operator:**
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name}, {analyst_1_firm}:**
    [Analyst Question 1]

    **{ceo_name}, CEO:**
    [Answer to Analyst Question 1]

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name}, {analyst_2_firm}:**
    [Analyst Question 2]

    **{cfo_name}, CFO:**
    [Answer to Analyst Question 2]

    **Operator:**
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    **{analyst_3_name}, {analyst_3_firm}:**
    [Analyst Question 3]

    **{chief_medical_officer_name}, Chief Medical Officer:**
    [Answer to Analyst Question 3]

    **Operator:**
    Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

    **{analyst_4_name}, {analyst_4_firm}:**
    [Analyst Question 4]

    **{head_of_commercial_name}, Head of Commercial:**
    [Answer to Analyst Question 4]

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, CEO:**
    Thank you for your questions. In closing, I want to thank our employees for their hard work and dedication. We are confident in our ability to continue to execute on our strategic priorities and deliver long-term value for our shareholders.

    **{ir_name}, {ir_title}:**
    Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. Have a great day.

    **Operator:**
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
    ("7", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s financial results for the {quarter}. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_medical_officer_name}, Chief Medical Officer; {chief_scientific_officer_name}, Chief Scientific Officer; {head_of_commercial_name}, Head of Commercial; and {head_of_manufacturing_name}, Head of Manufacturing.

    Before we begin, I would like to remind you that today's call will contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    **{ceo_name}, CEO:**
    Thank you, {ir_name}. Good morning, everyone. {company_name} delivered a strong performance in the {quarter}, driven by [mention key drivers]. We continue to make significant progress on our key strategic priorities.

    Today, I will provide an overview of our performance and strategic initiatives, focusing on:
    *   {aspect_1_topic}: {aspect_1_details}
    *   {aspect_2_topic}: {aspect_2_details}
    *   {aspect_3_topic}: {aspect_3_details}
    *   {aspect_4_topic}: {aspect_4_details}
    *   {aspect_5_topic}: {aspect_5_details}
    *   {aspect_6_topic}: {aspect_6_details}
    *   {aspect_7_topic}: {aspect_7_details}

    We are particularly excited about {new_product} and its potential {impact_of_product}.

    Now, I will turn the call over to {cfo_name}, our CFO, to provide a more detailed review of our financial results.

    **{cfo_name}, CFO:**
    Thank you, {ceo_name}. As {ceo_name} mentioned, we had a solid {quarter}. Revenue for the quarter was ${revenue} million, an increase of {revenue_growth}% compared to the same period last year. This increase was primarily driven by [explain increase].

    Our GAAP net income for the quarter was ${net_income} million, or ${earnings_per_share} per share. Non-GAAP net income was ${non_gaap_net_income} million, or ${non_gaap_earnings_per_share} per share.

    Our operating expenses were ${operating_expenses} million, reflecting [explain operating expenses]. We continue to invest in R&D to support our pipeline. Our cash position remains strong at ${cash_position} million.

    For the full year, we are updating our guidance to [provide guidance].

    Now, I'll turn the call over to {chief_medical_officer_name}, our Chief Medical Officer, to discuss our clinical programs.

    **{chief_medical_officer_name}, Chief Medical Officer:**
    Thank you, {cfo_name}. We are very pleased with the progress of our clinical trials. Specifically, [discuss clinical trial updates]. We expect to [mention upcoming milestones].

    Next, {chief_scientific_officer_name} will provide an update on our research pipeline.

    **{chief_scientific_officer_name}, Chief Scientific Officer:**
    Thank you, {chief_medical_officer_name}. We are making significant strides in our early-stage research. [Discuss research pipeline updates and advancements].

    Now I'll turn the call over to {head_of_commercial_name}, Head of Commercial, to discuss product sales and marketing.

    **{head_of_commercial_name}, Head of Commercial:**
    Thank you, {chief_scientific_officer_name}. Our sales performance this quarter was [state sales performance]. We are seeing strong uptake in [mention specific products and market segments]. Our marketing campaigns are proving effective in [explain marketing effectiveness].

    Finally, {head_of_manufacturing_name} will discuss our manufacturing operations.

    **{head_of_manufacturing_name}, Head of Manufacturing:**
    Thank you, {head_of_commercial_name}. Our manufacturing operations are running smoothly. [Discuss manufacturing capacity, efficiency, and any supply chain updates]. We are focused on [mention key manufacturing priorities].

    Now, I'll hand the call back to {ceo_name}.

    **{ceo_name}, CEO:**
    Thank you, {head_of_manufacturing_name}. We will now open the call for questions.

    **Operator:**
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name}, {analyst_1_firm}:**
    [Analyst Question 1]

    **{ceo_name}, CEO:**
    [Answer to Analyst Question 1]

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name}, {analyst_2_firm}:**
    [Analyst Question 2]

    **{cfo_name}, CFO:**
    [Answer to Analyst Question 2]

    **Operator:**
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    **{analyst_3_name}, {analyst_3_firm}:**
    [Analyst Question 3]

    **{chief_medical_officer_name}, Chief Medical Officer:**
    [Answer to Analyst Question 3]

    **Operator:**
    Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

    **{analyst_4_name}, {analyst_4_firm}:**
    [Analyst Question 4]

    **{head_of_commercial_name}, Head of Commercial:**
    [Answer to Analyst Question 4]

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, CEO:**
    Thank you for your questions. In closing, I want to thank our employees for their hard work and dedication. We are confident in our ability to continue to execute on our strategic priorities and deliver long-term value for our shareholders.

    **{ir_name}, {ir_title}:**
    Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. Have a great day.

    **Operator:**
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
    ("8", """
    **{company_name} - {quarter} Earnings Call Transcript**

    **Operator:**
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    **{ir_name}, {ir_title}:**
    Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s financial results for the {quarter}. Joining me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_medical_officer_name}, Chief Medical Officer; {chief_scientific_officer_name}, Chief Scientific Officer; {head_of_commercial_name}, Head of Commercial; {head_of_manufacturing_name}, Head of Manufacturing; and {head_of_regulatory_affairs_name}, Head of Regulatory Affairs.

    Before we begin, I would like to remind you that today's call will contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'd like to turn the call over to {ceo_name}, CEO of {company_name}.

    **{ceo_name}, CEO:**
    Thank you, {ir_name}. Good morning, everyone. {company_name} delivered a strong performance in the {quarter}, driven by [mention key drivers]. We continue to make significant progress on our key strategic priorities.

    Today, I will provide an overview of our performance and strategic initiatives, focusing on:
    *   {aspect_1_topic}: {aspect_1_details}
    *   {aspect_2_topic}: {aspect_2_details}
    *   {aspect_3_topic}: {aspect_3_details}
    *   {aspect_4_topic}: {aspect_4_details}
    *   {aspect_5_topic}: {aspect_5_details}
    *   {aspect_6_topic}: {aspect_6_details}
    *   {aspect_7_topic}: {aspect_7_details}
    *   {aspect_8_topic}: {aspect_8_details}

    We are particularly excited about {new_product} and its potential {impact_of_product}.

    Now, I will turn the call over to {cfo_name}, our CFO, to provide a more detailed review of our financial results.

    **{cfo_name}, CFO:**
    Thank you, {ceo_name}. As {ceo_name} mentioned, we had a solid {quarter}. Revenue for the quarter was ${revenue} million, an increase of {revenue_growth}% compared to the same period last year. This increase was primarily driven by [explain increase].

    Our GAAP net income for the quarter was ${net_income} million, or ${earnings_per_share} per share. Non-GAAP net income was ${non_gaap_net_income} million, or ${non_gaap_earnings_per_share} per share.

    Our operating expenses were ${operating_expenses} million, reflecting [explain operating expenses]. We continue to invest in R&D to support our pipeline. Our cash position remains strong at ${cash_position} million.

    For the full year, we are updating our guidance to [provide guidance].

    Now, I'll turn the call over to {chief_medical_officer_name}, our Chief Medical Officer, to discuss our clinical programs.

    **{chief_medical_officer_name}, Chief Medical Officer:**
    Thank you, {cfo_name}. We are very pleased with the progress of our clinical trials. Specifically, [discuss clinical trial updates]. We expect to [mention upcoming milestones].

    Next, {chief_scientific_officer_name} will provide an update on our research pipeline.

    **{chief_scientific_officer_name}, Chief Scientific Officer:**
    Thank you, {chief_medical_officer_name}. We are making significant strides in our early-stage research. [Discuss research pipeline updates and advancements].

    Now I'll turn the call over to {head_of_commercial_name}, Head of Commercial, to discuss product sales and marketing.

    **{head_of_commercial_name}, Head of Commercial:**
    Thank you, {chief_scientific_officer_name}. Our sales performance this quarter was [state sales performance]. We are seeing strong uptake in [mention specific products and market segments]. Our marketing campaigns are proving effective in [explain marketing effectiveness].

    Next, {head_of_manufacturing_name} will discuss our manufacturing operations.

    **{head_of_manufacturing_name}, Head of Manufacturing:**
    Thank you, {head_of_commercial_name}. Our manufacturing operations are running smoothly. [Discuss manufacturing capacity, efficiency, and any supply chain updates]. We are focused on [mention key manufacturing priorities].

    Finally, {head_of_regulatory_affairs_name} will provide an update on regulatory submissions and approvals.

    **{head_of_regulatory_affairs_name}, Head of Regulatory Affairs:**
    Thank you, {head_of_manufacturing_name}. We continue to work closely with regulatory agencies. [Discuss regulatory submissions, approvals, and ongoing interactions with regulatory bodies].

    Now, I'll hand the call back to {ceo_name}.

    **{ceo_name}, CEO:**
    Thank you, {head_of_regulatory_affairs_name}. We will now open the call for questions.

    **Operator:**
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    **{analyst_1_name}, {analyst_1_firm}:**
    [Analyst Question 1]

    **{ceo_name}, CEO:**
    [Answer to Analyst Question 1]

    **Operator:**
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    **{analyst_2_name}, {analyst_2_firm}:**
    [Analyst Question 2]

    **{cfo_name}, CFO:**
    [Answer to Analyst Question 2]

    **Operator:**
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    **{analyst_3_name}, {analyst_3_firm}:**
    [Analyst Question 3]

    **{chief_medical_officer_name}, Chief Medical Officer:**
    [Answer to Analyst Question 3]

    **Operator:**
    Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

    **{analyst_4_name}, {analyst_4_firm}:**
    [Analyst Question 4]

    **{head_of_commercial_name}, Head of Commercial:**
    [Answer to Analyst Question 4]

    **Operator:**
    [Optional: More Analyst Questions]

    **{ceo_name}, CEO:**
    Thank you for your questions. In closing, I want to thank our employees for their hard work and dedication. We are confident in our ability to continue to execute on our strategic priorities and deliver long-term value for our shareholders.

    **{ir_name}, {ir_title}:**
    Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. Have a great day.

    **Operator:**
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
])