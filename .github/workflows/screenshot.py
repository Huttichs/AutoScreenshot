from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        # Browser starten
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        
        # DWD Seite für Buttlar aufrufen
        url = "https://www.dwd.de/DE/wetter/warnungen_gemeinden/warnWetter_node.html?ort=Buttlar"
        page.goto(url, wait_until="networkidle")
        
        # Optional: Kurz warten, falls Scripte nachladen
        time.sleep(5) 
        
        # Das Element mit den Warnungen finden und fotografieren
        # #main ist der Hauptinhalt beim DWD
        page.locator("#main").screenshot(path="warnung_buttlar.png")
        
        browser.close()

if __name__ == "__main__":
    run()