#! /usr/bin/env python3

import os
import requests


# List all .txt files under /data/feedback directory that contains the actual
# feedback to be displayed on the company's website.

# Hint: Use os.listdir() method for this, which returns a list of all
# files and directories in the specified path.
filepath = '/data/feedback'

# You should now have a list that contains all of the feedback files from the path /data/feedback. 
filenames = os.listdir(filepath)

# A dictionary with keys and their respective values (content from feedback files).
# This will be uploaded through the Django REST API.
customer_reviews_dict = {}

# Traverse over each file and, from the contents of these text files, create a
# dictionary by keeping title, name, date, and feedback as keys for the
# content value, respectively.
for file in filenames:
    with open(filepath + '/' + file) as txt_file_review:
        customer_reviews_dict["title"] = txt_file_review.readline()
        customer_reviews_dict["name"] = txt_file_review.readline()
        customer_reviews_dict["date"] = txt_file_review.readline()
        customer_reviews_dict["feedback"] = txt_file_review.readline()
       
        # Use the Python requests module to post the dictionary to the company's website.
        # Use the request.post() method to make a POST request to
        #  http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with
        # corpweb's external IP address.
        response = requests.post("http://34.71.105.87/feedback/", json=customer_reviews_dict)
        print(response.request.body)
        print(response.ok)
        # You can also use the response status_code 201 for created success status response
        # code that indicates the request has succeeded.
        if response.status_code == 201:
            print("victory! " + file + " posting successful.")
        # Make sure an error message isn't returned. You can print the status_code and text
        # of the response objects to check out what's going on.
        else:
            print("error: " + file + " posting unsuccessful " + str(response.status_code))

