#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here 

from sklearn import tree
from sklearn.cross_validation import train_test_split

features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

print "total number in test set:", len(labels_test)
print "poi number in test set:", sum(labels_test)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
print "accuracy:", clf.score(features_test, labels_test)

labels_predicted = clf.predict(features_test)

true_positives = 0
for p, t in zip(labels_predicted, labels_test):
    if p == 1 and t == 1:
        true_positives += 1
print "true positives:", true_positives

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

print "recall score:", recall_score(labels_test, labels_predicted)
print "precision score:", precision_score(labels_test, labels_predicted)


