
# coding: utf-8

# In[70]:

# Ebay image retriever
# retrieve images according to keywords and page numbers
# usage: python ebay_retriever.py
# where pages is the total number of pages you would like to read

# Xilin Sun
# May 2016

import urllib
import bs4


# In[81]:

def get_img_links( key_word, pages ):
    image_urls = []
    for page_number in range(pages + 1):
        ebay_url = "http://www.ebay.com/sch/i.html?_pgn=" + str(page_number) + "&_nkw=" + key_word
        result_page = urllib.urlopen(ebay_url)
        try:
            soup = bs4.BeautifulSoup(result_page, "html5lib")
        except:
            print "Error while making soup"
        else:      
            pass 
            #print "Soup is done"
        imgs = soup.find_all('img')
        for image in imgs:
            if image['src'].startswith('http://thumbs'):
                image_urls.append(image['src'])
    return image_urls


# In[ ]:

def main():
    key_word = raw_input("Input keyword: ")
    page_number = int(raw_input("Input number of pages to retrieve: "))
    print "Retrieving urls for images with keyword", key_word, "in", page_number, " pages."
    image_urls = get_img_links(key_word, page_number)
    print image_urls
if __name__ == "__main__":
    main()


# In[ ]:



