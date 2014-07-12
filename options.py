import sys
import recommend
import review

def main(test_user):
	cont = 1
	while cont == 1:
		print '1. Do you want movie recommendations?\n2. Do you want to write a review?\n3. Do you want to log out?'
		x = raw_input()
		if x == '1':
			cont = 0
			print 'How many movies do you want to be recommended?'
			max_reco = raw_input()
			recommend.main(test_user,int(max_reco))
		elif x == '2':
			cont = 0
			print 'Name of the movie:'
			movie = raw_input()
			print 'Write the review here:'
			rev = raw_input()
			review.main(test_user,movie,rev)
		elif x == '3':
			cont = 0
			break
		else:
			print 'Please enter the correct choice!!'
			cont = 1