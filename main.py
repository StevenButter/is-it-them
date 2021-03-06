from textblob.classifiers import NaiveBayesClassifier
import whatsapp_reader
import argparse


def _GetFilename():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f')
    args = parser.parse_args()
    return args.f


if __name__ == "__main__":
    try:
        data = whatsapp_reader.read(_GetFilename())
        classifier = NaiveBayesClassifier(data)

        while True:
            txt = input('Type something: ')
            person = classifier.classify(txt)

            print('it\'s {}'.format(person))
    except KeyboardInterrupt:
        pass
