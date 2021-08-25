import json

from days_calculator import calculate_delta
from messaging import message

def main():
    #convert all print statements to logger statements

    # open json file
    file = open('data/Policy_data.json')
    # return json object as dictionary
    data = json.load(file)

    #iterate through file
    for i in data['policy_details']:
        days_left = calculate_delta(i)

        msg = "Policy for " + i['Policy Holder'] + " with number: " + str(i['Policy Number']) + " will mature in " + str(days_left) + ", on " + i['Maturity Date']

        if(days_left>30 and days_left<=60 and days_left%5 == 0):
            # send mail and sms once in 5 days
            pass

        elif(days_left>10 and days_left<=30 and days_left%3 == 0):
            # send sms once in 3 days
            message(msg)

        elif(days_left>=0 and days_left<=10):
            # send sms and mail daily
            pass

        else:
            pass

main()