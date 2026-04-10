from flask import Flask, render_template, request, jsonify
import pickle
import os
from data_fetch import get_live_data, simulate_flood
from translate_llm import translate
from send_sms import send_sms

app = Flask(__name__)

MODEL_PATH = "flood_model.pkl"
if os.path.exists(MODEL_PATH):
    model = pickle.load(open(MODEL_PATH, "rb"))
else:
    model = None
    print("WARNING: flood_model.pkl not found. Run train_model.py first.")


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/api/data", methods=["GET"])
def get_data():
    mode = request.args.get("mode", "live")
    
    if mode == "simulate":
        data = simulate_flood()
        is_simulated = True
    else:
        data = get_live_data()
        is_simulated = False

    prediction = 0
    if model:
        pred = model.predict([[data["rainfall"], data["water_level"], data["humidity"]]])
        prediction = int(pred[0])
    else:
        # Fallback rule-based prediction
        score = (data["rainfall"] / 300) * 0.5 + \
                (data["water_level"] / 15) * 0.3 + \
                (data["humidity"] / 100) * 0.2
        
        prediction = 1 if score > 0.45 else 0

    return jsonify({
        "rainfall": data["rainfall"],
        "humidity": data["humidity"],
        "water_level": data["water_level"],
        "prediction": prediction,
        "is_simulated": is_simulated
    })


@app.route("/api/alert", methods=["POST"])
def send_alert():
    body = request.get_json()
    lang = body.get("language", "eng_Latn")

    message = "Flood Warning in your area. Please move to a safe location immediately."

    try:
        translated = translate(message, lang)
        send_sms(translated)

        print("SMS Sent:", translated)   # 👈 add this line

        return jsonify({
            "success": True,
            "translated": translated
        })

    except Exception as e:
        print("ERROR:", str(e))   # 👈 add this line

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)