from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
    Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cuo_name}, Chief Underwriting Officer.

    Before we begin, I would like to remind you that some of the statements we are making today may be considered forward-looking. These statements are subject to certain risks and uncertainties that could cause our actual results to differ materially from those projected. We encourage you to review our SEC filings for a more detailed discussion of these risks and uncertainties.

    I will now turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. I'm pleased to report on {company_name}'s performance for {quarter}. We delivered strong results, driven by {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, and {aspect_4_details}. 

    {cfo_name}, our CFO, will now provide a more detailed review of our financial performance.

    {cfo_name}: Thank you, {ceo_name}. Good morning, everyone. As {ceo_name} mentioned, we had a solid quarter. Our net income was {net_income}, or {eps} per share. Key drivers of our financial performance included {financial_driver_1}, {financial_driver_2}. Our combined ratio was {combined_ratio}, reflecting effective underwriting and claims management. We continue to maintain a strong capital position, with {capital_level}.

    Operator, we are now ready to open the line for questions.

    Operator: Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}: Good morning. Can you provide more color on {analyst_1_question}?

    {ceo_name}: {analyst_1_answer}

    Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}: Good morning. Could you discuss the impact of {market_condition} on your business?

    {cfo_name}: {analyst_2_answer}

    Operator: [Potentially more questions]

    {ceo_name}: Thank you for your questions and your interest in {company_name}. In closing, we are confident in our ability to continue delivering strong results and creating value for our shareholders. Thank you for joining us today.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("5", """
    Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cuo_name}, Chief Underwriting Officer; and {cio_name}, Chief Investment Officer.

    Before we begin, I would like to remind you that some of the statements we are making today may be considered forward-looking. These statements are subject to certain risks and uncertainties that could cause our actual results to differ materially from those projected. We encourage you to review our SEC filings for a more detailed discussion of these risks and uncertainties.

    I will now turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. I'm pleased to report on {company_name}'s performance for {quarter}. We delivered strong results, driven by {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, and {aspect_5_details}. Our focus on {strategic_initiative} continues to yield positive outcomes.

    {cfo_name}, our CFO, will now provide a more detailed review of our financial performance.

    {cfo_name}: Thank you, {ceo_name}. Good morning, everyone. As {ceo_name} mentioned, we had a solid quarter. Our net income was {net_income}, or {eps} per share. Key drivers of our financial performance included {financial_driver_1}, {financial_driver_2}, and {financial_driver_3}. Our combined ratio was {combined_ratio}, reflecting effective underwriting and claims management. Investment income for the quarter was {investment_income}. We continue to maintain a strong capital position, with {capital_level}.

    {cuo_name}: Thank you, {cfo_name}. I'd like to provide an update on our underwriting performance. We've seen continued strong performance in our {line_of_business} line. We are actively managing our exposure to {risk_exposure} and have implemented several initiatives to improve our risk selection.

    Operator, we are now ready to open the line for questions.

    Operator: Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}: Good morning. Can you provide more color on {analyst_1_question}?

    {ceo_name}: {analyst_1_answer}

    Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}: Good morning. Could you discuss the impact of {market_condition} on your business?

    {cfo_name}: {analyst_2_answer}

    Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    {analyst_3_name}: What is the expected impact of {regulatory_change} on your underwriting strategy?

    {cuo_name}: {analyst_3_answer}

    Operator: [Potentially more questions]

    {ceo_name}: Thank you for your questions and your interest in {company_name}. In closing, we are confident in our ability to continue delivering strong results and creating value for our shareholders. Thank you for joining us today.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("6", """
    Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cuo_name}, Chief Underwriting Officer; {cio_name}, Chief Investment Officer; and {coo_name}, Chief Operating Officer.

    Before we begin, I would like to remind you that some of the statements we are making today may be considered forward-looking. These statements are subject to certain risks and uncertainties that could cause our actual results to differ materially from those projected. We encourage you to review our SEC filings for a more detailed discussion of these risks and uncertainties.

    I will now turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. I'm pleased to report on {company_name}'s performance for {quarter}. We delivered strong results, driven by {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, {aspect_5_details}, and {aspect_6_details}. We are particularly excited about the initial success of our {new_product} and its {impact_of_product}.

    {cfo_name}, our CFO, will now provide a more detailed review of our financial performance.

    {cfo_name}: Thank you, {ceo_name}. Good morning, everyone. As {ceo_name} mentioned, we had a solid quarter. Our net income was {net_income}, or {eps} per share. Key drivers of our financial performance included {financial_driver_1}, {financial_driver_2}, {financial_driver_3}, and {financial_driver_4}. Our combined ratio was {combined_ratio}. Investment income for the quarter was {investment_income}, reflecting strong performance in our {investment_segment}. We continue to maintain a strong capital position, with {capital_level}.

    {cuo_name}: Thank you, {cfo_name}. I'd like to provide an update on our underwriting performance. We've seen continued strong performance in our {line_of_business} line. We are actively managing our exposure to {risk_exposure} and have implemented several initiatives to improve our risk selection, including {underwriting_initiative}.

    {cio_name}: Thank you. From an investment perspective, we have continued to focus on diversifying our portfolio and managing risk in the current market environment. We are seeing positive returns from our investments in {investment_type}.

    Operator, we are now ready to open the line for questions.

    Operator: Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}: Good morning. Can you provide more color on {analyst_1_question}?

    {ceo_name}: {analyst_1_answer}

    Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}: Good morning. Could you discuss the impact of {market_condition} on your business?

    {cfo_name}: {analyst_2_answer}

    Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    {analyst_3_name}: What is the expected impact of {regulatory_change} on your underwriting strategy?

    {cuo_name}: {analyst_3_answer}

    Operator: [Potentially more questions]

    {ceo_name}: Thank you for your questions and your interest in {company_name}. In closing, we are confident in our ability to continue delivering strong results and creating value for our shareholders. Thank you for joining us today.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("7", """
    Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cuo_name}, Chief Underwriting Officer; {cio_name}, Chief Investment Officer; {coo_name}, Chief Operating Officer; and {chief_claims_officer_name}, Chief Claims Officer.

    Before we begin, I would like to remind you that some of the statements we are making today may be considered forward-looking. These statements are subject to certain risks and uncertainties that could cause our actual results to differ materially from those projected. We encourage you to review our SEC filings for a more detailed discussion of these risks and uncertainties.

    I will now turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. I'm pleased to report on {company_name}'s performance for {quarter}. We delivered strong results, driven by {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, {aspect_5_details}, {aspect_6_details}, and {aspect_7_details}. We are making significant progress on our digital transformation initiatives.

    {cfo_name}, our CFO, will now provide a more detailed review of our financial performance.

    {cfo_name}: Thank you, {ceo_name}. Good morning, everyone. As {ceo_name} mentioned, we had a solid quarter. Our net income was {net_income}, or {eps} per share. Key drivers of our financial performance included {financial_driver_1}, {financial_driver_2}, {financial_driver_3}, {financial_driver_4}, and {financial_driver_5}. Our combined ratio was {combined_ratio}. Investment income for the quarter was {investment_income}. We continue to maintain a strong capital position, with {capital_level}. Our expense ratio also improved to {expense_ratio}.

    {cuo_name}: Thank you, {cfo_name}. I'd like to provide an update on our underwriting performance. We've seen continued strong performance in our {line_of_business} line. We are actively managing our exposure to {risk_exposure} and have implemented several initiatives to improve our risk selection, including {underwriting_initiative}.

    {cio_name}: Thank you. From an investment perspective, we have continued to focus on diversifying our portfolio and managing risk in the current market environment. We are seeing positive returns from our investments in {investment_type}.

    {chief_claims_officer_name}: I'd like to briefly address our claims performance. We've implemented several initiatives to streamline our claims process and improve customer satisfaction. We are seeing positive results in terms of reduced claims processing times.

    Operator, we are now ready to open the line for questions.

    Operator: Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}: Good morning. Can you provide more color on {analyst_1_question}?

    {ceo_name}: {analyst_1_answer}

    Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}: Good morning. Could you discuss the impact of {market_condition} on your business?

    {cfo_name}: {analyst_2_answer}

    Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    {analyst_3_name}: What is the expected impact of {regulatory_change} on your underwriting strategy?

    {cuo_name}: {analyst_3_answer}

    Operator: [Potentially more questions]

    {ceo_name}: Thank you for your questions and your interest in {company_name}. In closing, we are confident in our ability to continue delivering strong results and creating value for our shareholders. Thank you for joining us today.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("8", """
    Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

    {ir_name}: Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {cuo_name}, Chief Underwriting Officer; {cio_name}, Chief Investment Officer; {coo_name}, Chief Operating Officer; {chief_claims_officer_name}, Chief Claims Officer; and {chief_technology_officer_name}, Chief Technology Officer.

    Before we begin, I would like to remind you that some of the statements we are making today may be considered forward-looking. These statements are subject to certain risks and uncertainties that could cause our actual results to differ materially from those projected. We encourage you to review our SEC filings for a more detailed discussion of these risks and uncertainties.

    I will now turn the call over to {ceo_name}.

    {ceo_name}: Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. I'm pleased to report on {company_name}'s performance for {quarter}. We delivered strong results, driven by {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, {aspect_5_details}, {aspect_6_details}, {aspect_7_details}, and {aspect_8_details}. Our commitment to innovation and customer service continues to drive our success.

    {cfo_name}, our CFO, will now provide a more detailed review of our financial performance.

    {cfo_name}: Thank you, {ceo_name}. Good morning, everyone. As {ceo_name} mentioned, we had a solid quarter. Our net income was {net_income}, or {eps} per share. Key drivers of our financial performance included {financial_driver_1}, {financial_driver_2}, {financial_driver_3}, {financial_driver_4}, {financial_driver_5}, and {financial_driver_6}. Our combined ratio was {combined_ratio}. Investment income for the quarter was {investment_income}. We continue to maintain a strong capital position, with {capital_level}. Our expense ratio also improved to {expense_ratio}.

    {cuo_name}: Thank you, {cfo_name}. I'd like to provide an update on our underwriting performance. We've seen continued strong performance in our {line_of_business} line. We are actively managing our exposure to {risk_exposure} and have implemented several initiatives to improve our risk selection, including {underwriting_initiative} and {pricing_strategy}.

    {cio_name}: Thank you. From an investment perspective, we have continued to focus on diversifying our portfolio and managing risk in the current market environment. We are seeing positive returns from our investments in {investment_type}.

    {chief_claims_officer_name}: I'd like to briefly address our claims performance. We've implemented several initiatives to streamline our claims process and improve customer satisfaction. We are seeing positive results in terms of reduced claims processing times and improved claims resolution rates.

    {chief_technology_officer_name}: We are making significant investments in technology to enhance our operations and improve the customer experience. Our new {technology_platform} is expected to drive significant efficiencies and cost savings.

    Operator, we are now ready to open the line for questions.

    Operator: Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

    {analyst_1_name}: Good morning. Can you provide more color on {analyst_1_question}?

    {ceo_name}: {analyst_1_answer}

    Operator: Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

    {analyst_2_name}: Good morning. Could you discuss the impact of {market_condition} on your business?

    {cfo_name}: {analyst_2_answer}

    Operator: Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

    {analyst_3_name}: What is the expected impact of {regulatory_change} on your underwriting strategy?

    {cuo_name}: {analyst_3_answer}

    Operator: Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

    {analyst_4_name}: Can you elaborate on the expected benefits of the new technology platform?

    {chief_technology_officer_name}: {analyst_4_answer}

    Operator: [Potentially more questions]

    {ceo_name}: Thank you for your questions and your interest in {company_name}. In closing, we are confident in our ability to continue delivering strong results and creating value for our shareholders. Thank you for joining us today.

    Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """)
])