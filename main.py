import requests
import bs4
sheet = 0
page = requests.get("https://wuzzuf.net/search/jobs/?a=hpb&q=full%20stack%20web%20develops&start=1")
sorc = page.content
soup = bs4.BeautifulSoup(sorc,"html.parser")
numjops = soup.find("strong")
print(numjops.text)

while True:
    page = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=full%20stack%20web%20develops&start={sheet}")
    sorc = page.content
    soup = bs4.BeautifulSoup(sorc,"html.parser")
    JopsName = soup.find_all("h2",{"class":"css-m604qf"})
    CompanyName = soup.find_all("a" , {"class":"css-17s97q8"})
    Address = soup.find_all("spam",{"class":"css-5wys0k"})
    Skills = soup.find_all("div",{"class":"css-y4udm8"})
    for x in range(len(JopsName)) :
        print(JopsName[x].text,"----",CompanyName[x].text,"----",Skills[x].text,"\n","_"*50)
    sheet+=1


#print(len(JopsName))
#print(numjops.text)
