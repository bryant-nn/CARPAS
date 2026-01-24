from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers’ presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference call is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; and other members of our leadership team.

Before we begin, I would like to remind you that today's discussion may contain forward-looking statements that are subject to risks and uncertainties. Actual results may differ materially from those expressed or implied by these statements. Please refer to our SEC filings for a complete discussion of these risks.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. {quarter} was a pivotal quarter for {company_name}. We made significant strides in key areas, including {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, and {aspect_4_details}. We are particularly excited about the upcoming launch of {new_product} and its anticipated {impact_of_product} on our market share.

Now, I'll turn the call over to {cfo_name} to discuss our financial performance in more detail.

{cfo_name}:
Thank you, {ceo_name}. Good morning, everyone. For {quarter}, our revenue was {revenue}, representing a {revenue_growth}% increase year-over-year. Our gross margin was {gross_margin}%, and our operating expenses were {operating_expenses}. Net income was {net_income}. We are maintaining a strong balance sheet with {cash_reserves} in cash and cash equivalents. Our guidance for next quarter is {next_quarter_guidance}.

Now, I'll hand the call back to the operator for the Q&A session.

Operator:
Thank you. We will now begin the question and answer session. [Operator Instructions]

Analyst 1:
[Analyst Question 1]
{ceo_name}:
[Answer to Analyst Question 1]

Analyst 2:
[Analyst Question 2]
{cfo_name}:
[Answer to Analyst Question 2]

Analyst 3:
[Analyst Question 3]
{ceo_name}:
[Answer to Analyst Question 3]

{ir_name}:
Thank you for your questions. We have time for one more.

Analyst 4:
[Analyst Question 4]
{cfo_name}:
[Answer to Analyst Question 4]

