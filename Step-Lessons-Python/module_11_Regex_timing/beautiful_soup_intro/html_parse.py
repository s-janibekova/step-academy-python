from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>Это заголовок первого уровня</h1>
<p class="subtitle">Параграф с классом.</p>
<p>Параграф без класса</p>
<ul>
    <li>Пайтон</li>
    <li>Джава</li>
    <li>Си</li>
    <li>Пхп</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
  print(simple_soup.find('h1').string)

def find_list_items():
  list_items = simple_soup.find_all('li')
  list_content = [e.string for e in list_items]
  print(list_content)

def find_paragraph():
  p = simple_soup.find('p', {'class': 'subtitle'}).string
  print(p)


def find_no_class_paragraph():
  paragraphs = simple_soup.find_all('p')
  other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
  print(other_paragraph[0].string)




def main():
  find_title()
  find_list_items()
  find_paragraph()
  find_no_class_paragraph()


main()