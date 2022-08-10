import requests
from bs4 import BeautifulSoup

for i in range(1,21):
    URL = f'https://projecteuler.net/problem={i}'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    rawtext = soup.find(class_="problem_content")

    text = rawtext.text.strip().splitlines()
    f = open(f'C:\\Users\\wljos\\Documents\\Coding\\Project Euler\\Problem {i}.py', 'w', encoding='utf-8')
    f.write(f'# {URL}\n\n')
    for words in text:
        line = f'# {words}\n'
        f.write(line)