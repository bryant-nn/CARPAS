from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.
I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator. Good morning, everyone, and welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and other members of our leadership team.
Before we begin, I would like to remind you that today's discussion may contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more complete discussion of these risks.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. I'm pleased to report our results for {quarter}. We achieved {aspect_1_details}, which reflects our strong execution in a dynamic market. We are particularly excited about the initial performance of our {new_product} service and its {impact_of_product}. Our investments in {aspect_2_details} are also paying off, driving increased customer satisfaction and loyalty. Furthermore, we have focused on {aspect_3_details}, which has allowed us to maintain profitability. Finally, our strategic focus remains on {aspect_4_details}.

{cfo_name}: Thank you, {ceo_name}. Turning to the financials, our revenue for the quarter was {revenue}, representing a {growth_rate} increase year-over-year. Our adjusted EBITDA was {ebitda}, with a margin of {margin}. We continue to manage our expenses effectively and are on track to meet our financial targets for the year. Our capital expenditures were {capex}, primarily driven by investments in our 5G network expansion.

Operator: Thank you. We will now begin the question-and-answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you provide more color on {analyst_1_question}?

{ceo_name}: Certainly. {analyst_1_answer}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Hi, thanks for taking my question. Could you elaborate on your plans for {analyst_2_question}?

{cfo_name}: Yes, {analyst_2_answer}

{ir_name}: Thank you for your questions. That concludes our Q&A session. {ceo_name}, would you like to provide closing remarks?

{ceo_name}: Thank you. In closing, I am proud of our team's performance this quarter. We are well-positioned to continue delivering value to our customers and shareholders. Thank you for joining us today.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
"""),
    ("5", """
Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.
I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator. Good morning, everyone, and welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cno_name}, Chief Network Officer; and other members of our leadership team.
Before we begin, I would like to remind you that today's discussion may contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more complete discussion of these risks.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. I'm pleased to report our results for {quarter}. We exceeded expectations in several key areas. First, {aspect_1_details}. Second, {aspect_2_details}. We are seeing very positive results from our investments in {new_product}, and its {impact_of_product} is significant. Third, we focused on {aspect_3_details}. Fourth, {aspect_4_details} is proving successful. Finally, we are strategically positioning ourselves for {aspect_5_details}.

{cfo_name}: Thank you, {ceo_name}. Turning to the financials, our revenue for the quarter was {revenue}, up {growth_rate} year-over-year. Our adjusted EBITDA was {ebitda}, resulting in a margin of {margin}. We are maintaining strict cost discipline. Capital expenditures were {capex}, primarily allocated to 5G rollout and fiber expansion.

{cno_name}: Thank you. I would like to provide an update on our network performance. We have made significant progress in expanding our 5G coverage. Our network reliability metrics continue to improve, and we are seeing increased data usage across our customer base. We are also actively working on enhancing our cybersecurity infrastructure. Our team's dedication to {network_focus_area} has been instrumental in achieving these results.

Operator: Thank you. We will now begin the question-and-answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you discuss the competitive landscape and your strategy for {analyst_1_question}?

{ceo_name}: Certainly. {analyst_1_answer}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Hi, thanks for taking my question. What are your expectations for subscriber growth in the next quarter, and how will that impact {analyst_2_question}?

{cfo_name}: We anticipate {analyst_2_answer}

Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}: Can you provide an update on your fiber deployment plans and the expected ROI on those investments?

{cno_name}: {analyst_3_answer}

{ir_name}: Thank you for your questions. That concludes our Q&A session. {ceo_name}, would you like to provide closing remarks?

{ceo_name}: Thank you. In closing, we are pleased with our progress this quarter and remain confident in our ability to execute our strategy and deliver long-term value. Thank you for your time and interest in {company_name}.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
"""),
    ("6", """
Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.
I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator. Good morning, everyone, and welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cno_name}, Chief Network Officer; {cco_name}, Chief Commercial Officer; and other members of our leadership team.
Before we begin, I would like to remind you that today's discussion may contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more complete discussion of these risks.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. I am excited to share our {quarter} results, which reflect our commitment to innovation and customer satisfaction. We achieved strong performance across several key areas.
First, our {aspect_1_details} exceeded expectations. Second, we continue to see strong adoption of our {new_product}, leading to {impact_of_product}. Third, our focus on {aspect_2_details} has yielded impressive results. Fourth, we are making significant strides in {aspect_3_details}. Fifth, our efforts to {aspect_4_details} are paying off. Sixth, we are strategically investing in {aspect_5_details}, and finally, we are exploring {aspect_6_details}.

