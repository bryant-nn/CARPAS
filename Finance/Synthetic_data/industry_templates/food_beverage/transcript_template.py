from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
**{company_name} - {quarter} Earnings Call Transcript**

**Operator:**
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

**{ir_name} ({ir_title}):**
Thank you, operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results.  Joining me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and {chief_growth_officer_name}, Chief Growth Officer.

Before we begin, I would like to remind you that this call may contain forward-looking statements.  Please refer to our SEC filings for a discussion of the factors that could cause actual results to differ materially from these statements.

With that, I'll turn the call over to {ceo_name}.

**{ceo_name} (CEO):**
Thank you, {ir_name}, and good morning, everyone.  We are pleased to report our results for {quarter}.  We delivered strong performance despite ongoing macroeconomic headwinds and inflationary pressures.

Today, I'll be focusing on four key areas: {aspect_1}, {aspect_2}, {aspect_3}, and {aspect_4}.

First, regarding {aspect_1}: {aspect_1_details}

Second, concerning {aspect_2}: {aspect_2_details}

Third, in terms of {aspect_3}: {aspect_3_details}

Finally, looking at {aspect_4}: {aspect_4_details}

Overall, we are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

Now, I'll turn the call over to {cfo_name} to provide more detail on our financial results.

**{cfo_name} (CFO):**
Thank you, {ceo_name}.  As {ceo_name} mentioned, we achieved solid results in {quarter}.  Net sales were {net_sales}, representing a {sales_growth_percentage}% increase year-over-year.  Gross margin was {gross_margin}%, impacted by {gross_margin_impact}.  Operating income was {operating_income}, and earnings per share were {eps}. We are managing our costs effectively and continue to invest in key growth initiatives.

Our balance sheet remains strong with {cash_position} in cash and marketable securities. We are committed to returning value to shareholders through dividends and share repurchases.

For the full year, we are reaffirming our guidance for {full_year_guidance}.

Now, let's open the call for questions.

**Operator:**
[Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please proceed.

**{analyst_1_name} ({analyst_1_firm}):**
Good morning.  Can you provide more color on the impact of {inflation_impact} on your business?

**{ceo_name} (CEO):**
{ceo_response_to_analyst_1}

**Operator:**
Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please proceed.

**{analyst_2_name} ({analyst_2_firm}):**
What are your plans for {new_product} and what is the expected {impact_of_product}?

**{chief_growth_officer_name} (Chief Growth Officer):**
{chief_growth_officer_response_to_analyst_2}

**Operator:**
Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please proceed.

**{analyst_3_name} ({analyst_3_firm}):**
How are you managing supply chain disruptions?

**{chief_supply_chain_officer_name} (Chief Supply Chain Officer):**
{chief_supply_chain_officer_response_to_analyst_3}

**Operator:**
Our last question comes from {analyst_4_name} with {analyst_4_firm}. Please proceed.

**{analyst_4_name} ({analyst_4_firm}):**
What is your outlook for the rest of the year?

**{cfo_name} (CFO):**
{cfo_response_to_analyst_4}

**Operator:**
I would now like to turn the call back over to {ceo_name} for closing remarks.

**{ceo_name} (CEO):**
Thank you for your questions and your continued interest in {company_name}. We are focused on executing our strategy and delivering strong results. We look forward to updating you on our progress next quarter.

**Operator:**
This concludes today's conference call. Thank you for your participation. You may now disconnect.
""",
    ),
    ("5", """
**{company_name} - {quarter} Earnings Call Transcript**

**Operator:**
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

**{ir_name} ({ir_title}):**
Thank you, operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results.  Joining me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_growth_officer_name}, Chief Growth Officer; and {chief_supply_chain_officer_name}, Chief Supply Chain Officer.

Before we begin, I would like to remind you that this call may contain forward-looking statements.  Please refer to our SEC filings for a discussion of the factors that could cause actual results to differ materially from these statements.

With that, I'll turn the call over to {ceo_name}.

**{ceo_name} (CEO):**
Thank you, {ir_name}, and good morning, everyone.  We are pleased to report our results for {quarter}.  We delivered strong performance despite ongoing macroeconomic headwinds and inflationary pressures.

Today, I'll be focusing on five key areas: {aspect_1}, {aspect_2}, {aspect_3}, {aspect_4}, and {aspect_5}.

First, regarding {aspect_1}: {aspect_1_details}

Second, concerning {aspect_2}: {aspect_2_details}

Third, in terms of {aspect_3}: {aspect_3_details}

Fourth, looking at {aspect_4}: {aspect_4_details}

