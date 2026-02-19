# Pingswitch Readme

Dieses Skript prüft ob ein Host auf Pings antwortet.
Wenn nicht wird ein Shelly Plug erst aus und dann wieder eingeschaltet.
Ist der Shelly Plug bereits aus, 
wird er eingeschaltet.

Das Skript funktioniert auf Windows und Linux.

## Anforderungen:

Es werden die requests und die icmplib Libraries benötigt.
Die können folgendermaßen installiert werden:

*pip3 install requests*<br>
*pip3 install icmplib*

## Einrichtung:

Es empfiehlt sich einen cronjob für die regelmäßige Ausführung einzurichten.

Beispiel für Ausführung per cronjob in<br> 
*/etc/crontab:* <br>
**/5 * * * * /usr/bin/python3 /home/user/pingswitch/main.py*

Das würde das Skript alle 5 Minuten ausführen.