Operator:
Thank you. I would now like to turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, operator, and thank you all for joining us today. We are confident that {company_name} is well-positioned for continued success in the rapidly evolving automotive landscape. We look forward to updating you on our progress next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} earnings call. You may now disconnect.
"""),
    ("5", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers’ presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference call is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {chief_manufacturing_officer_name}, Chief Manufacturing Officer; and other members of our leadership team.

Before we begin, I would like to remind you that today's discussion may contain forward-looking statements that are subject to risks and uncertainties. Actual results may differ materially from those expressed or implied by these statements. Please refer to our SEC filings for a complete discussion of these risks.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. {quarter} was a strong quarter for {company_name}. We made significant progress in several key areas, including {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, and {aspect_5_details}. The demand for our {new_product} continues to be strong, and we are working diligently to increase production capacity to meet that demand. The {impact_of_product} is exceeding our initial expectations.

Now, I'll turn the call over to {cfo_name} to discuss our financial performance in more detail.

{cfo_name}:
Thank you, {ceo_name}. Good morning, everyone. For {quarter}, our revenue was {revenue}, representing a {revenue_growth}% increase year-over-year. Our gross margin was {gross_margin}%, reflecting our ongoing efforts to improve operational efficiency. Our operating expenses were {operating_expenses}, and net income was {net_income}. We continue to maintain a healthy balance sheet with {cash_reserves} in cash and cash equivalents. Our guidance for the next quarter is {next_quarter_guidance}.

I'll now turn the call over to {chief_manufacturing_officer_name} to provide an update on our manufacturing operations.

{chief_manufacturing_officer_name}:
Thank you, {cfo_name}. We are pleased with the progress we've made in scaling up production of {new_product}. We are implementing several initiatives to further improve our manufacturing efficiency and reduce costs. We are on track to meet our production targets for the year.

Now, I'll hand the call back to the operator for the Q&A session.

Operator:
Thank you. We will now begin the question and answer session. [Operator Instructions]

Analyst 1:
[Analyst Question 1]
{ceo_name}:
[Answer to Analyst Question 1]

Analyst 2:
[Analyst Question 2]
{cfo_name}:
[Answer to Analyst Question 2]

Analyst 3:
[Analyst Question 3]
{chief_manufacturing_officer_name}:
[Answer to Analyst Question 3]

Analyst 4:
[Analyst Question 4]
{ceo_name}:
[Answer to Analyst Question 4]

{ir_name}:
Thank you for your questions. We have time for one more.

Analyst 5:
[Analyst Question 5]
{cfo_name}:
[Answer to Analyst Question 5]

Operator:
Thank you. I would now like to turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, operator, and thank you all for joining us today. We are confident in our ability to continue executing our strategy and delivering value to our shareholders. We look forward to updating you on our progress next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} earnings call. You may now disconnect.
"""),
    ("6", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers’ presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference call is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {chief_manufacturing_officer_name}, Chief Manufacturing Officer; {chief_technology_officer_name}, Chief Technology Officer; and other members of our leadership team.

Before we begin, I would like to remind you that today's discussion may contain forward-looking statements that are subject to risks and uncertainties. Actual results may differ materially from those expressed or implied by these statements. Please refer to our SEC filings for a complete discussion of these risks.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. {quarter} was a significant quarter for {company_name}, marked by progress across our key strategic initiatives. We achieved notable milestones in {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, {aspect_5_details}, and {aspect_6_details}. We are particularly pleased with the initial customer response to our {new_product}, and its {impact_of_product} on our backlog is substantial.

Now, I'll turn the call over to {cfo_name} to discuss our financial performance in more detail.

{cfo_name}:
Thank you, {ceo_name}. Good morning, everyone. For {quarter}, our revenue reached {revenue}, demonstrating a {revenue_growth}% increase compared to the same period last year. Our gross margin stood at {gross_margin}%, reflecting our commitment to operational excellence. Operating expenses amounted to {operating_expenses}, and net income was {net_income}. We maintain a robust financial position with {cash_reserves} in cash and cash equivalents. Our outlook for the upcoming quarter is {next_quarter_guidance}.

Next, I'll hand the call over to {chief_manufacturing_officer_name} for an update on our manufacturing operations.

{chief_manufacturing_officer_name}:
Thank you, {cfo_name}. Our manufacturing facilities are operating at peak efficiency to meet the growing demand for our vehicles. We have successfully implemented several lean manufacturing principles, resulting in improved throughput and reduced lead times. We are confident in our ability to scale production further as needed.

Following {chief_manufacturing_officer_name}, {chief_technology_officer_name} will provide insights into our technological advancements.

{chief_technology_officer_name}:
Thank you. We continue to invest heavily in research and development to maintain our technological edge. Our advancements in battery technology and autonomous driving systems are positioning us as a leader in the EV industry.

Now, I'll hand the call back to the operator for the Q&A session.

Operator:
Thank you. We will now begin the question and answer session. [Operator Instructions]

Analyst 1:
[Analyst Question 1]
{ceo_name}:
[Answer to Analyst Question 1]

Analyst 2:
[Analyst Question 2]
{cfo_name}:
[Answer to Analyst Question 2]

Analyst 3:
[Analyst Question 3]
{chief_manufacturing_officer_name}:
[Answer to Analyst Question 3]

Analyst 4:
[Analyst Question 4]
{chief_technology_officer_name}:
[Answer to Analyst Question 4]

{ir_name}:
Thank you for your questions. We have time for two more.

Analyst 5:
[Analyst Question 5]
{ceo_name}:
[Answer to Analyst Question 5]

Analyst 6:
[Analyst Question 6]
{cfo_name}:
[Answer to Analyst Question 6]

Operator:
Thank you. I would now like to turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, operator, and thank you all for joining us today. We are excited about the opportunities ahead and remain committed to creating long-term value for our shareholders. We look forward to sharing our progress with you next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} earnings call. You may now disconnect.
"""),
    ("7", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers’ presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference call is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {chief_manufacturing_officer_name}, Chief Manufacturing Officer; {chief_technology_officer_name}, Chief Technology Officer; {chief_supply_chain_officer_name}, Chief Supply Chain Officer; and other members of our leadership team.

Before we begin, I would like to remind you that today's discussion may contain forward-looking statements that are subject to risks and uncertainties. Actual results may differ materially from those expressed or implied by these statements. Please refer to our SEC filings for a complete discussion of these risks.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. {quarter} marked a period of significant advancement for {company_name}, as we continued to execute our strategic plan. Key achievements included {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, {aspect_5_details}, {aspect_6_details}, and {aspect_7_details}. The launch of our {new_product} has been incredibly successful, and we are seeing a very positive {impact_of_product} on our brand image.

Now, I'll turn the call over to {cfo_name} to discuss our financial performance in more detail.

{cfo_name}:
Thank you, {ceo_name}. Good morning, everyone. For {quarter}, our revenue was {revenue}, representing a substantial {revenue_growth}% increase year-over-year. Our gross margin reached {gross_margin}%, driven by increased production efficiencies and favorable product mix. Operating expenses totaled {operating_expenses}, and net income amounted to {net_income}. We are in a strong financial position with {cash_reserves} in cash reserves. We project {next_quarter_guidance} for the next quarter.

Next, {chief_manufacturing_officer_name} will share updates on our manufacturing operations.

{chief_manufacturing_officer_name}:
Thank you, {cfo_name}. We have made significant investments in our manufacturing facilities to enhance capacity and improve efficiency. Our efforts have resulted in record production volumes and reduced manufacturing costs.

After {chief_manufacturing_officer_name}, we will hear from {chief_technology_officer_name} regarding our technological advancements.

{chief_technology_officer_name}:
Thank you. Our R&D team continues to push the boundaries of innovation in battery technology, autonomous driving, and connectivity. We are committed to developing cutting-edge solutions that will shape the future of mobility.

Following {chief_technology_officer_name}, {chief_supply_chain_officer_name} will provide insights into our supply chain management.

{chief_supply_chain_officer_name}:
Thank you. We have implemented robust supply chain strategies to mitigate risks and ensure the reliable flow of materials. Our focus on diversification and strategic partnerships has strengthened our supply chain resilience.

Now, I'll hand the call back to the operator for the Q&A session.

Operator:
Thank you. We will now begin the question and answer session. [Operator Instructions]

Analyst 1:
[Analyst Question 1]
{ceo_name}:
[Answer to Analyst Question 1]

Analyst 2:
[Analyst Question 2]
{cfo_name}:
[Answer to Analyst Question 2]

Analyst 3:
[Analyst Question 3]
{chief_manufacturing_officer_name}:
[Answer to Analyst Question 3]

Analyst 4:
[Analyst Question 4]
{chief_technology_officer_name}:
[Answer to Analyst Question 4]

Analyst 5:
[Analyst Question 5]
{chief_supply_chain_officer_name}:
[Answer to Analyst Question 5]

{ir_name}:
Thank you for your questions. We have time for one more.

Analyst 6:
[Analyst Question 6]
{ceo_name}:
[Answer to Analyst Question 6]

Operator:
Thank you. I would now like to turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, operator, and thank you all for joining us today. We are well-positioned to capitalize on the growing demand for electric vehicles and deliver strong results. We look forward to updating you on our progress next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} earnings call. You may now disconnect.
"""),
    ("8", """
Operator:
Good morning, and welcome to the {company_name} {quarter} Earnings Conference Call. All participants are currently in a listen-only mode. After the speakers’ presentation, there will be a question and answer session. [Operator Instructions] As a reminder, this conference call is being recorded.

I would now like to turn the conference over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}:
Thank you, operator, and good morning, everyone. Welcome to {company_name}'s {quarter} earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {chief_manufacturing_officer_name}, Chief Manufacturing Officer; {chief_technology_officer_name}, Chief Technology Officer; {chief_supply_chain_officer_name}, Chief Supply Chain Officer; {chief_sales_officer_name}, Chief Sales Officer; and other members of our leadership team.

Before we begin, I would like to remind you that today's discussion may contain forward-looking statements that are subject to risks and uncertainties. Actual results may differ materially from those expressed or implied by these statements. Please refer to our SEC filings for a complete discussion of these risks.

Now, I'd like to turn the call over to {ceo_name}.

{ceo_name}:
Thank you, {ir_name}, and good morning, everyone. Thank you for joining us today. Reflecting on {quarter}, we are proud of the significant strides {company_name} has made across all facets of our business. We have achieved remarkable progress in {aspect_1_details}, {aspect_2_details}, {aspect_3_details}, {aspect_4_details}, {aspect_5_details}, {aspect_6_details}, {aspect_7_details}, and {aspect_8_details}. The market reception to our {new_product} has been overwhelmingly positive, with the associated {impact_of_product} far exceeding our initial estimates.

Now, I'll turn the call over to {cfo_name} to discuss our financial performance in greater detail.

{cfo_name}:
Thank you, {ceo_name}. Good morning, everyone. Our revenue for {quarter} reached {revenue}, marking an exceptional {revenue_growth}% increase compared to the same period last year. Our gross margin expanded to {gross_margin}%, driven by enhanced operational efficiencies and a favorable product mix. Operating expenses amounted to {operating_expenses}, resulting in a net income of {net_income}. Our financial position remains strong, with {cash_reserves} in cash and cash equivalents. We anticipate {next_quarter_guidance} for the upcoming quarter.

Next, we'll hear from {chief_manufacturing_officer_name} regarding the latest developments in our manufacturing operations.

{chief_manufacturing_officer_name}:
Thank you, {cfo_name}. Our manufacturing facilities are operating at optimal levels to meet the surging demand for our vehicles. We have successfully implemented advanced automation technologies, resulting in increased production output and reduced cycle times.

Following {chief_manufacturing_officer_name}, {chief_technology_officer_name} will provide an update on our technological innovations.

{chief_technology_officer_name}:
Thank you. Our R&D team is relentlessly pursuing breakthroughs in battery technology, autonomous driving systems, and vehicle connectivity. We are committed to delivering cutting-edge solutions that will redefine the future of mobility.

After {chief_technology_officer_name}, {chief_supply_chain_officer_name} will offer insights into our supply chain strategies.

{chief_supply_chain_officer_name}:
Thank you. We have established a resilient and diversified supply chain network to mitigate risks and ensure the seamless flow of materials. Our proactive approach to supply chain management has enabled us to navigate the ongoing global challenges effectively.

Next, {chief_sales_officer_name} will share updates on our sales performance and market expansion initiatives.

{chief_sales_officer_name}:
Thank you. Our sales team has achieved remarkable success in expanding our market reach and driving revenue growth. We are seeing strong demand for our vehicles across all regions, and we are actively pursuing new market opportunities.

Now, I'll hand the call back to the operator for the Q&A session.

Operator:
Thank you. We will now begin the question and answer session. [Operator Instructions]

Analyst 1:
[Analyst Question 1]
{ceo_name}:
[Answer to Analyst Question 1]

Analyst 2:
[Analyst Question 2]
{cfo_name}:
[Answer to Analyst Question 2]

Analyst 3:
[Analyst Question 3]
{chief_manufacturing_officer_name}:
[Answer to Analyst Question 3]

Analyst 4:
[Analyst Question 4]
{chief_technology_officer_name}:
[Answer to Analyst Question 4]

Analyst 5:
[Analyst Question 5]
{chief_supply_chain_officer_name}:
[Answer to Analyst Question 5]

Analyst 6:
[Analyst Question 6]
{chief_sales_officer_name}:
[Answer to Analyst Question 6]

{ir_name}:
Thank you for your questions. We have time for two more.

Analyst 7:
[Analyst Question 7]
{ceo_name}:
[Answer to Analyst Question 7]

Analyst 8:
[Analyst Question 8]
{cfo_name}:
[Answer to Analyst Question 8]

Operator:
Thank you. I would now like to turn the call back to {ceo_name} for closing remarks.

{ceo_name}:
Thank you, operator, and thank you all for joining us today. We are confident in our ability to continue delivering exceptional results and creating long-term value for our shareholders. We look forward to sharing our progress with you next quarter.

{ir_name}:
Thank you for joining us today. This concludes the {company_name} {quarter} earnings call. You may now disconnect.
""")
])