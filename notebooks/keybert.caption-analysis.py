import marimo

__generated_with = "0.14.10"
app = marimo.App(width="full")


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
            (r'\r\n|\r|\n', ' '),

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
def _(preprocessed_caption):
    import spacy
    import keybert

    """
    KeyBERT supports quite a few embedding models. Having the option to choose embedding models
    allow you to leverage pre-trained embeddings that suit your use-case.
    """

    def run_keyBERT_With_spacy():
        spacy.prefer_gpu()
        spacy_model = spacy.load("en_core_web_sm",
                                 exclude=["tagger", "parser", "ner", "attribute_ruler", "lemmatizer"])
    
        keyBERT_model = keybert.KeyBERT(model= spacy_model)
    
        keywords = keyBERT_model.extract_keywords(preprocessed_caption,
                                                  keyphrase_ngram_range=(1, 3),
                                                  stop_words="english")
        return keywords

    print(run_keyBERT_With_spacy())
    return (keybert,)


@app.cell
def _(keybert, preprocessed_caption):
    def run_keyBERT_with_sentence_transformer():
        keyBERT_model = keybert.KeyBERT(model="all-MiniLM-L6-v2")

        keywords = keyBERT_model.extract_keywords(preprocessed_caption,
                                                  keyphrase_ngram_range=(1, 3),
                                                  top_n=5,
                                                  stop_words="english")
        return keywords

    print(run_keyBERT_with_sentence_transformer())
    return


if __name__ == "__main__":
    app.run()
