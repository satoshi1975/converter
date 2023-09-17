import requests
from string import Template

API_KEY = 'd80d53c6fc48856687da0a76'
converter_template = Template('https://v6.exchangerate-api.com/v6/$key/pair/$from_curr/$to_curr')
list_of_rates_temp = Template('https://v6.exchangerate-api.com/v6/$key/latest/$curr')


def get_currency(from_curr, to_curr, value):
    """конвертация валют с учетом количества"""
    api_request = converter_template.substitute(key = API_KEY, from_curr = from_curr,to_curr=to_curr)
    response = requests.get(api_request).json()
    if response['result'] == 'success':
        rate = float(response['conversion_rate'])
        res_convert = rate*value
        return {'success':True,'result':res_convert}
    else:
        return{'success':False,'error':response['error-type']}
    
def list_of_rates(currency):
    """Список всех валют в отношении к базовой"""
    api_request = list_of_rates_temp.substitute(key=API_KEY,curr=currency)
    
    response = requests.get(api_request).json()
    print(response)
    if response['result'] == 'success':
        return{'success':True,'list':response['conversion_rates']}
    else:
        return{'success':False,'error':response['error-type']}