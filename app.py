from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)


# Example: if your DataFrame is df_songs
df_songs = pd.read_pickle('df.pkl')
# print(type(df_songs))   # should show <class 'dict'>
# print(df_songs.keys())  # see what keys are inside
songs = list(df_songs.values())[1]
songs = list(songs.values())

def recommend(title):
    # Replace with your actual recommendation logic
    return [f"Recommendation {i} for {title}" for i in range(1, 6)]


@app.route("/", methods=["GET", "POST"])
def index():
    selected_song = None
    recommendations = []

    if request.method == "POST":
        selected_song = request.form.get("song")
        recommendations = recommend(selected_song)

    return render_template("index.html", songs=songs,
                           selected_song=selected_song,
                           recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)

