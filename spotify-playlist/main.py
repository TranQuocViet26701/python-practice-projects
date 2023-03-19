import os
from typing import List
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

load_dotenv()

SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
SPOTIFY_REDIRECT_URI = os.environ["SPOTIFY_REDIRECT_URI"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope="user-library-read playlist-modify-private"))


def crawl_playlist(date):
    response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
    response.raise_for_status()

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    song_title_tags = soup.select(".o-chart-results-list-row-container ul #title-of-a-story")
    artist_tags = soup.select(".o-chart-results-list-row-container ul #title-of-a-story + span")
    song_titles = [tag.get_text().strip() for tag in song_title_tags]
    artists = [tag.get_text().strip() for tag in artist_tags]

    songs = []
    for i in range(len(song_titles)):
        songs.append({
            "title": song_titles[i],
            "artist": artists[i]
        })

    return songs


def search_songs(songs) -> List[str]:
    track_uris = []
    for song in songs:
        try:
            songs = sp.search(q=song["title"], limit=10, offset=0, type='track')
            track = songs["tracks"]["items"][0]
        except IndexError:
            print("Track Not Found")
        else:
            track_uris.append(track["uri"])
            # print(track["uri"])

    return track_uris


def make_playlist(date):
    songs = crawl_playlist(user_input)
    track_uris = search_songs(songs)

    current_user = sp.current_user()
    playlist = sp.user_playlist_create(user=current_user["id"], name=f"{date} Billboard 100", public=False)
    print(playlist)

    sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
    print(f"Make {date} Billboard 100 successful! 🎶🎶🎶. See it: {playlist['external_urls']['spotify']}")


user_input = input("Which year do you want to travel to? Type the date in format YYYY-MM-DD: ")
make_playlist(user_input)











