from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
Operator:
Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's call is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, Operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; and {cro_name}, Chief Revenue Officer.

Before we begin, I'd like to remind you that this call contains forward-looking statements. Actual results may differ materially. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good afternoon, everyone. I'm pleased to report on {company_name}'s performance for {quarter}. We achieved significant milestones this quarter, driven by strong demand for our {new_product} and continued execution of our strategic initiatives.

Our focus this quarter was on four key areas: {aspect_1}, {aspect_2}, {aspect_3}, and {aspect_4}.

{aspect_1_details}
{aspect_2_details}
{aspect_3_details}
{aspect_4_details}

We are confident in our ability to continue this momentum and deliver long-term value to our shareholders.

Now, I'll turn the call over to {cfo_name} to discuss the financials in more detail.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Revenue for the quarter was {revenue}, representing a {revenue_growth}% increase year-over-year. Our gross margin was {gross_margin}%, and operating income was {operating_income}.

We continue to invest in research and development to drive innovation and expand our product offerings. Our cash position remains strong, providing us with the flexibility to pursue strategic acquisitions and other growth opportunities.

We are updating our full-year guidance to reflect our strong performance in the first half of the year. We now expect revenue to be in the range of {rev_guidance_low} to {rev_guidance_high}.

Now, I'll turn the call back to the operator for Q&A.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}.

{analyst_1_name}:
Hi, good afternoon. Can you discuss the impact of {new_product} on your overall growth?

{ceo_name}:
{impact_of_product}

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_firm}.

{analyst_2_name}:
What are your plans for international expansion?

{cro_name}:
{international_expansion_plans}

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_firm}.

{analyst_3_name}:
How are you managing churn in the current economic environment?

{cfo_name}:
{churn_management_strategy}

Operator:
Thank you. I'm showing no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}:
Thank you for joining us today. We are pleased with our progress this quarter and remain committed to delivering strong results for our shareholders. We look forward to speaking with you again on our next earnings call.

Operator:
Thank you for your participation. You may now disconnect.
    """),
    ("5", """
Operator:
Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's call is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, Operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {cto_name}, CTO; and {cro_name}, Chief Revenue Officer.

Before we begin, I'd like to remind you that this call contains forward-looking statements. Actual results may differ materially. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good afternoon, everyone. I'm pleased to report on {company_name}'s performance for {quarter}. We achieved significant milestones this quarter, driven by strong demand for our {new_product} and continued execution of our strategic initiatives.

Our focus this quarter was on five key areas: {aspect_1}, {aspect_2}, {aspect_3}, {aspect_4}, and {aspect_5}.

{aspect_1_details}
{aspect_2_details}
{aspect_3_details}
{aspect_4_details}
{aspect_5_details}

We are confident in our ability to continue this momentum and deliver long-term value to our shareholders.

Now, I'll turn the call over to {cfo_name} to discuss the financials in more detail.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Revenue for the quarter was {revenue}, representing a {revenue_growth}% increase year-over-year. Our gross margin was {gross_margin}%, and operating income was {operating_income}.

We continue to invest in research and development to drive innovation and expand our product offerings. Our cash position remains strong, providing us with the flexibility to pursue strategic acquisitions and other growth opportunities.

We are updating our full-year guidance to reflect our strong performance in the first half of the year. We now expect revenue to be in the range of {rev_guidance_low} to {rev_guidance_high}.

Now, I'll turn the call over to {cto_name} for a technology update.

{cto_name}:
Thank you, {cfo_name}. This quarter, we made significant progress in advancing our AI capabilities and further integrating them into our core platform. We are seeing strong adoption of our new AI-powered features, which are driving increased user engagement and improved customer outcomes. We've also focused on enhancing our platform's security and scalability to meet the growing demands of our enterprise customers.

Now, I'll turn the call back to the operator for Q&A.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}.

{analyst_1_name}:
Hi, good afternoon. Can you discuss the impact of {new_product} on your overall growth, and what kind of attach rates are you seeing with it?

{cro_name}:
{impact_of_product} {attach_rates}

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_firm}.

{analyst_2_name}:
What are your plans for international expansion, specifically in the APAC region?

{ceo_name}:
{international_expansion_plans}

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_firm}.

{analyst_3_name}:
How are you managing churn in the current economic environment, and what's the trend you are seeing in NRR?

