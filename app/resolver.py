import pandas as pd


def random_items():
    movies_df = pd.read_csv("data/movies_final.csv")
    movies_df = movies_df.fillna('')
    result_items = movies_df.sample(n=10).to_dict(orient='records')

    return result_items

def random_genres_items(genre: str):
    movies_df = pd.read_csv("data/movies_final.csv")
    genre_df = movies_df[movies_df['genres'].apply(lambda x: genre in x.lower())]
    print(genre_df)

    return "result_genre_items"

