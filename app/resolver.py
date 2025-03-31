import pandas as pd


def random_items():
    movies_df = pd.read_csv("data/movies_final.csv")
    movies_df = movies_df.fillna('')
    result_items = movies_df.sample(n=10).to_dict(orient='records')

    return result_items

def random_genres_items(genre: str):
    movies_df = pd.read_csv("data/movies_final.csv")
    genre_df = movies_df[movies_df['genres'].apply(lambda x: genre in x.lower())]
    genre_df = genre_df.fillna('')

    # todo 선택한 장르의 갯수가 5보다 작은경우 처리해야함 2025.3.31

    nitem = min(5, len(genre_df)) #genre.df.shape[0] : 크기 [1]: 컬럼갯수
    print(len(genre_df))
    result_items = genre_df.sample(n=nitem).to_dict(orient='records')

    return result_items

# 지정된 장르를 포함하는 영화중 평점이 높은 5개의 영화를 추천함
# 단 추천인수가 5명이상
def random_genres_items_best(genre: str):
    movies_df = pd.read_csv("data/movies_final.csv")

    genre_df = movies_df[(movies_df['genres'].apply(lambda x: genre in x.lower())) &
                         (movies_df['rcount'] >= 5)
    ]

    genre_df = genre_df.fillna('')
    genre_df.sort_values(by=['rmean'], ascending=False, inplace=True)

    # todo 선택한 장르의 갯수가 5보다 작은경우 처리해야함

    result_items = genre_df.head().to_dict(orient='records')
    return result_items

