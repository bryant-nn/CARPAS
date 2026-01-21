from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
    Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and {coo_name}, Chief Operating Officer.

    Before we begin, I'd like to remind you that this call contains forward-looking statements. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

{ceo_name}:
    Thank you, {ir_name}, and good morning. {company_name} delivered a solid performance in {quarter}, demonstrating the resilience of our business model and the strength of our diversified portfolio.  Our priorities remain focused on executing our strategy, driving operational excellence, and delivering value to our shareholders. I will cover the following areas:

    1. {aspect_1_title}: {aspect_1_details}
    2. {aspect_2_title}: {aspect_2_details}
    3. {aspect_3_title}: {aspect_3_details}
    4. {aspect_4_title}: {aspect_4_details}

    We are particularly excited about the recent advancements in our {new_product} program and its potential {impact_of_product} to our future growth. We are seeing strong demand for our defense systems, and our commercial aerospace business is recovering steadily.

{cfo_name}:
    Thank you, {ceo_name}. Now, let's turn to the financials. In {quarter}, we reported revenue of {revenue}, representing a {revenue_growth} increase year-over-year. Our earnings per share were {eps}. We continue to maintain a strong balance sheet with {cash_on_hand} in cash and equivalents.  Our guidance for the full year remains unchanged. We are actively managing our costs and investing in key growth initiatives. We are also focused on returning capital to shareholders through dividends and share repurchases.

    Our specific financial highlights include:
    * Gross Margin: {gross_margin}
    * Operating Income: {operating_income}
    * Free Cash Flow: {free_cash_flow}

Operator:
    Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}:
    Good morning. Can you provide more color on the {analyst_1_question}?

{ceo_name}:
    Certainly, {analyst_1_name}. {ceo_answer_1}

Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}:
    Hi, I'm curious about {analyst_2_question}?

{cfo_name}:
    {analyst_2_name}, {cfo_answer_2}

Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}:
    Regarding the {analyst_3_question}?

{ceo_name}:
    {analyst_3_name}, {ceo_answer_3}

{ceo_name}:
    Thank you for your questions. In closing, I'm confident in our ability to navigate the current environment and deliver long-term value to our shareholders. We remain focused on our strategic priorities, operational excellence, and innovation.

{ir_name}:
    Thank you for joining us today. This concludes our earnings call.

Operator:
    This concludes today's conference call. Thank you for participating. You may now disconnect.
    """,
    ),
    ("5", """
Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
    Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; and {cto_name}, Chief Technology Officer.

    Before we begin, I'd like to remind you that this call contains forward-looking statements. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

{ceo_name}:
    Thank you, {ir_name}, and good morning. {company_name} delivered a solid performance in {quarter}, demonstrating the resilience of our business model and the strength of our diversified portfolio. Our priorities remain focused on executing our strategy, driving operational excellence, and delivering value to our shareholders. I will cover the following areas:

    1. {aspect_1_title}: {aspect_1_details}
    2. {aspect_2_title}: {aspect_2_details}
    3. {aspect_3_title}: {aspect_3_details}
    4. {aspect_4_title}: {aspect_4_details}
    5. {aspect_5_title}: {aspect_5_details}

    We are particularly excited about the recent advancements in our {new_product} program and its potential {impact_of_product} to our future growth. We are seeing strong demand for our defense systems, and our commercial aerospace business is recovering steadily.

{cfo_name}:
    Thank you, {ceo_name}. Now, let's turn to the financials. In {quarter}, we reported revenue of {revenue}, representing a {revenue_growth} increase year-over-year. Our earnings per share were {eps}. We continue to maintain a strong balance sheet with {cash_on_hand} in cash and equivalents. Our guidance for the full year remains unchanged. We are actively managing our costs and investing in key growth initiatives. We are also focused on returning capital to shareholders through dividends and share repurchases.

    Our specific financial highlights include:
    * Gross Margin: {gross_margin}
    * Operating Income: {operating_income}
    * Free Cash Flow: {free_cash_flow}