{cfo_name}: Thank you, {ceo_name}. Now, let's move on to the financial results. Our revenue for the quarter reached {revenue}, an increase of {growth_rate} compared to the same period last year. Adjusted EBITDA was {ebitda}, resulting in a margin of {margin}. We are diligently managing our costs and optimizing our capital allocation. Capital expenditures amounted to {capex}, primarily allocated to 5G infrastructure, fiber deployment, and content acquisition.

{cno_name}: Thank you. I would like to provide an update on our network performance and expansion. We continue to enhance our 5G network, achieving wider coverage and faster speeds. Our network reliability remains high, and we are investing in advanced technologies to further improve performance. We are also focused on optimizing our network for emerging applications like IoT and edge computing.

{cco_name}: Thank you. I'm excited to share our commercial achievements. We saw strong growth in subscriber additions, driven by our innovative product offerings and targeted marketing campaigns. Customer satisfaction remains a top priority, and we are continuously working to improve the customer experience across all touchpoints. We are also focused on expanding our partnerships to offer bundled services and enhance customer value.

Operator: Thank you. We will now begin the question-and-answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you elaborate on your subscriber acquisition costs and your strategy for reducing churn, specifically with regards to {analyst_1_question}?

{cco_name}: {analyst_1_answer}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Hi, thanks for taking my question. What are your plans for leveraging AI and automation to improve network efficiency and reduce operational costs, and how does that impact {analyst_2_question}?

{cno_name}: {analyst_2_answer}

Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}: Can you discuss the regulatory environment and any potential impacts on your business, including {analyst_3_question}?

{ceo_name}: {analyst_3_answer}

{ir_name}: Thank you for your questions. That concludes our Q&A session. {ceo_name}, would you like to provide closing remarks?

{ceo_name}: Thank you. In conclusion, we are pleased with our progress this quarter and remain focused on executing our strategic priorities. We are confident in our ability to deliver sustainable growth and create value for our shareholders. Thank you for joining us today.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
"""),
    ("7", """
Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.
I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator. Good morning, everyone, and welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cno_name}, Chief Network Officer; {cco_name}, Chief Commercial Officer; {cto_name}, Chief Technology Officer; and other members of our leadership team.
Before we begin, I would like to remind you that today's discussion may contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more complete discussion of these risks.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. We're very pleased with our performance in the {quarter}, driven by strong execution and a favorable market environment. We are focused on delivering long-term sustainable growth.
Our achievements include: {aspect_1_details}. We are also seeing substantial growth from {new_product} with a significant {impact_of_product}. Further, we are concentrating on {aspect_2_details}. Additionally, {aspect_3_details} is showing promise. We are also improving our {aspect_4_details}. We are strategically investing in {aspect_5_details}. Finally, {aspect_6_details} is underway and we are exploring {aspect_7_details}.

{cfo_name}: Thank you, {ceo_name}. Moving to the financials, our revenue for the quarter was {revenue}, representing a {growth_rate} year-over-year increase. Adjusted EBITDA was {ebitda}, resulting in a margin of {margin}. We continue to manage our expenses prudently and are optimizing our capital allocation. Capital expenditures were {capex}, primarily focused on expanding our 5G network and fiber infrastructure.

{cno_name}: Thank you. I'd like to provide an update on our network performance. We've made significant strides in expanding our 5G coverage and increasing network capacity. We're also investing in advanced technologies like network slicing and edge computing to support new applications and services. Our network uptime and reliability remain high. We are also improving {network_improvement}.

{cco_name}: Thank you. We've seen strong customer growth and improved customer satisfaction scores this quarter. Our bundled service offerings are resonating well with customers, and we're focused on providing a seamless and personalized customer experience. We are also focused on increasing {customer_focus}.

{cto_name}: Thank you. From a technology perspective, we are focused on driving innovation and leveraging emerging technologies to enhance our network and services. We are exploring the use of AI and machine learning to automate network operations and improve efficiency. We are also working on developing new products and services that leverage 5G and edge computing. Our R&D efforts are concentrated on {tech_focus}.

Operator: Thank you. We will now begin the question-and-answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you provide more details on your plans for expanding your presence in the enterprise market and how you plan to compete with existing players, specifically regarding {analyst_1_question}?

{cco_name}: {analyst_1_answer}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Hi, thanks for taking my question. What are your expectations for the impact of inflation and rising interest rates on your business, and how do you plan to mitigate those risks, especially regarding {analyst_2_question}?

