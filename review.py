import sys
from nltk.stem.porter import PorterStemmer
import string
import nltk
import pickle
import options

ps = PorterStemmer()

def remove_punc(d):      ##method to remove the punctuations from the data
    line = d.translate(None, string.punctuation)
    return line

def remove_stopwords(g):      ##method to remove the stop words
    for word in g:        
        if word in nltk.corpus.stopwords.words('english'):
            while word in g:
                g.remove(word)
    return g

def stem_words(g):      ##method to stem the words
    h = {}
    for k in range(0,len(g)):       
        while True:    
            h[k] = ps.stem(g[k])
            if h[k] == g[k] :
                break
            g[k] = h[k]
    return h

def create_index(rev,mov,user,ind):	
	if user in ind:
		ind[user][mov] = {}
	else:
		ind[user] = {mov:{}}
	for n in rev:
		if rev[n] in ind[user][mov]:
			ind[user][mov][rev[n]] += 1
		else:
			ind[user][mov][rev[n]] = 1
	return ind

def retrieve_pickle(file_name):      ##method to get index from the txt file
	f = open(file_name,'r')
	data_loaded = pickle.load(f)
	f.close()
	return data_loaded

def create_pickle(file_name,data_to_dump):      ##method to store the index in a txt file
	f = open(file_name,'w')
	pickle.dump(data_to_dump,f)
	f.close()

def main(test_user,movie,rev):
	final_review = {}

	ind = retrieve_pickle('review_index.txt')

	g = remove_punc(rev).lower().split()

	g = remove_stopwords(g)

	final_review = stem_words(g)

	del g[:]

	ind = create_index(final_review,movie,test_user,ind)

	create_pickle('review_index.txt',ind)

	options.main(test_user)