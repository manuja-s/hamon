from bs4 import BeautifulSoup
import requests
import urllib.request


url='https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2738542-7950'
page=requests.get(url, verify=False).text
soup = BeautifulSoup(page,features="html.parser")
i=1
for img in soup.find_all('img'):
    if img.has_attr("title"):
        if "Aamir Khan" in img["title"]:

            imgsrc=img.get('src')

            if imgsrc[:1]=='/':
                image='https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2738542-7950'+imgsrc

            else:
                image=imgsrc

            filename='image'+str(i)
            i=i+1
            imgfile=open(filename+".jpeg",'wb')
            imgfile.write(urllib.request.urlopen(image).read())
            imgfile.close()






