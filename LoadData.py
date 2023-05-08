import pandas as pd

df = pd.read_csv("docs/addresses.csv")
print(df.head())

# df1 = pd.read_excel("docs/Financial Sample.xlsx")
# print(df1.head())

dt = {
    'Name': ['Vaths', "Jack", "Kelly", "Pam"],
    'Major': ['Science', 'Arts', 'Engineering', 'Designing']
}

df = pd.DataFrame(dt)
print(df, end="\n\n")
print(df[['Name']])

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
print(df.head())

print()
df = pd.read_excel('docs/Financial Sample.xlsx')
print(df.head())