{coo_name}:
    Thank you, {cfo_name}. Operationally, we have seen significant improvements in our supply chain management, allowing us to increase production rates on key programs. We are also investing in automation and digital technologies to improve efficiency and reduce costs. Specifically, {operational_details}.

Operator:
    Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}:
    Good morning. Can you provide more color on the {analyst_1_question}?

{ceo_name}:
    Certainly, {analyst_1_name}. {ceo_answer_1}

Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}:
    Hi, I'm curious about {analyst_2_question}?

{cfo_name}:
    {analyst_2_name}, {cfo_answer_2}

Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}:
    Regarding the {analyst_3_question}?

{cto_name}:
    {analyst_3_name}, {cto_answer_3}

{ceo_name}:
    Thank you for your questions. In closing, I'm confident in our ability to navigate the current environment and deliver long-term value to our shareholders. We remain focused on our strategic priorities, operational excellence, and innovation.

{ir_name}:
    Thank you for joining us today. This concludes our earnings call.

Operator:
    This concludes today's conference call. Thank you for participating. You may now disconnect.
    """,
    ),
    ("6", """
Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
    Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; {cto_name}, Chief Technology Officer; and {chief_strategy_officer_name}, Chief Strategy Officer.

    Before we begin, I'd like to remind you that this call contains forward-looking statements. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

{ceo_name}:
    Thank you, {ir_name}, and good morning. {company_name} delivered a solid performance in {quarter}, demonstrating the resilience of our business model and the strength of our diversified portfolio. Our priorities remain focused on executing our strategy, driving operational excellence, and delivering value to our shareholders. I will cover the following areas:

    1. {aspect_1_title}: {aspect_1_details}
    2. {aspect_2_title}: {aspect_2_details}
    3. {aspect_3_title}: {aspect_3_details}
    4. {aspect_4_title}: {aspect_4_details}
    5. {aspect_5_title}: {aspect_5_details}
    6. {aspect_6_title}: {aspect_6_details}

    We are particularly excited about the recent advancements in our {new_product} program and its potential {impact_of_product} to our future growth. We are seeing strong demand for our defense systems, and our commercial aerospace business is recovering steadily.

{cfo_name}:
    Thank you, {ceo_name}. Now, let's turn to the financials. In {quarter}, we reported revenue of {revenue}, representing a {revenue_growth} increase year-over-year. Our earnings per share were {eps}. We continue to maintain a strong balance sheet with {cash_on_hand} in cash and equivalents. Our guidance for the full year remains unchanged. We are actively managing our costs and investing in key growth initiatives. We are also focused on returning capital to shareholders through dividends and share repurchases.

    Our specific financial highlights include:
    * Gross Margin: {gross_margin}
    * Operating Income: {operating_income}
    * Free Cash Flow: {free_cash_flow}

{coo_name}:
    Thank you, {cfo_name}. Operationally, we have seen significant improvements in our supply chain management, allowing us to increase production rates on key programs. We are also investing in automation and digital technologies to improve efficiency and reduce costs. Specifically, {operational_details}.

{cto_name}:
    Thank you, {coo_name}. On the technology front, we're making significant strides in our next-generation propulsion systems. We anticipate these advancements will give us a competitive edge in the years to come. More specifically, {technology_details}.

Operator:
    Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}:
    Good morning. Can you provide more color on the {analyst_1_question}?

{ceo_name}:
    Certainly, {analyst_1_name}. {ceo_answer_1}

Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}:
    Hi, I'm curious about {analyst_2_question}?

{cfo_name}:
    {analyst_2_name}, {cfo_answer_2}

Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}:
    Regarding the {analyst_3_question}?

{cto_name}:
    {analyst_3_name}, {cto_answer_3}

{ceo_name}:
    Thank you for your questions. In closing, I'm confident in our ability to navigate the current environment and deliver long-term value to our shareholders. We remain focused on our strategic priorities, operational excellence, and innovation.

{ir_name}:
    Thank you for joining us today. This concludes our earnings call.

