# 📡 Pingswitch

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux-lightgrey.svg)](#)

Ein leichtgewichtiges Automatisierungstool, das die Erreichbarkeit eines Netzwerk-Hosts prüft und bei Bedarf einen **Shelly Plug** schaltet (Power Cycle), um hängengebliebene Geräte neu zu starten.

---

## 🚀 Funktionsweise

Das Skript überwacht ein Zielgerät per Ping. Je nach Status reagiert es wie folgt:

* **Host ist offline:** Der Shelly Plug wird kurz aus- und nach 10 Sekunden wieder eingeschaltet (Reboot-Zyklus).
* **Plug ist aus:** Falls der Shelly Plug bereits ausgeschaltet ist, wird er automatisch aktiviert.
* **Host ist online:** Keine Aktion erforderlich – alles läuft wie gewünscht.

> [!TIP]
> Ideal für Router, Access Points oder Server, die gelegentlich einen "harten" Neustart benötigen, um wieder erreichbar zu sein.

---

## 🛠 Anforderungen

Pingswitch funktioniert unter **Windows** und **Linux**. Du benötigst Python 3 und die folgenden Bibliotheken:

```bash
pip3 install requests icmplib