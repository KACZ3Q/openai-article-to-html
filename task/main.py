from downloader import download
from generator import read, generate, save
from config import URL, API_KEY


def main():
    download(URL, 'artykul.txt')

    article_content = read('artykul.txt')
    html_content = generate(article_content, API_KEY)
    
    save(html_content, 'artykul.html')

if __name__ == "__main__":
    main()
