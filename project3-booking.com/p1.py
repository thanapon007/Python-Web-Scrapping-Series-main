import requests
from bs4 import BeautifulSoup
import random
import time
import csv

# url_text = 'https://www.booking.com/searchresults.en-gb.html?ss=Bangkok&ssne=Bangkok&ssne_untouched=Bangkok&efdco=1&label=bangkok-3it2SaMYLYoRmShHjrkKxAS453829065535%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-298538156831%3Alp9074847%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YfpWGnRw6lOGgfEoJVv7zYo&aid=1610687&lang=en-gb&sb=1&src_elem=sb&src=city&dest_id=-3414440&dest_type=city&checkin=2025-05-25&checkout=2025-05-26&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&sb_lp=1'


def web_scrapper2(web_url, f_name):
    
    # greetings
    print("Thank you sharing the url and file name!\n⏳\nReading the content!")
    
    num = random.randint(3, 7)
    
    # processing
    time.sleep(num)
 
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}

    response = requests.get(web_url, headers=header)
    

    if response.status_code == 200:
        print("Connected to the website")
        html_content = response.text
        
        
        # creating soup
        soup =  BeautifulSoup(html_content, 'lxml')
        
        # print(soup.prettify())
        
        # main containers
        hotel_divs = soup.find_all('div', role="listitem")
        
        with open(f'{f_name}.csv', 'w', encoding='utf-8') as file_csv:
            writer = csv.writer(file_csv)
            
            # adding header
            writer.writerow(['hotel_name', 'locality', 'price', 'rating', 'score', 'review', 'link'])
        
            for hotel in hotel_divs:
                hotel_name = hotel.find('div', class_="b87c397a13 a3e0b4ffd1").text.strip()
                hotel_name if hotel_name else "NA"
                
                location = hotel.find('span', class_="d823fbbeed f9b3563dd4").text.strip()
                location if location else "NA"
                
                # price
                price = hotel.find('span', class_="b87c397a13 f2f358d1de ab607752a2").text.replace(' ', '')
                if price:
                    price
                else:
                    "NA"
                
                rating = hotel.find('div', class_="f63b14ab7a f546354b44 becbee2f63").text
                rating if rating else "NA"
            
            
                score = hotel.find('div', class_="f63b14ab7a dff2e52086").text.strip().split(' ')[-1]
                score if score else "NA"
                
                review = hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879").text.strip()
                review if review else 'NA'
                
                
                # getting link
                link = hotel.find('a', href=True).get('href')
                link if link else 'NA'
                

                # saving the file into csv
                writer.writerow([hotel_name, location, price, rating, score, review, link])
    
            
            # print(hotel_name)
            # print(location)
            # print(price)
            # print(rating)
            # print(score)
            # print(review)
            # print(link)
            # print('')
        print("Web Scrapped done")
        # print(hotel_divs)
        
        

    else:
        print(f"Connection Failed!{response.status_code}")



# if using this script directly than below task will be executed
if __name__ == '__main__':

    url = input("Please enter url! :")
    fn = input('Please give file name! :')

    # calling the function
    web_scrapper2(url, fn)
