import pandas as pd
from .textutil import read_csv_d


def list_authors(by_languages, alias):
    """
    This function takes boolen input and returns alias list w.r.t. tranaslation count, otherwise just returns the authors list.
    """
    
    df_a, df_l, df_m = read_csv_d()
    
    
    # merges two datasets on gutenberg_id
    merged_df_l_m = pd.merge(
        df_m,
        df_l,   
        on='gutenberg_id', 
        how='inner'           
    )

    #print(merged_df_l_m.columns)

    merged_df = pd.merge(
        merged_df_l_m,
        df_a,   
        on='gutenberg_author_id',
        how='inner'           
    )

    #print(merged_df.columns)

    merged_df['alias'].dropna().drop_duplicates()

    if by_languages and alias:
        out=merged_df.groupby('alias')['total_languages'].sum().reset_index()
        #print(out.head(10))
        alias_trans_count_sorted = out.sort_values(by='total_languages', ascending=False)
        auth_list = alias_trans_count_sorted['alias'].tolist()
    
    else:
        out = df_a['author'].dropna().drop_duplicates()
        auth_list=out.tolist()
    
    

    return auth_list
