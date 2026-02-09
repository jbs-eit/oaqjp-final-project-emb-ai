"""
Flask server for app.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detector import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Render index on base route.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
    """
    Runs emotion detecion with Watson AI.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text
    response = emotion_detector(text_to_analyze)

    # Extract
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalid text! Please try again!.'

    # Return a formatted string
    return (f"For the given statement, the system response is 'anger': {anger_score}, "
            f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
            f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 