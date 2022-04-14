import requests
def SendMessage(msg,number):
    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = "variables_values={}&route=otp&numbers={}".format(msg,number)
    headers = {
        'authorization': "ZcmeHGgW8v4zfoq3RUnurIiYMxj6DN1dSEkb0OyXBCKPFl5VsLtygC8Wh1oTqGwKREZX4bs7pvLlYHmF",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text