import marimo

__generated_with = "0.14.10"
app = marimo.App(width="full", app_title="Caption Analysis")


@app.cell
def _():
    caption = """
    Spent an amazing night in the heart of Copenhagen, with 2 of my lovely colleagues ❤️
    @codingsafari and @johannesholzel.

    We talked primarily about CloudNative Distributed Systems, Data stream processing using Apache
    Flink and building Recommendation Engines.

    And dammnn! Those pastries were real good....😋

    #copenhagen #tech #distributed-systems #big-data #data-stream-processing
    """

    import re

    def preprocess_caption(caption):
        replacements = [
            # replace newline characters with simple spaces.
            (r'\r\n|\r|\n', ''),

            # remove mentions and hashtags.
            (r'@[^\s]+', ''),
            (r'#[^\s]+', '')
        ]

        for replacement in replacements:
            old, new = replacement
            caption = re.sub(old, new, caption)

        return caption

    preprocessed_caption = preprocess_caption(caption)
    print(preprocessed_caption)
    return (preprocessed_caption,)


@app.cell
def _():
    import spacy

    """
    spaCy provides different models / trained pipelines, which can be installed as Python packages.
    We'll use the 'en_core_web_sm' model : English pipeline optimized for CPU.
    """
    spacy_model = spacy.load("en_core_web_sm")
    return (spacy_model,)


@app.cell
def _(preprocessed_caption, spacy_model):
    """
    Processing raw text intelligently is difficult: most words are rare, and it’s common for words
    that look completely different to mean almost the same thing. The same words in a different
    order can mean something completely different. Even splitting text into useful word-like units
    can be difficult in many languages.

    While it’s possible to solve some problems starting from only the raw characters, it’s usually
    better to use linguistic knowledge to add useful information. That’s exactly what spaCy is
    designed to do:
    you put in raw text, and get back a Doc object, that comes with a variety of annotations.
    """
    doc = spacy_model(preprocessed_caption)
    return (doc,)


@app.cell
def _(doc):
    """
    Linguistic annotations are available as Token attributes.

    NOTE : Like many NLP libraries, spaCy encodes all strings to hash values to reduce memory usage
           and improve efficiency. So to get the readable string representation of an attribute, we
           need to add an underscore _ to its name.
    """
    for token in doc:
        print((token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.is_stop))
    return


@app.cell
def _(doc):
    def filter_tokens(doc):

        def filter_token(token):
            return (not token.is_alpha or
                    token.is_stop or
                    token.pos_ not in ["ADJ", "NOUN", "PROPN"] or
                    token.dep_ not in ["nsubj", "dobj", "pobj", "compound", "amod", "appos"])

        filtered_tokens = [token for token in doc if not filter_token(token)]
        return filtered_tokens

    filtered_tokens = filter_tokens(doc)

    for filtered_token in filtered_tokens:
        print((filtered_token.lemma_, filtered_token.pos_, filtered_token.tag_, filtered_token.dep_))
    return (filtered_tokens,)


@app.cell
def _(doc):
    """
    Noun chunks are ”base noun phrases” – flat phrases that have a noun as their head. You can
    think of noun chunks as a noun plus the words describing the noun – for example :
    “the lavish green grass” or “the world’s largest tech fund”. 
    """
    for noun_chunk in doc.noun_chunks:
        print((noun_chunk.text, noun_chunk.root.text, noun_chunk.root.dep_))
    return


@app.cell
def _(doc):
    """
    spaCy features an extremely fast statistical entity recognition system, that assigns labels
    to contiguous spans of tokens. The default trained pipelines can identify a variety of named
    and numeric entities, including companies, locations, organizations and products.
    """
    for entity in doc.ents:
        print((entity.text, entity.label_))
    return


@app.cell
def _(doc):
    def filter_entities(doc):

        def filter_entity(entity):
            return (entity.label_ not in ["ORG", "PRODUCT"])

        filtered_entities = [entity for entity in doc.ents if not filter_entity(entity)]
        return filtered_entities

    filtered_entities = filter_entities(doc)

    for filtered_entity in filtered_entities:
        print((filtered_entity.text, filtered_entity.label_))
    return (filtered_entities,)


@app.cell
def _(filtered_entities, filtered_tokens):
    caption_labels = (
        [filtered_token.text.lower() for filtered_token in filtered_tokens] +
        [filtered_entity.text for filtered_entity in filtered_entities])

    print(caption_labels)
    return


if __name__ == "__main__":
    app.run()
