import json
from urllib.request import urlopen
working = True
while working:
    zip_code = input("Enter A Valid Zip Code")
    country = input("Enter a Valid Country")
    with urlopen("https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid=b9afdec440a1959b3d10963dad34a524".format(zip_code, country)) as response:
        source = response.read()
    data = json.loads(source)
    conditions = data['weather'][0]['description']
    temp = data['main']['temp'] - 273
    humidity = data['main']['humidity']

    print("Based on your location we have gathered the folliwing information:")
    print("Your current temperature is : " + str(temp))
    print("Your current conditions are : " + conditions)
    print("Your current humidex rating is : " + str(humidity))

    try_again = input("Would you like to enter another zipcode?")
    if try_again == "yes":
        continue
    else:
        working = False
