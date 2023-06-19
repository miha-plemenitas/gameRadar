import tkinter as tk
from tkinter import ttk
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
        game_platforms = [platform['platform']['name'] for platform in game['platforms']]
        upcoming_games.append((game_title, game_release_date, game_platforms))

    return upcoming_games


def display_upcoming_games():
    upcoming_games = get_upcoming_games()

    if not upcoming_games:
        message = "No upcoming games this week!"
    else:
        root = tk.Tk()
        root.title("GameRadar")

        # Configure root window attributes
        root.geometry("1100x450")
        root.configure(bg="#f0f0f0")

        # Create a frame for the table
        frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        # Create and configure the header label
        header_label = tk.Label(
            frame,
            text="GameRadar",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 16, "bold"),
            padx=10,
            pady=10
        )
        header_label.pack()

        # Create a treeview for the table
        treeview = ttk.Treeview(frame)
        treeview.pack(fill=tk.BOTH, expand=True)

        # Configure the columns
        treeview["columns"] = ("Title", "Release Date", "Platforms")
        treeview.column("#0", width=0, stretch=tk.NO)
        treeview.column("Title", anchor=tk.W, width=200)
        treeview.column("Release Date", anchor=tk.W, width=100)
        treeview.column("Platforms", anchor=tk.W, width=200)

        # Create the table headings
        treeview.heading("#0", text="", anchor=tk.W)
        treeview.heading("Title", text="Title", anchor=tk.W)
        treeview.heading("Release Date", text="Release Date", anchor=tk.W)
        treeview.heading("Platforms", text="Platforms", anchor=tk.W)

        # Insert the game data into the table
        for game_title, game_release_date, game_platforms in upcoming_games:
            treeview.insert("", tk.END, text="", values=(game_title, game_release_date, ", ".join(game_platforms)))

        root.mainloop()


display_upcoming_games()
