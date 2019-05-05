from baseapp.models import Movie
# import pandas as pd

# import pandas as pd
# import datetime
# from myapp.models import BlogPost

# df = pd.DataFrame(list(BlogPost.objects.all().values()))
# df = pd.DataFrame(list(BlogPost.objects.filter(date__gte=datetime.datetime(2012, 5, 1)).values()))

# # limit which fields
# df = pd.DataFrame(list(BlogPost.objects.all().values('author', 'date', 'slug')))


from django_pandas.io import read_frame
#qs = Movie.objects.all()

def sortbysales(movie_list):
    df = read_frame(movie_list)
    df.sort_values(by=['year', 'sales'], ascending=False)
    df = df[['title','sales']][:5]
    #df.to_json()
    #eval(df)
    return df

