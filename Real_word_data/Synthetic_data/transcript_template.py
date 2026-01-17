from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
Operator:
Good day and thank you for standing by. Welcome to the {company_name} {quarter} Earnings Conference Call. At this time, all participants are in a listen-only mode. After the speakers' presentation, there will be a Q&A session. Today's call is being recorded.
I would now like to hand the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}, {ir_title}:
Thank you, Operator. Good {time_of_day}, and welcome to {company_name}’s earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; and {exec_name}, {exec_title}.
Earlier today, we published our earnings press release and slides, which are available on our IR site. Please note this call may contain forward-looking statements. Now, I’ll turn it over to {ceo_name}.

{ceo_name}, Chief Executive Officer:
Thanks, {ir_name}. Hello, everyone.

Let’s start with a look at the quarter:

  This quarter, we achieved significant progress, including {aspect_1_details}.

  We’re seeing strong performance in this area, supported by {aspect_2_details}.

These results reflect our strategy in action. I’ll now hand it over to {cfo_name} to discuss the financials.

{cfo_name}, Chief Financial Officer:
Thanks, {ceo_name}, and hello, everyone.

Let’s take a closer look at the numbers:

{aspect_2_details}  

{aspect_3_details}.


Now to {exec_name}, who will cover operational and product updates.

{exec_name}, {exec_title}:
Thanks, {cfo_name}.

Let’s revisit {aspect_1} from an innovation standpoint:
We launched {new_product} which contributed to {impact_of_product}.

We’ve made strong headway with {aspect_4_details}, and expect meaningful results in {aspect_4_timeline}.

Let’s move to Q&A.

Q&A SESSION

Analyst 1:
On {aspect_2}, could you expand on ?

{cfo_name}:
Absolutely. We believe {aspect_2_followup}.

Analyst 2:
Regarding {aspect_4}, what's the scale and outlook?

{exec_name}:
We’re seeing momentum with {aspect_4_impact}, especially in.

Closing

{ceo_name}:
Thank you all for joining. We’re proud of our progress and excited for what’s ahead.

Operator:
Thank you. This concludes the call. You may now disconnect.
"""),

("5", """
Operator:
Good day and thank you for standing by. Welcome to the {company_name} {quarter} Earnings Conference Call. At this time, all participants are in a listen-only mode. After the speakers' presentation, there will be a Q&A session. Today's call is being recorded.
I would now like to hand the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}, {ir_title}:
Thank you, Operator. Good {time_of_day}, and welcome to {company_name}’s earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; and {exec_name}, {exec_title}.
Earlier today, we published our earnings press release and slides, which are available on our IR site. Please note this call may contain forward-looking statements. Now, I’ll turn it over to {ceo_name}.

{ceo_name}, Chief Executive Officer:
Thanks, {ir_name}. Hello, everyone.

Let’s start with a look at the quarter:

  We made strong progress this quarter. 
  {aspect_1_details}.

  We also saw great momentum in {aspect_2_details}.

These achievements underscore our commitment to disciplined execution and innovation.

Now I’ll pass it to {cfo_name} to walk through in more detail.

{cfo_name}, Chief Financial Officer:
Thanks, {ceo_name}, and hello, everyone.

Let me take you through the financials:

  First, building on what {ceo_name} said, we’ve continued to drive improvements there, specifically {aspect_2_details}.

  We invested strategically in this area, resulting in {aspect_3_details}.

  Additionally, we’ve seen progress in {aspect_5_details}, and we believe.

Now I’ll turn it over to {exec_name}, who will speak about operations and innovation.

{exec_name}, {exec_title}:
Thanks, {cfo_name}.

Let me begin with a closer look at {aspect_1_details}, particularly on. We introduced {new_product}, and it’s already contributing to {impact_of_product}.

I’d also like to expand on {aspect_4_details}. Our teams have made solid progress here,.

Let’s move to the Q&A.

Q&A SESSION

Analyst 1:
You mentioned strong improvements in {aspect_2_details}. Can you talk more about ?

{cfo_name}:


Analyst 2:
Can you elaborate on the trajectory of {aspect_4_details} and the ?

{exec_name}:
Sure.

Analyst 3:
With regard to {aspect_5_details}, how does?

{cfo_name}:

Closing

{ceo_name}:
Thank you all for joining us today. We're energized by the momentum we’re seeing and look forward to sharing continued progress next quarter.