Finally, reviewing {aspect_5}: {aspect_5_details}

Overall, we are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

Now, I'll turn the call over to {cfo_name} to provide more detail on our financial results.

**{cfo_name} (CFO):**
Thank you, {ceo_name}.  As {ceo_name} mentioned, we achieved solid results in {quarter}.  Net sales were {net_sales}, representing a {sales_growth_percentage}% increase year-over-year.  Gross margin was {gross_margin}%, impacted by {gross_margin_impact}.  Operating income was {operating_income}, and earnings per share were {eps}. We are managing our costs effectively and continue to invest in key growth initiatives.

Our balance sheet remains strong with {cash_position} in cash and marketable securities. We are committed to returning value to shareholders through dividends and share repurchases.

For the full year, we are reaffirming our guidance for {full_year_guidance}.

Now, let's open the call for questions.

**Operator:**
[Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please proceed.

**{analyst_1_name} ({analyst_1_firm}):**
Good morning.  Can you provide more color on the impact of {inflation_impact} on your business?

**{ceo_name} (CEO):**
{ceo_response_to_analyst_1}

**Operator:**
Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please proceed.

**{analyst_2_name} ({analyst_2_firm}):**
What are your plans for {new_product} and what is the expected {impact_of_product}?

**{chief_growth_officer_name} (Chief Growth Officer):**
{chief_growth_officer_response_to_analyst_2}

**Operator:**
Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please proceed.

**{analyst_3_name} ({analyst_3_firm}):**
How are you managing supply chain disruptions?

**{chief_supply_chain_officer_name} (Chief Supply Chain Officer):**
{chief_supply_chain_officer_response_to_analyst_3}

**Operator:**
Our last question comes from {analyst_4_name} with {analyst_4_firm}. Please proceed.

**{analyst_4_name} ({analyst_4_firm}):**
What is your outlook for the rest of the year?

**{cfo_name} (CFO):**
{cfo_response_to_analyst_4}

**Operator:**
I would now like to turn the call back over to {ceo_name} for closing remarks.

**{ceo_name} (CEO):**
Thank you for your questions and your continued interest in {company_name}. We are focused on executing our strategy and delivering strong results. We look forward to updating you on our progress next quarter.

**Operator:**
This concludes today's conference call. Thank you for your participation. You may now disconnect.
""",
    ),
    ("6", """
**{company_name} - {quarter} Earnings Call Transcript**

**Operator:**
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

**{ir_name} ({ir_title}):**
Thank you, operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results.  Joining me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_growth_officer_name}, Chief Growth Officer; and {chief_supply_chain_officer_name}, Chief Supply Chain Officer.

Before we begin, I would like to remind you that this call may contain forward-looking statements.  Please refer to our SEC filings for a discussion of the factors that could cause actual results to differ materially from these statements.

With that, I'll turn the call over to {ceo_name}.

**{ceo_name} (CEO):**
Thank you, {ir_name}, and good morning, everyone.  We are pleased to report our results for {quarter}.  We delivered strong performance despite ongoing macroeconomic headwinds and inflationary pressures.

Today, I'll be focusing on six key areas: {aspect_1}, {aspect_2}, {aspect_3}, {aspect_4}, {aspect_5}, and {aspect_6}.

First, regarding {aspect_1}: {aspect_1_details}

Second, concerning {aspect_2}: {aspect_2_details}

Third, in terms of {aspect_3}: {aspect_3_details}

Fourth, looking at {aspect_4}: {aspect_4_details}

Fifth, reviewing {aspect_5}: {aspect_5_details}

Sixth, analyzing {aspect_6}: {aspect_6_details}

Overall, we are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

Now, I'll turn the call over to {cfo_name} to provide more detail on our financial results.

**{cfo_name} (CFO):**
Thank you, {ceo_name}.  As {ceo_name} mentioned, we achieved solid results in {quarter}.  Net sales were {net_sales}, representing a {sales_growth_percentage}% increase year-over-year.  Gross margin was {gross_margin}%, impacted by {gross_margin_impact}.  Operating income was {operating_income}, and earnings per share were {eps}. We are managing our costs effectively and continue to invest in key growth initiatives.

Our balance sheet remains strong with {cash_position} in cash and marketable securities. We are committed to returning value to shareholders through dividends and share repurchases.

For the full year, we are reaffirming our guidance for {full_year_guidance}.

Now, let's open the call for questions.

