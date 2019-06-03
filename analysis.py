import pickle
import glob
import nltk
import math
import csv
from nltk import FreqDist

dem_count = 0
rep_count = 0
all_rep_tokens  = []
all_dem_tokens = []
    
print("\n-----TRAINING WITH DEMOCRATIC AND REPUBLICAN TWEETS-----\n")

#https://realpython.com/python-csv/                                                                 
with open('datasets/train/ExtractedTweets.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: #party, handle, tweets row[1],2,3                                        
        if line_count == 0:
            line_count += 1
        else:
            if row[0] == "Democrat":
                all_dem_tokens += nltk.word_tokenize(row[2])
                dem_count += 1
            elif row[0] == "Republican":
                all_rep_tokens += nltk.word_tokenize(row[2])
                rep_count += 1
            line_count += 1

print("\n-------------------TRAINING COMPLETED-------------------\n")
print("\n-----------TESTING WITH RUSSIAN TROLL TWEETS------------\n")

dem_fd = nltk.FreqDist(all_dem_tokens)
rep_fd = nltk.FreqDist(all_rep_tokens)
output_file = open('predictions.txt', 'w')

total_fd = dem_fd + rep_fd
dem_prior = math.log(dem_count / (dem_count+rep_count))
rep_prior = math.log(rep_count / (dem_count+rep_count))

dem_tweets = 0
rep_tweets = 0

#need this for concordance later                                                                                 
dem_word_list = []
rep_word_list = []

with open('datasets/test/russian-troll-tweets/tweets.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            temp_word_list = []
            #p_doc_pos and p_doc_neg start out containing the priors                                        
            p_doc_dem = dem_prior
            p_doc_rep = rep_prior
            for token in nltk.word_tokenize(row[7]):
                temp_word_list.append(token)
                p_doc_dem += math.log((dem_fd[token]+1) / (dem_fd.N()+total_fd.B()))
                p_doc_rep += math.log((rep_fd[token]+1) / (rep_fd.N()+total_fd.B()))
            if p_doc_dem > p_doc_rep:
                dem_word_list += temp_word_list
                dem_tweets += 1
                print(row[1]+str(line_count), 'DEM', file=output_file)
            else:
                rep_word_list += temp_word_list
                rep_tweets += 1
                print(row[1]+str(line_count), 'REP', file=output_file)
            line_count += 1
   

output_file.close()

print("\n----TESTING COMPLETED... RESULTS IN predictions.txt-----\n")
print(dem_tweets, "Democratic tweets and", rep_tweets, "Republican tweets predicted out of", dem_tweets+rep_tweets)
print("\n------------------RUNNING CONCORDANCE-------------------\n")

while True:

    word = input("TO EXIT, HIT ENTER. OTHERWISE, ENTER WORD FOR CONCORDANCE\n")
    if word == '':
        break
    print("\nDEMOCRATIC CONCORDANCE FOR",word, "\n")
    nltk.Text(dem_word_list).concordance(word)
    print("\nREPUBLICAN CONCORDANCE FOR",word, "\n")
    nltk.Text(rep_word_list).concordance(word)
    print("\n")
