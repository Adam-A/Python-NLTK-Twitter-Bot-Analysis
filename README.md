# LIN-127-Project-14

Adam Ali (adaali@ucdavis.edu)

Cameron Lee (cmnlee@ucdavis.edu)

### (Part 1) Training and Testing Our Model

#### Before Implementation

We will train using democratic and republican tweets, and run the probabilities on the russian-troll-tweet to determine whether the tweets are demo or repub

We will need to separate the data and only use the tweet contents from the CSV. To do this, we will copy each tweet from the CSV content column into a file in a folder with "demo" and "repub" labels for each.

We will then use the trained models to predict probabilities on the russian-troll-tweets. 

#### After Implementation

At first, we implemented it just like how we did in the first few homeworks (folder for dems and reps). After realizing we could cut testing times by a huge margin, we stopped using glob and began doing the training, testing, and later concordance, in the same analysis file.

(2-5 minute run-time) There were 124074 Democratic tweets and 79408 Republican tweets predicted out of 203482 for the smaller dataset. There were definitely some false-positives (tested it during production). 

(10-20 minute run-time) There were 22227186 Democratic tweets and 15366872 Republican tweets predicted out of 37594058. The predictions file was ~850 MBs 

### (Part 2) Concordance

#### Before Implementation

Our next analysis will be building concordance tabels. We will attempt to study the contexts of each words (undetermined yet). We will also tag the words from the tweets, and maybe analyze the parts of speech

#### After Implementation

Testing words include (but not limited to): we, strong, vaccinations

### Observations

- It was difficult finding categorized Democrat and Republican files. This basically made or broke how many false-positives we would get. Plus, tweets having hashtags and emojis didn't help. This, along with people's tendancy for sarcasm on the web, made our lives a bit more difficult
- Sort of the counterpoint to the first bulletpoint, we had a lot more test data than train data. In our opinion, there should be a good amount of both for correct predictions

# Source data:

- https://www.kaggle.com/kapastor/democratvsrepublicantweets <-- for the collection of categorized democratic/republican tweets
- https://www.kaggle.com/vikasg/russian-troll-tweets <-- for the troll tweet collection
- https://github.com/fivethirtyeight/russian-troll-tweets <-- for the troll tweet collection w/ IRA handles

