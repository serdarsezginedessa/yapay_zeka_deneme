from flask import Flask, request, render_template
import pickle

# Model ve vectorizer yükle
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def tahmin_et(metin):
    metin_vec = vectorizer.transform([metin])
    return model.predict(metin_vec)[0]

# Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tahmin = None
    if request.method == "POST":
        metin = request.form.get("metin", "")
        tahmin = tahmin_et(metin)
    return render_template("index.html", tahmin=tahmin)

if __name__ == "__main__":
    app.run(debug=True)
#deneme
