import json

from days_calculator import calculate_delta
from messaging import message
from writer import clear_file, append_string, show_file

def main():
    #convert all print statements to logger statements

    # open json file
    file = open('data/Policy_data.json')
    # return json object as dictionary
    data = json.load(file)

    # clear the message_string file beforehand
    clear_file()

    #iterate through file
    for i in data['policy_details']:
        days_left = calculate_delta(i)

        if(days_left<60 and days_left>=0):
            msg = "Policy for " + i['Policy Holder'] + " with number: " + str(i['Policy Number']) + " will mature in " + str(days_left) + " days, on " + i['Maturity Date']
            append_string(msg)

    message(show_file())

main()