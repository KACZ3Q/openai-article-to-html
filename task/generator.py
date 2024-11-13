import openai

def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def generate(content, api_key):
    openai.api_key = api_key

    prompt = f"""
    Wygeneruj kod HTML dla poniższego artykułu. Kod powinien spełniać następujące wytyczne:
    - Użyj odpowiednich tagów HTML do strukturyzacji treści np. h1, h2.
    - Wskaż miejsca, gdzie warto wstawić grafiki, używając tagu <img> z atrybutem src="image_placeholder.jpg".
    - Dodaj atrybut alt do każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki. 
    - Umieść podpisy pod grafikami używając odpowiedniego tagu HTML np. figacaption.
    - Nie używaj CSS ani JavaScript. 
    - Kod powinien zawierać wyłącznie zawartość do wstawienia pomiędzy tagami <body> i </body>. 
    - Nie dołączaj znaczników <html>, <head> ani <body>.
    - Wygenerowany kod HTML powinien być gotowy do wklejenia między tagi <body> w istniejącej stronie.
    - Kod nie powinien zawierać na początku ani na końcu frazy \"""html \"""
    
    Oto treść artykułu:
    {content}
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Jesteś pomocnym asystentem specjalizującym się w konwersji tekstów do HTML."},
                  {"role": "user", "content": prompt}],
        max_tokens=1500,
        temperature=0.7,
    )

    return response.choices[0].message.content

def save(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def generate_template():
    template = """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Podgląd Artykułu</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
                background-color: #4f95bd;
            }
            img {
                max-width: 100%;
                height: auto;
                display: block;
                margin: 20px auto;
            }
            figcaption {
                text-align: center;
                font-style: italic;
                color: #555;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <!-- Content will be inserted here -->
    </body>
    </html>
    """
    return template

def create_preview(article_content):
    template = generate_template()
    preview = template.replace("<!-- Content will be inserted here -->", article_content)

    save(preview, "podglad.html")