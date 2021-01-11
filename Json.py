# manipulando arquivos JSON
  
import json
import os


dict = {'Name': 'Pablo', 
        'languages': 'Python, JavaScript',
        'similar': ['NodeJs', '.Net', 'Java'], 
        'users': 1000
}

for k, v in dict.items():
    print(k,v)


json.dumps(dict)
print(dict)

# criando arquivo json

with open('tratamentos-de-arquivos/arquivos/data.json', 'w') as file:
    file.write(json.dumps(dict))



# leitura do arquivo json

with open('tratamentos-de-arquivos/arquivos/data.json', 'r') as file:
    text = file.read()
    data = json.loads(text)
    print(data)
    print(data['Name'])


# imprimindo arquivo da internet

from urllib.request import urlopen
response = urlopen('https://vimeo.com/api/v2/video/440505769.json').read().decode('utf8')
data = json.loads(response)[0]

print('Título: ', data['title'])
print('URL: ', data['url'])
print('Duração: ', data['duration'])
print('Número de visualizações: ', data['stats_number_of_plays'])

# copiando conteúdo de um arquivo para outro

arquivo_fonte = ('tratamentos-de-arquivos/arquivos/data.json')
arquivo_destino = ('tratamentos-de-arquivos/arquivos/data.txt')

open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())

with open('tratamentos-de-arquivos/arquivos/data.json', 'r') as file:
    text = file.read()
    data = json.loads(text)
    print(data)