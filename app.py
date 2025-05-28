from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from school_bot import get_school_response

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")  # ← this renders your chatbot page

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"response": "Please say something!"})
    
    try:
        response = get_school_response(user_message)
    except Exception as e:
        print("Error in get_school_response:", e)
        response = "There was an error processing your message."
    
    return jsonify({"response": response})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

