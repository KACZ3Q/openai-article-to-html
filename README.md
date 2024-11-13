"# openai-article-to-html" 
**Opis aplikacji**Aplikacja służy do pobierania artykułu w formacie tekstowym z internetu, generowania na jego podstawie kodu HTML przy użyciu API OpenAI oraz tworzenia podglądu artykułu w HTML.Proces obejmuje następujące kroki:

1.  Pobranie artykułu z podanego URL.
    
2.  Przetworzenie treści artykułu na kod HTML, z dodanymi miejscami na grafiki i odpowiednimi tagami.
    
3.  Zapisanie wygenerowanego kodu HTML do pliku.
    
4.  Wygenerowanie szablonu HTML, który może służyć do wyświetlania artykułu.
    
5.  Stworzenie podglądu artykułu w wygenerowanym szablonie HTML.
    

**Wymagania**

*   Python 3.6 lub nowszy
    
*   Zainstalowane biblioteki:
    
    *   requests
        
    *   openai
        
    *   python-dotenv
        

**Instrukcja uruchomienia**

1.  Aby zainstalować wymagane zależności, uruchom polecenie:
    
    *   pip install requests openai python-dotenv
        
2.  W głównym katalogu projektu utwórz plik .env i dodaj w nim następujące zmienne środowiskowe:
    
    *   URL=URL\_DO\_ARTYKULU — Adres URL artykułu, który ma zostać pobrany.
        
    *   API\_KEY=TWÓJ\_KLUCZ\_API\_OPENAI — Twój klucz API do OpenAI (możesz go uzyskać na stronie OpenAI).
        
3.  Po skonfigurowaniu pliku .env, uruchom aplikację za pomocą poniższego polecenia:
    
    *   python main.py
        

Po uruchomieniu aplikacji:

*   Artykuł zostanie pobrany z podanego URL.
    
*   Treść artykułu zostanie przetworzona na kod HTML.
    
*   Wygenerowany kod HTML zapisze się do pliku artykul.html.
    
*   Zostanie również wygenerowany podgląd artykułu w pliku podglad.html.
    

**Struktura plików**

*   main.py – Główny plik uruchamiający aplikację.
    
*   downloader.py – Moduł odpowiedzialny za pobieranie artykułów.
    
*   generator.py – Moduł generujący kod HTML na podstawie treści artykułu oraz szablonu.
    
*   config.py – Plik konfiguracyjny zawierający URL i klucz API.
    
*   .env – Plik konfiguracyjny z danymi do API i URL artykułu.
    
*   artykul.txt – Pobraną treść artykułu w formacie tekstowym.
    
*   artykul.html – Wygenerowany kod HTML dla artykułu.
    
*   szablon.html – Szablon HTML.
    
*   podglad.html – Podgląd artykułu w wygenerowanym szablonie HTML.
    

**Funkcje aplikacji**

1.  **download(url, filename)**Funkcja pobiera treść artykułu z podanego URL i zapisuje ją do pliku o nazwie filename.
    
2.  **read(filename)**Funkcja odczytuje zawartość pliku tekstowego o nazwie filename.
    
3.  **generate(content, api\_key)**Funkcja generuje kod HTML z treści artykułu, wykorzystując OpenAI API do przetworzenia tekstu na odpowiednią strukturę HTML z tagami, takimi jak h1, h2, oraz img.
    
4.  **save(content, filename)**Funkcja zapisuje podaną zawartość do pliku o nazwie filename.
    
5.  **generate\_template()**Funkcja generuje szablon HTML, który będzie używany do wyświetlania artykułu. Zawiera podstawowe style CSS dla treści artykułu i obrazków.
    
6.  **create\_preview(article\_content)**Funkcja tworzy podgląd artykułu, wstawiając wygenerowany kod HTML do szablonu, a następnie zapisuje go do pliku podglad.html.