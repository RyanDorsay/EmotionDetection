"""
This module for runs the Emotion Detector on a Flask server.

It sets up a Flask server with an endpoint '/emotionDetector' that
receives text from the 'textToAnalyze' query parameter, processes it with the
emotion_detector function, and returns an HTML response with the detected emotions.
"""

from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def get_emotion():
    """
    Analyze given input text for emotions and return the result.

    This endpoint gets the value of the 'textToAnalyze' query parameter, strips any
    surrounding quotation marks, and passes the cleaned text to the emotion_detector
    function. If the dominant emotion is None, it responds with an error message;
    otherwise, it returns an HTML-formatted string with the emotion scores and the
    dominant emotion.
    """

    text_to_analyse = request.args.get('textToAnalyze')
    # Strip any leading and trailing quotation marks if they exist
    if text_to_analyse.startswith('"') and text_to_analyse.endswith('"'):
        text_to_analyse = text_to_analyse[1:-1]
    elif text_to_analyse.startswith("'") and text_to_analyse.endswith("'"):
        text_to_analyse = text_to_analyse[1:-1]
    result = emotion_detector(text_to_analyse)

    # Check if the dominant emotion is None. If so, display an error message.
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
