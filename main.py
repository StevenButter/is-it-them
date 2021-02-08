from textblob.classifiers import NaiveBayesClassifier
from data import data

if __name__ == "__main__":
    classifier = NaiveBayesClassifier(data)

    txt = input('Type something: ')
    person = classifier.classify(txt)

    print('it\'s {}'.format(person))
