from downloader import download
from generator import read, generate, save, generate_template, create_preview
from config import URL, API_KEY


def main():
    download(URL, 'artykul.txt')

    article_content = read('artykul.txt')
    html_content = generate(article_content, API_KEY)
    
    save(html_content, 'artykul.html')
    
    save(generate_template(), 'szablon.html')
    
    article_preview=read('artykul.html')
    
    create_preview(article_preview)

if __name__ == "__main__":
    main()
