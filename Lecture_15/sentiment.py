import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
# pip install nltk
import nltk

from collections import OrderedDict
 
nltk.download('movie_reviews')

def word_feats(words):
    return dict([(word, 1) for word in words])
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

# print(negfeats[:5])
 
classifier = NaiveBayesClassifier.train(negfeats + posfeats)

if __name__ == "__main__":
    import pickle
    with open("model.pk", "wb") as file:
        pickle.dump(classifier, file)
        print("Wrote the model to file !")
