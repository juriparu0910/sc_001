# Webページを取得して解析する
#load_url = "https://arxiv.org/"
load_url = "https://arxiv.org/search/astro-ph?searchtype=author&query=Bernhard%2C+E"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# title、h2、liタグを検索して表示する
#print(soup.find("title"))    # タグを検索して表示
print(soup.find("h2"))
#print(soup.find("li"))

# すべてのliタグを検索して、その文字列を表示する
#for element in soup.find_all("li"):    # すべてのliタグを検索して表示
#    print(element.text)
    
# classで検索して、そのタグの中身を表示する
#abstract1 = soup.find(class_="abstract mathjax")    # classs が「abstract mathjax」のclass要素を表示
abstract1 = soup.find(class_="abstract")    # classs が「abstract」のclass要素を表示

print(abstract1)