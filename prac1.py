import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2016-05-19',
    iam_apikey='KRnaLFSHyWwMX4BQ87--BxYDMdSoraFPj-noSvdEFHW7',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)
text ="die in hell"
'''
 ['You are bad in this','You are useless','You are retarded','Just kill yourself',"You are no good", "You're doing a good job","You should work hard","Your code looks great","The project could be more impressive than this",\
"Chatting is very fun",	'The weather is pretty good today',	'How are you?', "Don't worry, you'll do better next time", "I like your new dress", "I hope you die"]
'''




tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))

##variables:

#emotion_tone
anger = (tone_analysis["document_tone"]["tone_categories"][0]["tones"][0]["score"])
disgust = (tone_analysis["document_tone"]["tone_categories"][0]["tones"][1]["score"])
fear = (tone_analysis["document_tone"]["tone_categories"][0]["tones"][2]["score"])
joy = (tone_analysis["document_tone"]["tone_categories"][0]["tones"][3]["score"])
sadness = (tone_analysis["document_tone"]["tone_categories"][0]["tones"][4]["score"])

#language_tone
analytical = (tone_analysis["document_tone"]["tone_categories"][1]["tones"][0]["score"])
confident = (tone_analysis["document_tone"]["tone_categories"][1]["tones"][1]["score"])
tentative = (tone_analysis["document_tone"]["tone_categories"][1]["tones"][2]["score"])

#social_tone
openness = (tone_analysis["document_tone"]["tone_categories"][2]["tones"][0]["score"])
conscientiousness = (tone_analysis["document_tone"]["tone_categories"][2]["tones"][1]["score"])
extraversion = (tone_analysis["document_tone"]["tone_categories"][2]["tones"][2]["score"])
agreeableness =  (tone_analysis["document_tone"]["tone_categories"][2]["tones"][3]["score"])
emtional_range =  (tone_analysis["document_tone"]["tone_categories"][2]["tones"][4]["score"])

#mean_scores

anger_mn = .04#anger_mean
anger_sd = .027203

disgust_mn = .04
disgust_mn = 0

fear_mn =.064545
fear_sd =.069622

joy_mn =.609
joy_sd =.308469

sadness_mn =.084545
sadness_sd =.109669

emotional_range_mn =.446086091
emotional_range_sd =.215674682


#bullying means and sd:

anger_mnbad =.24375 #anger_mean
anger_sdbad = .424026

disgust_mnbad = .09
disgust_sdbad =0.01

fear_mnbad =.3475
fear_sdbad =.365933

joy_mnbad =.13
joy_sdbad =0

sadness_mnbad =.5275
sadness_sdbad =.392528

emotional_range_mnbad =.29482275
emotional_range_sdbad =.111930793







# predicting bullying

def bully(angr, dsgst, sdns, fer):
    if ((anger_mnbad - anger_sdbad) <= angr <= (anger_mnbad + anger_sdbad)) and ((disgust_mnbad - disgust_sdbad) <= dsgst <= (disgust_mnbad + disgust_sdbad)) and ((sadness_mnbad - sadness_sdbad) <= sdns <= (sadness_mnbad + sadness_sdbad)) and ((fear_mnbad - fear_sdbad) <= fer <= (fear_mnbad + fear_sdbad)):
        return True
    else:
        return False


print(bully(anger, disgust, sadness, fear))

def text_edit(str):
    if ((bully(anger, disgust, sadness, fear))== True):
        str = "*" * (len(str))
        return str
    else:
        return str

print(text_edit(text))
