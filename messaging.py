import requests
import configparser

def message(msg):
    if __name__ == '__message__':
        message()

    url = "https://www.fast2sms.com/dev/bulk"

    config = configparser.ConfigParser()
    config.read('application.properties')

    #payload = "sender_id=FSTSMS&message=hello&language=english&route=p&numbers=9993097022,9686055388,9826265314"
    payload = {
        'sender_id': 'FSTSMS',
        'message': msg,
        'language': 'english',
        'route': 'p',
        #'numbers': '9993097022, 9686055388, 9826265314'
        'numbers': '9686055388, 9993097022, 9826265314'
    }

    headers = {
        'authorization': "NkzRhtjaZgirTuGIMOUneWpFQP6LKyCwcmXV7ABDdJbl4SqY52yvA4Onr9ecFY23VdZkwaClJ6WhMSmX",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return

message("Test")