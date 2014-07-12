import sys
from nltk.stem.porter import PorterStemmer
import string
import nltk
import pickle

ps = PorterStemmer()

def read_file(user_path,j):                                       ##method to read the corpus
	if j < 10 :
		incomplete_path = ('000' + str(j) + '.html')
	elif j < 100 :
		incomplete_path = ('00' + str(j) + '.html')
	elif j < 1000 :
		incomplete_path = ('0' + str(j) + '.html')
	else:
		incomplete_path = (str(j) + '.html')
	path_to_data = (user_path + '' + incomplete_path)
	try:
		f = open(path_to_data)
		s = f.read()
		f.close()
	except IOError:
		s = ''
	return s

def html_parse(s,start,end):                                      ##method for html parsing
	try:
		d = {}
		a = s.split(start,1)
		b = ''.join(a[1])
		c = b.split(end)
		d = ''.join(c[0])		
	except IndexError:
		d = ''
	return d

def remove_punc(d):                                               ##method to remove the punctuations from the data
    line = d.translate(None, string.punctuation)
    return line

def remove_stopwords(g):                                          ##method to remove the stop words
    for word in g:        
        if word in nltk.corpus.stopwords.words('english'):
            while word in g:
                g.remove(word)
    return g

def stem_words(g):                                                ##method to stem the words
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

def create_pickle(file_name,data_to_dump):                        ##method to store the index in a txt file
	f = open(file_name,'w')
	pickle.dump(data_to_dump,f)
	f.close()

def main():
	ind = {}
	review = {}
	movie = {}
	user = {}
	for j in range(1,29871):				##29871
		final_review = {}
		s = read_file(sys.argv[1],j)                              ##takes the path to the data as a command line argument
		if not s == '':			
			review[j] = html_parse(s,'</PRE>','<HR><P CLASS=flush>')
			movie[j] = html_parse(s,'<TITLE>Review for ','</TITLE>')			
			user[j] = html_parse(s,'reviewed by<BR><A HREF="/ReviewsBy?','">')
			user[j] = user[j].replace("+"," ")			 
			if not review[j] == '' and not movie[j] == '' and not user[j] == '':				
				g = remove_punc(review[j]).lower().split()		
				g = remove_stopwords(g)
				final_review = stem_words(g)
				del g[:]
				ind = create_index(final_review,movie[j],user[j],ind)
	create_pickle('review_index.txt',ind)

main()