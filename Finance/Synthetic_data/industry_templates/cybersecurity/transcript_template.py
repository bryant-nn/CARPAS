from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, operator. Good afternoon, everyone, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. With me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and {cto_name}, Chief Technology Officer.

    Before we begin, I would like to remind you that today's call may contain forward-looking statements. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good afternoon, everyone. Thank you for joining us. {company_name} had a strong {quarter}, driven by continued demand for our cybersecurity solutions and our commitment to innovation. We are seeing increased adoption of our {new_product} platform, which is helping organizations better protect themselves against increasingly sophisticated cyber threats.

    Our focus remains on four key areas: {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, and {aspect_4_details}.

    Now, I'll turn the call over to {cfo_name} to discuss our financial results in more detail.

    {cfo_name}: Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong {quarter}. Revenue for the quarter was {revenue}, representing a {revenue_growth}% increase year-over-year. This growth was driven by strong performance across all of our product lines. Our gross margin was {gross_margin}%, and our operating expenses were {operating_expenses}. Net income for the quarter was {net_income}, or {earnings_per_share} per share.

    We are confident that we are well-positioned to continue to drive growth and profitability in the years to come.

    Operator, we are now ready to open the call for questions.

    Operator: [Instructions for Q&A session]. First question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}: [Analyst 1 Question]

    {ceo_name}: [Answer to Analyst 1]

    Operator: Next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}: [Analyst 2 Question]

    {cfo_name}: [Answer to Analyst 2]

    Operator: Next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}: [Analyst 3 Question]

    {cto_name}: [Answer to Analyst 3]

    Operator: Next question comes from {analyst_4_name} with {analyst_4_firm}.

    {analyst_4_name}: [Analyst 4 Question]

    {ceo_name}: [Answer to Analyst 4]

    {ceo_name}: Thank you, everyone, for your questions. In closing, I want to thank our employees, customers, and partners for their continued support. We are excited about the opportunities ahead and are confident that we can continue to deliver strong results.

    {ir_name}: Thank you for joining us today. This concludes our call. You may now disconnect.
    """),
    ("5", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, operator. Good afternoon, everyone, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. With me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cto_name}, Chief Technology Officer, and {cso_name}, Chief Security Officer.

    Before we begin, I would like to remind you that today's call may contain forward-looking statements. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good afternoon, everyone. Thank you for joining us. {company_name} had an exceptional {quarter}, exceeding expectations across all key metrics. We are seeing significant traction with our cloud-native security platform and are benefiting from the increased focus on cybersecurity across all industries. The {impact_of_product} of our new AI-powered threat detection is evident in the reduced incident response times reported by our customers.

    Our strategy is centered around five core pillars: {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, and {aspect_5_details}.

    Now, I'll turn the call over to {cfo_name} to discuss our financial results in more detail.

    {cfo_name}: Thank you, {ceo_name}. As {ceo_name} highlighted, we had a remarkable {quarter}. Revenue reached {revenue}, reflecting a {revenue_growth}% year-over-year increase. This growth was fueled by both new customer acquisition and expansion within our existing customer base. Our gross margin remained strong at {gross_margin}%, demonstrating our ability to scale efficiently. Operating expenses were {operating_expenses}, and net income was {net_income}, translating to {earnings_per_share} per share. We are increasing our guidance for the full year based on these outstanding results.

    Next {cto_name} will provide more technicial details.

    {cto_name}: Thank you {cfo_name}. We continue to innovate and push the boundaries of what's possible in cybersecurity. Our team is focused on developing cutting-edge solutions that address the evolving threat landscape. We are investing heavily in research and development to stay ahead of the curve and deliver unparalleled value to our customers. Key areas of focus include: {aspect_3_details}.

    {cso_name}: Thank you. Cybersecurity is paramount, and we are taking proactive measures to protect our customers and ourselves. We are committed to maintaining the highest standards of security and compliance.

    Operator, we are now ready to open the call for questions.

    Operator: [Instructions for Q&A session]. First question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}: [Analyst 1 Question]

    {ceo_name}: [Answer to Analyst 1]

    Operator: Next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}: [Analyst 2 Question]

    {cfo_name}: [Answer to Analyst 2]

    Operator: Next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}: [Analyst 3 Question]

    {cto_name}: [Answer to Analyst 3]

    Operator: Next question comes from {analyst_4_name} with {analyst_4_firm}.

    {analyst_4_name}: [Analyst 4 Question]

    {ceo_name}: [Answer to Analyst 4]

    {ceo_name}: Thank you all for your insightful questions. We are confident in our ability to execute our strategy and deliver long-term value to our shareholders. Thank you to our dedicated employees, loyal customers, and valued partners.

    {ir_name}: Thank you for joining us today. This concludes our call. You may now disconnect.
    """),
    ("6", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, operator. Good afternoon, everyone, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. With me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cto_name}, Chief Technology Officer; {cso_name}, Chief Security Officer; and {vp_sales_name}, VP of Sales.

    Before we begin, I would like to remind you that today's call may contain forward-looking statements. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good afternoon, everyone. {company_name} continues to demonstrate leadership in the cybersecurity market. We achieved record bookings in the {quarter}, driven by strong demand for our integrated security platform and our expanding global presence. The positive customer feedback about {new_product} and the resulting {impact_of_product} is very encouraging.

    We are focused on six strategic priorities: {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, {aspect_5_details}, and {aspect_6_details}.

    Now, I'll turn the call over to {cfo_name} to provide a more detailed review of our financial performance.

    {cfo_name}: Thank you, {ceo_name}. We delivered another quarter of strong financial results. Total revenue for the {quarter} was {revenue}, representing a {revenue_growth}% increase year-over-year. We saw significant growth in our subscription revenue, which now accounts for {subscription_revenue_percentage}% of our total revenue. Gross margin was {gross_margin}%, while operating expenses were {operating_expenses}. Net income was {net_income}, resulting in earnings per share of {earnings_per_share}. We are reiterating our full-year guidance and remain confident in our ability to achieve our financial objectives.

    {cto_name}: Thank you {cfo_name}. Our engineering team is laser-focused on innovation and delivering cutting-edge security solutions. We are leveraging artificial intelligence and machine learning to enhance our threat detection and response capabilities. Key areas of focus include: {aspect_3_details}.

    {cso_name}: Security remains our top priority. We are constantly monitoring the threat landscape and adapting our security posture to protect our customers and our own infrastructure.

    {vp_sales_name}: Thank you. We are seeing strong demand for our solutions across all geographies and industry verticals. Our sales team is executing well, and we are expanding our channel partnerships to reach a wider audience.

    Operator, we are now ready to open the call for questions.

    Operator: [Instructions for Q&A session]. First question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}: [Analyst 1 Question]

    {ceo_name}: [Answer to Analyst 1]

    Operator: Next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}: [Analyst 2 Question]

    {cfo_name}: [Answer to Analyst 2]

    Operator: Next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}: [Analyst 3 Question]

    {cto_name}: [Answer to Analyst 3]

     Operator: Next question comes from {analyst_4_name} with {analyst_4_firm}.

    {analyst_4_name}: [Analyst 4 Question]

    {cso_name}: [Answer to Analyst 4]

    {ceo_name}: Thank you for your thoughtful questions. We believe we are well-positioned to capitalize on the growing demand for cybersecurity solutions. Thank you to our employees, customers, and partners for their continued support.

    {ir_name}: Thank you for joining us today. This concludes our call. You may now disconnect.
    """),
    ("7", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, operator. Good afternoon, everyone, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. With me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cto_name}, Chief Technology Officer; {cso_name}, Chief Security Officer; {vp_sales_name}, VP of Sales; and {chief_marketing_officer_name}, Chief Marketing Officer.

    Before we begin, I would like to remind you that today's call may contain forward-looking statements. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good afternoon, everyone. We are pleased to report another strong quarter for {company_name}. Our results reflect the growing importance of cybersecurity in today's digital landscape and our ability to deliver innovative solutions that meet the evolving needs of our customers. The market reception to {new_product} has been overwhelmingly positive, significantly contributing to its {impact_of_product}.

    Our strategy is built on seven key pillars: {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, {aspect_5_details}, {aspect_6_details}, and {aspect_7_details}.

    Now, I'll turn the call over to {cfo_name} to discuss our financial performance in more detail.

    {cfo_name}: Thank you, {ceo_name}. We achieved record revenue of {revenue} in the {quarter}, representing a {revenue_growth}% increase year-over-year. Our gross margin remained healthy at {gross_margin}%, and we continued to invest in growth initiatives. Operating expenses were {operating_expenses}. Net income was {net_income}, resulting in earnings per share of {earnings_per_share}. We are raising our full-year revenue and earnings guidance based on our strong performance to date.

    {cto_name}: Thank you {cfo_name}. Our technology roadmap is focused on delivering next-generation security solutions that leverage artificial intelligence, machine learning, and cloud computing. Key areas of focus include: {aspect_3_details}.

    {cso_name}: We are committed to providing our customers with the highest level of security. We are constantly monitoring the threat landscape and adapting our security posture to protect against emerging threats.

    {vp_sales_name}: We are seeing strong demand for our solutions across all geographies and industry verticals. Our sales team is focused on building strong relationships with our customers and partners.

    {chief_marketing_officer_name}: Our marketing efforts are focused on building brand awareness and generating demand for our solutions. We are using a variety of channels to reach our target audience, including digital marketing, public relations, and events.

    Operator, we are now ready to open the call for questions.

    Operator: [Instructions for Q&A session]. First question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}: [Analyst 1 Question]

    {ceo_name}: [Answer to Analyst 1]

    Operator: Next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}: [Analyst 2 Question]

    {cfo_name}: [Answer to Analyst 2]

    Operator: Next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}: [Analyst 3 Question]

    {cto_name}: [Answer to Analyst 3]

    Operator: Next question comes from {analyst_4_name} with {analyst_4_firm}.

    {analyst_4_name}: [Analyst 4 Question]

    {cso_name}: [Answer to Analyst 4]

    {ceo_name}: Thank you for your insightful questions. We are excited about the opportunities ahead and are confident in our ability to deliver long-term value to our shareholders.

    {ir_name}: Thank you for joining us today. This concludes our call. You may now disconnect.
    """),
    ("8", """
    Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, operator. Good afternoon, everyone, and thank you for joining us today to discuss {company_name}'s results for the {quarter}. With me on today's call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cto_name}, Chief Technology Officer; {cso_name}, Chief Security Officer; {vp_sales_name}, VP of Sales; {chief_marketing_officer_name}, Chief Marketing Officer; and {chief_product_officer_name}, Chief Product Officer.

    Before we begin, I would like to remind you that today's call may contain forward-looking statements. These statements are based on current expectations and assumptions and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

    Now, I'd like to turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good afternoon, everyone. {company_name} delivered exceptional results in the {quarter}, exceeding expectations across all key metrics. Our performance reflects the strength of our product portfolio, our expanding customer base, and our commitment to innovation. The adoption rate of {new_product} is accelerating, demonstrating the {impact_of_product} and the value we bring to our customers.

    Our strategic priorities are focused on eight key areas: {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, {aspect_5_details}, {aspect_6_details}, {aspect_7_details}, and {aspect_8_details}.

    Now, I'll turn the call over to {cfo_name} to provide a more detailed review of our financial results.

    {cfo_name}: Thank you, {ceo_name}. We achieved record revenue of {revenue} in the {quarter}, representing a {revenue_growth}% increase year-over-year. Our gross margin remained strong at {gross_margin}%, and we continued to invest in growth initiatives. Operating expenses were {operating_expenses}. Net income was {net_income}, resulting in earnings per share of {earnings_per_share}. We are increasing our full-year revenue and earnings guidance based on our strong performance to date.

    {cto_name}: Thank you {cfo_name}. Our technology team is focused on developing cutting-edge security solutions that leverage the latest advancements in artificial intelligence, machine learning, and cloud computing. Key areas of focus include: {aspect_3_details}.

    {cso_name}: Security remains our top priority. We are continuously monitoring the threat landscape and adapting our security posture to protect our customers and our own infrastructure.

    {vp_sales_name}: We are seeing strong demand for our solutions across all geographies and industry verticals. Our sales team is focused on building strong relationships with our customers and partners and expanding our market share.

    {chief_marketing_officer_name}: Our marketing efforts are focused on building brand awareness and generating demand for our solutions. We are using a variety of channels to reach our target audience, including digital marketing, public relations, and events. We are also investing in thought leadership initiatives to establish {company_name} as a trusted advisor in the cybersecurity industry.

    {chief_product_officer_name}: Thank you. Our product strategy focuses on delivering innovative and integrated security solutions that address the evolving needs of our customers. We are constantly gathering feedback from our customers and partners to ensure that our products meet their needs and exceed their expectations.

    Operator, we are now ready to open the call for questions.

    Operator: [Instructions for Q&A session]. First question comes from {analyst_1_name} with {analyst_1_firm}.

    {analyst_1_name}: [Analyst 1 Question]

    {ceo_name}: [Answer to Analyst 1]

    Operator: Next question comes from {analyst_2_name} with {analyst_2_firm}.

    {analyst_2_name}: [Analyst 2 Question]

    {cfo_name}: [Answer to Analyst 2]

    Operator: Next question comes from {analyst_3_name} with {analyst_3_firm}.

    {analyst_3_name}: [Analyst 3 Question]

    {cto_name}: [Answer to Analyst 3]

    Operator: Next question comes from {analyst_4_name} with {analyst_4_firm}.

    {analyst_4_name}: [Analyst 4 Question]

    {cso_name}: [Answer to Analyst 4]

    {ceo_name}: Thank you for your insightful questions. We are confident in our ability to continue to deliver strong results and create value for our shareholders. Thank you to our employees, customers and partners.

    {ir_name}: Thank you for joining us today. This concludes our call. You may now disconnect.
    """)
])