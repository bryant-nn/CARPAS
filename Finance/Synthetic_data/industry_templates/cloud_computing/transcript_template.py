from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the presentation, we will conduct a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good afternoon, everyone, and thank you for joining us. Today, we will be discussing {company_name}'s results for the {quarter}. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and {cto_name}, Chief Technology Officer.

    Before we begin, I would like to remind you that today's call contains forward-looking statements. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'll turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. Thank you for joining us today. {company_name} had a strong {quarter}, driven by continued growth in our cloud platform and increasing adoption of our AI-powered services.

    During the quarter, we focused on four key areas:
    1. Expanding our global infrastructure.
    2. Enhancing our platform security.
    3. Driving innovation in AI and machine learning.
    4. Strengthening our partnerships.

    {aspect_1_details}

    Now I'll turn the call over to {cfo_name} to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong financial performance in the {quarter}. Revenue grew by {revenue_growth_percentage}% year-over-year to {revenue_amount}. Our gross margin was {gross_margin_percentage}%, and our operating margin was {operating_margin_percentage}%.

    {aspect_2_details}

    Now, I'll hand it back to {ceo_name} for further comments.

    {ceo_name}:
    Thank you, {cfo_name}. We are particularly excited about the momentum we are seeing with {new_product}, which is driving significant {impact_of_product} for our customers.

    {aspect_3_details}

    We continue to invest in research and development to stay ahead of the curve in the rapidly evolving cloud landscape. Our commitment to innovation is reflected in our recent advancements in {technology_advancement}.

    {aspect_4_details}

    With that, let's open the call for questions.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}:
    [Analyst Question 1]

    {ceo_name}:
    [Answer to Analyst Question 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}:
    [Analyst Question 2]

    {cfo_name}:
    [Answer to Analyst Question 2]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    {analyst_3_name}:
    [Analyst Question 3]

    {cto_name}:
    [Answer to Analyst Question 3]

    Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

    {analyst_4_name}:
    [Analyst Question 4]

    {ceo_name}:
    [Answer to Analyst Question 4]

    {ceo_name}:
    Thank you for your questions and your continued support. We are confident in our ability to continue to deliver strong results and create long-term value for our shareholders.

    {ir_name}:
    Thank you for joining us today. This concludes the call.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
    ("5", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the presentation, we will conduct a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good afternoon, everyone, and thank you for joining us. Today, we will be discussing {company_name}'s results for the {quarter}. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cto_name}, Chief Technology Officer; and {chief_product_officer_name}, Chief Product Officer.

    Before we begin, I would like to remind you that today's call contains forward-looking statements. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'll turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. Thank you for joining us today. {company_name} had an exceptional {quarter}, exceeding expectations across all key metrics. This success is a testament to our innovative technology, dedicated team, and strong customer relationships.

    During the quarter, we focused on five key areas:
    1. Expanding our market share in key verticals.
    2. Investing in cutting-edge research and development.
    3. Enhancing our cloud security posture.
    4. Driving operational efficiencies.
    5. Strengthening our ecosystem partnerships.

    {aspect_1_details}

    Now I'll turn the call over to {cfo_name} to discuss our financial results in more detail.

    {cfo_name}:
    Thank you, {ceo_name}. As {ceo_name} mentioned, we had a stellar financial performance in the {quarter}. Revenue grew by {revenue_growth_percentage}% year-over-year to {revenue_amount}, significantly outpacing industry averages. Our gross margin was {gross_margin_percentage}%, reflecting our pricing power and efficient cost management. Our operating margin was {operating_margin_percentage}%.

    {aspect_2_details}

    Now, I'll hand it over to {cto_name} for a technical update.

    {cto_name}:
    Thank you, {cfo_name}. From a technology perspective, we made significant strides in several key areas this quarter. We are proud to announce the general availability of our new {new_technology} platform, which offers unparalleled performance and scalability.

    {aspect_3_details}

    I'll now pass it to {chief_product_officer_name} for a product roadmap update.

    {chief_product_officer_name}:
    Thank you, {cto_name}. This quarter, we launched {new_product}, a game-changing solution for {target_market}. Early customer feedback has been overwhelmingly positive. We are seeing strong demand and a rapid increase in adoption.

    {aspect_4_details}

    Now, back to {ceo_name}.

    {ceo_name}:
    Thank you, {chief_product_officer_name}. We are incredibly excited about the future. We believe our investments in innovation, our commitment to customer success, and our talented team will continue to drive strong growth and value creation.

    {aspect_5_details}

    With that, let's open the call for questions.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}:
    [Analyst Question 1]

    {ceo_name}:
    [Answer to Analyst Question 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}:
    [Analyst Question 2]

    {cfo_name}:
    [Answer to Analyst Question 2]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    {analyst_3_name}:
    [Analyst Question 3]

    {cto_name}:
    [Answer to Analyst Question 3]

    {ceo_name}:
    Thank you for your insightful questions and your continued interest in {company_name}. We remain focused on executing our strategy and delivering long-term value for our shareholders.

    {ir_name}:
    Thank you for joining us today. This concludes the call.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
    ("6", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the presentation, we will conduct a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good afternoon, everyone, and thank you for joining us. Today, we will be discussing {company_name}'s results for the {quarter}. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cto_name}, Chief Technology Officer; {chief_product_officer_name}, Chief Product Officer; and {chief_marketing_officer_name}, Chief Marketing Officer.

    Before we begin, I would like to remind you that today's call contains forward-looking statements. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'll turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. Thank you for joining us today. {company_name} delivered another strong {quarter}, marked by significant growth in our core cloud business and increasing adoption of our innovative AI solutions.

    During the quarter, our priorities were focused on six key areas:
    1. Expanding our global cloud infrastructure footprint.
    2. Driving innovation in serverless computing.
    3. Enhancing our cybersecurity offerings.
    4. Strengthening our partnerships with leading ISVs.
    5. Improving customer satisfaction and retention.
    6. Investing in our talent pool and fostering a culture of innovation.

    {aspect_1_details}

    Now I'll turn the call over to {cfo_name} to provide a detailed review of our financial performance.

    {cfo_name}:
    Thank you, {ceo_name}. We are pleased with our financial results for the {quarter}. Revenue increased by {revenue_growth_percentage}% year-over-year to {revenue_amount}, driven by strong demand for our cloud services. Our gross margin was {gross_margin_percentage}%, reflecting our focus on operational efficiency. Our operating margin was {operating_margin_percentage}%.

    {aspect_2_details}

    Next, I'd like to introduce {cto_name}, who will provide an update on our technology initiatives.

    {cto_name}:
    Thank you, {cfo_name}. On the technology front, we made significant progress in several areas. We successfully launched our next-generation {cloud_service} platform, which offers enhanced performance and scalability.

    {aspect_3_details}

    Now, I'll pass it over to {chief_product_officer_name} for a product roadmap update.

    {chief_product_officer_name}:
    Thank you, {cto_name}. We are excited about the market reception to our new {product_name} offering. This product is designed to address the evolving needs of our customers in the {industry_segment} sector.

    {aspect_4_details}

    I'll now hand it over to {chief_marketing_officer_name} to discuss our marketing initiatives.

    {chief_marketing_officer_name}:
    Thank you, {chief_product_officer_name}. We have been focused on driving brand awareness and generating demand for our solutions. Our recent marketing campaigns have been highly effective in reaching our target audience.

    {aspect_5_details}

    Back to {ceo_name}.

    {ceo_name}:
    Thank you, {chief_marketing_officer_name}. We are confident that our strong financial performance, innovative technology, and talented team will enable us to continue to deliver exceptional value to our customers and shareholders.

    {aspect_6_details}

    With that, let's open the call for questions.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}:
    [Analyst Question 1]

    {ceo_name}:
    [Answer to Analyst Question 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}:
    [Analyst Question 2]

    {cfo_name}:
    [Answer to Analyst Question 2]

    {ceo_name}:
    Thank you for your insightful questions. We are committed to transparency and open communication with our investors.

    {ir_name}:
    Thank you for joining us today. This concludes the call.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
    ("7", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the presentation, we will conduct a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good afternoon, everyone, and thank you for joining us. Today, we will be discussing {company_name}'s results for the {quarter}. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cto_name}, Chief Technology Officer; {chief_product_officer_name}, Chief Product Officer; {chief_marketing_officer_name}, Chief Marketing Officer; {chief_sales_officer_name}, Chief Sales Officer; and {chief_security_officer_name}, Chief Security Officer.

    Before we begin, I would like to remind you that today's call contains forward-looking statements. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'll turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. Thank you for joining us today. {company_name} continued its strong growth trajectory in the {quarter}, driven by robust demand for our comprehensive suite of cloud services and solutions.

    During the quarter, our key priorities included:
    1. Expanding our presence in emerging markets.
    2. Accelerating the adoption of our AI-powered platform.
    3. Enhancing our developer ecosystem.
    4. Strengthening our commitment to sustainability.
    5. Investing in employee training and development.
    6. Improving cross-functional collaboration.
    7. Ensuring the security and privacy of our customers' data.

    {aspect_1_details}

    Now, I'll turn the call over to {cfo_name} to discuss our financial performance in more detail.

    {cfo_name}:
    Thank you, {ceo_name}. We are pleased to report another quarter of strong financial results. Revenue grew by {revenue_growth_percentage}% year-over-year to {revenue_amount}, exceeding our guidance. Our gross margin was {gross_margin_percentage}%, reflecting our efficient cost structure. Our operating margin was {operating_margin_percentage}%.

    {aspect_2_details}

    Next, I'd like to introduce {cto_name}, who will provide an update on our technology roadmap.

    {cto_name}:
    Thank you, {cfo_name}. We are making significant investments in research and development to stay at the forefront of cloud innovation. We are particularly excited about our progress in {technology_focus}.

    {aspect_3_details}

    Now, I'll pass it to {chief_product_officer_name} for a product update.

    {chief_product_officer_name}:
    Thank you, {cto_name}. We recently launched {new_product}, which is already gaining significant traction in the market.

    {aspect_4_details}

    I'll now hand it over to {chief_marketing_officer_name} to discuss our marketing strategy.

    {chief_marketing_officer_name}:
    Thank you, {chief_product_officer_name}. Our marketing efforts are focused on building brand awareness and generating demand for our solutions.

    {aspect_5_details}

    Next, I'd like to introduce {chief_sales_officer_name}, who will provide an update on our sales performance.

    {chief_sales_officer_name}:
    Thank you, {chief_marketing_officer_name}. Our sales team delivered a strong performance in the {quarter}, driven by increased customer adoption of our cloud services.

    {aspect_6_details}

    Finally, I'll pass it to {chief_security_officer_name} to discuss our security initiatives.

    {chief_security_officer_name}:
    Thank you, {chief_sales_officer_name}. Security is our top priority. We are committed to protecting our customers' data and maintaining the highest standards of security.

    {aspect_7_details}

    Back to {ceo_name}.

    {ceo_name}:
    Thank you, everyone. We are confident in our ability to continue to execute our strategy and deliver long-term value for our shareholders.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}:
    [Analyst Question 1]

    {ceo_name}:
    [Answer to Analyst Question 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}:
    [Analyst Question 2]

    {cfo_name}:
    [Answer to Analyst Question 2]

    Operator:
     Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    {analyst_3_name}:
    [Analyst Question 3]

    {cto_name}:
    [Answer to Analyst Question 3]

    {ceo_name}:
    Thank you for your questions. We appreciate your continued support.

    {ir_name}:
    Thank you for joining us today. This concludes the call.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
    ("8", """
    Operator:
    Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the presentation, we will conduct a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}:
    Good afternoon, everyone, and thank you for joining us. Today, we will be discussing {company_name}'s results for the {quarter}. With me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cto_name}, Chief Technology Officer; {chief_product_officer_name}, Chief Product Officer; {chief_marketing_officer_name}, Chief Marketing Officer; {chief_sales_officer_name}, Chief Sales Officer; {chief_security_officer_name}, Chief Security Officer; and {chief_innovation_officer_name}, Chief Innovation Officer.

    Before we begin, I would like to remind you that today's call contains forward-looking statements. These statements are subject to risks and uncertainties that could cause actual results to differ materially. Please refer to our SEC filings for a complete discussion of these risks.

    Now, I'll turn the call over to {ceo_name}.

    {ceo_name}:
    Thank you, {ir_name}, and good afternoon, everyone. Thank you for joining us today. {company_name} delivered exceptional results for the {quarter}, demonstrating the strength of our cloud platform and the increasing demand for our AI-driven solutions across diverse industries.

    During the quarter, we focused on eight key strategic priorities:
    1. Expanding our global reach through strategic partnerships.
    2. Driving innovation in edge computing and IoT solutions.
    3. Enhancing our commitment to open source technologies.
    4. Strengthening our data privacy and compliance programs.
    5. Investing in our employees' professional development.
    6. Improving our operational efficiency through automation.
    7. Fostering a diverse and inclusive workplace.
    8. Accelerating the adoption of sustainable cloud practices.

    {aspect_1_details}

    Now, I'll turn the call over to {cfo_name} to provide a detailed overview of our financial performance.

    {cfo_name}:
    Thank you, {ceo_name}. We are very pleased with our financial results for the {quarter}. Revenue increased by {revenue_growth_percentage}% year-over-year to {revenue_amount}, exceeding our guidance for the quarter. Our gross margin was {gross_margin_percentage}%, driven by our efficient cost management and economies of scale. Our operating margin was {operating_margin_percentage}%.

    {aspect_2_details}

    Next, I'd like to introduce {cto_name}, who will provide an update on our technology strategy and roadmap.

    {cto_name}:
    Thank you, {cfo_name}. We are committed to leading the way in cloud technology innovation. We are making significant investments in research and development to create cutting-edge solutions for our customers.

    {aspect_3_details}

    Now, I'll pass it over to {chief_product_officer_name} to discuss our product roadmap and recent launches.

    {chief_product_officer_name}:
    Thank you, {cto_name}. We recently launched {new_product}, a groundbreaking solution designed to revolutionize {industry_application}.

    {aspect_4_details}

    I'll now hand it over to {chief_marketing_officer_name} to provide an update on our marketing initiatives and brand strategy.

    {chief_marketing_officer_name}:
    Thank you, {chief_product_officer_name}. Our marketing efforts are focused on building brand awareness and driving demand for our innovative solutions.

    {aspect_5_details}

    Next, I'd like to introduce {chief_sales_officer_name}, who will discuss our sales performance and customer acquisition strategies.

    {chief_sales_officer_name}:
    Thank you, {chief_marketing_officer_name}. Our sales team has been instrumental in driving our strong growth in the {quarter}. We are focused on expanding our customer base and strengthening our existing relationships.

    {aspect_6_details}

    Now, I'll pass it over to {chief_security_officer_name} to discuss our security initiatives and commitment to data protection.

    {chief_security_officer_name}:
    Thank you, {chief_sales_officer_name}. Security is paramount to our mission. We are committed to protecting our customers' data and ensuring the integrity of our cloud platform.

    {aspect_7_details}

    Finally, I'd like to introduce {chief_innovation_officer_name}, who will share insights into our innovation strategy and future growth opportunities.

    {chief_innovation_officer_name}:
    Thank you, {chief_security_officer_name}. We are constantly exploring new technologies and business models to drive innovation and create value for our customers.

    {aspect_8_details}

    Back to {ceo_name}.

    {ceo_name}:
    Thank you, everyone. We are confident in our ability to continue to execute our strategy and deliver long-term sustainable growth.

    Operator:
    [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}:
    [Analyst Question 1]

    {ceo_name}:
    [Answer to Analyst Question 1]

    Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}:
    [Analyst Question 2]

    {cfo_name}:
    [Answer to Analyst Question 2]

    Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    {analyst_3_name}:
    [Analyst Question 3]

    {chief_innovation_officer_name}:
    [Answer to Analyst Question 3]

    Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

    {analyst_4_name}:
    [Analyst Question 4]

    {cto_name}:
    [Answer to Analyst Question 4]

    {ceo_name}:
    Thank you for your thoughtful questions and your continued interest in {company_name}.

    {ir_name}:
    Thank you for joining us today. This concludes the call.

    Operator:
    This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """,
    ),
])