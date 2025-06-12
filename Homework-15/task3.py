country_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "UK": "London"
}

country = input("Enter a country name : ")

if country in country_capitals:
    print(f"The capital of {country} is {country_capitals[country]}.")
else:
    print("Sorry, capital city not found for that country.")
