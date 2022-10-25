import requests
import bs4

HEADERS = {
    'Cookies': 'yandexuid=7872100861644332491; yuidss=7872100861644332491; my=YwA=; ymex=1972109901.yrts.1656749901;'
               ' yandex_gid=117428; gdpr=0; _ym_uid=1645464466702207110; amcuid=4972560311656757599;'
               ' is_gdpr=1; is_gdpr_b=CNzDcxCdfBgBKAI=; _ym_d=1657306071;',
    'Acceept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua-mobile': '?0'}

KEYWORDS = {'дизайн', 'фото', 'web', 'Python', 'python'}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'
response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')
#print(articles)

for article in articles:
    previews = dict()
    k = 0
    for i in articles :
        preview = i.find(class_="article-formatted-body article-formatted-body article-formatted-body_version-1")
        if preview :
            previews.setdefault(k, preview.text)
        else :
            preview = i.find(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
            previews.setdefault(k, preview.text)
        k += 1
    date = article.find('time').text
    title = article.find('a', class_='tm-article-snippet__title-link')
    span_title = title.find('span').text
    print(span_title)
    print(date)
    print(previews)

    if KEYWORDS & previews:
        href = title['href']
        result = f'Название татьи => {span_title} / Дата статьи {date} / Ссылка {base_url + href}'
        print(result)
