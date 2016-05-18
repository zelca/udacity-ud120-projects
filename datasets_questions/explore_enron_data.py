#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "data size: ", len(enron_data)

print "features size: ", len(enron_data.itervalues().next())

poi = {k: v for k, v in enron_data.iteritems() if v["poi"] == 1}
print "poi", len(poi)

print "James Prentice stock value: ", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Wesley Colwell mails count: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Jeffrey Skilling value of stock options exercised: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

for p in ['SKILLING JEFFREY K','LAY KENNETH L','FASTOW ANDREW S']:

    print p, enron_data[p]["total_payments"]

print "filled quantified salary: " , len ({k: v for k, v in enron_data.iteritems() if v["salary"] != "NaN"})

print "filled known email adress: " , len ({k: v for k, v in enron_data.iteritems() if v["email_address"] != "NaN"})

missing_total_payments = {k: v for k, v in enron_data.iteritems() if v["total_payments"] == "NaN"}

print "missing payments: ", len(missing_total_payments), " in % ", 100 * len(missing_total_payments) / len(enron_data)

poi_missing_total_payments = {k: v for k, v in enron_data.iteritems() if v["poi"] == 1 and v["total_payments"] == "NaN"}

print "missing payments: ", len(poi_missing_total_payments), " in % ", 100 * len(poi_missing_total_payments) / len(enron_data)

print "new NaN in total payments: ", 10.0 / (10 + len(poi))
