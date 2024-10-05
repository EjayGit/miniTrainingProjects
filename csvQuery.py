import pandas

data = pandas.read_csv("EuropePopulation.csv")
print(data[data["pop"]>500000])
print(data[data.country == "Germany"])
notNullData = data[data["pop"].notnull()] # notna() is an option
print(notNullData)
citiesWithA = data[data.name.str.startswith("Al")]
print(citiesWithA)
newCitiesData = data[(data.name.str.endswith("e")) & (data.country == "Germany")]
print(newCitiesData)
averagePop = int(data["pop"].mean()) # .pop.mean() would work if pop was not the column name, or not an in built method
print(averagePop)
cityFrance = data[(data["pop"] > averagePop) & (data.country == "France")]
print(cityFrance)

newData = data.groupby("country", sort=False)["pop"].sum()
print(newData)
cityData = data.groupby("country", sort=False)["name"].count()
print(cityData)
cityData.to_csv("city_data.csv")