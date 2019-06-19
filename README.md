## Performing Sentiment and Concordance analysis on Russia's Twitter Bots

Adam Ali (adaali@ucdavis.edu)

Cameron Lee (cmnlee@ucdavis.edu)

**TLDR:** We analyzed Russia's twitter bots and one of the interesting things we found was that among other things, the bots push agendas such as the anti-vaccination movement. Please visit [this google drive folder](https://drive.google.com/drive/folders/1YdP61uRxt10GlX3WXLQ_1aiEglZ28Wve?usp=sharing) in order to download the entire tool and datasets. Instructions are present in the README of that project folder.

### Abstract

The analysis was done through the NLTK toolkit with training data of categorized Democratic and Republican tweets. Pre-analysis, we hypothesized that the bots were biased to provide heavy support towards one party. After analysis, however, it was revealed that the Twitter bots take both sides in an attempt by the Russian government to cause disinformation and sow discord among the American public. Further analysis by concordance tables was performed to show how Russia could be influencing the anti-vaccinations movement.

### Background

The purpose of this analysis is to study and dive into Russia’s purpose in commandeering an army of Twitter bots deployed from the Internet Research Agency based primarily in St. Petersburg. We believe that the bots’ existence is to spread disinformation and divide parties, specifically within the United States. For example, according to the US National Library of Medicine, Russia’s twitter bots even fed fuel to the fire for the current Anti-Vaccination movement. This is a new era in cyber-warfare that is worth consideration.

### The Analysis

There were three total datasets used. All three were acquired from Kaggle.com.  The first one was a training data-set with pre-labeled democrat/republican tweets used for training our model. The other two were small and large datasets of Russian Twitter troll tweets used for testing.

 The analysis includes two parts: The sentiment analysis and the concordance analysis. The datasets were all in comma-separated-value form and thus had to be extracted and labeled based on the format of their columns (which differed). For our analysis, there are two separate test suites. One testing the smaller dataset of about 200,000 bot tweets, and the other testing a big dataset of about 35,000,000 bot tweets. This approach was deliberately chosen to give users a choice based on their available computing power. Analysing the 35 million tweets took upwards of 15-20 minutes as opposed to the smaller set’s 3-5 minutes. 

#### (Part 1) Sentiment Analysis

