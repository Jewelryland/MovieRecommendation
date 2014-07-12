import sys
import string
import pickle
import operator
import math
import predict

def retrieve_pickle(file_name):      ##method to get index from the txt file
	f = open(file_name,'r')
	data_loaded = pickle.load(f)
	f.close()
	return data_loaded

def calc_idf(ind, test_user):                                   ##calculates the idf for every word in the reviews by the test user
	idf = {}
	for i in ind[test_user]:
		for j in ind[test_user][i]:                  ##for every word in the review of test user
			
			if not j in idf:
				present = 0
				no_of_docs = 0
			 	for n in ind:                         ##for every other user
			 		
			 		for m in ind[n]:                           ##for every movie's review by a user
			 			no_of_docs += 1
			 			if j in ind[n][m]:                  ##if the word is present in the review
							present += 1				
			
				idf[j] = (1 + math.log(float(no_of_docs)/(present + 1)))                    ##calculates idf of each word
	return idf

def find_similarity(ind, test_user):                      ##calculates the similarity score for every movie
	similarity_score = {}	
	for n in ind:
		similarity_score[n] = {}
		for m in ind[n]:
			score = 0
			for i in ind[test_user]:
				for j in ind[test_user][i]:
					if j in ind[n][m]:
						score += (ind[n][m][j] * idf[j] * idf[j])                  ##calculates the similarity score
			similarity_score[n][m] = score                                     ##similarity score of each movie review
	return similarity_score

def take_max(similarity_score):                           ##calculates the similarity score for every user using take_max method
	sim_score = {}
	for n in similarity_score:
		sim_score[n] = max(similarity_score[n].values())               ##takes the maximum score from the set of movie reviews of each user 
	return sim_score

def take_avg(similarity_score):                           ##calculates the similarity score for every user using take_avg method
	sim_score = {}
	for n in similarity_score:
		total = 0	
		for m in similarity_score[n]:
			total += similarity_score[n][m]
		sim_score[n] = float(total) / len(similarity_score[n].keys())        ##takes the average score from the set of movie reviews of each user
	return sim_score

def select_no_of_users(sim_score, k):                     ##selects k most similar users
	best_users = {}
	for i in range(0,k):                             ##takes 50 most similar users
		best_users[i] = str(sim_score[i])[2:str(sim_score[i]).rfind("'")]
	return best_users

def main(test_user, max_reco):	
	ind = retrieve_pickle('review_index.txt')

	idf = calc_idf(ind, test_user)

	similarity_score = find_similarity(ind, test_user)	

	#sim_score = take_max(similarity_score)

	sim_score = take_avg(similarity_score)	

	sim_score = sorted(sim_score.iteritems(), key=operator.itemgetter(1), reverse=True)	
	
	best_users = select_no_of_users(sim_score, 100)
		
	predict.main(ind, best_users, test_user, max_reco)