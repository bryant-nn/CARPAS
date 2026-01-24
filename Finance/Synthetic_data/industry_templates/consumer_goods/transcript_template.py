from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}.

{ir_name}:
Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and other members of our leadership team.

Before we begin, I would like to remind you that some of the statements we will be making today are forward-looking and are based on our current expectations and beliefs. These statements are subject to certain risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}. Good morning, everyone. Thank you for joining us. {company_name} delivered a solid {quarter}, demonstrating the resilience of our brands and the strength of our team. We are navigating a dynamic environment and remain focused on executing our strategic priorities.

Our discussion today will cover four key aspects:
1.  Overall Financial Performance: {aspect_1_details}
2.  Brand Performance and Innovation: {aspect_2_details}
3.  Supply Chain and Operational Efficiency: {aspect_3_details}
4.  Outlook for the Remainder of the Year: {aspect_4_details}

I will now turn the call over to {cfo_name} to provide more detail on our financial results.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we delivered a solid quarter. Net sales were {net_sales}, representing a {sales_growth_percent}% increase compared to the prior year. Gross margin was {gross_margin_percent}%, driven by {gross_margin_drivers}. Operating income was {operating_income}. Diluted earnings per share were {eps}. We continue to manage our costs effectively and invest in our long-term growth initiatives.

(Detailed financial discussion continues...)

Operator, we are now ready to open the call for questions.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}.

{analyst_1_name}:
Good morning. Can you provide more color on the impact of {inflation_impact} on your consumer spending habits?

{ceo_name}:
(Answers question)

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_company}.

{analyst_2_name}:
Regarding your new product {new_product}, what are the projections for its market impact?

{chief_marketing_officer_name}:
(Answers question)

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_company}.

{analyst_3_name}:
Can you provide more details on the promotional spending for the quarter?

{cfo_name}:
(Answers question)

Operator:
There are no further questions at this time. I will now turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, Operator, and thank you all for your questions and participation in today's call. We are confident in our ability to navigate the current environment and deliver long-term value for our shareholders. We look forward to speaking with you again next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. You may now disconnect.
    """),
    ("5", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}.

{ir_name}:
Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_marketing_officer_name}, Chief Marketing Officer; and other members of our leadership team.

Before we begin, I would like to remind you that some of the statements we will be making today are forward-looking and are based on our current expectations and beliefs. These statements are subject to certain risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}. Good morning, everyone. Thank you for joining us. {company_name} delivered a solid {quarter}, demonstrating the resilience of our brands and the strength of our team. We are navigating a dynamic environment and remain focused on executing our strategic priorities.

Our discussion today will cover five key aspects:
1.  Overall Financial Performance: {aspect_1_details}
2.  Brand Performance and Innovation: {aspect_2_details}
3.  Supply Chain and Operational Efficiency: {aspect_3_details}
4.  Marketing and Promotional Activities: {aspect_4_details}
5.  Outlook for the Remainder of the Year: {aspect_5_details}

I will now turn the call over to {cfo_name} to provide more detail on our financial results.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we delivered a solid quarter. Net sales were {net_sales}, representing a {sales_growth_percent}% increase compared to the prior year. Gross margin was {gross_margin_percent}%, driven by {gross_margin_drivers}. Operating income was {operating_income}. Diluted earnings per share were {eps}. We continue to manage our costs effectively and invest in our long-term growth initiatives.

(Detailed financial discussion continues...)

I will now turn the call over to {chief_marketing_officer_name} to discuss marketing and brand performance.

{chief_marketing_officer_name}:
Thank you, {cfo_name}. We saw strong performance in our {brand_1} and {brand_2} brands this quarter. Our recent marketing campaigns, including the {campaign_name} campaign, have resonated well with consumers. We are also excited about the launch of our new product, {new_product}, which is already generating positive feedback. {impact_of_product}

Operator, we are now ready to open the call for questions.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}.

{analyst_1_name}:
Good morning. Can you elaborate on the details of the new marketing campaign and its impact on sales?

{chief_marketing_officer_name}:
(Answers question)

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_company}.

{analyst_2_name}:
What are your plans for addressing rising commodity costs in the coming quarters?

{cfo_name}:
(Answers question)

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_company}.

{analyst_3_name}:
How is the current inflationary environment impacting consumer demand for your premium product lines?

{ceo_name}:
(Answers question)

Operator:
Our next question comes from {analyst_4_name} with {analyst_4_company}.

{analyst_4_name}:
Can you discuss the performance of your e-commerce channel this quarter?

{chief_marketing_officer_name}:
(Answers question)

Operator:
There are no further questions at this time. I will now turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, Operator, and thank you all for your questions and participation in today's call. We are confident in our ability to navigate the current environment and deliver long-term value for our shareholders. We look forward to speaking with you again next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. You may now disconnect.
    """),
    ("6", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}.

