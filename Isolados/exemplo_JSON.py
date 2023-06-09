import requests
import json

class App:
    def __init__(self, dados):
        self.__dados = IParse(dados)

class IParse:
    def __init__(self, dados):
        self.__dados = dados

    def parse(self, arq:dict):
        return arq

class JSONParser(IParse):
    def __init__(self, url:str):
        self.__arq = json.loads(json.dumps(url))

    def parse(self):
        super().parse(self.__arq)

class CSVParser(IParse):
    def __init__(self, arq):
        self.__arq = arq

    def parse(self):
        a = CSVAdapter(list(self.__arq))
        super().parse(a.parse())

class CSVAdapter(CSVParser):
    def __init__(self, lista):
        L = len(lista)
        self.__r = {}
        for i in range(0, L, 2):
            self.__r[lista[i]] = lista[i+1]

    def parse(self, arq):
        return self.__r