{cfo_name}: {analyst_2_answer}

Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}: Can you discuss your sustainability initiatives and your plans for reducing your carbon footprint, and how will you measure your success, specifically addressing {analyst_3_question}?

{ceo_name}: {analyst_3_answer}

{ir_name}: Thank you for your questions. That concludes our Q&A session. {ceo_name}, would you like to provide closing remarks?

{ceo_name}: Thank you. In closing, we are confident in our ability to continue delivering strong results and creating value for our shareholders. We are committed to innovation, customer satisfaction, and sustainable growth. Thank you for your time and interest in {company_name}.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
"""),
    ("8", """
Operator: Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.
I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, Operator. Good morning, everyone, and welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cno_name}, Chief Network Officer; {cco_name}, Chief Commercial Officer; {cto_name}, Chief Technology Officer; {coo_name}, Chief Operating Officer; and other members of our leadership team.
Before we begin, I would like to remind you that today's discussion may contain forward-looking statements. These statements are based on management's current expectations and are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a more complete discussion of these risks.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. We are pleased to report a strong {quarter}, demonstrating our continued commitment to growth and innovation. Our success is driven by our dedicated team and strategic investments.
Our key achievements include: {aspect_1_details}. The launch of {new_product} is exceeding expectations, resulting in {impact_of_product}. Further milestones are: {aspect_2_details}. We are also focusing on {aspect_3_details}. Our dedication to {aspect_4_details} is bearing fruit. Our strategy is to enhance {aspect_5_details}. We are actively investing in {aspect_6_details}. We are also exploring {aspect_7_details} and finally, analyzing {aspect_8_details}.

{cfo_name}: Thank you, {ceo_name}. Now, let's review our financial performance. Revenue for the quarter reached {revenue}, reflecting a {growth_rate} increase year-over-year. Adjusted EBITDA was {ebitda}, resulting in a margin of {margin}. We maintain a disciplined approach to cost management and capital allocation. Capital expenditures totaled {capex}, primarily allocated to expanding our 5G network, fiber infrastructure, and content investments.

{cno_name}: Thank you. I'm pleased to provide an update on our network advancements. We've significantly expanded our 5G coverage, delivering faster speeds and lower latency. Our network reliability remains high, and we are continuously optimizing our infrastructure to meet growing demand. We are also focusing on enhancing our cybersecurity posture. We are committed to {network_commitment}.

{cco_name}: Thank you. I'm excited to share our commercial achievements. We've seen strong subscriber growth across our various service offerings. Customer satisfaction remains a top priority, and we are continuously improving the customer experience. We are also focused on expanding our partnerships to offer bundled services and enhance customer value. We are prioritizing {commercial_priority}.

{cto_name}: Thank you. From a technology perspective, we are focused on driving innovation and leveraging emerging technologies to transform our business. We are exploring the use of AI and machine learning to automate network operations, improve customer service, and develop new products and services. We are also investing in research and development to stay ahead of the curve. Our technological direction is {tech_direction}.

{coo_name}: Thank you. Operationally, we are focused on improving efficiency and streamlining our processes. We are leveraging data analytics to optimize our resource allocation and improve decision-making. We are also committed to sustainability and reducing our environmental impact. Our operational focus is {operational_focus}.

Operator: Thank you. We will now begin the question-and-answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}: Good morning. Can you provide more details on your content strategy and your plans for investing in original programming, and what is the anticipated impact on {analyst_1_question}?

{ceo_name}: {analyst_1_answer}

Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}: Hi, thanks for taking my question. What are your plans for addressing the digital divide and ensuring that all communities have access to affordable broadband, and how do you plan to achieve {analyst_2_question}?

{cco_name}: {analyst_2_answer}

Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}: Can you discuss your capital allocation priorities and your plans for returning capital to shareholders, including {analyst_3_question}?

{cfo_name}: {analyst_3_answer}

Operator: Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

{analyst_4_name}: What are your strategies for navigating the changing regulatory landscape?

{ceo_name}: {analyst_4_answer}

{ir_name}: Thank you for your questions. That concludes our Q&A session. {ceo_name}, would you like to provide closing remarks?

{ceo_name}: Thank you. In conclusion, we are pleased with our performance this quarter and remain confident in our ability to execute our strategy and deliver long-term value to our shareholders. We are committed to innovation, customer satisfaction, and sustainability. Thank you for joining us today.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
""")
])