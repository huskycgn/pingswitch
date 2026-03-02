import requests
from icmplib import ping
from requests.auth import HTTPDigestAuth


def switch_shelly_lan(ip_address: str):
    """
    Invertiert den aktuellen Status des Shelly Plugs (Toggle).

    Args:
        ip_address (str): Die IP-Adresse des Shelly-Geräts.
    Returns:
        bool: True wenn erfolgreich, False bei Fehler.
    """
    url = f"http://{ip_address}/rpc/Switch.Toggle?id=0"
    try:
        response = requests.get(url, timeout=5, auth=HTTPDigestAuth("admin", "dein_passwort"))
        # Der username ist einfach "admin" und das Passwort ist das welches in der Web-GUI vergeben wurde.

        # response = requests.get(url, timeout=5)

        # Falls kein Passwort vergeben wurde, kann diese Codezeile entkommentiert werden.
        # Die oben muss dann auskommentiert werden.

        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Fehler beim Schalten des Shelly ({ip_address}): {e}")
        return False


def get_shelly_status(ip_address: str):
    """
    Fragt ab, ob der Shelly Plug aktuell eingeschaltet ist.

    Args:
        ip_address (str): Die IP-Adresse des Shelly-Geräts.
    Returns:
        bool: True wenn eingeschaltet (output=True), sonst False.
    """
    url = f"http://{ip_address}/rpc/Switch.GetStatus?id=0"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json().get('output', False)
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Fehler beim Status-Abruf ({ip_address}): {e}")
        return False


def is_host_alive(address: str):
    """
    Prüft die Erreichbarkeit eines Hosts per ICMP (Ping).

    Args:
        address (str): IP oder Hostname des Zielgeräts.
    Returns:
        bool: True wenn erreichbar, sonst False.
    """
    try:
        # privileged=False ist wichtig für Linux-User ohne Root
        result = ping(address, count=2, interval=0.5, timeout=2, privileged=False)
        return result.is_alive
    except Exception as e:
        print(f"Ping-Fehler: {e}")
        return False