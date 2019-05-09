from baseapp.models import Movie
from django_pandas.io import read_frame
import pandas as pd

def sortbysales(movie_list):
    df = read_frame(movie_list)
    #df = df.query('year>=2017')
    df.sort_values(by='sales', ascending=False)
    df = df[['title','sales']][:5].to_json()
    #lst = df.values
    return eval(df)

