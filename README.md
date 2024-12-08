YouTube View Bot
📖 Description
This project is a YouTube View Bot designed to automate views for YouTube videos. It uses Python and Selenium to open multiple browser tabs and simulate watching videos. The bot allows users to set the number of views, playback duration, and more via a configuration file.

⚙️ Features
Open multiple browser tabs automatically.
Play YouTube videos with customizable watch time.
Automated tab refreshing and cache clearing.
Easy-to-use configuration via config.json.
🛠️ Setup
Prerequisites
Python 3.10 or later
Required Python libraries:
bash
Copier le code
pip install selenium webdriver-manager
Installation
Clone the repository:

bash
Copier le code
git clone https://github.com/YourUsername/YouTube-View-Bot.git
cd YouTube-View-Bot
Install dependencies:

bash
Copier le code
pip install -r requirements.txt
Edit the config.json file to customize the bot settings.

🚀 Usage
Run the bot with the following command:

bash
Copier le code
python main.py
Configuration Options
website: URL of the YouTube video to automate views for.
tab_amount: Number of browser tabs to open.
view_cycles: Number of cycles to repeat watching.
watch_time: Time (in seconds) to watch the video before refreshing.
⚠️ Disclaimer
This project is for educational purposes only. Using bots to manipulate YouTube views is against YouTube's terms of service and could result in penalties, including account suspension. Use at your own risk.
