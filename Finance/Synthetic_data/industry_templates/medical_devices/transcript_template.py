from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. To ask a question, you may press star then one on your telephone. Please note, this call is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today. Before we begin, I'd like to remind you that this call will contain forward-looking statements, including expectations regarding our future performance, business outlook, and financial results. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Joining me on today's call are {ceo_name}, CEO; {cfo_name}, CFO; {cto_name}, Chief Technology Officer.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} delivered solid results this quarter, driven by strong execution and continued demand for our innovative medical device solutions.

    Today, I will cover four key aspects of our performance:
    1. {aspect_1}: {aspect_1_details}
    2. {aspect_2}: {aspect_2_details}
    3. {aspect_3}: {aspect_3_details}
    4. {aspect_4}: {aspect_4_details}

    {cfo_name} will then provide a more detailed review of our financials. After that, we'll open the call for your questions.

    Now, let's get started with {aspect_1}.

    [CEO provides details on aspect 1]

    Now, let's talk about {aspect_2}.

    [CEO provides details on aspect 2]

    Moving on to {aspect_3}.

    [CEO provides details on aspect 3]

    Finally, {aspect_4}.

    [CEO provides details on aspect 4]

    I will now turn the call over to {cfo_name} for a review of our financial results.

    {cfo_name}:
    Thank you, {ceo_name}. As {ceo_name} mentioned, we delivered a strong financial performance this quarter.

    [CFO provides details on revenue, expenses, profitability, and guidance]

    Now, I'll turn the call back to {ceo_name} for Q&A.

    {ceo_name}:
    Thank you, {cfo_name}. Operator, we are now ready to take questions.

    Operator:
    Thank you. [Instructions for asking questions]. Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 1:
    [Analyst asks a question]

    {ceo_name}:
    [CEO answers the question]

    Analyst 2:
    [Analyst asks a question]

    {cfo_name}:
    [CFO answers the question]

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 3:
    [Analyst asks a question]

    {cto_name}:
    [CTO answers the question]

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 4:
    [Analyst asks a question]

    {ceo_name}:
    [CEO answers the question]

    {ceo_name}:
    Thank you for your questions. Before we conclude, I want to reiterate our confidence in the long-term growth potential of {company_name}. We are committed to delivering innovative medical device solutions that improve patient outcomes and create value for our shareholders.

    Thank you for joining us today.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("5", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. To ask a question, you may press star then one on your telephone. Please note, this call is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today. Before we begin, I'd like to remind you that this call will contain forward-looking statements, including expectations regarding our future performance, business outlook, and financial results. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Joining me on today's call are {ceo_name}, CEO; {cfo_name}, CFO; {cto_name}, Chief Technology Officer; and {cco_name}, Chief Commercial Officer.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} delivered strong results this quarter, driven by increasing adoption of our innovative medical devices and strategic partnerships.

    Today, I will cover five key aspects of our performance:
    1. {aspect_1}: {aspect_1_details}
    2. {aspect_2}: {aspect_2_details}
    3. {aspect_3}: {aspect_3_details}
    4. {aspect_4}: {aspect_4_details}
    5. {aspect_5}: {aspect_5_details}

    {cfo_name} will then provide a more detailed review of our financials. After that, we'll open the call for your questions.

    Now, let's get started with {aspect_1}.

    [CEO provides details on aspect 1]

    Now, let's talk about {aspect_2}.

    [CEO provides details on aspect 2]

    Moving on to {aspect_3}.

    [CEO provides details on aspect 3]

    Next, {aspect_4}.

    [CEO provides details on aspect 4]

    Finally, {aspect_5}.

    [CEO provides details on aspect 5]

    I will now turn the call over to {cfo_name} for a review of our financial results.

    {cfo_name}:
    Thank you, {ceo_name}. As {ceo_name} mentioned, we delivered a strong financial performance this quarter.

    [CFO provides details on revenue, expenses, profitability, and guidance]

    Now, I'll turn the call over to {cto_name} for an update on our product pipeline.

    {cto_name}:
    Thank you, {cfo_name}. I'm excited to share some updates on our innovative pipeline. We recently received FDA clearance for {new_product}, a groundbreaking device that promises to {impact_of_product}.

    [CTO provides details on product pipeline]

    Now, back to {ceo_name} for Q&A.

    {ceo_name}:
    Thank you, {cto_name}. Operator, we are now ready to take questions.

    Operator:
    Thank you. [Instructions for asking questions]. Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 1:
    [Analyst asks a question]

    {ceo_name}:
    [CEO answers the question]

    Analyst 2:
    [Analyst asks a question]

    {cfo_name}:
    [CFO answers the question]

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 3:
    [Analyst asks a question]

    {cco_name}:
    [CCO answers the question]

    {ceo_name}:
    Thank you for that insight, {cco_name}.

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 4:
    [Analyst asks a question]

    {cto_name}:
    [CTO answers the question]

    {ceo_name}:
    Thank you for your questions. Before we conclude, I want to thank our employees, customers, and partners for their continued support. We are confident in our ability to continue delivering strong results and creating value for our shareholders.

    Thank you for joining us today.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("6", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. To ask a question, you may press star then one on your telephone. Please note, this call is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today. Before we begin, I'd like to remind you that this call will contain forward-looking statements, including expectations regarding our future performance, business outlook, and financial results. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Joining me on today's call are {ceo_name}, CEO; {cfo_name}, CFO; {cto_name}, Chief Technology Officer; and {cco_name}, Chief Commercial Officer.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} had a productive {quarter}, marked by significant advancements in our product portfolio and expansion into new markets.

    Today, I will cover six key aspects of our performance:
    1. {aspect_1}: {aspect_1_details}
    2. {aspect_2}: {aspect_2_details}
    3. {aspect_3}: {aspect_3_details}
    4. {aspect_4}: {aspect_4_details}
    5. {aspect_5}: {aspect_5_details}
    6. {aspect_6}: {aspect_6_details}

    {cfo_name} will then provide a more detailed review of our financials. {cto_name} will follow with updates on our R&D initiatives, and then we'll open the call for your questions.

    Now, let's get started with {aspect_1}.

    [CEO provides details on aspect 1]

    Now, let's talk about {aspect_2}.

    [CEO provides details on aspect 2]

    Moving on to {aspect_3}.

    [CEO provides details on aspect 3]

    Next, {aspect_4}.

    [CEO provides details on aspect 4]

    Then, {aspect_5}.

    [CEO provides details on aspect 5]

    Finally, {aspect_6}.

    [CEO provides details on aspect 6]

    I will now turn the call over to {cfo_name} for a review of our financial results.

    {cfo_name}:
    Thank you, {ceo_name}. As {ceo_name} mentioned, we delivered a solid financial performance this quarter.

    [CFO provides details on revenue, expenses, profitability, and guidance]

    Now, I'll turn the call over to {cto_name} for an update on our product pipeline.

    {cto_name}:
    Thank you, {cfo_name}. We are making significant progress in our R&D efforts. Particularly excited about our ongoing clinical trials for {new_product}, which is showing promising results in {impact_of_product}.

    [CTO provides details on product pipeline and R&D]

    Now, back to {ceo_name} for Q&A.

    {ceo_name}:
    Thank you, {cto_name}. Operator, we are now ready to take questions.

    Operator:
    Thank you. [Instructions for asking questions]. Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 1:
    [Analyst asks a question]

    {ceo_name}:
    [CEO answers the question]

    Analyst 2:
    [Analyst asks a question]

    {cfo_name}:
    [CFO answers the question]

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 3:
    [Analyst asks a question]

    {cco_name}:
    [CCO answers the question]

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 4:
    [Analyst asks a question]

    {cto_name}:
    [CTO answers the question]

    {ceo_name}:
    Thank you for your questions. In closing, we are well-positioned to continue our growth trajectory and deliver long-term value.

    Thank you for joining us today.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("7", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. To ask a question, you may press star then one on your telephone. Please note, this call is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today. Before we begin, I'd like to remind you that this call will contain forward-looking statements, including expectations regarding our future performance, business outlook, and financial results. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Joining me on today's call are {ceo_name}, CEO; {cfo_name}, CFO; {cto_name}, Chief Technology Officer; and {cco_name}, Chief Commercial Officer.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} demonstrated significant progress this {quarter}, driven by our focus on innovation, operational excellence, and strategic partnerships.

    Today, I will cover seven key aspects of our performance:
    1. {aspect_1}: {aspect_1_details}
    2. {aspect_2}: {aspect_2_details}
    3. {aspect_3}: {aspect_3_details}
    4. {aspect_4}: {aspect_4_details}
    5. {aspect_5}: {aspect_5_details}
    6. {aspect_6}: {aspect_6_details}
    7. {aspect_7}: {aspect_7_details}

    {cfo_name} will then provide a more detailed review of our financials. {cto_name} will offer insights into our technology roadmap, and {cco_name} will discuss our commercial strategies. Afterwards, we'll open the call for your questions.

    Now, let's get started with {aspect_1}.

    [CEO provides details on aspect 1]

    Now, let's talk about {aspect_2}.

    [CEO provides details on aspect 2]

    Moving on to {aspect_3}.

    [CEO provides details on aspect 3]

    Next, {aspect_4}.

    [CEO provides details on aspect 4]

    Then, {aspect_5}.

    [CEO provides details on aspect 5]

    Then, {aspect_6}.

    [CEO provides details on aspect 6]

    Finally, {aspect_7}.

    [CEO provides details on aspect 7]

    I will now turn the call over to {cfo_name} for a review of our financial results.

    {cfo_name}:
    Thank you, {ceo_name}. As {ceo_name} highlighted, we achieved strong financial results this quarter.

    [CFO provides details on revenue, expenses, profitability, and guidance]

    Now, I'll turn the call over to {cto_name} for an update on our product pipeline.

    {cto_name}:
    Thank you, {cfo_name}. We continue to invest in cutting-edge technologies. Our development of {new_product} is progressing well, and we anticipate it will revolutionize {impact_of_product}.

    [CTO provides details on product pipeline and R&D]

    Next, {cco_name} with some insights on our commercial strategy.

    {cco_name}:
    Thank you, {cto_name}. Our commercial team has been instrumental in driving adoption of our products. We are focused on expanding our market presence and enhancing customer engagement.

    [CCO provides details on commercial strategy]

    Now, back to {ceo_name} for Q&A.

    {ceo_name}:
    Thank you, {cco_name}. Operator, we are now ready to take questions.

    Operator:
    Thank you. [Instructions for asking questions]. Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 1:
    [Analyst asks a question]

    {ceo_name}:
    [CEO answers the question]

    Analyst 2:
    [Analyst asks a question]

    {cfo_name}:
    [CFO answers the question]

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 3:
    [Analyst asks a question]

    {cco_name}:
    [CCO answers the question]

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 4:
    [Analyst asks a question]

    {cto_name}:
    [CTO answers the question]

    {ceo_name}:
    Thank you for your insightful questions. We are dedicated to driving innovation and delivering value to our shareholders.

    Thank you for joining us today.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("8", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. To ask a question, you may press star then one on your telephone. Please note, this call is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good morning, everyone, and thank you for joining us today. Before we begin, I'd like to remind you that this call will contain forward-looking statements, including expectations regarding our future performance, business outlook, and financial results. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Joining me on today's call are {ceo_name}, CEO; {cfo_name}, CFO; {cto_name}, Chief Technology Officer; and {cco_name}, Chief Commercial Officer.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good morning, everyone. {company_name} achieved record results this {quarter}, reflecting the strength of our diversified portfolio and our commitment to innovation.

    Today, I will cover eight key aspects of our performance:
    1. {aspect_1}: {aspect_1_details}
    2. {aspect_2}: {aspect_2_details}
    3. {aspect_3}: {aspect_3_details}
    4. {aspect_4}: {aspect_4_details}
    5. {aspect_5}: {aspect_5_details}
    6. {aspect_6}: {aspect_6_details}
    7. {aspect_7}: {aspect_7_details}
    8. {aspect_8}: {aspect_8_details}

    {cfo_name} will then provide a more detailed review of our financials. {cto_name} will update us on our technology advancements, and {cco_name} will discuss our market strategies. We'll then conclude with a Q&A session.

    Now, let's get started with {aspect_1}.

    [CEO provides details on aspect 1]

    Now, let's talk about {aspect_2}.

    [CEO provides details on aspect 2]

    Moving on to {aspect_3}.

    [CEO provides details on aspect 3]

    Next, {aspect_4}.

    [CEO provides details on aspect 4]

    Then, {aspect_5}.

    [CEO provides details on aspect 5]

    Then, {aspect_6}.

    [CEO provides details on aspect 6]

    Then, {aspect_7}.

    [CEO provides details on aspect 7]

    Finally, {aspect_8}.

    [CEO provides details on aspect 8]

    I will now turn the call over to {cfo_name} for a review of our financial results.

    {cfo_name}:
    Thank you, {ceo_name}. As {ceo_name} mentioned, we delivered exceptional financial performance this quarter.

    [CFO provides details on revenue, expenses, profitability, and guidance]

    Now, I'll turn the call over to {cto_name} for an update on our product pipeline.

    {cto_name}:
    Thank you, {cfo_name}. We are excited about the progress we are making in our technology roadmap. Our latest innovation, {new_product}, is poised to transform {impact_of_product}. We expect FDA approval in Q{next_approval_quarter}.

    [CTO provides details on product pipeline and R&D]

    Next, {cco_name} with some insights on our commercial strategy.

    {cco_name}:
    Thank you, {cto_name}. We are focused on driving commercial excellence and expanding our global reach. Our strategic partnerships are enabling us to access new markets and customer segments.

    [CCO provides details on commercial strategy]

    Now, back to {ceo_name} for Q&A.

    {ceo_name}:
    Thank you, {cco_name}. Operator, we are now ready to take questions.

    Operator:
    Thank you. [Instructions for asking questions]. Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 1:
    [Analyst asks a question]

    {ceo_name}:
    [CEO answers the question]

    Analyst 2:
    [Analyst asks a question]

    {cfo_name}:
    [CFO answers the question]

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 3:
    [Analyst asks a question]

    {cco_name}:
    [CCO answers the question]

    Operator:
    Our next question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

    Analyst 4:
    [Analyst asks a question]

    {cto_name}:
    [CTO answers the question]

    {ceo_name}:
    Thank you for your thoughtful questions. We remain confident in our ability to execute our strategy and deliver sustainable growth.

    Thank you for joining us today.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """)
])