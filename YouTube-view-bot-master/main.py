import json
from time import sleep
import driver


def get_config():
    """Read configuration file."""
    try:
        with open('config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: 'config.json' not found. Please ensure the file is present in the directory.")
        exit()


def init_tabs(website, tab_amount):
    """Open tabs according to the tab amount in config.json."""
    for _ in range(tab_amount):
        website.new_tab()


def open_links(website, tab_amount):
    """Open the YouTube link in each tab."""
    for tab in range(tab_amount):
        website.switch_tab(tab)
        website.get_vid()


def play_video(website, tab_amount):
    """Click on the play button in each tab."""
    for tab in range(tab_amount):
        website.switch_tab(tab)
        website.play_video()


def refresh_all(website, tab_amount):
    """Refresh all tabs."""
    for tab in range(tab_amount):
        website.switch_tab(tab)
        website.refresh()


def main():
    """Main function."""
    print("Initialization")
    config = get_config()

    print("Starting browser")
    website = driver.Bot(config['website'], config['browser'])

    print("Opening new tabs")
    init_tabs(website, config['tab_amount'])

    print("Opening links")
    open_links(website, config['tab_amount'])

    print("Cycle start")
    for i in range(config['view_cycles']):
        print(f"Playing videos (Cycle {i + 1}/{config['view_cycles']})")
        play_video(website, config['tab_amount'])

        sleep(config['watch_time'])  # Watch the video for the specified time.

        print("Refreshing all tabs")
        refresh_all(website, config['tab_amount'])

        print("Clearing cache")
        website.clear_cache()

    print("Complete. Closing browser.")
    website.driver.quit()


if __name__ == '__main__':
    main()
