from flair.data import Sentence
from flair.models.text_classification_model import TARSClassifier

# Download the following file, and set its path down below
# TODO find a better way to do it
# https://nlp.informatik.hu-berlin.de/resources/models/tars-base/tars-base.pt
tars = TARSClassifier.load('tars-base.pt')

# The classes: a single keyword that should be self-explanatory
# Additionally it's possible to give a few examples
CLASSES = ["politics", "sport"]


def predict(sentence_str):
    sentence = Sentence(sentence_str)
    tars.predict_zero_shot(sentence, CLASSES)
    return sentence


print(predict("They scored and won the tournament."))
print(predict("The president refused to admit he lost."))
