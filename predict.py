import sys
import csv
import operator
import options

def read_file(file_name):
	trained_data = {}
	a = 1
	cr = csv.reader(open(file_name,"rb"))
	for row in cr:
		if a == 1:
			pp = float(row[0])
			pn = float(row[1])
			a += 1
		else:
			trained_data[row[0]] = {'p_word_1':float(row[1]), 'p_word_0':float(row[2])}
	return (trained_data, pp, pn)

def predict_review(ind, best_users, test_user, trained_data, pp, pn):                         ##this method predicts the review as positive or negative
	prediction = {}
	test_user_prediction = {}
	p1 = 1
	p0 = 1
	for i in best_users:		
		for j in ind[best_users[i]]:
			for k in ind[best_users[i]][j]:
				if k in trained_data:
					for n in range(1,ind[best_users[i]][j][k] + 1):
						p1 = p1 * trained_data[k]['p_word_1']
						p0 = p0 * trained_data[k]['p_word_0']
			p1 = p1 * pp
			p0 = p0 * pn					
			if p1 >= p0:				
				if j in ind[test_user]:
					test_user_prediction[j] = 1
				if not j in prediction:
					prediction[j] = 1
				else:
					prediction[j] += 1
			else:				
				if j in prediction:
					prediction[j] -= 1
			p1 = 1
			p0 = 1	
	return (prediction, test_user_prediction)

def print_user_liking(ind, test_user, test_user_prediction, count):	                            ##print the liking of the test user
	print ('----------MOVIES LIKED BY ' + test_user + '----------')
	for n in ind[test_user]:
		if n in test_user_prediction:
			print (str(count) + ". " + n)
			count += 1

def print_reco(ind, prediction, max_reco, test_user, count):                                    ##print the recommendations for the user
	print '----------MOVIES RECOMMENDED FOR ' + test_user + '----------'	
	for n in prediction:
		x = str(n)[2:str(n).find(")")]
		check = (x + ")")
		if count < (max_reco + 1):
			if not check in ind[test_user]:			
				
				print (str(count) + ". " + check)
				count += 1
		else:
			break

def main(ind, best_users, test_user, max_reco):		
	trained_data, pp, pn = read_file('model_file.csv')

	prediction, test_user_prediction = predict_review(ind, best_users, test_user, trained_data, pp, pn)

	cnt = 1

	print_user_liking(ind, test_user, test_user_prediction, cnt)

	prediction = sorted(prediction.iteritems(), key=operator.itemgetter(1), reverse=True)

	print_reco(ind, prediction, max_reco, test_user, cnt)

	print ''	
	
	options.main(test_user)