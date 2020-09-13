import pandas

def read_file(file_name : str, file_sep : str = ",", file_header : int = 0):
    print("Accepted Parameters for file : ")
    print("Reading file {}".format(file_name))
    print("Delimited by {}".format(file_sep))
    print("Header Pos {}".format(file_header))

    df = pandas.read_csv(
        filepath_or_buffer=file_name,
        sep = file_sep,
        header = file_header
    )
    print("File read successfully with counts {}".format(len(df)))
    return df

def split_name(df : pandas.DataFrame):


    if "name" in df.columns:
        df[["firstname", "lastname"]] = df["name"].str.split(pat = " ", n = 1, expand = True)
        return df
    else:
        raise("Column 'name' not in dataframe")

if __name__ == "__main__" :
    try:
        df = read_file("dataset.csv")
        print(df)

        df = split_name(df)
        print(df)
    except Exception as e:
        print(e)
