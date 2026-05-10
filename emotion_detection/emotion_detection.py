import requests
import json

def emotion_detector(text_to_analyse):
    """
    Menganalisis teks untuk mendeteksi emosi menggunakan layanan web,
    dengan penanganan error koneksi.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json = myobj, headers=header, timeout=5)
    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None,
            'sadness': None, 'dominant_emotion': None
        }

    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None,
            'sadness': None, 'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    if 'emotionPredictions' not in formatted_response:
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None,
            'sadness': None, 'dominant_emotion': None
        }

    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_predictions.items(), key=lambda item: item[1])[0]
    emotion_predictions['dominant_emotion'] = dominant_emotion

    return emotion_predictions