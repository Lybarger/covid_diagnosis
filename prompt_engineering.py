
import os

api_key_file = "/projects/klybarge/OPENAI_API_KEY"
with open(api_key_file, "r") as file:
    api_key = file.read().strip()

# Set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = api_key

import openai

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

post = """9/4 10 yo daughter tests positive 9/7 I (39F) I wake up with a sore throat and headache./
Test positive with very faint line. Day 0. Day 0: Sore throat, headache, temp ranging from normal to 99.5/
(high for me), body aches Day 1: Temp ranging from normal to 100.2, sort of tired, very mild sore throat,/ 
very mild body aches Day 2: Temp ranging from normal to 99.9, cough has begun, no sore throat, no body aches,/
head congestion, sneezing, test positive instantly with very bold line Day 3: Temp ranging from normal to 99.1,/
cough continues, head congestion continues, ears wont pop, no sneezing, sweating after low exertion, sudden and/
complete loss of smell and taste. This virus is a wild ride. This morning (day 3) I had perfectly normal taste/
and smell. Now Im staring at a box of Cocoa Pebbles and other delicious Im sick and will drown my sorrows in food/
items that I added to my shopping list this morning. The minute my ex husband delivered the cereal, as well as/
other groceries for me, my senses disappeared. Id like to say Im getting better, but each day brings a new surprise!"""

