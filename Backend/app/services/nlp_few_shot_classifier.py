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
CLASSES = ['media', 'people', 'business', 'biology', 'sport', 'education', 'architecture', 'government', 'medicine',
              'gaming', 'geography', 'astronomy', 'military', 'aviation', 'food', 'chemistry', 'law', 'religion',
              'travel', 'theater', 'celebrity', 'film', 'performance', 'computer hardware', 'music',
              'computer software', 'digicatal_camera', 'engineering', 'fashion', 'physics', 'animals', 'fiction',
              'literature', 'gadgets', 'history', 'robotics', 'invention', 'automotive', 'hobby']


def classify_text_into_keyword(sentence_str):
    """Classifies a text document into a keyword category."""
    sentence = Sentence(sentence_str)
    tars.predict_zero_shot(sentence, CLASSES)
    return sentence.annotation_layers["label"][0]
