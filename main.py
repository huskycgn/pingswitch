from time import sleep
from funcs import is_host_alive, get_shelly_status, switch_shelly_lan

# --- KONFIGURATION ---
SHELLY_IP = "192.168.x.x"
TARGET_HOST = "192.168.x.x"
REBOOT_DELAY = 10  # Sekunden Wartezeit beim Power-Cycle


def main():
    print(f"Prüfe Status von {TARGET_HOST}...")

    if is_host_alive(TARGET_HOST):
        print("✅ Host erreichbar. Alles in Ordnung.")
        return

    print("⚠️ Host nicht erreichbar!")

    # Status prüfen: Liefert der Shelly Strom?
    is_on = get_shelly_status(SHELLY_IP)

    if is_on:
        print("🔌 Shelly ist AN. Starte Power-Cycle (Neustart)...")
        switch_shelly_lan(SHELLY_IP)  # Ausschalten
        print(f"Warte {REBOOT_DELAY}s...")
        sleep(REBOOT_DELAY)
        switch_shelly_lan(SHELLY_IP)  # Einschalten
        print("🚀 Shelly wurde neu gestartet.")
    else:
        print("🔌 Shelly ist AUS. Schalte jetzt ein...")
        switch_shelly_lan(SHELLY_IP)
        print("🚀 Shelly wurde aktiviert.")


if __name__ == "__main__":
    main()