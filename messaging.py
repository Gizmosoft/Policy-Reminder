import requests
import configparser

def message(msg):
    if __name__ == '__message__':
        message()

    url = "https://www.fast2sms.com/dev/bulk"

    #payload = "sender_id=FSTSMS&message=hello&language=english&route=p&numbers=9993097022,9686055388,9826265314"
    payload1 = {
        'sender_id': 'FSTSMS',
        'message': msg,
        'language': 'english',
        'route': 'p',
        'numbers': '9686055388'
    }

    payload2 = {
        'sender_id': 'FSTSMS',
        'message': msg,
        'language': 'english',
        'route': 'p',
        'numbers': '9993097022'
    }

    payload3 = {
        'sender_id': 'FSTSMS',
        'message': msg,
        'language': 'english',
        'route': 'p',
        'numbers': '9826265314'
    }

    headers = {
        'authorization': "NkzRhtjaZgirTuGIMOUneWpFQP6LKyCwcmXV7ABDdJbl4SqY52yvA4Onr9ecFY23VdZkwaClJ6WhMSmX",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload1, headers=headers)
    print(response.text)
    response = requests.request("POST", url, data=payload2, headers=headers)
    print(response.text)
    response = requests.request("POST", url, data=payload3, headers=headers)
    print(response.text)
    return

#message("Test")