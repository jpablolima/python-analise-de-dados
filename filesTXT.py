# Manipulando arquivos txt

import os

text = 'Python, JavaScript, NodeJs, C#, '
text = text + 'HTML, css, .net,  '
text += 'Google, Amazon, X-team'
print(text)


 # Criando arquivo
tech = open(os.path.join('tratamentos-de-arquivos/arquivos/tech.txt'), "w")

# Gravando os dados no arquivo
for palavra in text.split():
    tech.write(palavra+' ')
tech.close()

tech = open('tratamentos-de-arquivos/arquivos/tech.txt', 'r')
conteudo = tech.read()
tech.close()
print(conteudo)