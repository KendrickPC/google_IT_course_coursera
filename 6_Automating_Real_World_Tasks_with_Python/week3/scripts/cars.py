#!/usr/bin/env python3

import json
import locale
import sys
import operator
import os
import emails
import reports



def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  # Creating dictionary to calculate the car model which had the most sales.
  max_sales = {"sales": 0, "model": ""}
  # Creating dictionary to calculate the most popular car_year across all car make/models
  car_year = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item

    # TODO: also handle max sales
    # Calculate the car model which had the most sales
    if item['total_sales'] > max_sales['sales']:
    	max_sales['sales'] = item['total_sales']
    	max_sales['modal'] = item['car']['car_model']
    # TODO: also handle most popular car_year
    # Calculate the most popular car_year across all car make/models
    # in other words, find the total count of cars with the car_year
    # equal to 2005, equal to 2006, etc. and then figure out the most popular year)
    year = item['car']['car_year']
    if year not in car_year:
    	car_year[year] = item['total_sales']
    else:
    	car_year[year] += item['total_sales']
  # Variable to sort car year.
  # import Operator
  sorted_car_year = sorted(car_year.items(), key=operator.itemgetter(1), reverse=True)
  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    # "The {car model} had the most sales: {total sales}"
    "The {} had the most sales: {}".format(max_sales['model'], max_sales['sales']),
    #  "The most popular year was {year} with {total sales in that year} sales."
    "The most popular year was {} with {} sales.".format(sorted_car_year[0][0], sorted_car_year[0][1])
  ]
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data(os.path.expanduser('~') + "/car_sales.json")
  summary = process_data(data)
  print(summary)
  # TODO: turn this into a PDF report
  cars_table_data = cars_dict_to_table(data)
  # The report should be named as cars.pdf, and placed in the folder /tmp/.
  path = '/tmp/cars.pdf'
  # Note: To add line breaks in the PDF, use: <br/> between the lines.
  line_breaks = "<br/>".join(summary)
  title = "Sales summary for last month"
  # Using the reports.generate() function within the main function.
  reports.generate(path, title, line_breaks, cars_table_data)

  # TODO: send the PDF report as an email attachment
  # Look at the example.py file as a template for this section.
  email_from = 'automation@example.com'
  # import OS from example.py
  email_to = '{}@example.com'.format(os.environ.get('USER'))
  email_subject = "Sales summary for last month"
  email_body = '\n'.join(summary)
  message = emails.generate(email_from, email_to, email_subject, email_body, path)
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)

