import requests
from bs4 import BeautifulSoup
 
print("\nWelcome To My Python Weather Application!")
#getWeather function that gets the weather data from google
place = ''

def getWeather(place):
    place = input("Enter your cities name: ")
# requesting data from weather website
    websiteUrl = ("https://www.google.com/search?q="+"weather"+place)
    website = requests.get(websiteUrl).content
    
    # importing data from the website
    soup = BeautifulSoup(website, 'html.parser')
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    # Putting the data together by splitting the lines, designating the time and the lines that data is found on
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    
    #using div tags to locate data
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    
    # getting wind data
    pos = strd.find('Wind')
    # Presenting the data to the user

    print("\nThe current time in ",place," is: ", time)

    print("\nThe weather description in ",place," is: ", sky)

    print("\nThe Temperature in ",place," is: ", temperature,"\n")


try:    
    repeatWeather = int(input("How many places would you like to get the weather of? "))
    if repeatWeather == 0:
        print("Thanks for using! Come Again!")
        quit()
    for i in range(0,repeatWeather):
        try:    
            getWeather(place)
        except AttributeError:
            print("Invalid Location, Check your spelling and capitalization.")

    print("Thanks for using! Come Again!")
except AttributeError:
    print("Enter a valid number.")