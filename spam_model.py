# spam_model.py

import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

# Eğitim verisi
X = [
    "Ücretsiz tatil kazandınız", "Hemen kredi alın", "Kazandınız!",
    "Borçlarınızı hemen kapatın", "Tıklayın ve hediyenizi alın",
    "İnternet kazancınızı katlayın", "Sadece bugün geçerli kampanya",
    "Baban arıyor", "Toplantı 3’te", "Ders programını inceledim",
    "SERDAR bugün müsait misin?", "Bugün okulda yoktum",
    "Marketten bir şey ister misin?", "Yarın görüşelim mi?"
]
y = [
    "spam", "spam", "spam", "spam", "spam", "spam", "spam",
    "ham", "ham", "ham", "ham", "ham", "ham", "ham"
]

# Metinleri vektöre dönüştür
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Modeli eğit
model = MultinomialNB()
model.fit(X_vec, y)

# Kayıt klasörü oluştur (yoksa)
os.makedirs("model", exist_ok=True)

# Model ve vectorizer dosyalarını kaydet
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model ve vectorizer başarıyla kaydedildi.")
