import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyze text and detect emotions using Watson NLP service.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    body_json =  {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, json=body_json, headers=header, timeout=7)
    except (
        requests.exceptions.RequestException,
        requests.exceptions.ConnectionError,
    ) as e:
        print(e)
        return {"error": e.args}

    try:
        response.raise_for_status()
    except Exception  as e:
        print("status error")
        return {"error": e.args}

    formatted_response = json.loads(response.text)

    if "emotionPredictions" not in formatted_response:
        return {"error": '"emotionPredictions" not in formatted_response'}

    emotion_predictions = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotion_predictions.items(), key=lambda item: item[1])[0]
    emotion_predictions["dominant_emotion"] = dominant_emotion

    return emotion_predictions


if __name__ == "__main__":
    emo_dict = dict(
        joy="Great to meet @BrightonChoir @MJParanzino tonight. What a lively and enthusiastic bunch! Look forward to working with you again!",
        fear="She chuckles, shaking her head. 'No...I just have a really vivid imagination, I guess. It happens when you meet someone",
        anger="Losing the will 2 live with @virginmedia business bb gone down on hold for 23 minutes &amp; whoever picked up cut me off",
        sadness="it's still not sunk in that im seeing joe next month, im so grateful and excited shit",
        joy_2="Sometimes I watch shitty tv to reinforce never giving up cuz if something is that fucking awful on tv, I still stand a chance.",
        fear_2="#Everything you've ever wanted awaits you on the other side of #fear . #IfIWasTheOppositeSex #AskAMan",
        anger_2="@SkyUK what a joke!! Cut our internet off early 'by mistake' and then don't reinstate it when we no longer need an engineer",
    )
    for emo, text in emo_dict.items():
        emotion_predictions = emotion_detector(text)
        print(emo, emotion_predictions)
