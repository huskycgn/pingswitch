import requests
import icmplib


def switch_shelly_lan(ipaddress):
    '''Schaltet den Shelly Plug aus und ein'''
    try:
        base_url = f"http://{ipaddress}/rpc/Switch.Toggle?id=0"
        response = requests.get(url=base_url)
        return response.text
    except:
        return "Error"


def get_shelly_lan(ipaddress):
    '''Wertet den aktuellen Status des Shelly Plugs aus'''
    try:
        base_url = f"http://{ipaddress}/rpc/Switch.GetStatus?id=0"
        response = requests.get(url=base_url)
        json_data = response.json()
        return json_data['output']
    except:
        return "Error"

def check_host(address):
    '''Prüft, ob ein Host online ist'''
    host = icmplib.ping(address=address, count=1, interval=1, timeout=2, privileged=False)
    return host.is_alive