{ir_name}:
Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_marketing_officer_name}, Chief Marketing Officer; {chief_supply_chain_officer_name}, Chief Supply Chain Officer; and other members of our leadership team.

Before we begin, I would like to remind you that some of the statements we will be making today are forward-looking and are based on our current expectations and beliefs. These statements are subject to certain risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}. Good morning, everyone. Thank you for joining us. {company_name} delivered a solid {quarter}, demonstrating the resilience of our brands and the strength of our team. We are navigating a dynamic environment and remain focused on executing our strategic priorities.

Our discussion today will cover six key aspects:
1.  Overall Financial Performance: {aspect_1_details}
2.  Brand Performance and Innovation: {aspect_2_details}
3.  Supply Chain and Operational Efficiency: {aspect_3_details}
4.  Marketing and Promotional Activities: {aspect_4_details}
5.  Sustainability Initiatives: {aspect_5_details}
6.  Outlook for the Remainder of the Year: {aspect_6_details}

I will now turn the call over to {cfo_name} to provide more detail on our financial results.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we delivered a solid quarter. Net sales were {net_sales}, representing a {sales_growth_percent}% increase compared to the prior year. Gross margin was {gross_margin_percent}%, driven by {gross_margin_drivers}. Operating income was {operating_income}. Diluted earnings per share were {eps}. We continue to manage our costs effectively and invest in our long-term growth initiatives.

(Detailed financial discussion continues...)

Next, I will turn the call over to {chief_marketing_officer_name} to discuss marketing and brand performance.

{chief_marketing_officer_name}:
Thank you, {cfo_name}. We saw strong performance in our core brands, particularly {brand_1}. Our digital marketing efforts are driving significant engagement, and we are seeing strong results from our {campaign_name} campaign.

Following {chief_marketing_officer_name}, {chief_supply_chain_officer_name} will provide an update on our supply chain initiatives.

{chief_supply_chain_officer_name}:
Thank you, {chief_marketing_officer_name}. We continue to focus on optimizing our supply chain to improve efficiency and reduce costs. We are implementing new technologies and processes to enhance our responsiveness to changing market conditions. We are also actively working to mitigate the impact of supply chain disruptions.

Operator, we are now ready to open the call for questions.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}.

{analyst_1_name}:
Could you provide more insight into the geographic performance, particularly in emerging markets?

{ceo_name}:
(Answers question)

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_company}.

{analyst_2_name}:
How are you managing inventory levels given the current economic uncertainty?

{cfo_name}:
(Answers question)

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_company}.

{analyst_3_name}:
Can you discuss the progress on your sustainability goals and any related cost implications?

{chief_supply_chain_officer_name}:
(Answers question)

Operator:
Our next question comes from {analyst_4_name} with {analyst_4_company}.

{analyst_4_name}:
What are your expectations for pricing elasticity in the coming quarters?

{chief_marketing_officer_name}:
(Answers question)