Operator:
    This concludes today's conference call. Thank you for participating. You may now disconnect.
    """,
    ),
    ("7", """
Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
    Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; {cto_name}, Chief Technology Officer; {chief_strategy_officer_name}, Chief Strategy Officer; and {chief_marketing_officer_name}, Chief Marketing Officer.

    Before we begin, I'd like to remind you that this call contains forward-looking statements. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

{ceo_name}:
    Thank you, {ir_name}, and good morning. {company_name} delivered a solid performance in {quarter}, demonstrating the resilience of our business model and the strength of our diversified portfolio. Our priorities remain focused on executing our strategy, driving operational excellence, and delivering value to our shareholders. I will cover the following areas:

    1. {aspect_1_title}: {aspect_1_details}
    2. {aspect_2_title}: {aspect_2_details}
    3. {aspect_3_title}: {aspect_3_details}
    4. {aspect_4_title}: {aspect_4_details}
    5. {aspect_5_title}: {aspect_5_details}
    6. {aspect_6_title}: {aspect_6_details}
    7. {aspect_7_title}: {aspect_7_details}

    We are particularly excited about the recent advancements in our {new_product} program and its potential {impact_of_product} to our future growth. We are seeing strong demand for our defense systems, and our commercial aerospace business is recovering steadily.

{cfo_name}:
    Thank you, {ceo_name}. Now, let's turn to the financials. In {quarter}, we reported revenue of {revenue}, representing a {revenue_growth} increase year-over-year. Our earnings per share were {eps}. We continue to maintain a strong balance sheet with {cash_on_hand} in cash and equivalents. Our guidance for the full year remains unchanged. We are actively managing our costs and investing in key growth initiatives. We are also focused on returning capital to shareholders through dividends and share repurchases.

    Our specific financial highlights include:
    * Gross Margin: {gross_margin}
    * Operating Income: {operating_income}
    * Free Cash Flow: {free_cash_flow}

{coo_name}:
    Thank you, {cfo_name}. Operationally, we have seen significant improvements in our supply chain management, allowing us to increase production rates on key programs. We are also investing in automation and digital technologies to improve efficiency and reduce costs. Specifically, {operational_details}.

{cto_name}:
    Thank you, {coo_name}. On the technology front, we're making significant strides in our next-generation propulsion systems. We anticipate these advancements will give us a competitive edge in the years to come. More specifically, {technology_details}.

{chief_strategy_officer_name}:
    Thank you, {cto_name}. From a strategic perspective, we are actively evaluating potential acquisitions that would complement our existing portfolio and expand our market reach. We are also focused on developing new business models that will allow us to capture emerging opportunities. For instance, {strategy_details}.

Operator:
    Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}:
    Good morning. Can you provide more color on the {analyst_1_question}?

{ceo_name}:
    Certainly, {analyst_1_name}. {ceo_answer_1}

Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}:
    Hi, I'm curious about {analyst_2_question}?

{cfo_name}:
    {analyst_2_name}, {cfo_answer_2}

Operator:
    Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}:
    Regarding the {analyst_3_question}?

{cto_name}:
    {analyst_3_name}, {cto_answer_3}

{ceo_name}:
    Thank you for your questions. In closing, I'm confident in our ability to navigate the current environment and deliver long-term value to our shareholders. We remain focused on our strategic priorities, operational excellence, and innovation.

{ir_name}:
    Thank you for joining us today. This concludes our earnings call.

Operator:
    This concludes today's conference call. Thank you for participating. You may now disconnect.
    """,
    ),
    ("8", """
Operator:
    Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] Please note this event is being recorded.

    I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
    Thank you, Operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Conference Call. Joining me today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; {cto_name}, Chief Technology Officer; {chief_strategy_officer_name}, Chief Strategy Officer; {chief_marketing_officer_name}, Chief Marketing Officer; and {chief_compliance_officer_name}, Chief Compliance Officer.

    Before we begin, I'd like to remind you that this call contains forward-looking statements. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

