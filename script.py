from flask import Flask, render_template, request

app = Flask(__name__)

# Replace this with your AI logic for processing user messages
def process_message(message):
    response = "Hi there! How can I help you today?"  # Replace with your AI response logic
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    user_message = request.form["message"]
    ai_response = process_message(user_message)
    return render_template("index.html"), ai_response
