from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    def format_response(response_dict):
        emotions = ", ".join(f"'{emotion}': {score}" for emotion, score in response_dict.items() if emotion != "dominant_emotion")
        dominant_emotion = response_dict["dominant_emotion"]

        if dominant_emotion is None:
            return "Invalid text! Please try again!"
        else:
            return f"For the given statement, the system response is {emotions}. The dominant emotion is {dominant_emotion}."

    formatted_response = format_response(response)
    return formatted_response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)