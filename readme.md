# Pingswitch Readme

Dieses Skript prüft ob ein Host auf Pings antwortet.<br>
Wenn nicht wird ein Shelly Plug erst aus und dann wieder eingeschaltet.<br>
Ist der Shelly Plug bereits aus, wird er eingeschaltet.<br>

Das Skript funktioniert auf Windows und Linux.

## Anforderungen:

Es werden die *requests* und die *icmplib* Libraries benötigt.<br>
Die können folgendermaßen installiert werden:
<br><br>
*pip3 install requests*<br>
*pip3 install icmplib*
<br>
## Einrichtung:<br>

Die Konstanten<br> *SHELLY_IP = "192.168.x.x"* <br>
(IP des Shelly Plugs)
<br>und<br>
*SWITCH_HOST_IP = "192.168.x.x"*
<br>(IP des Hosts der geprüft werden soll)<br>
In der *main.py* Datei müssen angepasst werden.<br>

Es empfiehlt sich einen cronjob für die regelmäßige Ausführung einzurichten.<br>

Beispiel für Ausführung per cronjob in<br> 
*/etc/crontab:* <br>
**/5 * * * * /usr/bin/python3 /home/user/pingswitch/main.py*

Das würde das Skript alle 5 Minuten ausführen.