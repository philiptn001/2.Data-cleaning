import pandas as pd


def clean_city(cell):
    if "London" in cell:
        return "London"
    else:
        return cell


df = pd.read_csv("Books.csv")
# print(df.to_string())
drop_columns = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver',
                'Contributors', 'Issuance type', 'Shelfmarks']
df.drop(drop_columns, axis="columns", inplace=True)
df.columns = [c.replace(" ", "_") for c in df.columns]
df["Place_of_Publication"] = df["Place_of_Publication"].apply(clean_city)
df["Date_of_Publication"] = df["Date_of_Publication"].str.extract(r"^(\d{4})")
df["Date_of_Publication"] = df["Date_of_Publication"].fillna(0)
df["Date_of_Publication"] = df["Date_of_Publication"].apply(int)
# df["Date_of_Publication"] = pd.to_numeric(df["Date_of_Publication"])
# df = df.query("Place_of_Publication == 'London' and Date_of_Publication > 1866")
df2 = pd.read_csv("City.csv")

rdf = pd.merge(df, df2, how= 'left', left_on=["Place_of_Publication"], right_on=["City"] )
rdf.groupby("Country")["Identifier"].count()
# rdf.groupby("Country").count()
print(df.to_string())
print(df2.to_string())
print(rdf.to_string())

# print(rdf.isnull().sum()/ rdf.shape[0]*100)