{cfo_name}:
{churn_management_strategy} {net_retention_rate}

Operator:
Thank you. I'm showing no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}:
Thank you for joining us today. We are pleased with our progress this quarter and remain committed to delivering strong results for our shareholders. We look forward to speaking with you again on our next earnings call.

Operator:
Thank you for your participation. You may now disconnect.
    """),
    ("6", """
Operator:
Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's call is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, Operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {cto_name}, CTO; {cro_name}, Chief Revenue Officer; and {chief_product_officer_name}, Chief Product Officer.

Before we begin, I'd like to remind you that this call contains forward-looking statements. Actual results may differ materially. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good afternoon, everyone. I'm pleased to report on {company_name}'s performance for {quarter}. We achieved significant milestones this quarter, driven by strong demand for our {new_product} and continued execution of our strategic initiatives.

Our focus this quarter was on six key areas: {aspect_1}, {aspect_2}, {aspect_3}, {aspect_4}, {aspect_5}, and {aspect_6}.

{aspect_1_details}
{aspect_2_details}
{aspect_3_details}
{aspect_4_details}
{aspect_5_details}
{aspect_6_details}

We are confident in our ability to continue this momentum and deliver long-term value to our shareholders.

Now, I'll turn the call over to {cfo_name} to discuss the financials in more detail.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Revenue for the quarter was {revenue}, representing a {revenue_growth}% increase year-over-year. Our gross margin was {gross_margin}%, and operating income was {operating_income}.

We continue to invest in research and development to drive innovation and expand our product offerings. Our cash position remains strong, providing us with the flexibility to pursue strategic acquisitions and other growth opportunities.

We are updating our full-year guidance to reflect our strong performance in the first half of the year. We now expect revenue to be in the range of {rev_guidance_low} to {rev_guidance_high}.

Now, I'll turn the call over to {cto_name} for a technology update.

{cto_name}:
Thank you, {cfo_name}. This quarter, we made significant progress in advancing our AI capabilities and further integrating them into our core platform. We are seeing strong adoption of our new AI-powered features, which are driving increased user engagement and improved customer outcomes. We've also focused on enhancing our platform's security and scalability to meet the growing demands of our enterprise customers.

And now {chief_product_officer_name} will provide update on product roadmap.

{chief_product_officer_name}:
Thank you, {cto_name}. We have been focusing on the user experience of our products and are excited to announce the launch of {new_feature}. This new feature significantly improves {benefit_of_feature}. We are seeing strong adoption of this feature which aligns with our product strategy.

Now, I'll turn the call back to the operator for Q&A.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}.

{analyst_1_name}:
Hi, good afternoon. Can you discuss the impact of {new_product} on your overall growth, what kind of attach rates are you seeing, and how it compares to your initial expectations?

{cro_name}:
{impact_of_product} {attach_rates} {comparison_to_expectations}

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_firm}.

{analyst_2_name}:
What are your plans for international expansion, specifically in the APAC region, and what are your key target markets?

{ceo_name}:
{international_expansion_plans} {target_markets}

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_firm}.

{analyst_3_name}:
How are you managing churn in the current economic environment, what's the trend you are seeing in NRR, and what are your strategies to improve customer retention?

{cfo_name}:
{churn_management_strategy} {net_retention_rate} {customer_retention_strategies}

Operator:
Thank you. I'm showing no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}:
Thank you for joining us today. We are pleased with our progress this quarter and remain committed to delivering strong results for our shareholders. We look forward to speaking with you again on our next earnings call.

Operator:
Thank you for your participation. You may now disconnect.
    """),
    ("7", """
Operator:
Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's call is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, Operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {cto_name}, CTO; {cro_name}, Chief Revenue Officer; {chief_product_officer_name}, Chief Product Officer; and {chief_marketing_officer_name}, Chief Marketing Officer.

Before we begin, I'd like to remind you that this call contains forward-looking statements. Actual results may differ materially. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good afternoon, everyone. I'm pleased to report on {company_name}'s performance for {quarter}. We achieved significant milestones this quarter, driven by strong demand for our {new_product} and continued execution of our strategic initiatives.

Our focus this quarter was on seven key areas: {aspect_1}, {aspect_2}, {aspect_3}, {aspect_4}, {aspect_5}, {aspect_6}, and {aspect_7}.

