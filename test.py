import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2016-05-19',
    iam_apikey='KRnaLFSHyWwMX4BQ87--BxYDMdSoraFPj-noSvdEFHW7',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)
text = "'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'"

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
#print(tone_analysis[document_tone][tone_categories][0][tones][0][score])