Operator:
Thank you. This concludes the call. You may now disconnect.
"""
),

("6", """
Operator:
Good day and thank you for standing by. Welcome to the {company_name} {quarter} Earnings Conference Call. At this time, all participants are in a listen-only mode. After the speakers' presentation, there will be a Q&A session. Today's call is being recorded.
I would now like to hand the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}, {ir_title}:
Thank you, Operator. Good {time_of_day}, and welcome to {company_name}’s earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; and {exec_name}, {exec_title}.
Earlier today, we published our earnings press release and presentation, which are available on our Investor Relations site. Today’s discussion may include forward-looking statements. With that, let me turn the call over to {ceo_name}.

{ceo_name}, Chief Executive Officer:
Thanks, {ir_name}, and welcome everyone.

We’re pleased with our performance this quarter. I want to highlight a few areas:

{aspect_1_details}

{aspect_2_details}

{aspect_3_details}

I’ll now pass it over to {cfo_name} to walk through the numbers in more detail.

{cfo_name}, Chief Financial Officer:
Thanks, {ceo_name}, and hello, everyone.

Let me break it down starting with {aspect_3_details}. We saw healthy 

Now, moving to {aspect_5_details}, which we’ve been tracking closely. 

Lastly, I'd like to briefly touch on {aspect_6_details}. This has historically been more volatile, 

Now, let me hand things over to {exec_name} to talk about product and operational progress.

{exec_name}, {exec_title}:
Thanks, {cfo_name}.

This was a busy quarter for our teams. On the innovation front, we made meaningful advances around {aspect_4_details}. This included the release of {new_product}, which is already 

Also worth noting is our improvement in {aspect_1_details}.

And we’ve made foundational changes in how we approach {aspect_6_details}, particularly on the fulfillment and logistics side.

Let’s now open the floor for questions.

Q&A SESSION

Analyst 1:
Hi, thanks for taking my question. On {aspect_2_details}, could you expand on what’s driving that strength?

{ceo_name}:


Analyst 2:
A follow-up on {aspect_5_details}. How confident are you that

{cfo_name}:


Analyst 3:
And for {aspect_4_details}, any update on ?

{exec_name}:


Analyst 4:
Just a final one — on {aspect_6_details}, is the improvement mostly ?

{cfo_name}:


Closing

{ceo_name}:
Thank you again for joining us today. We remain confident in our long-term growth story and are committed to disciplined execution. We appreciate your continued interest and support.

Operator:
Thank you. This concludes today’s call. You may now disconnect.
"""
),

("7", """
Operator:
Good day and thank you for standing by. Welcome to the {company_name} {quarter} Earnings Conference Call. At this time, all participants are in a listen-only mode. After the speakers’ presentation, there will be a Q&A session. Today’s call is being recorded.
I would now like to hand the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}, {ir_title}:
Thank you, Operator. Good {time_of_day}, everyone, and welcome to {company_name}’s earnings call. Joining me today are {ceo_name}, CEO; {cfo_name}, CFO; {coo_name}, COO; and {cto_name}, CTO.
Earlier today, we issued our earnings press release and presentation, which are available on our Investor Relations website. Please note this call may include forward-looking statements. With that, I’ll turn it over to {ceo_name}.

{ceo_name}, Chief Executive Officer:
Thanks, {ir_name}. Hello, everyone, and thank you for joining us.

This quarter, we saw meaningful progress across several fronts.

To start, {aspect_1_details}. This reflects.

We also continued to drive improvements through {aspect_2_details}, which.

Lastly, I want to briefly highlight {aspect_3_details}, where we’ve.

Now I’ll hand it over to {cfo_name} to discuss the financials in greater detail.

{cfo_name}, Chief Financial Officer:
Thanks, {ceo_name}, and good day, everyone.

From a financial perspective, we’re pleased with the breadth and durability of our results.

First, {aspect_4_details} has contributed meaningfully to.

Second, we saw positive contribution from {aspect_5_details}, which.

And although still early, {aspect_6_details} is.

With that, I’ll turn it to {coo_name} for a deeper look at operational performance.

{coo_name}, Chief Operating Officer:
Thanks, {cfo_name}.

From an operational lens, this was a solid quarter.

One of the highlights was {aspect_1_details}, particularly in.

