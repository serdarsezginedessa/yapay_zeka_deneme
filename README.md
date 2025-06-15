# 🚫 Spam Mesaj Tespit Uygulaması (Flask + ML)

Bu proje, kullanıcıların yazdığı metinlerin **spam** (istenmeyen içerik) olup olmadığını tespit eden basit ama etkili bir yapay zekâ uygulamasıdır. Python, Flask ve makine öğrenimi teknikleri kullanılarak geliştirilmiş ve Render üzerinden internete açılmıştır.

## 🎯 Amaç

- Kullanıcıdan alınan metni analiz etmek
- Makine öğrenimi modeli ile mesajı **"spam"** veya **"ham"** (normal) olarak sınıflandırmak
- Türkçe ve İngilizce kısa metinlerde temel spam tespiti sağlamak

---

## 🛠️ Kullanılan Teknolojiler

- 🐍 Python 3.x
- ⚙️ Flask (web uygulaması)
- 🧠 scikit-learn (Naive Bayes sınıflandırıcı)
- 🌐 HTML + CSS (temel arayüz)
- ☁️ Render.com (ücretsiz yayınlama)
- 🔧 Gunicorn (sunucu çalıştırıcı)

---

## 🚀 Uygulama Linki

👉 [Canlı Uygulama İçin Tıkla](https://yapay-zeka-deneme.onrender.com/)

---

## 📦 Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için:

```bash
git clone https://github.com/kullaniciadi/yapayzeka-deneme.git
cd yapayzeka-flask
pip install -r requirements.txt
python app.py
```

Ardından `http://127.0.0.1:5000` adresinden çalıştırabilirsiniz.

---

## 🔍 Model Eğitimi

Makine öğrenimi modeli `spam_model.py` dosyasında eğitilmiştir.

- Kullanılan veri seti: [SMS Spam Collection Dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- Model: `MultinomialNB` + `TfidfVectorizer`
- Eğitilen dosyalar:
  - `model/model.pkl`
  - `model/vectorizer.pkl`

---

## 📁 Proje Yapısı

```
yapayzeka-flask/
├── app.py                 # Flask uygulaması
├── spam_model.py          # Model eğitimi
├── model/
│   ├── model.pkl          # Eğitilmiş model
│   └── vectorizer.pkl     # Tfidf vektörizer
├── templates/
│   └── index.html         # Web arayüzü
├── requirements.txt       # Bağımlılıklar
└── Procfile               # Render için çalışma komutu
```

---

## 💡 Gelecekteki Geliştirmeler

- ✅ Türkçe özel stopword desteği
- ✅ Daha güçlü modeller (BERT, SVM)
- 🔄 Kullanıcı girdilerini kaydedip yeniden eğitim
- 📱 Mobil uyumlu tasarım
- 🌍 API formatında servis olarak sunma

---

## 👨‍💻 Geliştirici

**Serdar Sezgin**
📧 serdar.sezgin52@gmail.com.com
💼 [LinkedIn](https://www.linkedin.com/in/serdar-sezgin-5559a855/)
📂 [GitHub](https://github.com/serdarsezginedessa)

---

## 📜 Lisans

MIT Lisansı altında açık kaynak olarak sunulmuştur.
