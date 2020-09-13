import pandas

# Requirement : Remove any zeros prepended to the price field
# Pandas will automatically infer datatypes and cast price field as float
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

# Requirement : Split the name field into first_name, and last_name
# Using pandas, split name col on with " " seperator
def split_name(df : pandas.DataFrame):
    if "name" in df.columns:
        df[["first_name", "last_name"]] = df["name"].str.split(pat = " ", n = 1, expand = True)
        return df
    else:
        raise("Column 'name' not in dataframe")

# Requirement : Delete any rows which do not have a name
# Filter dataframe where len of name is > 0
def filter_name(df : pandas.DataFrame):
    if "name" in df.columns:
        return df[(df["name"].str.len() > 0)]
    else:
        raise("Column 'name' not in dataframe")

# Requirement : Create a new field named above_100, which is true if the price is strictly greater than 100
# 
def price_above100(df : pandas.DataFrame):
    df["above_100"] = df["price"] > 100

    return df

if __name__ == "__main__" :
    try:
        df = read_file("dataset.csv")
        print(df)

        df = filter_name(df)
        print(df)

        df = split_name(df)
        print(df)

        df = price_above100(df)
        print(df)

        df.to_csv("processed_dataset.csv", sep=",", header=True, index=False)

    except Exception as e:
        print(e)
