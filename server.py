from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def get_emotion():

    text_to_analyse = request.args.get('textToAnalyze')
    # Strip any leading and trailing quotation marks if they exist
    if text_to_analyse.startswith('"') and text_to_analyse.endswith('"'):
        text_to_analyse = text_to_analyse[1:-1]
    elif text_to_analyse.startswith("'") and text_to_analyse.endswith("'"):
        text_to_analyse = text_to_analyse[1:-1]
    result = emotion_detector(text_to_analyse)

    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)