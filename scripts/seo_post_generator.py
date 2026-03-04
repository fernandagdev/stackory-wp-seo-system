import datetime
import os
import unicodedata

title = input("Título do post: ")
keyword = input("Palavra-chave principal: ")

date = datetime.date.today()

# função para gerar slug sem acentos
def slugify(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")
    text = text.replace(" ", "-")
    return text

slug = slugify(title)

content = f"""
# {title}

Palavra-chave foco: {keyword}

Publicado em: {date}

## Introdução
Este artigo explica de forma simples o tema {keyword}.

## Desenvolvimento
Aqui você pode desenvolver o conteúdo otimizado para SEO.

## Conclusão
Resumo final reforçando a palavra-chave {keyword}.
"""

# garantir que a pasta docs exista
os.makedirs("docs", exist_ok=True)
import unicodedata
import os

def slugify(text):
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")
    text = text.replace(":", "")
    text = text.replace(" ", "-")
    return text

slug = slugify(title)

os.makedirs("docs", exist_ok=True)

filename = f"docs/{slug}.md"

with open(filename, "w") as f:
    f.write(content)

print("Post gerado em:", filename)