propmt = """You have the role of a feature extractor tasked with analyzing a Reddit/
    post where a user describes their COVID experience. Your objective is to extract a/
    set of features from the provided information and generate an output list. It's/
    important to note that the user may not always explicitly mention the features./
    They might use abbreviations like "M" for "Male" or describe symptoms like "high/
    temperature" instead of "fever". To assist you in this task, I will provide a list
    of desired features and some of their associated synonyms. While you should consider/
    these suggestions, feel free to utilize your extensive knowledge of synonyms and /
    related terms for these features.

The output should include a list of all the observed features in the following format:
OUTPUT: [FEATURE, FEATURE, FEATURE, FEATURE]

When you extract a feature, look if its one of the capatelized features enclosed in the asterisks below: 
If it is, include it in the output.
If not, look if it is a synonym to any of the capatelized features enclosed in the asterisks below:
If it is, include the capetalized term in the asterisks that this feature is a synonym to. 
If not, don't include it.

The set of features (demographics and symptoms):
1.	*AGE 18 TO 30*: User explicitly state age between 18 and 30 years old. 
2.	*AGE MORE THAN 30*: User's age is greater than 30 years. 
3.	*MALE*: User identifies as male. 
4.	*FEMALE*: User identifies as female. 
5.	*ABDOMINAL PAIN*: User experiencing the symptom of abdominal pain. Example synonyms for abdominal pain include stomachache, tummy ache, stomach cramps, etc. 
6.	*BLUISH*: User experiencing the symptom of bluish discoloration. Example synonyms for bluish discoloration include blue tint, blue hue, cyanosis, etc. 
7.	*CHEST PAIN*: User experiencing the symptom of chest pain. Example synonyms for chest pain include heart pain, angina, chest tightness, etc. 
8.	*CHILLS*: User experiencing the symptom of chills. Example synonyms for chills include rigor, shivering, feeling cold, cold sweats, gooseflesh, night sweats, etc. 
9.	*CONFUSION*: User experiencing the symptom of confusion. Example synonyms for confusion include disorientation, mental fog, cognitive impairment, etc. 
10.	*COUGH*: User experiencing the symptom of cough. Example synonyms for cough include coughing, hacking, etc. 
11.	*DIARRHEA*: User experiencing the symptom of diarrhea. Example synonyms for diarrhea include loose stools, watery stool, frequent bowel movements, etc. 
12.	*DIFFICULTY BREATHING*: User experiencing the symptom of difficulty breathing. Example synonyms for difficulty breathing include breathlessness, dyspnea, etc. 
13.	*EXCESS SWEAT*: User experiencing the symptom of excessive sweating. Example synonyms for excess sweat include profuse sweating, hyperhidrosis, etc. 
14.	*FATIGUE*: User experiencing the symptom of fatigue. Example synonyms for fatigue include tiredness, exhaustion, lethargy, weakness etc. 
15.	*FEVER*: User experiencing the symptom of fever. Example synonyms for fever include high temperature, pyrexia, elevated body temperature, etc. 
16.	*HEADACHES*: User experiencing the symptom of headaches. Example synonyms for headaches include migraines, tension headaches, head pain, etc. 
17.	*JOINT PAIN*: User experiencing the symptom of joint pain. Example synonyms for joint pain include arthritis, joint inflammation, etc. 
18.	*LOSS OF APPETITE*: User experiencing the symptom of loss of appetite. Example synonyms for loss of appetite include anorexia, lack of appetite, decreased appetite, etc. 
19.	*LOSS OF BALANCE*: User experiencing the symptom of loss of balance. Example synonyms for loss of balance include unsteadiness, vertigo, dizziness, etc. 
20.	*LOSS OF SMELL*: User experiencing the symptom of loss of smell. Example synonyms for loss of smell include anosmia, olfactory dysfunction, etc. 
21.	*LOSS OF TASTE*:User experiencing the symptom of loss of taste. Example synonyms for loss of taste include ageusia, tastelessness, etc. 
22.	*MUSCLE ACHES*: User experiencing the symptom of muscle aches. Example synonyms for muscle aches include myalgia, muscle pain, etc. 
23.	*NUMBNESS*: User experiencing the symptom of numbness. Example synonyms for numbness include paresthesia, tingling, etc. 
24.	*PINKEYE*: User experiencing the symptom of pink eye. Example synonyms for pink eye include conjunctivitis, eye infection, etc. 
25.	*RED RASH*: User experiencing the symptom of a red rash. Example synonyms for red rash include skin eruption, skin inflammation, etc. 
26.	*RUNNY NOSE*: User experiencing the symptom of a runny nose. Example synonyms for runny nose include rhinorrhea, nasal discharge, etc. 
27.	*SHIVERING*: User experiencing the symptom of shivering. Example synonyms for shivering include tremors, shaking, chills, etc. 
28.	*SHORTNESS OF BREATH*: User experiencing the symptom of shortness of breath. Example synonyms for shortness of breath include breathlessness, dyspnea, difficulty breathing, etc. 
29.	*SLURRED SPEECH*: User experiencing the symptom of slurred speech. Example synonyms for slurred speech include speech impairment, speech difficulties, etc. 
30.	*SORE THROAT*: User experiencing the symptom of a sore throat. Example synonyms for sore throat include pharyngitis, throat pain, etc. 
31.	*UNEXPLAINED RASH*: User experiencing the symptom of an unexplained rash. Example synonyms for unexplained rash include unknown rash, mysterious rash, etc. 
32.	*VOMITING*: User experiencing the symptom of vomiting. Example synonyms for vomiting include throwing up, emesis, nausea, etc. 
33.	*WHEEZING*: User experiencing the symptom of wheezing. Example synonyms for wheezing include whistling breath, labored breathing, etc. 

Important instructions to consider:
1-	Regardless of the synonymous terms employed in the post, the output should consist solely of the features indicated within the asterisks above. 
Example:
POST: “27M. I felt off on Tuesday was negative. Took a test Wednesday instantly positive - I had chills and EXTREME headache until probably Friday morning. I was able to work on Friday (WFH) and then today I was super tired. Plus having anxiety that I couldn't breathe but I think that is my anxiety and not shortness of breath... I hope. Anyway - my husband (vaxxed / boosted) and our two small kids have been downstairs this whole time and I'm locked in the bedroom. We run our air filters, I wear a mask to go to the bathroom, Lysol everything basically I'm trying my best to not give it to anyone. I'm still testing positive day 4? Which I think is normal.. so when can I be around them in a mask? Is it day 6? The kids and him have been feeling fine with no symptoms.”
CORRECT OUTPUT: [“AGE 18 TO 30 “, “MALE”, “CHILLS”, “HEADACHES”, “FATIGUE”, “DIFFICULTY BREATHING”]
WRONG OUTPUT: ["“AGE 18 TO 30 “, “MALE”, “CHILLS”, “HEADACHES”, “SUPER TIRED”, “DIFFICULTY BREATHING”]
2-	Sometimes there are no relevant features in the post, where the user will be talking about the experience in general. In this case return an empty list.
Example: 
POST: “I’m fully vaccinated for Covid but also currently battling my second infection in only 3-4 months. I’ve previously gone years without so much as a cold or needing to use any sick leave and always had a good bank. But I now find myself for the first time with no sick leave left. There is no longer any compensation to support people taking time off when they have Covid so they’re going to work, ill, in many cases because they have no choice (they need the money). So you go to work and you get Covid again. I tested positive today (Sunday) and having already exhausted all my leave from my last Covid bout and subsequent illnesses, I just seem to have been sick pretty much all year. So if I don’t go to work tomorrow it will be unpaid. I have 3 children and bills that need to be paid. How are we supposed to live with Covid?”
OUTPUT: []
3-	Sometimes there is a mention of a feature but it shouldn’t be included in the output. Like for example when someone says “I don’t have fever” or when its in a question “have you experienced runny nose during your illness?”
Example:
POST: “Hi all, After avoiding everything and everyone for the past 2 years it finally got me. Just thought I would share my experience and it hopefully may help some people out there. I’ll keep this brief and to the point. 34 y/o F with no other PMHx. Double vaccinated and boosted with Pfizer. Last Booster Vaccine on 13-Dec-2021. 1/17: Felt a little off from the morning, overall, I was super tired and fatigue. I also had a very minor throat discomfort. It wasn’t a sore throat or anything but an annoyance. I knew something was off, so I drank a lot of liquids that day and kept it very easy. That evening started to become more anxious as I felt my symptoms (sx) getting worse. Decided to end the night with a Tylenol Cold/Flu and go to bed. Overall sleep quality was very poor that night. 1/18: Woke up sick and not feeling well. No headache, no cough, no loss of taste or smell, minor throat discomfort, a little bit of a runny nose and mild-grade fever (~100.5). Knew it was COVID, so I decided to get tested. Scheduled a PCR test that day and picked up some home COVID”
OUTPUT: [“AGE MORE THAN 30”, “FEMALE”, “FATIGUE”, “RUNNY NOSE”, “FEVER”]
Now it is your turn:
POST: "As title says really. Exposed to a few positive cases over the past fortnight. A few days ago I woke up with whole body aches, fever on and off, nausea, fatigue. Tested negative on lateral flows. Day later and still slightly achey but loads better. Negative lateral flows again. Now this morning Im again feeling marginally better, just a slight sore throat and aches. Faint positive line on first test yet I did another straight after and it was negative?! Just wondering if anyone else has had this? Awaiting a PCR to confirm as isolating regardless."
"""
prompt2 = """
Based on the provided information, you have the role of a feature extractor tasked with analyzing a Reddit post where a user describes their COVID experience. Your objective is to extract a set of features from the information and generate an output list. The output should include a list of observed features in a specific format.

The features you need to extract are divided into two categories: demographics and symptoms. Here is a breakdown of the features and their associated synonyms. I will capetalize the gold standard features and enclose them in asterisks:

Demographics:
1. *AGE 18 TO 30*
2. *AGE MORE THAN 30*
3. *MALE*
4. *FEMALE*

if the post doesn't explicitly mention demographics, dont include any in the output.

Symptoms:
5. *ABDOMINAL PAIN*: Example synonyms include stomachache, tummy ache, stomach cramps.
6. *BLUISH*: Example synonyms include blue tint, blue hue, cyanosis.
7. *CHEST PAIN*: Example synonyms include heart pain, angina, chest tightness.
8. *CHILLS*: Example synonyms include rigor, shivering, feeling cold, cold sweats.
9. *CONFUSION*: Example synonyms include disorientation, mental fog, cognitive impairment.
10. *COUGH*: Example synonyms include coughing, hacking.
11. *DIARRHEA*: Example synonyms include loose stools, watery stool, frequent bowel movements.
12. *DIFFICULTY BREATHING*: Example synonyms include breathlessness, dyspnea.
13. *EXCESS SWEAT*: Example synonyms include profuse sweating, hyperhidrosis.
14. *FATIGUE*: Example synonyms include tiredness, exhaustion, lethargy, weakness.
15. *FEVER*: Example synonyms include high temperature, pyrexia, elevated body temperature.
16. *HEADACHES*: Example synonyms include migraines, tension headaches, head pain.
17. *JOINT PAIN*: Example synonyms include arthritis, joint inflammation.
18. *LOSS OF APPETITE*: Example synonyms include anorexia, lack of appetite, decreased appetite.
19. *LOSS OF BALANCE*: Example synonyms include unsteadiness, vertigo, dizziness and nausea.
20. *LOSS OF SMELL*: Example synonyms include anosmia, olfactory dysfunction.
21. *LOSS OF TASTE*: Example synonyms include ageusia, tastelessness.
22. *MUSCLE ACHES*: Example synonyms include myalgia, muscle pain, aches.
23. *NUMBNESS*: Example synonyms include paresthesia, tingling.
24. *PINKEYE*: Example synonyms include conjunctivitis, eye infection.
25. *RED RASH*: Example synonyms include skin eruption, skin inflammation.
26. *RUNNY NOSE*: Example synonyms include rhinorrhea, nasal discharge.
27. *SHIVERING*: Example synonyms include tremors, shaking, chills.
28. *SHORTNESS OF BREATH*: Example synonyms include breathlessness, dyspnea.
29. *SLURRED SPEECH*: Example synonyms include speech impairment, speech difficulties.
30. *SORE THROAT*: Example synonyms include pharyngitis, throat pain.
31. *UNEXPLAINED RASH*: Example synonyms include unknown rash, mysterious rash.
32. *VOMITING*: Example synonyms include throwing up, emesis.
33. *WHEEZING*: Example synonyms include whistling breath, labored breathing.

Your task is to analyze the users post and extract the mentioned features. If a synonym is found, don't include it itself in the output, but include the gold standard features that it belongs to.  Once you have extracted the features, generate an output list in the following format:
OUTPUT: [FEATURE, FEATURE, FEATURE, FEATURE]


Based on the provided instructions and examples, let's analyze the given posts and extract the relevant features while adhering to the rules:

1. POST: "27M. I felt off on Tuesday was negative. Took a test Wednesday instantly positive - I had chills and EXTREME headache 
until probably Friday morning. I was able to work on Friday (WFH) and then today I was super tired. Plus having anxiety that I 
couldn't breathe but I think that is my anxiety and not shortness of breath... I hope. Anyway - my husband (vaxxed / boosted) 
and our two small kids have been downstairs this whole time and I'm locked in the bedroom. We run our air filters, I wear a mask
to go to the bathroom, Lysol everything basically I'm trying my best to not give it to anyone. I'm still testing positive day 4?
Which I think is normal.. so when can I be around them in a mask? Is it day 6? The kids and him have been feeling fine with no
symptoms."

CORRECT OUTPUT: [“AGE 18 TO 30 “, “MALE”, “CHILLS”, “HEADACHES”, “FATIGUE”, “DIFFICULTY BREATHING”]
WRONG OUTPUT: [“AGE 18 TO 30 “, “MALE”, “CHILLS”, “HEADACHES”, “SUPER TIRED”, “DIFFICULTY BREATHING”, "ANXIETY"] -> wrong because it included a synonym in the output, and not its gold standard

2. If the post has no demographics and no symptoms, return an empty list
Example:

POST: "I’m fully vaccinated for Covid but also currently battling my second infection in only 3-4 months. I’ve previously gone
years without so much as a cold or needing to use any sick leave and always had a good bank. But I now find myself for the first
time with no sick leave left. There is no longer any compensation to support people taking time off when they have Covid, so 
they’re going to work, ill, in many cases because they have no choice (they need the money). So you go to work and you get Covid 
again. I tested positive today (Sunday) and having already exhausted all my leave from my last Covid bout and subsequent illnesses,
I just seem to have been sick pretty much all year. So if I don’t go to work tomorrow it will be unpaid. I have 3 children and
bills that need to be paid. How are we supposed to live with Covid?"

OUTPUT: []

3. POST: "Hi all, After avoiding everything and everyone for the past 2 years it finally got me. Just thought I would share my 
experience, and it hopefully may help some people out there. I’ll keep this brief and to the point. 34 y/o F with no other PMHx.
Double vaccinated and boosted with Pfizer. Last Booster Vaccine on 13-Dec-2021. 1/17: Felt a little off from the morning, overall,
I was super tired and fatigue. I also had a very minor throat discomfort. It wasn’t a sore throat or anything but an annoyance. 
I knew something was off, so I drank a lot of liquids that day and kept it very easy. That evening started to become more anxious
as I felt my symptoms (sx) getting worse. Decided to end the night with a Tylenol Cold/Flu and go to bed. Overall sleep quality
was very poor that night. 1/18: Woke up sick and not feeling well. No headache, no cough, no loss of taste or smell, minor
throat discomfort, a little bit of a runny nose, and mild-grade fever (~100.5). Knew it was COVID, so I decided to get tested.
Scheduled a PCR test that day and picked up some home COVID."

OUTPUT: [“AGE MORE THAN 30”, “FEMALE”, “FATIGUE”, “RUNNY NOSE”, “FEVER”]


Please note that the mentioned features are extracted based on the rules provided, and only the features related to the person talking himself, not to other people he is talking about.

Now its your turn. 
POST: "i had covid in january of this year and it sucked big time, i was sick for about two weeks. left me with POTS or IST, not sure which is the right diagnosis. anyways, lately my tachycardia has been flaring up so i've been resting a lot. had a uti so i went to urgent care, then suddenly when i got home i had a notification i was exposed. this was two days ago. today i tested positive with a PCR test. i am absolutely fucking terrified. i don't want to die. i'm not vaccinated because i was scared it would aggravate my long covid. i feel so so so guilty that i am not vaccinated and i'm truly terrified i'm going to die. i have no heart damage, no lung damage, just sinus tachycardia &amp; i am on beta blockers. i'm 20 years old.
"
OUTPUT:
"""


response = get_completion(prompt2)
print(response)

