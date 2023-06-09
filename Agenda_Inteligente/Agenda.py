from tkinter import *
from functools import partial
from AgendaDAO import AgendaDAO

class App:
    def __init__(self, toplevel):

        self.mensal = ['', "Janeiro", "Fevereiro", "Março",
                       "Abril", "Maio", "Junho", "Julho",
                       "Agosto", "Setembro", "Outubro",
                       "Novembro", "Dezembro"]

        self.ano = ['']*13
        self.display = ['']*13
        self.nome_meses = ['']*13

        self.dias_meses = [
            '', ['']*32, ['']*29, ['']*32,
            ['']*31, ['']*32, ['']*31,
            ['']*32, ['']*32, ['']*31,
            ['']*32, ['']*31, ['']*32
        ]

        self.semanas = [
            '', ['']*5, ['']*5, ['']*5, ['']*5,
            ['']*5, ['']*5, ['']*5, ['']*5,
            ['']*5, ['']*5, ['']*5, ['']*5
        ]

        self.sel = {'prova': ('Estudar para ', 8),
                    'trabalho': ('Fazer o ', 15)}

        self.MesAtual = 1

        self.conteiner = Frame(toplevel)
        self.menu = Frame(toplevel)

        self.entrada = Entry(toplevel,
                             font=('Arial',
                                   '12',
                                   'bold'))

        self.entrada.focus_force()

        self.entrada.bind('<Return>',
                          self.agenda)

        self.entrada.pack(fill='x')
        self.menu.pack(fill='x')
        self.conteiner.pack(fill='x')

        self.save = AgendaDAO()

        self.set_pack()

    def set_pack(self):
        for i in range(1, 13):
            self.display[i] = Button(self.menu)
            self.display[i]['text'] = self.mensal[i]
            self.display[i]['font'] = ('Arial', '20', 'bold')
            self.display[i]['fg'] = 'white'
            self.display[i]['bg'] = 'black'
            self.display[i]['command'] = partial(self.selecionar, i)
            self.display[i].pack(side=LEFT, fill='x')

            self.ano[i] = Frame(self.conteiner)

            self.nome_meses[i] = Label(self.ano[i])
            self.nome_meses[i]['font'] = 'Arial', '20', 'bold'
            self.nome_meses[i]['text'] = self.mensal[i]
            self.nome_meses[i].pack()

            for j in range(1, 5):
                self.semanas[i][j] = Frame(self.ano[i])
                self.semanas[i][j].pack(fill='both', expand='1')

            for j in range(1, len(self.dias_meses[i])):
                d = (j-1)//8 + 1
                self.dias_meses[i][j] = Button(self.semanas[i][d])
                self.dias_meses[i][j]['font'] = 'Arial', '10', 'bold'
                self.dias_meses[i][j]['fg'] = 'white'
                self.dias_meses[i][j]['bg'] = 'black'
                self.dias_meses[i][j]['height'] = '9'
                self.dias_meses[i][j]['text'] = self.save.get(j, i)
                self.dias_meses[i][j].pack(side=LEFT,
                                           fill='both',
                                           expand='1')

    def selecionar(self, mes: int):
        self.ano[self.MesAtual].pack_forget()
        self.ano[mes].pack(fill='both')
        self.MesAtual = mes

    def agenda(self, event):

        entrada = self.entrada.get()
        evento, materia, dia, hora = entrada.split()

        materia = list(materia)
        while '_' in materia:
            materia[materia.index('_')] = '\n'
        materia = ''.join(materia)

        d = int(dia[0] + dia[1])
        mes = int(dia[3] + dia[4])

        a, j = self.sel[evento.lower()]
        a = '\n' + a + evento
        a += " de " + '\n'
        a += materia + '\n'
        a += " Dia " + dia
        a += ' às ' + hora + '\n'

        for i in range(j):
            if d-i <= 0:
                mes -= 1
                d += len(self.dias_meses[mes])-1
            dia = d-i
            self.save.add(dia, mes, a)
            self.dias_meses[mes][dia]['text'] = self.save.get(dia, mes)
