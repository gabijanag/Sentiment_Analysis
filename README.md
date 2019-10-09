# Sentiment Analyses

Classifies movie reviews into positive and negative. Classification is done using different classification methods in python 3.

### Dataset

The dataset is referred to as “sentence polarity dataset v1.0“. It was collected by Bo Pang and Lillian Lee and released in 2005. First used in Bo Pang and Lillian Lee, "Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales.", Proceedings of the ACL, 2005. The Movie Review data shows good/bad ("fresh"/"rotten") sentiment classification based on a collection of short review excerpts from Rotten Tomatoes. 

### Data processing pipeline

#### The data has been cleaned up somewhat, for example:

* The dataset is balanced, comprised of 5331 positive and 5331 negative processed senteces. 
* The dataset is comprised of only English reviews.
* All text has been converted to lowercase.
* There is white space around punctuation like periods, commas, and brackets.
* Text has been split into one snippet per line.


#### To further proccess data:

* Firstly replace contractions to their equivalents;
* Then remove punctuation and numbers;
* Remove all the single characters;
* Replace multiple spaces with a single space;
* Replace slang words and abbreviations with their equivalents;
* Negation replacement. Dealing with negations (like “not good”) is a critical step in Sentiment Analysis. A negation word can influence the tone of all the words around it, and ignoring negations is one of the main causes of misclassification;
* Remove stopwords. Stop words are the most common words in a language like “the”, “a”, “on”, “is”, “all”. These words usually carry little importance to the sentiment analyces.
* Lemmatization. The aim of lemmatization, like stemming, is to reduce inflectional forms to a common base form. As opposed to stemming, lemmatization does not simply chop off inflections. Instead it uses lexical knowledge bases to get the correct base forms of words;
* Tokenization;


