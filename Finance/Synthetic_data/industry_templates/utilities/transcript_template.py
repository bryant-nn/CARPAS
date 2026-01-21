from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; and {coo_name}, Chief Operating Officer.

Before we begin, I'd like to remind you that statements made during this call that are not historical facts are forward-looking statements and are subject to risks and uncertainties that could cause actual results to differ materially from those expressed or implied. Please refer to our SEC filings for a detailed discussion of these risks.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. I'm pleased to report on our performance this quarter. We continued to execute on our strategic priorities, delivering solid results in a challenging environment.

Our performance was driven by:
    1.  Strong operational performance in our generation fleet.
    2.  Continued growth in our renewable energy portfolio.
    3.  Effective cost management.
    4.  Progress on our infrastructure investments.

Let me provide some more detail on these four key aspects:

    *   Aspect 1: {aspect_1_details}
    *   Aspect 2: {aspect_2_details}
    *   Aspect 3: {aspect_3_details}
    *   Aspect 4: {aspect_4_details}

Now, I'll turn the call over to {cfo_name} to discuss the financials.

{cfo_name}: Thank you, {ceo_name}. Good morning, everyone. For the {quarter}, we reported earnings per share of ${eps} and revenue of ${revenue}. Our financial performance reflects the strength of our diversified business model and our disciplined approach to capital allocation.

Our capital expenditure for the quarter was ${capex}, primarily focused on {capex_focus}. We remain committed to maintaining a strong balance sheet and returning value to shareholders.

{ceo_name}: Thank you, {cfo_name}. Now, we'll open the line for questions.