Operator:
There are no further questions at this time. I will now turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, Operator, and thank you all for your insightful questions. We remain committed to delivering strong results and creating value for our shareholders. We look forward to updating you on our progress next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. You may now disconnect.
    """),
    ("7", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}.

{ir_name}:
Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_marketing_officer_name}, Chief Marketing Officer; {chief_supply_chain_officer_name}, Chief Supply Chain Officer; {chief_innovation_officer_name}, Chief Innovation Officer; and other members of our leadership team.

Before we begin, I would like to remind you that some of the statements we will be making today are forward-looking and are based on our current expectations and beliefs. These statements are subject to certain risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}. Good morning, everyone. Thank you for joining us. {company_name} delivered a solid {quarter}, demonstrating the resilience of our brands and the strength of our team. We are navigating a dynamic environment and remain focused on executing our strategic priorities.

Our discussion today will cover seven key aspects:
1.  Overall Financial Performance: {aspect_1_details}
2.  Brand Performance and Innovation: {aspect_2_details}
3.  Supply Chain and Operational Efficiency: {aspect_3_details}
4.  Marketing and Promotional Activities: {aspect_4_details}
5.  Sustainability Initiatives: {aspect_5_details}
6.  Digital Transformation: {aspect_6_details}
7.  Outlook for the Remainder of the Year: {aspect_7_details}

I will now turn the call over to {cfo_name} to provide more detail on our financial results.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we delivered a solid quarter. Net sales were {net_sales}, representing a {sales_growth_percent}% increase compared to the prior year. Gross margin was {gross_margin_percent}%, driven by {gross_margin_drivers}. Operating income was {operating_income}. Diluted earnings per share were {eps}. We continue to manage our costs effectively and invest in our long-term growth initiatives.

(Detailed financial discussion continues...)

Following my remarks, {chief_marketing_officer_name} will provide an update on our marketing and brand performance.

{chief_marketing_officer_name}:
Thank you, {cfo_name}. We continue to see strong performance across our key brands. Our marketing investments are driving increased consumer engagement, and we are particularly pleased with the results of our recent {campaign_name} campaign.

After {chief_marketing_officer_name}, {chief_supply_chain_officer_name} will discuss our supply chain initiatives.

{chief_supply_chain_officer_name}:
Thank you, {chief_marketing_officer_name}. Our focus remains on optimizing our supply chain to enhance efficiency and resilience. We are implementing advanced analytics to improve forecasting and inventory management.

Finally, {chief_innovation_officer_name} will share insights on our innovation pipeline.

{chief_innovation_officer_name}:
Thank you, {chief_supply_chain_officer_name}. We are excited about the progress we are making on our new product development initiatives. Our pipeline is robust, and we are confident that our innovations will drive future growth. Our recent product, {new_product}, is showing promising early results. {impact_of_product}

Operator, we are now ready to open the call for questions.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}.

{analyst_1_name}:
Can you provide an update on your efforts to reduce packaging waste and the associated cost savings?

{chief_supply_chain_officer_name}:
(Answers question)

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_company}.

{analyst_2_name}:
How are you leveraging data analytics to personalize your marketing efforts and improve customer engagement?

{chief_marketing_officer_name}:
(Answers question)

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_company}.

{analyst_3_name}:
What is the expected impact of recent commodity price increases on your gross margins?

{cfo_name}:
(Answers question)

Operator:
Our next question comes from {analyst_4_name} with {analyst_4_company}.

{analyst_4_name}:
Can you discuss the competitive landscape and any emerging trends that are impacting your market share?

{ceo_name}:
(Answers question)

Operator:
There are no further questions at this time. I will now turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, Operator, and thank you all for your thoughtful questions and participation. We are confident in our ability to execute our strategy and deliver long-term value for our shareholders. We look forward to updating you next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. You may now disconnect.
    """),
    ("8", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}.

