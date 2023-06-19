# 08ccf41a961845bfb645ed7fc8cf038c

import tkinter as tk
from datetime import datetime, timedelta
import requests


def get_upcoming_games():
    today = datetime.now().date()
    next_week = today + timedelta(days=7)

    url = f"https://api.rawg.io/api/games?key=08ccf41a961845bfb645ed7fc8cf038c&dates={today},{next_week}&ordering" \
          f"=released"
    # Replace 'YOUR_API_KEY' with your actual API key from RAWG.io

    response = requests.get(url)
    data = response.json()

    upcoming_games = []

    for game in data['results']:
        game_title = game['name']
        game_release_date = datetime.strptime(game['released'], "%Y-%m-%d").date()
        upcoming_games.append((game_title, game_release_date))

    return upcoming_games


def display_upcoming_games():
    upcoming_games = get_upcoming_games()

    if not upcoming_games:
        message = "No upcoming games this week!"
    else:
        message = "Upcoming Games This Week:\n\n"
        for game_title, game_release_date in upcoming_games:
            message += f"{game_title} - {game_release_date}\n"

    root = tk.Tk()
    root.title("Upcoming Game Releases")

    label = tk.Label(root, text=message, padx=10, pady=10)
    label.pack()

    root.mainloop()


display_upcoming_games()