We modified the code from our homework assignments to fit our needs for this project. Since we are not explicitly labeling files, we decided to go for the approach of training and immediately testing in the same program, as this helps with speeding up performance. The training was done using a dataset of labeled Democrat and Republican tweets, using NLTK’s frequency distribution. In [Figure-1](https://drive.google.com/file/d/1OCciZ6QiVI9VwvVHCOuL8ZsMdvXfR3Ff/view?usp=sharing), you see the process of training to testing. This was a run for the smaller dataset.

#### (Part 2) Concordance

Concordance text building was done during the tokenization process for the sentiment analysis to make the program efficient. We built the word lists for each party and ran concordance for both using our scripts.

In [Figure-2](https://drive.google.com/file/d/1V42sbS2Y1W5IZxr-vpdrlAbdu6RKfHxB/view?usp=sharing), and [Figure-3](https://drive.google.com/file/d/1IdlcZ9sGsDFXE8czkIS9vVAyWRm1uHOZ/view?usp=sharing), we analyze the concordance of the words “we”, and “strong” (respectively). There were unfortunately a few false-positives for both words, but as predicted, the emotion received from the uses of the words are completely different between the two parties. For instance: in the democratic concordance table, “strong” appears to be associated with minority and women empowerment in several cases. The republican concordance table on the other hand has “strong” linked with the U.S. military, the nation, and the current sitting president Donald Trump. It is evident thus that the two parties have strongly differing ideas on what type of “strong” they value: that of social progressive attitudes or that of a united nation in terms of military and individual leadership strength.

In [Figure-4](https://drive.google.com/file/d/1NO3fmdmFb96KNIBUP8Cq_2RztGnULkM5/view?usp=sharing), we tested with a “💩“ emoji. We do believe that emojis are a powerful tool to recognize patterns or the running emotions in a text conversation.  We did try a few other emojis, but came up short. One emoji we tried was the syringe emoji in an attempt to dive deeper into Russia’s interest in anti-vaccination movements. Unfortunately, there were scant results. However,  as can be seen
in [Figure-5](https://drive.google.com/file/d/17Rhf7x5r9fvrjPTKk95LkP45QNI-m00s/view?usp=sharing), [Figure-6](https://drive.google.com/file/d/15xUj4zKjm3h6ltzjrm79FfLsHVBA6bIh/view?usp=sharing), and [Figure-7](https://drive.google.com/file/d/11doodFEc4uvHMWIQdr6BbPlt07jFLTLW/view?usp=sharing), there were a few tweets very relevant to those sorts of “health” movements. We decided to test the concordance of the word “vaccination” on the dataset of 35 million tweets. This took about 25 minutes of computing time. In [Figure-8](https://drive.google.com/file/d/1--t3jZv8PVLkQcfKA8v8ImRMdRPpgkol/view?usp=sharing), you see almost 2,000 matches for just the word “vaccination” spread between both parties with the majority being the Democrat side. One of the biggest drivers of the “anti-vaccination” group is the notion that vaccines cause Autism, which as you see in [Figure-8](https://drive.google.com/file/d/1--t3jZv8PVLkQcfKA8v8ImRMdRPpgkol/view?usp=sharing), is also an agenda that is pushed by these bots. Similar concordance results in this corpora can be found by searching for buzzwords of other groups similar to the anti-vaccination movement.

### Further Observations

One interesting point in performing this analysis was the realization that the Russian government is not spreading disinformation through just one party, but instead through a joint effort of Democrat and Republican bots in order to cause friction. This contradicted our previous hypothesis that only a single party would have found dominant support through the twitter bots. In actuality, there were 124,074 Democratic tweets and 79,408 Republican tweets predicted out of 203,482 for the smaller dataset. Furthermore, there were 22,227,186 Democratic tweets and 15,366,872 Republican tweets predicted out of 37,594,058 for the large dataset. 

The predictions file for the large dataset was ~850 MBs. The prediction file outputs twitter handles, along with the prediction of their party. This was used to attempt to manually compare handles and to form a pattern. Many accounts’ twitter handles were prefixed with a “Rep” as to “Represent” certain political figures they support. This was the easiest way to identify parties through usernames. It was difficult to perform the manual analysis as a result of sheer size of the data. Twitter handles without any political identifiers were the most difficult to categorize, as they were mostly random words. 

### Difficulties

There were two false-positive influencing factors within the datasets. First, there was a large variation in sample size between the training and testing datasets. Second, due to the nature of the web, there was a large amount of sarcasm within the tweets, which caused our model to predict false-positives.

Another issue was the general sheer size of the samples. Manual analysis was difficult and slow with the millions of tweets. Running concordance analysis on the 35 million tweet dataset took a surprisingly long amount of time.  This brings into question the actual accuracy of the labeled Democrat and Republican tweets. According to the dataset’s poster on Kaggle, it was done using the same type of sentiment analysis we are doing. The question then becomes: what did they use to train his own model for that analysis? Would it have had a higher or lower labeling accuracy if we were to compare their training data with ours? 
One final issue we had no choice but to deal with was the accuracy of Twitter’s bot detection system. There are false-positives in such systems. As such, some of our analysis was further limited by this system.

### Conclusion and Extension

One noteworthy extension of our analysis was to perform both sentiment and concordance analysis on the twitter handles themselves.  Unfortunately, we predicted that this would be rather difficult in maintaining high accuracy and precision due to the small length of the usernames. This could technically be done with certain usernames with certain characters you can split by, such as an “_”, in order to form a short “sentence” of sorts, and then perform the analysis on that result..

In summation, the result of our analysis was eye opening to us. By far the most surprising thing this revealed to us was Russia’s usage of the bots to push politically related agendas across both parties. In other words, it was not just one party the twitter bots were pushing as we originally had suspected, but both. We can only conclude that the goal for these bots is to spread political polarization, disinformation, and distrust among the American political landscape in order to further Russia’s geopolitical goals as the United States’ current rival. The party’s politics do not matter: they are only a means to an end to weaken support for media and political institutions, a disturbing finding that has deep implications for both the present and future of cyber warfare.

## Source data:

- https://www.kaggle.com/kapastor/democratvsrepublicantweets <-- for the collection of categorized democratic/republican tweets
- https://www.kaggle.com/vikasg/russian-troll-tweets <-- for the troll tweet collection
- https://github.com/fivethirtyeight/russian-troll-tweets <-- for the troll tweet collection w/ IRA handles

