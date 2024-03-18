import pandas as pd

def clean_csv(file_path):
    df = pd.read_csv(file_path)
    df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)
    return df


def write_cleaned_csv(df, output_file):
    df.to_csv(output_file, sep=';', index=False)

file_path = "_data/events.csv"
cleaned_df = clean_csv(file_path)
output_file = "cleaned_events.csv"
write_cleaned_csv(cleaned_df, output_file)
