import requests
import json

def emotion_detector(text_to_analyse):
    # Set the parameters to call the emotion predict
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Call emotion predict with the text to analyse
    response = requests.post(url, json=input_json, headers=headers)

    # Check if the server returns a 400 status code (e.g., for blank entries)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }  

    # Parse the json text into a dictionary
    emotion_dictionary = json.loads(response.text)

    # Extract the list of emotion predictions.
    predictions = emotion_dictionary.get('emotionPredictions', [])

    # Handle empty predictions
    if not predictions:
        return {
            'anger': 0,
            'disgust': 0,
            'fear': 0,
            'joy': 0,
            'sadness': 0,
            'dominant_emotion': None
        }

    # Extract the list of emotion predictions.
    predictions = emotion_dictionary.get('emotionPredictions', [])

    # Extract the emotion scores from the predictions.
    emotion_scores = predictions[0].get('emotion', {})

    # Define the emotions to extract
    required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']

    # Extract each required emotion's score, defaulting to 0 if a key is missing.
    extracted_emotions = {emotion: emotion_scores.get(emotion, 0) for emotion in required_emotions}

    # Find dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the emotions with their scores and the dominant emotion
    return {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }
	