# É uma classe de parâmetro não obrigatório. 
from typing import Optional

from typing import Union

from fastapi import FastAPI, Header, Response, Cookie

from pydantic import BaseModel

# Precisamos definir os valores que possui dentro da classe BaseModel ou Item
# BaseModel ajuda a tipar ou seja guiando os tipos que precisamos criar.
# Base Model é o elemento Pai no conceito de herança e o Item o elemento filho.
# id, desc, valor, são variáveis do objeto Item
# Toda classe é um objeto!!!
class Item(BaseModel):
    id:int
    desc: str
    valor: float

app = FastAPI()

#@app é o parâmetro  da aplicação  podendo ser alterada, exemplo @principal, porém terei que alterar 
# os demais campos.

# A função abaixo fica responsavél por ler e enviar a resposta final, retornando assim a palavra Hello Word.

# @ = Annotation, ou seja é uma função que vai ser executada antes da função principal
# O get irá receber uma str(String) como parâmetro para definir o caminho da URL
# Na RD utilizando apenas processo sync, na ordem da requisição.
#Header utilizado para pegar informações do que estiver no cabeçalho

@app.get("/")
def read_root(user_agent: Optional[str] = Header(123)):
    return {"user-agent": user_agent}

#deixa a informação armazenada
#Response: fica responsavél pelos envios das mensagens
@app.get("/cookie")
def cookie(response: Response):
    response.set_cookie(key="meucookie", value=123456) 
    return {"cookie": True}

@app.get("/get-cookie")    
def get_cookie(meucookie: Optional[str] = Cookie(None)):
    return {"Cookie": meucookie}

# A função abaixo fica responsavél por substituir o item_id e a string(texto) q por qualquer outra palavra,
# Lembrando que o item_id possui int de valores inteiros.
# (caminho) = Quando tiver uma variavél dentro do path do verbo(Get, Put), ele vira uma variavél da função,
# do verbo, pois todo verbo precisa de uma função.
# path = caminho
# Get não possui body por definição, podemos criar o body mas definidamente não possui.
# q = Querry String, é um parâmetro que vai dentro das requisições GET.
# Union é uma classe em Python para tipagem, recebendo 2 parÂmetros po definição.
#o q pode ser tanto ou uma string, valor diferente da erro, linha 46 def read_item.
@app.get("/items/{item_id}")
def read_item(item_id: int, p: bool, q: Optional[str] = None):
    return {"item_id": item_id, "q": q, "p": p} 

# Método para adicionar novos itens
# O parâmetro da funçao será os valores que serão preenchidas na requisição, 
# requisição será observada no localhost/docs

@app.post("/item")
def add_item(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]