{aspect_1_details}
{aspect_2_details}
{aspect_3_details}
{aspect_4_details}
{aspect_5_details}
{aspect_6_details}
{aspect_7_details}

We are confident in our ability to continue this momentum and deliver long-term value to our shareholders.

Now, I'll turn the call over to {cfo_name} to discuss the financials in more detail.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Revenue for the quarter was {revenue}, representing a {revenue_growth}% increase year-over-year. Our gross margin was {gross_margin}%, and operating income was {operating_income}.

We continue to invest in research and development to drive innovation and expand our product offerings. Our cash position remains strong, providing us with the flexibility to pursue strategic acquisitions and other growth opportunities.

We are updating our full-year guidance to reflect our strong performance in the first half of the year. We now expect revenue to be in the range of {rev_guidance_low} to {rev_guidance_high}.

Now, I'll turn the call over to {cto_name} for a technology update.

{cto_name}:
Thank you, {cfo_name}. This quarter, we made significant progress in advancing our AI capabilities and further integrating them into our core platform. We are seeing strong adoption of our new AI-powered features, which are driving increased user engagement and improved customer outcomes. We've also focused on enhancing our platform's security and scalability to meet the growing demands of our enterprise customers.

And now {chief_product_officer_name} will provide update on product roadmap.

{chief_product_officer_name}:
Thank you, {cto_name}. We have been focusing on the user experience of our products and are excited to announce the launch of {new_feature}. This new feature significantly improves {benefit_of_feature}. We are seeing strong adoption of this feature which aligns with our product strategy.

{chief_marketing_officer_name}:
Thank you, {chief_product_officer_name}. This quarter our focus was on increasing our brand awareness and lead generation through targeted digital campaigns and strategic partnerships. We saw a {percentage_increase}% increase in website traffic and a {percentage_increase_leads}% increase in qualified leads, demonstrating the effectiveness of our marketing initiatives.

Now, I'll turn the call back to the operator for Q&A.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}.

{analyst_1_name}:
Hi, good afternoon. Can you discuss the impact of {new_product} on your overall growth, what kind of attach rates are you seeing, how it compares to your initial expectations, and what's the competitive landscape like?

{cro_name}:
{impact_of_product} {attach_rates} {comparison_to_expectations} {competitive_landscape}

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_firm}.

{analyst_2_name}:
What are your plans for international expansion, specifically in the APAC region, what are your key target markets, and what are your expected ROI from these investments?

{ceo_name}:
{international_expansion_plans} {target_markets} {expected_roi}

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_firm}.

{analyst_3_name}:
How are you managing churn in the current economic environment, what's the trend you are seeing in NRR, what are your strategies to improve customer retention, and what's the impact of pricing changes on churn?

{cfo_name}:
{churn_management_strategy} {net_retention_rate} {customer_retention_strategies} {pricing_changes_impact}

Operator:
Thank you. I'm showing no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}:
Thank you for joining us today. We are pleased with our progress this quarter and remain committed to delivering strong results for our shareholders. We look forward to speaking with you again on our next earnings call.

Operator:
Thank you for your participation. You may now disconnect.
    """),
    ("8", """
Operator:
Good day, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are in listen-only mode. After the speakers' presentation, there will be a question and answer session. [Operator Instructions] Please be advised that today's call is being recorded.

I would now like to turn the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, Operator. Good afternoon, everyone, and welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {cto_name}, CTO; {cro_name}, Chief Revenue Officer; {chief_product_officer_name}, Chief Product Officer; {chief_marketing_officer_name}, Chief Marketing Officer; and {chief_customer_officer_name}, Chief Customer Officer.

Before we begin, I'd like to remind you that this call contains forward-looking statements. Actual results may differ materially. Please refer to our SEC filings for a complete discussion of risks and uncertainties.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good afternoon, everyone. I'm pleased to report on {company_name}'s performance for {quarter}. We achieved significant milestones this quarter, driven by strong demand for our {new_product} and continued execution of our strategic initiatives.

Our focus this quarter was on eight key areas: {aspect_1}, {aspect_2}, {aspect_3}, {aspect_4}, {aspect_5}, {aspect_6}, {aspect_7}, and {aspect_8}.