{ir_name}:
Thank you, Operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_marketing_officer_name}, Chief Marketing Officer; {chief_supply_chain_officer_name}, Chief Supply Chain Officer; {chief_innovation_officer_name}, Chief Innovation Officer; {chief_sales_officer_name}, Chief Sales Officer; and other members of our leadership team.

Before we begin, I would like to remind you that some of the statements we will be making today are forward-looking and are based on our current expectations and beliefs. These statements are subject to certain risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more detailed description of these risks and uncertainties.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}. Good morning, everyone. Thank you for joining us. {company_name} delivered a solid {quarter}, demonstrating the resilience of our brands and the strength of our team. We are navigating a dynamic environment and remain focused on executing our strategic priorities.

Our discussion today will cover eight key aspects:
1.  Overall Financial Performance: {aspect_1_details}
2.  Brand Performance and Innovation: {aspect_2_details}
3.  Supply Chain and Operational Efficiency: {aspect_3_details}
4.  Marketing and Promotional Activities: {aspect_4_details}
5.  Sustainability Initiatives: {aspect_5_details}
6.  Digital Transformation: {aspect_6_details}
7.  Sales Performance and Channel Strategy: {aspect_7_details}
8.  Outlook for the Remainder of the Year: {aspect_8_details}

I will now turn the call over to {cfo_name} to provide more detail on our financial results.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we delivered a solid quarter. Net sales were {net_sales}, representing a {sales_growth_percent}% increase compared to the prior year. Gross margin was {gross_margin_percent}%, driven by {gross_margin_drivers}. Operating income was {operating_income}. Diluted earnings per share were {eps}. We continue to manage our costs effectively and invest in our long-term growth initiatives.

(Detailed financial discussion continues...)

Next, {chief_marketing_officer_name} will provide insights on our marketing and brand initiatives.

{chief_marketing_officer_name}:
Thank you, {cfo_name}. Our brand building efforts have contributed significantly to our performance. We are seeing strong engagement across all our channels, especially with our new {campaign_name} campaign.

Following {chief_marketing_officer_name}, {chief_supply_chain_officer_name} will discuss supply chain performance.

{chief_supply_chain_officer_name}:
Thank you. We continue to optimize our supply chain network and implement advanced technologies to improve efficiency and resilience. We are also focused on reducing our carbon footprint.

After {chief_supply_chain_officer_name}, {chief_innovation_officer_name} will share updates on our product innovation pipeline.

{chief_innovation_officer_name}:
Thank you. We are excited about our pipeline of innovative products. Our recent product launch, {new_product}, has been well-received by consumers. {impact_of_product}

Finally, {chief_sales_officer_name} will discuss our sales performance and channel strategy.

{chief_sales_officer_name}:
Thank you. We are focused on expanding our distribution channels and improving our sales execution. We are seeing strong growth in our e-commerce channel, and we are also investing in our retail partnerships.

Operator, we are now ready to open the call for questions.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_company}.

{analyst_1_name}:
How is your company addressing the increasing demand for sustainable products?

{chief_innovation_officer_name}:
(Answers question)

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_company}.

{analyst_2_name}:
What are your plans for expanding your presence in international markets?

{chief_sales_officer_name}:
(Answers question)

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_company}.

{analyst_3_name}:
Can you discuss the impact of inflation on your pricing strategy and consumer demand?

{cfo_name}:
(Answers question)

Operator:
Our next question comes from {analyst_4_name} with {analyst_4_company}.

{analyst_4_name}:
How are you leveraging artificial intelligence to improve your supply chain efficiency?

{chief_supply_chain_officer_name}:
(Answers question)

Operator:
There are no further questions at this time. I will now turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, Operator, and thank you all for your insightful questions and participation. We are confident in our ability to deliver long-term sustainable growth and create value for our shareholders. We look forward to speaking with you again next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} Earnings Conference Call. You may now disconnect.
    """)
])