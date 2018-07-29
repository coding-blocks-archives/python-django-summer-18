import pickle
from collections import OrderedDict

with open("model.pk", "rb") as file:
    classifier = pickle.load(file)

def word_feats(words):
    return dict([(word, 1) for word in words])

def classify_sentiment(s):
	d = OrderedDict()
	res = classifier.prob_classify(word_feats(s))
	for x in res.samples():
		d[x] = res.prob(x)
	return d