Operator: [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

[Analyst Name]: Good morning. Can you elaborate on your plans for {analyst_question_1}?

{ceo_name}: Certainly. {ceo_response_1}

Operator: Our next question comes from [Analyst Name 2] with [Analyst Firm 2]. Please go ahead.

[Analyst Name 2]: What is your outlook for {analyst_question_2}?

{cfo_name}: {cfo_response_2}

Operator: Our next question comes from [Analyst Name 3] with [Analyst Firm 3]. Please go ahead.

[Analyst Name 3]: How are you mitigating risks related to {analyst_question_3}?

{coo_name}: {coo_response_3}

Operator: There are no further questions at this time. I would like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you. In summary, we delivered solid results in the {quarter}, demonstrating the strength of our business model and our commitment to creating long-term value for our shareholders. We remain focused on executing our strategic priorities and positioning {company_name} for continued success. Thank you for your time and interest in {company_name}.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("5", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer, and {chief_strategy_officer_name}, Chief Strategy Officer.

Before we begin, I'd like to remind you that statements made during this call that are not historical facts are forward-looking statements and are subject to risks and uncertainties that could cause actual results to differ materially from those expressed or implied. Please refer to our SEC filings for a detailed discussion of these risks.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. I'm pleased to report on our performance this quarter. We continued to execute on our strategic priorities, delivering solid results in a challenging environment.

Our performance was driven by:
    1.  Strong operational performance in our generation fleet.
    2.  Continued growth in our renewable energy portfolio.
    3.  Effective cost management.
    4.  Progress on our infrastructure investments.
    5.  Successful integration of {acquired_asset}.

Let me provide some more detail on these five key aspects:

    *   Aspect 1: {aspect_1_details}
    *   Aspect 2: {aspect_2_details}
    *   Aspect 3: {aspect_3_details}
    *   Aspect 4: {aspect_4_details}
    *   Aspect 5: {aspect_5_details}

Now, I'll turn the call over to {cfo_name} to discuss the financials.

{cfo_name}: Thank you, {ceo_name}. Good morning, everyone. For the {quarter}, we reported earnings per share of ${eps} and revenue of ${revenue}. Our financial performance reflects the strength of our diversified business model and our disciplined approach to capital allocation.

Our capital expenditure for the quarter was ${capex}, primarily focused on {capex_focus}. We remain committed to maintaining a strong balance sheet and returning value to shareholders. We anticipate {future_financial_outlook}.

{coo_name}: Thank you, {cfo_name}. Let me provide an update on the operational front. We are seeing improved efficiency in our {power_plant_type} power plants due to the implementation of {new_technology}. This has resulted in a {percentage_improvement}% increase in output.

{chief_strategy_officer_name}: Thank you, {coo_name}. Turning to our long-term strategy, we are actively exploring opportunities in the {emerging_technology} space. We believe this will be a key driver of future growth.

{ceo_name}: Thank you, {cfo_name}, {coo_name}, and {chief_strategy_officer_name}. Now, we'll open the line for questions.

Operator: [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

[Analyst Name]: Good morning. Can you elaborate on your plans for {analyst_question_1}?

{ceo_name}: Certainly. {ceo_response_1}

Operator: Our next question comes from [Analyst Name 2] with [Analyst Firm 2]. Please go ahead.

[Analyst Name 2]: What is your outlook for {analyst_question_2}?

{cfo_name}: {cfo_response_2}

Operator: Our next question comes from [Analyst Name 3] with [Analyst Firm 3]. Please go ahead.

[Analyst Name 3]: How are you mitigating risks related to {analyst_question_3}?

{coo_name}: {coo_response_3}

Operator: There are no further questions at this time. I would like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you. In summary, we delivered solid results in the {quarter}, demonstrating the strength of our business model and our commitment to creating long-term value for our shareholders. We remain focused on executing our strategic priorities and positioning {company_name} for continued success. Thank you for your time and interest in {company_name}.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("6", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; {chief_strategy_officer_name}, Chief Strategy Officer; and {chief_technology_officer_name}, Chief Technology Officer.

Before we begin, I'd like to remind you that statements made during this call that are not historical facts are forward-looking statements and are subject to risks and uncertainties that could cause actual results to differ materially from those expressed or implied. Please refer to our SEC filings for a detailed discussion of these risks.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. I'm pleased to report on our performance this quarter. We continued to execute on our strategic priorities, delivering solid results in a challenging environment.

Our performance was driven by:
    1.  Strong operational performance in our generation fleet.
    2.  Continued growth in our renewable energy portfolio.
    3.  Effective cost management.
    4.  Progress on our infrastructure investments.
    5.  Successful integration of {acquired_asset}.
    6.  Advancement of our {sustainability_initiative} program.

Let me provide some more detail on these six key aspects:

    *   Aspect 1: {aspect_1_details}
    *   Aspect 2: {aspect_2_details}
    *   Aspect 3: {aspect_3_details}
    *   Aspect 4: {aspect_4_details}
    *   Aspect 5: {aspect_5_details}
    *   Aspect 6: {aspect_6_details}

Now, I'll turn the call over to {cfo_name} to discuss the financials.

{cfo_name}: Thank you, {ceo_name}. Good morning, everyone. For the {quarter}, we reported earnings per share of ${eps} and revenue of ${revenue}. Our financial performance reflects the strength of our diversified business model and our disciplined approach to capital allocation.

Our capital expenditure for the quarter was ${capex}, primarily focused on {capex_focus}. We remain committed to maintaining a strong balance sheet and returning value to shareholders. We anticipate {future_financial_outlook}.

{coo_name}: Thank you, {cfo_name}. Let me provide an update on the operational front. We are seeing improved efficiency in our {power_plant_type} power plants due to the implementation of {new_technology}. This has resulted in a {percentage_improvement}% increase in output. Our outage rates are also down {outage_reduction}%.

{chief_strategy_officer_name}: Thank you, {coo_name}. Turning to our long-term strategy, we are actively exploring opportunities in the {emerging_technology} space. We believe this will be a key driver of future growth. We are also evaluating potential acquisitions in the {geographic_region} market.

{chief_technology_officer_name}: Thank you, {chief_strategy_officer_name}. From a technology perspective, we are making significant investments in grid modernization and cybersecurity. We recently deployed {new_cybersecurity_solution} to enhance our defenses against cyber threats.

{ceo_name}: Thank you, {cfo_name}, {coo_name}, {chief_strategy_officer_name}, and {chief_technology_officer_name}. Now, we'll open the line for questions.

Operator: [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

[Analyst Name]: Good morning. Can you elaborate on your plans for {analyst_question_1}?

{ceo_name}: Certainly. {ceo_response_1}

Operator: Our next question comes from [Analyst Name 2] with [Analyst Firm 2]. Please go ahead.

[Analyst Name 2]: What is your outlook for {analyst_question_2}?

{cfo_name}: {cfo_response_2}

Operator: Our next question comes from [Analyst Name 3] with [Analyst Firm 3]. Please go ahead.

[Analyst Name 3]: How are you mitigating risks related to {analyst_question_3}?

{coo_name}: {coo_response_3}

Operator: There are no further questions at this time. I would like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you. In summary, we delivered solid results in the {quarter}, demonstrating the strength of our business model and our commitment to creating long-term value for our shareholders. We remain focused on executing our strategic priorities and positioning {company_name} for continued success. Thank you for your time and interest in {company_name}.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("7", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; {chief_strategy_officer_name}, Chief Strategy Officer; {chief_technology_officer_name}, Chief Technology Officer; and {chief_regulatory_officer_name}, Chief Regulatory Officer.

Before we begin, I'd like to remind you that statements made during this call that are not historical facts are forward-looking statements and are subject to risks and uncertainties that could cause actual results to differ materially from those expressed or implied. Please refer to our SEC filings for a detailed discussion of these risks.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. I'm pleased to report on our performance this quarter. We continued to execute on our strategic priorities, delivering solid results in a challenging environment.

Our performance was driven by:
    1.  Strong operational performance in our generation fleet.
    2.  Continued growth in our renewable energy portfolio.
    3.  Effective cost management.
    4.  Progress on our infrastructure investments.
    5.  Successful integration of {acquired_asset}.
    6.  Advancement of our {sustainability_initiative} program.
    7.  Positive regulatory outcomes in {regulatory_jurisdiction}.

Let me provide some more detail on these seven key aspects:

    *   Aspect 1: {aspect_1_details}
    *   Aspect 2: {aspect_2_details}
    *   Aspect 3: {aspect_3_details}
    *   Aspect 4: {aspect_4_details}
    *   Aspect 5: {aspect_5_details}
    *   Aspect 6: {aspect_6_details}
    *   Aspect 7: {aspect_7_details}

Now, I'll turn the call over to {cfo_name} to discuss the financials.

{cfo_name}: Thank you, {ceo_name}. Good morning, everyone. For the {quarter}, we reported earnings per share of ${eps} and revenue of ${revenue}. Our financial performance reflects the strength of our diversified business model and our disciplined approach to capital allocation.

Our capital expenditure for the quarter was ${capex}, primarily focused on {capex_focus}. We remain committed to maintaining a strong balance sheet and returning value to shareholders. We anticipate {future_financial_outlook}.

{coo_name}: Thank you, {cfo_name}. Let me provide an update on the operational front. We are seeing improved efficiency in our {power_plant_type} power plants due to the implementation of {new_technology}. This has resulted in a {percentage_improvement}% increase in output. Our outage rates are also down {outage_reduction}%.

{chief_strategy_officer_name}: Thank you, {coo_name}. Turning to our long-term strategy, we are actively exploring opportunities in the {emerging_technology} space. We believe this will be a key driver of future growth. We are also evaluating potential acquisitions in the {geographic_region} market.

{chief_technology_officer_name}: Thank you, {chief_strategy_officer_name}. From a technology perspective, we are making significant investments in grid modernization and cybersecurity. We recently deployed {new_cybersecurity_solution} to enhance our defenses against cyber threats. We are also piloting {new_grid_technology} in {pilot_location}.

{chief_regulatory_officer_name}: Thank you, {chief_technology_officer_name}. On the regulatory front, we received approval for our {regulatory_filing} in {regulatory_jurisdiction}. This will allow us to {regulatory_benefit}.

{ceo_name}: Thank you, {cfo_name}, {coo_name}, {chief_strategy_officer_name}, {chief_technology_officer_name}, and {chief_regulatory_officer_name}. Now, we'll open the line for questions.

Operator: [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

[Analyst Name]: Good morning. Can you elaborate on your plans for {analyst_question_1}?

{ceo_name}: Certainly. {ceo_response_1}

Operator: Our next question comes from [Analyst Name 2] with [Analyst Firm 2]. Please go ahead.

[Analyst Name 2]: What is your outlook for {analyst_question_2}?

{cfo_name}: {cfo_response_2}

Operator: Our next question comes from [Analyst Name 3] with [Analyst Firm 3]. Please go ahead.

[Analyst Name 3]: How are you mitigating risks related to {analyst_question_3}?

{coo_name}: {coo_response_3}

Operator: Our next question comes from [Analyst Name 4] with [Analyst Firm 4]. Please go ahead.

[Analyst Name 4]: What is the anticipated impact of {analyst_question_4} on your earnings?

{chief_regulatory_officer_name}: {regulatory_response_4}

Operator: There are no further questions at this time. I would like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you. In summary, we delivered solid results in the {quarter}, demonstrating the strength of our business model and our commitment to creating long-term value for our shareholders. We remain focused on executing our strategic priorities and positioning {company_name} for continued success. Thank you for your time and interest in {company_name}.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """),
    ("8", """
Operator: Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants will be in listen-only mode. After today's presentation, there will be an opportunity to ask questions. [Operator Instructions] As a reminder, this conference is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}: Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} Earnings Call. Joining me on the call today are {ceo_name}, Chief Executive Officer; {cfo_name}, Chief Financial Officer; {coo_name}, Chief Operating Officer; {chief_strategy_officer_name}, Chief Strategy Officer; {chief_technology_officer_name}, Chief Technology Officer; {chief_regulatory_officer_name}, Chief Regulatory Officer; and {chief_communications_officer_name}, Chief Communications Officer.

Before we begin, I'd like to remind you that statements made during this call that are not historical facts are forward-looking statements and are subject to risks and uncertainties that could cause actual results to differ materially from those expressed or implied. Please refer to our SEC filings for a detailed discussion of these risks.

Now, I'll turn the call over to {ceo_name}.

{ceo_name}: Thank you, {ir_name}, and good morning, everyone. I'm pleased to report on our performance this quarter. We continued to execute on our strategic priorities, delivering solid results in a challenging environment.

Our performance was driven by:
    1.  Strong operational performance in our generation fleet.
    2.  Continued growth in our renewable energy portfolio.
    3.  Effective cost management.
    4.  Progress on our infrastructure investments.
    5.  Successful integration of {acquired_asset}.
    6.  Advancement of our {sustainability_initiative} program.
    7.  Positive regulatory outcomes in {regulatory_jurisdiction}.
    8.  Enhanced community engagement in {community_name}.

Let me provide some more detail on these eight key aspects:

    *   Aspect 1: {aspect_1_details}
    *   Aspect 2: {aspect_2_details}
    *   Aspect 3: {aspect_3_details}
    *   Aspect 4: {aspect_4_details}
    *   Aspect 5: {aspect_5_details}
    *   Aspect 6: {aspect_6_details}
    *   Aspect 7: {aspect_7_details}
    *   Aspect 8: {aspect_8_details}

Now, I'll turn the call over to {cfo_name} to discuss the financials.

{cfo_name}: Thank you, {ceo_name}. Good morning, everyone. For the {quarter}, we reported earnings per share of ${eps} and revenue of ${revenue}. Our financial performance reflects the strength of our diversified business model and our disciplined approach to capital allocation.

Our capital expenditure for the quarter was ${capex}, primarily focused on {capex_focus}. We remain committed to maintaining a strong balance sheet and returning value to shareholders. We anticipate {future_financial_outlook}.

{coo_name}: Thank you, {cfo_name}. Let me provide an update on the operational front. We are seeing improved efficiency in our {power_plant_type} power plants due to the implementation of {new_technology}. This has resulted in a {percentage_improvement}% increase in output. Our outage rates are also down {outage_reduction}%.

{chief_strategy_officer_name}: Thank you, {coo_name}. Turning to our long-term strategy, we are actively exploring opportunities in the {emerging_technology} space. We believe this will be a key driver of future growth. We are also evaluating potential acquisitions in the {geographic_region} market.

{chief_technology_officer_name}: Thank you, {chief_strategy_officer_name}. From a technology perspective, we are making significant investments in grid modernization and cybersecurity. We recently deployed {new_cybersecurity_solution} to enhance our defenses against cyber threats. We are also piloting {new_grid_technology} in {pilot_location}.

{chief_regulatory_officer_name}: Thank you, {chief_technology_officer_name}. On the regulatory front, we received approval for our {regulatory_filing} in {regulatory_jurisdiction}. This will allow us to {regulatory_benefit}.

{chief_communications_officer_name}: Thank you, {chief_regulatory_officer_name}. We are pleased to announce that our community outreach program in {community_name} has resulted in a {positive_impact} increase in positive sentiment towards {company_name}.

{ceo_name}: Thank you, {cfo_name}, {coo_name}, {chief_strategy_officer_name}, {chief_technology_officer_name}, {chief_regulatory_officer_name}, and {chief_communications_officer_name}. Now, we'll open the line for questions.

Operator: [Operator Instructions] Our first question comes from [Analyst Name] with [Analyst Firm]. Please go ahead.

[Analyst Name]: Good morning. Can you elaborate on your plans for {analyst_question_1}?

{ceo_name}: Certainly. {ceo_response_1}

Operator: Our next question comes from [Analyst Name 2] with [Analyst Firm 2]. Please go ahead.

[Analyst Name 2]: What is your outlook for {analyst_question_2}?

{cfo_name}: {cfo_response_2}

Operator: Our next question comes from [Analyst Name 3] with [Analyst Firm 3]. Please go ahead.

[Analyst Name 3]: How are you mitigating risks related to {analyst_question_3}?

{coo_name}: {coo_response_3}

Operator: Our next question comes from [Analyst Name 4] with [Analyst Firm 4]. Please go ahead.

[Analyst Name 4]: What is the anticipated impact of {analyst_question_4} on your earnings?

{chief_regulatory_officer_name}: {regulatory_response_4}

Operator: There are no further questions at this time. I would like to turn the call back over to {ceo_name} for closing remarks.

{ceo_name}: Thank you. In summary, we delivered solid results in the {quarter}, demonstrating the strength of our business model and our commitment to creating long-term value for our shareholders. We remain focused on executing our strategic priorities and positioning {company_name} for continued success. Thank you for your time and interest in {company_name}.

Operator: This concludes today's conference call. Thank you for your participation. You may now disconnect.
    """)
])