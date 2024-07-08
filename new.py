import secret 
import requests


def account_number(account_num, accountname):
    url = f"https://api.paystack.co/bank/resolve?account_number={account_num}&bank_code={accountname}"
    headers = {
        "Authorization": "Bearer " + secret.secret
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
         data = response.json()
         return data



def bank_code(bankname, account_number):
     baseurl = f"https://api.paystack.co/bank"
     headers = {
         "Authorization": "Bearer " + secret.secret
     }
     response = requests.get(baseurl, headers=headers)
     if response.status_code == 200:
         data = response.json()['data']
         for bank_info in data:
                #  banks = {
                #       'bank_name': bank_info['name'], 
                #       'bank_code': bank_info['code']
                #  }
                 if bank_info['name'] ==bankname:
                      bankname=  bank_info['code']
                      url = f"https://api.paystack.co/bank/resolve?account_number={account_number}&bank_code={bankname}"
                      response2 = requests.get(url, headers=headers)
                      if response2.status_code == 200:
                            data = response2.json()['data']
                            return data['account_name']



# print(account_number(2270268887, "057" ))
print(bank_code("Kuda Bank", 2020097356))














