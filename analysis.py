import pickle
import glob
import nltk
import math
from nltk import FreqDist

democrat_files = glob.glob('datasets/train/democratic/*')
republican_files = glob.glob('datasets/train/republican/*')
all_neg_tokens  = []
all_pos_tokens = []

print("Training model...")

#reading each file from pos folder and tokenizing its contents and appending to all_pos_tokens
for fname in democrat_files:
    all_pos_tokens +=  nltk.word_tokenize(open(fname,"r").read())

#reading each file from neg folder and tokenizing its contents and appending to all_neg_tokens  
for fname in republican_files:
    all_neg_tokens +=  nltk.word_tokenize(open(fname,"r").read())

#puts number of positive samples, negative samples, freqdist for pos_tokens, and freqdist for neg_tokens into a map dumps it in a file for future use
pickle.dump({'dem_count': len(democrat_files),'rep_count': len(republican_files),'dem_fd': nltk.FreqDist(all_pos_tokens),'rep_fd': nltk.FreqDist(all_neg_tokens)}, open('sentiment.nb', 'wb'))

print("Training completed... Running tests now")

model = pickle.load(open('sentiment.nb', 'rb'))
test_files = sorted(glob.glob('datasets/test/testpayload/*'))
output_file = open('predictions.txt', 'w')

total_fd = model['dem_fd'] + model['rep_fd']
dem_prior = math.log(model['dem_count'] / (model['dem_count']+model['rep_count']))
rep_prior = math.log(model['rep_count'] / (model['dem_count']+model['rep_count']))

dem_tweets = 0
rep_tweets = 0

for fname in test_files:
    
    #p_doc_pos and p_doc_neg start out containing the priors
    p_doc_dem = dem_prior
    p_doc_rep = rep_prior
    
    #then we add each logged predicition for each token
    for token in nltk.word_tokenize(open(fname,"r").read()):
        p_doc_dem += math.log((model['dem_fd'][token]+1) / (model['dem_fd'].N()+total_fd.B()))
        p_doc_rep += math.log((model['rep_fd'][token]+1) / (model['rep_fd'].N()+total_fd.B()))    
    if p_doc_dem > p_doc_rep:
        dem_tweets += 1
        print(fname, 'DEM', file=output_file)
    else:
        rep_tweets += 1
        print(fname, 'REP', file=output_file)
    #print(fname, 'dem' if p_doc_dem > p_doc_rep else 'rep', file=output_file)

output_file.close()


print("Model tests ended... Results in predictions.txt")
print(dem_tweets, "Democratic tweets and", rep_tweets, "Republican tweets predicted out of", dem_tweets+rep_tweets)
