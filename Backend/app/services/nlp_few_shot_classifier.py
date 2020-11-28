import os

from flair.data import Sentence
from flair.models.text_classification_model import TARSClassifier

# Download the following file, and put it in `resources` (btw it will be ignored by .gitignore)
# https://nlp.informatik.hu-berlin.de/resources/models/tars-base/tars-base.pt
tars = TARSClassifier.load(
    os.path.join(os.path.dirname(__file__), "..", "resources", "tars-base.pt")
)

# The classes: a single keyword that should be self-explanatory
# Additionally it's possible to give a few examples
CLASSES = ["politics", "cooking", "sport", "science"]


def predict(sentence_str):
    sentence = Sentence(sentence_str)
    tars.predict_zero_shot(sentence, CLASSES)
    return sentence


"""
Examples:
print(predict("They scored and won the tournament."))
print(predict("The president refused to admit he lost."))
"""
