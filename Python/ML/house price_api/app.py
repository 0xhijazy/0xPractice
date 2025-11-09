from flask import Flask, jsonify, request
import joblib
import numpy as np

app = Flask(__name__)


model = joblib.load("house_price.pkl")

@app.route("/predict", methods=["GET"])
def predict():
    try:
        
        lot_area = float(request.args.get("lot_area"))
        year_built = float(request.args.get("year_built"))
        gr_liv_area = float(request.args.get("gr_liv_area"))
        full_bath = float(request.args.get("full_bath"))
        bedroom = float(request.args.get("bedroom"))
        garage = float(request.args.get("garage"))

        
        features = np.array([[lot_area, year_built, gr_liv_area, full_bath, bedroom, garage]])
        prediction = model.predict(features)[0]

        return jsonify({
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)


"""

ساختار تست

"http://127.0.0.1:5000/predict?lot_area=8450&year_built=2003&gr_liv_area=1710&full_bath=2&bedroom=3&garage=2"
   
"""