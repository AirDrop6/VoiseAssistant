import speech_recognition as sr
from sklearn.feature_extraction.text import CountVectorizer     #pip install scikit-learn
from sklearn.linear_model import LogisticRegression

import Dataset, Syntes_pyttsx3
from Functions import *

r = sr.Recognizer()
mic = sr.Microphone(device_index=2)


def func_selection(data, vectorizer, clf):
    trg = Dataset.TRIGGERS.intersection(data.split())

    if not trg:
        return
    print(data)
    data.replace(list(trg)[0], '')

    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]

    Syntes_pyttsx3.speaker(answer.replace(func_name, ''))
    #Syntes_torch.speaker(answer.replace(func_name, ''))

    exec(func_name + '()')

def record():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(Dataset.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(Dataset.data_set.values()))

    del Dataset.data_set

    while True:
        print('Rec:')
        with mic as sourse:
            r.adjust_for_ambient_noise(sourse)
            audio = r.listen(sourse)
            try:
                data = r.recognize_google(audio, language='ru-RU').lower()

            except sr.UnknownValueError:
                data = ''
                pass
        #print(data)
        func_selection(data, vectorizer, clf)

if __name__ == '__main__':
    record()
