import pandas as pd

def read_csv_d():
    """
    This function simply reads author and language csv and returns the dataset 
    I have just used this fucntion to understand how modules can call each other within same package
    """
    gutenberg_authors = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    gutenberg_languages = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
    return gutenberg_authors, gutenberg_languages