{ceo_name}:
    Thank you, {ir_name}, and good morning. {company_name} delivered a solid performance in {quarter}, demonstrating the resilience of our business model and the strength of our diversified portfolio. Our priorities remain focused on executing our strategy, driving operational excellence, and delivering value to our shareholders. I will cover the following areas:

    1. {aspect_1_title}: {aspect_1_details}
    2. {aspect_2_title}: {aspect_2_details}
    3. {aspect_3_title}: {aspect_3_details}
    4. {aspect_4_title}: {aspect_4_details}
    5. {aspect_5_title}: {aspect_5_details}
    6. {aspect_6_title}: {aspect_6_details}
    7. {aspect_7_title}: {aspect_7_details}
    8. {aspect_8_title}: {aspect_8_details}

    We are particularly excited about the recent advancements in our {new_product} program and its potential {impact_of_product} to our future growth. We are seeing strong demand for our defense systems, and our commercial aerospace business is recovering steadily.

{cfo_name}:
    Thank you, {ceo_name}. Now, let's turn to the financials. In {quarter}, we reported revenue of {revenue}, representing a {revenue_growth} increase year-over-year. Our earnings per share were {eps}. We continue to maintain a strong balance sheet with {cash_on_hand} in cash and equivalents. Our guidance for the full year remains unchanged. We are actively managing our costs and investing in key growth initiatives. We are also focused on returning capital to shareholders through dividends and share repurchases.

    Our specific financial highlights include:
    * Gross Margin: {gross_margin}
    * Operating Income: {operating_income}
    * Free Cash Flow: {free_cash_flow}

{coo_name}:
    Thank you, {cfo_name}. Operationally, we have seen significant improvements in our supply chain management, allowing us to increase production rates on key programs. We are also investing in automation and digital technologies to improve efficiency and reduce costs. Specifically, {operational_details}.

{cto_name}:
    Thank you, {coo_name}. On the technology front, we're making significant strides in our next-generation propulsion systems. We anticipate these advancements will give us a competitive edge in the years to come. More specifically, {technology_details}.

{chief_strategy_officer_name}:
    Thank you, {cto_name}. From a strategic perspective, we are actively evaluating potential acquisitions that would complement our existing portfolio and expand our market reach. We are also focused on developing new business models that will allow us to capture emerging opportunities. For instance, {strategy_details}.

{chief_marketing_officer_name}:
    Thank you, {chief_strategy_officer_name}. From a marketing perspective, we are seeing great success with our new branding campaign, which is resonating well with our target audience. We are also leveraging digital channels to reach new customers and increase brand awareness. The results are {marketing_details}.

Operator:
    Thank you. We will now begin the question and answer session. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please go ahead.

{analyst_1_name}:
    Good morning. Can you provide more color on the {analyst_1_question}?

{ceo_name}:
    Certainly, {analyst_1_name}. {ceo_answer_1}

Operator:
    Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please go ahead.

{analyst_2_name}:
    Hi, I'm curious about {analyst_2_question}?

{cfo_name}:
    {analyst_2_name}, {cfo_answer_2}

Operator:
     Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please go ahead.

{analyst_3_name}:
    Regarding the {analyst_3_question}?

{cto_name}:
    {analyst_3_name}, {cto_answer_3}

Operator:
    Our next question comes from {analyst_4_name} with {analyst_4_firm}. Please go ahead.

{analyst_4_name}:
    Question about {analyst_4_question}?

{chief_strategy_officer_name}:
    {analyst_4_name}, {chief_strategy_officer_answer_4}.

{ceo_name}:
    Thank you for your questions. In closing, I'm confident in our ability to navigate the current environment and deliver long-term value to our shareholders. We remain focused on our strategic priorities, operational excellence, and innovation.

{ir_name}:
    Thank you for joining us today. This concludes our earnings call.

Operator:
    This concludes today's conference call. Thank you for participating. You may now disconnect.
    """,
    ),
])