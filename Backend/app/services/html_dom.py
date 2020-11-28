from bs4 import BeautifulSoup, Comment

_TAGS_BLACKLIST = ['style', 'script', 'head', 'title', 'meta', '[document]']
"""A blacklist of all the tags that should be ignored."""


def _tag_visible(element):
    return (
        element.parent.name not in _TAGS_BLACKLIST and
        not isinstance(element, Comment)
    )


def extract_text_from_dom(dom_str):
    """Extracts the text from the DOM and returns a list of strings."""
    soup = BeautifulSoup(dom_str, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(_tag_visible, texts)
    return [t.strip() for t in visible_texts if t.strip()]
