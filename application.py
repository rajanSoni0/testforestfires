from flask import Flask, request, render_template, redirect, url_for
import pickle
import numpy as np

application = Flask(__name__)
app = application

ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))


# ------------- HOME PAGE -----------------
@app.route("/")
def home():
    result = request.args.get("result")  # None if not predicting
    return render_template("home.html", result=result)


# ------------- PREDICT DATA --------------
@app.route("/predictdata", methods=["POST"])
def predict_datapoint():

    # Get input values
    try:
        Temperature = float(request.form['Temperature'])
        RH          = float(request.form['RH'])
        Ws          = float(request.form['Ws'])
        Rain        = float(request.form['Rain'])
        FFMC        = float(request.form['FFMC'])
        DMC         = float(request.form['DMC'])
        ISI         = float(request.form['ISI'])
        Classes     = float(request.form['Classes'])
        Region      = float(request.form['Region'])
    except:
        return redirect(url_for("home"))

    # Prepare input
    data = np.array([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
    scaled = standard_scaler.transform(data)
    prediction = ridge_model.predict(scaled)[0]

    # redirect with result
    return redirect(url_for("home", result=round(prediction, 3)))


# ------------- MAIN -----------------
if __name__ == "__main__":
    app.run(debug=True)