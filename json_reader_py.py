import json

with open('bibliotecaProdutos.json', encoding="utf8") as arquivo:
    dados = json.load(arquivo)
    for i in range(len(dados)):
        print(dados[i]['titulo'])
    for i in range(len(dados)):    
        print('---------------------------------------------------------------')
        for j in range(len(dados[i]['atributos'])):
            for k in range(len(dados[i]['atributos'][j]['children'])):
                if(k != len(dados[i]['atributos'][j]['children']) - 1):
                    print(dados[i]['atributos'][j]['children'][k]['valor'], end=", ")
                else:
                    print(dados[i]['atributos'][j]['children'][k]['valor'])
        print('---------------------------------------------------------------')