Additionally, {aspect_5_details} has enabled more 

We’re also seeing early traction in {aspect_7_details}, where updated processes and .

Now I’ll pass it to {cto_name} for the tech and product update.

{cto_name}, Chief Technology Officer:
Thanks, {coo_name}.

Our product and engineering teams made excellent progress this quarter.

We launched key capabilities tied to {aspect_2_details}, supporting broader adoption and .

We’ve also support {aspect_6_details}, and.

And finally, on {aspect_7_details}, our new architecture .

Let’s now move on to the Q&A.

Q&A SESSION

Analyst 1:
Thanks. Could you expand on the {aspect_3_details} and whether?

{ceo_name}:


Analyst 2:
On {aspect_4_details}, how much ?

{cfo_name}:


Analyst 3:
Could you talk more about the rollout of features linked to {aspect_6_details}?

{cto_name}:


Analyst 4:
And finally, on {aspect_7_details}, is this?

{coo_name}:


Closing

{ceo_name}:
Thanks again to everyone for joining us today. We’re proud of the progress we’ve made and confident in our ability to execute in the quarters ahead.

Operator:
Thank you. This concludes today’s call. You may now disconnect.
"""
),

("8", """
Operator:
Good day and thank you for standing by. Welcome to the {company_name} {quarter} Earnings Conference Call. At this time, all participants are in a listen-only mode. After the speakers’ presentation, there will be a Q&A session. Today’s call is being recorded.
I would now like to hand the call over to {ir_name}, {ir_title}. Please go ahead.

{ir_name}, {ir_title}:
Thank you, Operator. Good {time_of_day}, everyone, and welcome to {company_name}’s earnings call. With me today are {ceo_name}, CEO; {cfo_name}, CFO; {coo_name}, COO; and {cto_name}, CTO.
Earlier today, we published our press release and earnings slides, which are available on our IR website. Please note that this call may contain forward-looking statements. With that, I’ll turn it over to {ceo_name}.

{ceo_name}, Chief Executive Officer:
Thanks, {ir_name}, and welcome, everyone.

We had a strong quarter with performance driven by several key initiatives. First, I’d like to talk, {aspect_1_details}, which reflects our continued execution on core growth priorities.

We also made meaningful progress with {aspect_2_details}, 

On a broader level, {aspect_3_details} supported our positioning 

I’ll now hand it over to {cfo_name} to walk you through the financials.

{cfo_name}, Chief Financial Officer:
Thanks, {ceo_name}, and hello, everyone.

This quarter’s financial results were underpinned by operational rigor and discipline. Let’s walk through the key metrics.

To start, {aspect_4_details} helped drive improvements in 

Additionally, {aspect_5_details} showed strong 

{aspect_6_details}, where we’ve increased 

Now I’ll pass it to {coo_name} to provide color on execution.

{coo_name}, Chief Operating Officer:
Thanks, {cfo_name}.

From a delivery and operations standpoint, this was one of our more efficient quarters in recent memory.

A big part of that was {aspect_1_details}, which allowed us to 

We also saw execution gains related to {aspect_5_details}, including

Lastly, we began pilots tied to {aspect_7_details}, where early signs are 

Now I’ll turn it over to {cto_name} to discuss

{cto_name}, Chief Technology Officer:
Thanks, {coo_name}.

On the technology side, our teams delivered important milestones across multiple streams.

First, we completed major feature work aligned with {aspect_2_details}, especially 
 
We also rolled out enhancements supporting {aspect_6_details}, 

One final point — we’ve made structural improvements to better enable {aspect_8_details}, 

Let’s now open the floor for Q&A.

Q&A SESSION

Analyst 1:
Thanks. You mentioned gains in {aspect_3_details}. What gives you confidence that these are sustainable?

{ceo_name}:

Analyst 2:
On {aspect_4_details}, is this ?

{cfo_name}:

Analyst 3:
Can you elaborate on early traction with {aspect_7_details}?

{coo_name}:

Analyst 4:
How are you thinking about long-term opportunity in {aspect_8_details}?

{cto_name}:

Closing

{ceo_name}:
Thanks again to everyone for joining us. We’re energized by the results this quarter and remain focused on disciplined execution and strategic expansion. Looking forward to sharing continued progress next time.

Operator:
Thank you. This concludes today’s call. You may now disconnect.
"""
)
])