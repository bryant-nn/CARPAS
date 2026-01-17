from collections import OrderedDict

transcript_template_dict = OrderedDict([
    ("4", """
Host:
Good day and welcome to today’s press briefing from the Centers for Disease Control and Prevention (CDC). I’m {host_name}, your host. Joining us today are {official_1}, {official_2}, and {official_3}.

We begin with the latest developments. Let’s turn to {official_1} for an overview.

{official_1}:
Thank you, {host_name}. Good {time_of_day}, everyone.

Let’s start with today’s situation:

  {aspect_2_details}

  {aspect_3_details}

These data points reflect the impact of ..., but also highlight ... . I’ll now pass it to {official_2} for updates on ... .

{official_2}:
Thanks, {official_1}.

Before moving on, I’d like to expand on {official_1}’s comments regarding ... :

  {aspect_2_followup}

Now, concerning ... :

  {aspect_3_details}

I’ll hand it over to {official_3}, who will touch on our ... efforts, and then revisit ... .

{official_3}:
Thank you, {official_2}.

  {aspect_4_details}

Also, to supplement what {official_3} shared earlier about ... :

  {aspect_3_details}
     
  {aspect_1_details}

We’ve seen positive signs, but also remain cautious as new trends develop. That concludes our summary for today.

Let’s move into the Q&A.

Q&A Session

Reporter 1:
Can you clarify the next steps regarding {aspect_2}?

{official_1}:
Yes, we’re currently executing {aspect_2_followup}, including ... .

{official_2}:
If I may add — our {aspect_2_details} ... .

Reporter 2:
For the international topic raised by {official_3}, what’s the ... ?

{official_3}:
We’re anticipating rollout of {aspect_4_plan}, with results expected by {aspect_4_timeline}.

Reporter 3:
About the statistics mentioned earlier, are you expecting the current trend to reverse?

{official_1}:
That’s something we’re watching closely. As mentioned, {aspect_1_trend}, ... .

Closing Remarks

{official_3}:
Thank you for your questions. We’re grateful for the public’s cooperation and will continue to provide updates as we learn more.

Host:
That concludes today’s press conference from the CDC. Thank you to all media attendees. Stay safe and take care.
"""),

("5", """
Host:
Good day and welcome to today’s press briefing from the Centers for Disease Control and Prevention (CDC). I’m {host_name}, your host. Joining us today are {official_1}, {official_2}, and {official_3}.

Let’s begin with an overview of the current situation. I’ll now turn it over to {official_1}.

{official_1}:
Thank you, {host_name}. Good {time_of_day}, everyone.

We’ll start with today’s key information:

  {aspect_3_details}

  {aspect_2_details}

These developments highlight ... . Now, I’ll hand over to {official_2} for additional context and updates.

{official_2}:
Thank you, {official_1}.

Let me first expand briefly on {aspect_2}, particularly the ... :

  {aspect_2_followup}

  {aspect_1_details}

Additionally, there are important changes in ... :

  {aspect_4_details}

These updates reflect ... . I’ll now turn to {official_3} for information on ... .

{official_3}:
Thank you, {official_2}.

  {aspect_5_details}

  {aspect_1_supplement}

We are seeing early indicators of {aspect_1_trend}, but we remain ... .

Q&A Session

Reporter 1:
On the topic of {aspect_2}, can you explain what ?

{official_1}:
Yes, we are evaluating and {aspect_2_followup} is being ... .

{official_2}:
To add to that, ... .
 
Reporter 2:
About the policy adjustments mentioned, what’s the aspect_4_question?

{official_2}:
We aim to initiate {aspect_4_plan} starting next Monday, with nationwide coordination in place.

Reporter 3:
can you explain more on {aspect_5}?

{official_3}:
Certainly. We’re currently {aspect_5_details} .

Closing Remarks

{official_3}:
Thank you all. The CDC remains committed to transparency and collaboration as we move through this phase of the response.

Host:
That concludes today’s press conference from the CDC. Thank you for attending, and please continue to follow health guidance.
"""),

("6", """
Host:
Good day, and welcome to today’s press conference from the Centers for Disease Control and Prevention (CDC). I’m {host_name}, and I’ll be facilitating today’s briefing. With me are {official_1}, {official_2}, and {official_3}.

Let’s begin with an update on the overall situation. {official_1}, please go ahead.

{official_1}:
Thank you, {host_name}. Good {time_of_day}, everyone.

We’ll start with the current status across key areas:

  {aspect_1_details}

  Updates include: {aspect_2_details}
  {aspect_3_details}

I’ll now pass things over to {official_2} for updates on healthcare operations and ongoing public health efforts.

{official_2}:
Thanks, {official_1}.

To complement the previous points, I’d like to elaborate on a few ongoing developments:

  {aspect_2_followup}

  {aspect_4_details}

  {aspect_5_details}

Next, {official_3} will cover international coordination efforts and offer additional context on today’s data.

{official_3}:
Thank you, {official_2}.

Here are the latest on our international partnerships and comparisons:

  {aspect_6_details}

I would also like to revisit the trends mentioned earlier:

  {aspect_1_supplement}

Finally, let me highlight one ... :

  {aspect_3_details}

We’ll continue to monitor these closely. That concludes our prepared updates. We’ll now open the floor for questions.

Q&A Session

Reporter 1:
{aspect_2_question}

{official_1}:
Thank you. {aspect_2_followup}

Reporter 2:
{aspect_4_question}

{official_2}:
We’re currently working on {aspect_4_plan} and expect outcomes by {aspect_4_timeline}.

Reporter 3:
{aspect_5_question}

{official_3}:
That’s ongoing. We’re coordinating closely with {aspect_5_details}.

Reporter 4:
{aspect_6_question}

{official_3}:
We’ve increased monitoring and expect more clarity on ... .

Reporter 5:
{aspect_1_question}

{official_1}:
It’s still early to call a clear trend, but {aspect_1_trend} is something we’re watching closely.

Closing Remarks

{official_3}:
Thank you to everyone. As always, we urge continued cooperation and will provide further updates as needed.

Host:
That concludes today’s CDC briefing. Stay safe and thank you for joining.
"""),

("7", """
Host:
Good day and welcome to today’s press briefing from the Centers for Disease Control and Prevention (CDC). I’m {host_name}, and I’ll be moderating today’s session. With me are {official_1}, {official_2}, {official_3}, {official_4}.

Let’s begin with a situational overview. {official_1}, please start us off.

{official_1}:
Thank you, {host_name}, and good {time_of_day}, everyone.

Let me begin with today’s key national updates:

  {aspect_1_details}

  {aspect_2_details}

I’ll now turn it over to {official_2} to provide more depth on operational and healthcare responses.

{official_2}:
Thank you, {official_1}.

To expand on what’s been shared so far: {aspect_2_followup}

Now, updates on the ... and response efforts: {aspect_3_details}

We’ve also implemented recent policy adjustments: {aspect_4_details}

Let me invite {official_3} to speak on international and public sentiment issues.

{official_3}:
Thank you, {official_2}.

Collaboration continues on several fronts: {aspect_5_details}

{aspect_6_details}
 
{aspect_3_supplement}

To close this section, I’ll turn to {official_4} for additional insight on ... .

{official_4}:
Thank you, {official_3}.

We’re continuing to track ... :

  {aspect_7_details}
  {aspect_1_supplement}

Q&A Session

Reporter 1:
{aspect_1_question}

{official_1}:
Great question. We’ve seen {aspect_1_trend}, and we’re ... .

Reporter 2:
{aspect_2_question}

{official_2}:
We’ve enacted {aspect_2_followup}, including ... .

Reporter 3:
{aspect_4_question}

{official_2}:
We expect to implement {aspect_4_plan} and see progress within {aspect_4_timeline}.

Reporter 4:
{aspect_5_question}

{official_3}:
We’re working closely with {aspect_5_partners} to ensure coordinated delivery of {aspect_5_initiative}.

Reporter 5:
{aspect_6_question}

{official_3}:
... .

Reporter 6:
{aspect_7_question}

{official_4}:
... .

Closing Remarks

{closing_official}:
Thank you for your questions and continued vigilance. We will provide further updates as more data becomes available.

Host:
That concludes today’s CDC briefing. Stay safe, and thank you for joining us.
""")
,

("8", """
Host:
Good day, and welcome to today’s press briefing from the Centers for Disease Control and Prevention (CDC). I’m {host_name}, and I’ll be moderating today’s briefing. Joining me are {official_1}, {official_2}, {official_3}, {official_4}{official_5}.

Let’s begin with an update on the overall situation. {official_1}, please start us off.

{official_1}:
Thank you, {host_name}, and good {time_of_day}, everyone.

Here are today’s key updates:

  {aspect_3_details}

  {aspect_5_details}

I’ll now turn it over to {official_2} for further updates.

{official_2}:
Thanks, {official_1}.

Let me first follow up:

  {aspect_5_followup}

Now, let’s talk about ... : 
{aspect_2_details}

Additionally, we are continuing to ... :

{aspect_7_details}

Next, I’ll hand it over to {official_3} to give us insight on ... .

{official_3}:
Thank you, {official_2}.

In terms of ... :

  {aspect_1_details}
  {aspect_5_details}

To complement the above, we’ve also been making progress on ... :

  {aspect_6_details}

Let me now turn to {official_4} to discuss ... .

{official_4}:
Thank you, {official_3}.

In terms of ... :

  {aspect_4_details}

We’ve seen a significant ... :

  {aspect_8_details}
  {aspect_3_supplement}
Now, let's go into the Q&A portion of the session.

Q&A Session

Reporter 1:
{aspect_3_question}

{official_1}:
We’ve seen significant improvements in {aspect_3_trend}, but we ... .

Reporter 2:
{aspect_5_question}

{official_2}:
We’re expecting more clarity in the next {aspect_5_timeline}, and we’ll be adjusting accordingly.

Reporter 3:
{aspect_7_question}

{official_3}:
We’re closely ... .

Reporter 4:
{aspect_1_question}

{official_3}:
... . 

Reporter 5:
{aspect_6_question}

{official_2}:
... .

Reporter 6:
{aspect_8_question}

{official_4}:
We’re actively engaged with {aspect_8_initiative}, ... .

Closing Remarks

{closing_official}:
Thank you for your questions. We appreciate the public’s continued cooperation and commitment to safety.

Host:
That concludes today’s CDC briefing. Stay safe, and thank you for joining us.
""")

])