**Operator:**
[Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please proceed.

**{analyst_1_name} ({analyst_1_firm}):**
Good morning.  Can you provide more color on the impact of {inflation_impact} on your business?

**{ceo_name} (CEO):**
{ceo_response_to_analyst_1}

**Operator:**
Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please proceed.

**{analyst_2_name} ({analyst_2_firm}):**
What are your plans for {new_product} and what is the expected {impact_of_product}?

**{chief_growth_officer_name} (Chief Growth Officer):**
{chief_growth_officer_response_to_analyst_2}

**Operator:**
Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please proceed.

**{analyst_3_name} ({analyst_3_firm}):**
How are you managing supply chain disruptions?

**{chief_supply_chain_officer_name} (Chief Supply Chain Officer):**
{chief_supply_chain_officer_response_to_analyst_3}

**Operator:**
Our last question comes from {analyst_4_name} with {analyst_4_firm}. Please proceed.

**{analyst_4_name} ({analyst_4_firm}):**
What is your outlook for the rest of the year?

**{cfo_name} (CFO):**
{cfo_response_to_analyst_4}

**Operator:**
I would now like to turn the call back over to {ceo_name} for closing remarks.

**{ceo_name} (CEO):**
Thank you for your questions and your continued interest in {company_name}. We are focused on executing our strategy and delivering strong results. We look forward to updating you on our progress next quarter.

**Operator:**
This concludes today's conference call. Thank you for your participation. You may now disconnect.
""",
    ),
    ("7", """
**{company_name} - {quarter} Earnings Call Transcript**

**Operator:**
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

**{ir_name} ({ir_title}):**
Thank you, operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results.  Joining me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_growth_officer_name}, Chief Growth Officer; and {chief_supply_chain_officer_name}, Chief Supply Chain Officer.

Before we begin, I would like to remind you that this call may contain forward-looking statements.  Please refer to our SEC filings for a discussion of the factors that could cause actual results to differ materially from these statements.

With that, I'll turn the call over to {ceo_name}.

**{ceo_name} (CEO):**
Thank you, {ir_name}, and good morning, everyone.  We are pleased to report our results for {quarter}.  We delivered strong performance despite ongoing macroeconomic headwinds and inflationary pressures.

Today, I'll be focusing on seven key areas: {aspect_1}, {aspect_2}, {aspect_3}, {aspect_4}, {aspect_5}, {aspect_6}, and {aspect_7}.

First, regarding {aspect_1}: {aspect_1_details}

Second, concerning {aspect_2}: {aspect_2_details}

Third, in terms of {aspect_3}: {aspect_3_details}

Fourth, looking at {aspect_4}: {aspect_4_details}

Fifth, reviewing {aspect_5}: {aspect_5_details}

Sixth, analyzing {aspect_6}: {aspect_6_details}

Seventh, examining {aspect_7}: {aspect_7_details}

Overall, we are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

Now, I'll turn the call over to {cfo_name} to provide more detail on our financial results.

**{cfo_name} (CFO):**
Thank you, {ceo_name}.  As {ceo_name} mentioned, we achieved solid results in {quarter}.  Net sales were {net_sales}, representing a {sales_growth_percentage}% increase year-over-year.  Gross margin was {gross_margin}%, impacted by {gross_margin_impact}.  Operating income was {operating_income}, and earnings per share were {eps}. We are managing our costs effectively and continue to invest in key growth initiatives.

Our balance sheet remains strong with {cash_position} in cash and marketable securities. We are committed to returning value to shareholders through dividends and share repurchases.

For the full year, we are reaffirming our guidance for {full_year_guidance}.

Now, let's open the call for questions.

