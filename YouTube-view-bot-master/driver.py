from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Bot:
    def __init__(self, url, browser="chrome"):
        if browser.lower() == "chrome":
            options = Options()
            options.add_argument("--start-maximized")  # Ouvrir en mode plein écran
            options.add_argument("--disable-popup-blocking")  # Bloquer les popups
            options.add_argument("--incognito")  # Mode navigation privée

            # Initialiser le driver Chrome
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.url = url

    def new_tab(self):
        """Ouvrir un nouvel onglet."""
        self.driver.execute_script("window.open('');")

    def switch_tab(self, tab_index):
        """Passer à un onglet spécifique."""
        self.driver.switch_to.window(self.driver.window_handles[tab_index])

    def get_vid(self):
        """Accéder à l'URL définie."""
        self.driver.get(self.url)

    def play_video(self):
        """Appuyer sur le bouton play (vous devez adapter pour détecter le bouton)."""
        play_button = self.driver.find_element("css selector", "button[class*='play']")
        play_button.click()

    def refresh(self):
        """Rafraîchir l'onglet actuel."""
        self.driver.refresh()

    def clear_cache(self):
        """Effacer le cache (peut nécessiter une implémentation personnalisée)."""
        self.driver.delete_all_cookies()