{aspect_1_details}
{aspect_2_details}
{aspect_3_details}
{aspect_4_details}
{aspect_5_details}
{aspect_6_details}
{aspect_7_details}
{aspect_8_details}

We are confident in our ability to continue this momentum and deliver long-term value to our shareholders.

Now, I'll turn the call over to {cfo_name} to discuss the financials in more detail.

{cfo_name}:
Thank you, {ceo_name}. As {ceo_name} mentioned, we had a strong quarter. Revenue for the quarter was {revenue}, representing a {revenue_growth}% increase year-over-year. Our gross margin was {gross_margin}%, and operating income was {operating_income}.

We continue to invest in research and development to drive innovation and expand our product offerings. Our cash position remains strong, providing us with the flexibility to pursue strategic acquisitions and other growth opportunities.

We are updating our full-year guidance to reflect our strong performance in the first half of the year. We now expect revenue to be in the range of {rev_guidance_low} to {rev_guidance_high}.

Now, I'll turn the call over to {cto_name} for a technology update.

{cto_name}:
Thank you, {cfo_name}. This quarter, we made significant progress in advancing our AI capabilities and further integrating them into our core platform. We are seeing strong adoption of our new AI-powered features, which are driving increased user engagement and improved customer outcomes. We've also focused on enhancing our platform's security and scalability to meet the growing demands of our enterprise customers.

And now {chief_product_officer_name} will provide update on product roadmap.

{chief_product_officer_name}:
Thank you, {cto_name}. We have been focusing on the user experience of our products and are excited to announce the launch of {new_feature}. This new feature significantly improves {benefit_of_feature}. We are seeing strong adoption of this feature which aligns with our product strategy.

{chief_marketing_officer_name}:
Thank you, {chief_product_officer_name}. This quarter our focus was on increasing our brand awareness and lead generation through targeted digital campaigns and strategic partnerships. We saw a {percentage_increase}% increase in website traffic and a {percentage_increase_leads}% increase in qualified leads, demonstrating the effectiveness of our marketing initiatives.

{chief_customer_officer_name}:
Thank you, {chief_marketing_officer_name}. We are committed to delivering exceptional customer experiences and this quarter, we focused on improving our customer support and onboarding processes. As a result, we have seen a {percentage_increase_customer_satisfaction}% increase in customer satisfaction scores.

Now, I'll turn the call back to the operator for Q&A.

Operator:
Thank you. [Operator Instructions] Our first question comes from {analyst_1_name} with {analyst_1_firm}.

{analyst_1_name}:
Hi, good afternoon. Can you discuss the impact of {new_product} on your overall growth, what kind of attach rates are you seeing, how it compares to your initial expectations, what's the competitive landscape like, and how do you plan to differentiate yourselves?

{cro_name}:
{impact_of_product} {attach_rates} {comparison_to_expectations} {competitive_landscape} {differentiation_strategy}

Operator:
Our next question comes from {analyst_2_name} with {analyst_2_firm}.

{analyst_2_name}:
What are your plans for international expansion, specifically in the APAC region, what are your key target markets, what are your expected ROI from these investments, and what are the key challenges you anticipate?

{ceo_name}:
{international_expansion_plans} {target_markets} {expected_roi} {anticipated_challenges}

Operator:
Our next question comes from {analyst_3_name} with {analyst_3_firm}.

{analyst_3_name}:
How are you managing churn in the current economic environment, what's the trend you are seeing in NRR, what are your strategies to improve customer retention, what's the impact of pricing changes on churn, and what are your long-term targets for NRR?

{cfo_name}:
{churn_management_strategy} {net_retention_rate} {customer_retention_strategies} {pricing_changes_impact} {long_term_nrr_targets}

Operator:
Our next question comes from {analyst_4_name} with {analyst_4_firm}.

{analyst_4_name}:
Can you provide more color on customer acquisition costs (CAC) and payback periods for new customers?

{cfo_name}:
{customer_acquisition_cost} {payback_period}

Operator:
Thank you. I'm showing no further questions at this time. I'd like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}:
Thank you for joining us today. We are pleased with our progress this quarter and remain committed to delivering strong results for our shareholders. We look forward to speaking with you again on our next earnings call.

Operator:
Thank you for your participation. You may now disconnect.
    """)
])