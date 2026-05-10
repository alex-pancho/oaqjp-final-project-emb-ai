from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    anger = response.get('anger', "not found")
    disgust = response.get('disgust', "not found")
    fear = response.get('fear', "not found")
    joy = response.get('joy', "not found")
    sadness = response.get('sadness', "not found")
    domina = response.get('dominant_emotion', "not found")

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {domina}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)