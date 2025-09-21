import pandas as pd
from .read_csv_d import read_csv_d

def list_authors(by_languages, alias):
    
    df_a,df_l = read_csv_d()


    merged_df = merged_df = pd.merge(
        df_a,
        df_l,
        left_on='gutenberg_author_id',    
        right_on='gutenberg_id', 
        how='inner'           
    )

    #print(merged_df.head(10))
    #print(list(merged_df.columns))

    out = merged_df.groupby('alias')['language'].nunique().reset_index()

    alias_lang_count_sorted = out.sort_values(by='language', ascending=False)

    alias_list = alias_lang_count_sorted['alias'].tolist()

    return alias_list