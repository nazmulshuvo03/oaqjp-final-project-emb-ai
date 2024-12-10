import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        ooi = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = ooi['anger']
        disgust_score = ooi['disgust']
        fear_score = ooi['fear']
        joy_score = ooi['joy']
        sadness_score = ooi['sadness']
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': None if response.status_code == 400 else find_dominant_emotion(anger_score, disgust_score, fear_score, joy_score, sadness_score)
    }


def find_dominant_emotion(anger, disgust, fear, joy, sadness):
    max_emotion = max(anger, disgust, fear, joy, sadness)
    if max_emotion == anger:
        return 'anger'
    elif max_emotion == disgust:
        return 'disgust'
    elif max_emotion == fear:
        return 'fear'
    elif max_emotion == joy:
        return 'joy'
    elif max_emotion == sadness:
        return 'sadness'
    else:
        return None
