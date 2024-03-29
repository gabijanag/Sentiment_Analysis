import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


'''Importing Dataset'''
pos_reviews = [line.rstrip('\n') for line in open('rt-polarity.pos')]
neg_reviews = [line.rstrip('\n') for line in open('rt-polarity.neg')]
all_reviews = pos_reviews + neg_reviews


'''Data preprocessing'''
data = []
stopwords = [k for k in stopwords.words('english') if k not in ['not']]  # neisimam not

for line in range(0, len(all_reviews)):
    # Remove all the special characters
    review = re.sub('[^a-zA-Z ]', '', str(all_reviews[line]))

    # # remove all single characters
    review = re.sub(r'\s+[a-zA-Z]\s+', ' ', review)

    # Remove the stopwords and get the stemwords.
    ps = PorterStemmer()
    review = word_tokenize(review)  # Tokenize the reviews
    # review = [ps.stem(word) for word in review if not word in set(stopwords)]
    review = ' '.join(review)
    data.append(review)


'''Converting human-readable data to machine-readable data'''
# max_features: using 3500 most occurring words as features for training our classifier.
vectorizer = CountVectorizer(max_features=3500,
                             ngram_range=(1, 4))

X = vectorizer.fit_transform(all_reviews).toarray()
pos = len(pos_reviews)
neg = len(neg_reviews)
y = [1] * pos + [0] * neg


'''Splitting data into Training and Testing Sets'''
# divide data into 20% test set and 80% training set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


'''Training and testing the model'''
classifier = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(X_train, y_train)

# predict the sentiment for the documents in our test
y_pred = classifier.predict(X_test)
x_pred = classifier.predict(X_train)


'''Accuracy of the model'''
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_train, x_pred))
print(classification_report(y_train, x_pred))
print(accuracy_score(y_train, x_pred))


# '''Saving and Loading the Model'''
# # save trained model for later use.
# with open('RF_classifier', 'wb') as picklefile:
#     pickle.dump(classifier, picklefile)
# # to load the model use
# with open('RF_classifier', 'rb') as training_model:
#     RF_model = pickle.load(training_model)
#
# # predict the sentiment for the test set using our loaded model
# y_pred2 = RF_model.predict(X_test)
#
# print(confusion_matrix(y_test, y_pred2))
# print(classification_report(y_test, y_pred2))
# print(accuracy_score(y_test, y_pred2))
