Title: Movie Recommendation using IMDb dataset
UNI: ssb2171
Email: ssb2171@columbia.edu

### user_input.py
 - Run this Python script using the command "python user_input.py" on terminal/command prompt to use the application.
 - The system will first ask the user to input his/her name.
 - Once the user enters the name, they will be given 3 options where they have to decide if they want to get movie       recommendations, write a movie review or log out. The user will enter the number 1, 2 or 3 to choose the options.
 - If the user enters 1, they are asked to enter the number of recommendations they want. Once they do that, the system       displays a list of movies recommended for the user.
 - If the user enters 2, they are asked to put in the movie name for which they want to write the review and then the user    is asked to write the review. This review then gets stored in the review_index.txt file.
 - If the user enters 3, the application ends.

### index_reviews.py
 - This script has already been run to create the file review_index.txt that contains the indexed reviews.
 - Since the script takes a lot of time to run, the user doesn't have to run this file.
 - However, if the user wants to run the script, they can use the command "python index_reviews.py path_to_dataset" where     path_to_dataset is the path to where the dataset (html files) are stored.
 - This creates a txt file review_index.txt.