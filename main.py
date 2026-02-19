from funcs import *
from time import sleep

SHELLY_IP = "192.168.x.x"
# hier die IP-Adresse des Shelly Geräts eintragen, findet man in der App.

SWITCH_HOST_IP = "192.168.x.x"
# hier die IP-Adresse des Servers eintragen, gegen den geprüft werden soll.

if not check_host(SWITCH_HOST_IP):
    print("Host nicht erreichbar!")
    if get_shelly_lan(SHELLY_IP):
        print("Shelly liefert Strom, schalte ab!")
        switch_shelly_lan(SHELLY_IP)
        print("Warte 10 Sekunden, dann schalte Shelly wieder ein!")
        sleep(10)
        print("Shelly wieder eingeschaltet!")
        switch_shelly_lan(SHELLY_IP)
    else:
        print("Shelly liefert keinen Strom, schalte ein!")
        switch_shelly_lan(SHELLY_IP)
else: print("Host erreichbar!")