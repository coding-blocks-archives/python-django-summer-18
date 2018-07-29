import pickle
from collections import OrderedDict

def word_feats(words):
    return dict([(word, 1) for word in words])

def classify_sentiment(classifier, s):
	d = OrderedDict()
	res = classifier.prob_classify(word_feats(s))
	for x in res.samples():
		d[x] = res.prob(x)
	return d

if __name__ == "__main__" :
    with open("model.pk", "rb") as file:
        classifier = pickle.load(file)
    while True:
        print("Input thje string: ", end = '')
        s = input()
        print(classify_sentiment(classifier, s))