import pandas as pd
from .textutil import read_csv_d

def list_authors(by_languages, alias):
    
    df_a,df_l = read_csv_d()

    #print(df_l['total_languages'].nunique)
    merged_df = merged_df = pd.merge(
        df_a,
        df_l,
        left_on='gutenberg_author_id',    
        right_on='gutenberg_id', 
        how='inner'           
    )

    merged_df = merged_df.dropna(subset=['alias'])
    #print(merged_df.head(10))
    #print(list(merged_df.columns))


    if by_languages and alias:
        out=merged_df.groupby('alias')['total_languages'].sum().reset_index()
        #print(out.head(10))
        alias_trans_count_sorted = out.sort_values(by='total_languages', ascending=False)
        auth_list = alias_trans_count_sorted['alias'].tolist()
    
    else:
        out = df_a['author'].dropna().drop_duplicates()
        auth_list=df_a['author'].tolist()
    
    

    return auth_list

