# Criando e escrevendo em arquivos de texto (modo 'w').
# -*- coding: utf-8 -*-
'''
arquivo = open('arq01.txt','w')
arquivo.write("Bóson Treinamentos\n")
arquivo.write("Criando um arquivo de texto com Python\n")
arquivo.write("Arquivo criado por Fábio dos Reis\n")
arquivo.write("É isso ai pessoal!\n")
arquivo.close()

# Lendo o arquivo criado:
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()
'''
import PySimpleGUI as sg


def CalcularIMC(valores):
    alturaStr = valores('altura').replace('','',"").replace(".","")
    peso = float(valores['peso'])
    altura = float(alturaStr)/100
    imc = peso / (altura*altura)
    return round(imc, 2)


l0 = [sg.Text("Qual o seu peso?"), sg.InputText('', key='peso'), sg.Text('Kg')]
l1 = [sg.Text("Qual a sua altura?"), sg.InputText('', key= 'altura'), sg.Text('cm')]
l2 = [sg.Text('Seu IMC é'), sg.Text('', key='imc', size=(6,1))]
l3 = [sg.Text('', size=(14,1)), sg.Button('Calcular IMC')]

container = [l0, l1, l2, l3]

janela = sg.Window('Calculadora de IMC', container, font=('Helvetica', 14))

rodando = True
while rodando:
    eventos, valores = window.read()
    print(valores)
    if eventos == sg.WIN_CLOSED:
        rodando = False
    elif eventos == 'Calcular IMC':
        imc = CalcularIMC(valores)
        janela.Element('imc').Update(imc)
janela.close
