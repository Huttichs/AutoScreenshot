from playwright.sync_api import sync_playwright
import sys

def run():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Seite laden mit großzügigem Timeout (60 Sek)
            print("Lade DWD Seite...")
            page.goto("https://www.dwd.de/DE/wetter/warnungen_gemeinden/warnWetter_node.html?ort=Buttlar", wait_until="networkidle", timeout=60000)
            
            # Kurz warten, bis alles gerendert ist
            page.wait_for_timeout(5000)
            
            # Screenshot vom gesamten sichtbaren Bereich
            print("Erstelle Screenshot...")
            page.screenshot(path="warnung_buttlar.png", full_page=False)
            
            browser.close()
            print("Erfolgreich abgeschlossen!")
    except Exception as e:
        print(f"FEHLER aufgetreten: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()
