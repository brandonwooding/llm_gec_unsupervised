import spacy_udpipe

#[spacy_udpipe.download(lang) for lang in ['cs', 'de', 'el', 'en', 'et', 'it', 'lv', 'ru', 'sl', 'sv', 'uk']]

# only English needed for W&I evaluation
spacy_udpipe.download('en')