**Operator:**
[Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please proceed.

**{analyst_1_name} ({analyst_1_firm}):**
Good morning.  Can you provide more color on the impact of {inflation_impact} on your business?

**{ceo_name} (CEO):**
{ceo_response_to_analyst_1}

**Operator:**
Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please proceed.

**{analyst_2_name} ({analyst_2_firm}):**
What are your plans for {new_product} and what is the expected {impact_of_product}?

**{chief_growth_officer_name} (Chief Growth Officer):**
{chief_growth_officer_response_to_analyst_2}

**Operator:**
Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please proceed.

**{analyst_3_name} ({analyst_3_firm}):**
How are you managing supply chain disruptions?

**{chief_supply_chain_officer_name} (Chief Supply Chain Officer):**
{chief_supply_chain_officer_response_to_analyst_3}

**Operator:**
Our last question comes from {analyst_4_name} with {analyst_4_firm}. Please proceed.

**{analyst_4_name} ({analyst_4_firm}):**
What is your outlook for the rest of the year?

**{cfo_name} (CFO):**
{cfo_response_to_analyst_4}

**Operator:**
I would now like to turn the call back over to {ceo_name} for closing remarks.

**{ceo_name} (CEO):**
Thank you for your questions and your continued interest in {company_name}. We are focused on executing our strategy and delivering strong results. We look forward to updating you on our progress next quarter.

**Operator:**
This concludes today's conference call. Thank you for your participation. You may now disconnect.
""",
    ),
    ("8", """
**{company_name} - {quarter} Earnings Call Transcript**

**Operator:**
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in a listen-only mode. After the speakers' presentation, there will be a question-and-answer session. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

**{ir_name} ({ir_title}):**
Thank you, operator. Good morning, everyone, and thank you for joining us today to discuss {company_name}'s {quarter} results.  Joining me on the call are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {chief_growth_officer_name}, Chief Growth Officer; and {chief_supply_chain_officer_name}, Chief Supply Chain Officer.

Before we begin, I would like to remind you that this call may contain forward-looking statements.  Please refer to our SEC filings for a discussion of the factors that could cause actual results to differ materially from these statements.

With that, I'll turn the call over to {ceo_name}.

**{ceo_name} (CEO):**
Thank you, {ir_name}, and good morning, everyone.  We are pleased to report our results for {quarter}.  We delivered strong performance despite ongoing macroeconomic headwinds and inflationary pressures.

Today, I'll be focusing on eight key areas: {aspect_1}, {aspect_2}, {aspect_3}, {aspect_4}, {aspect_5}, {aspect_6}, {aspect_7}, and {aspect_8}.

First, regarding {aspect_1}: {aspect_1_details}

Second, concerning {aspect_2}: {aspect_2_details}

Third, in terms of {aspect_3}: {aspect_3_details}

Fourth, looking at {aspect_4}: {aspect_4_details}

Fifth, reviewing {aspect_5}: {aspect_5_details}

Sixth, analyzing {aspect_6}: {aspect_6_details}

Seventh, examining {aspect_7}: {aspect_7_details}

Eighth, considering {aspect_8}: {aspect_8_details}

Overall, we are confident in our ability to navigate the current environment and deliver long-term value for our shareholders.

Now, I'll turn the call over to {cfo_name} to provide more detail on our financial results.

**{cfo_name} (CFO):**
Thank you, {ceo_name}.  As {ceo_name} mentioned, we achieved solid results in {quarter}.  Net sales were {net_sales}, representing a {sales_growth_percentage}% increase year-over-year.  Gross margin was {gross_margin}%, impacted by {gross_margin_impact}.  Operating income was {operating_income}, and earnings per share were {eps}. We are managing our costs effectively and continue to invest in key growth initiatives.

Our balance sheet remains strong with {cash_position} in cash and marketable securities. We are committed to returning value to shareholders through dividends and share repurchases.

For the full year, we are reaffirming our guidance for {full_year_guidance}.

Now, let's open the call for questions.

**Operator:**
[Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}. Please proceed.

**{analyst_1_name} ({analyst_1_firm}):**
Good morning.  Can you provide more color on the impact of {inflation_impact} on your business?

**{ceo_name} (CEO):**
{ceo_response_to_analyst_1}

**Operator:**
Our next question comes from {analyst_2_name} with {analyst_2_firm}. Please proceed.

**{analyst_2_name} ({analyst_2_firm}):**
What are your plans for {new_product} and what is the expected {impact_of_product}?

**{chief_growth_officer_name} (Chief Growth Officer):**
{chief_growth_officer_response_to_analyst_2}

**Operator:**
Our next question comes from {analyst_3_name} with {analyst_3_firm}. Please proceed.

**{analyst_3_name} ({analyst_3_firm}):**
How are you managing supply chain disruptions?

**{chief_supply_chain_officer_name} (Chief Supply Chain Officer):**
{chief_supply_chain_officer_response_to_analyst_3}

**Operator:**
Our last question comes from {analyst_4_name} with {analyst_4_firm}. Please proceed.

**{analyst_4_name} ({analyst_4_firm}):**
What is your outlook for the rest of the year?

**{cfo_name} (CFO):**
{cfo_response_to_analyst_4}

**Operator:**
I would now like to turn the call back over to {ceo_name} for closing remarks.

**{ceo_name} (CEO):**
Thank you for your questions and your continued interest in {company_name}. We are focused on executing our strategy and delivering strong results. We look forward to updating you on our progress next quarter.

**Operator:**
This concludes today's conference call. Thank you for your participation. You may now disconnect.
""",
    ),
])