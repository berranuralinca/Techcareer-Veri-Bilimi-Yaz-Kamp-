import pandas as pd
import random

def train_test(books):
    df = pd.DataFrame(books)

    train_size = int(len(df) * 0.7)
    train_indices = random.sample(list(df.index), train_size)
    test_indices = list(set(df.index) - set(train_indices))

    train_df = df.loc[train_indices]
    test_df = df.loc[test_indices]

    author_avg = train_df.groupby("author")["sales"].mean()

    test_df = test_df.copy()
    test_df["author_average"] = test_df["author"].map(author_avg)
    bigger_than = test_df[test_df["sales"] > test_df["author_average"]]

    return author_avg,bigger_than,train_df,test_df