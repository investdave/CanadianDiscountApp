import spacy
nlp = spacy.load('en_core_web_sm')

def hashtags(text):
	doc = nlp(text)
	thread_hashtags = [(X.text, X.label_) for X in doc.ents if X.label_ == 'ORG' or X.label_ == 'PERSON']
	return thread_hashtags