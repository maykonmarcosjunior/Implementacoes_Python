from DAO import DAO

class AgendaDAO(DAO):
    def __init__(self):
        super().__init__('agenda.pkl')

        self.diario = ["Dia 01\n", "Dia 02\n", "Dia 03\n",
                       "Dia 04\n", "Dia 05\n", "Dia 06\n",
                       "Dia 07\n", "Dia 08\n", "Dia 09\n",
                       "Dia 10\n", "Dia 11\n", "Dia 12\n",
                       "Dia 13\n", "Dia 14\n", "Dia 15\n",
                       "Dia 16\n", "Dia 17\n", "Dia 18\n",
                       "Dia 19\n", "Dia 20\n", "Dia 21\n",
                       "Dia 22\n", "Dia 23\n", "Dia 24\n",
                       "Dia 25\n", "Dia 26\n", "Dia 27\n",
                       "Dia 28\n", "Dia 29\n", "Dia 30\n",
                       "Dia 31\n"]

        self.dias = ["01/", "02/", "03/",
                     "04/", "05/", "06/",
                     "07/", "08/", "09/",
                     "10/", "11/", "12/",
                     "13/", "14/", "15/",
                     "16/", "17/", "18/",
                     "19/", "20/", "21/",
                     "22/", "23/", "24/",
                     "25/", "26/", "27/",
                     "28/", "29/", "30/",
                     "31/"]

        self.meses = ["01", "02", "03",
                      "04", "05", "06",
                      "07", "08", "09",
                      "10", "11", "12",]

        self.__instanciar()

    def add(self, dia: int, mes: int, tarefa: str):
        cond = isinstance(tarefa, str)
        cond = cond and isinstance(dia, int)
        cond = cond and isinstance(mes, int)

        if cond:
            tarefa = self.get(dia, mes) + tarefa
            data = self.dias[dia-1] + self.meses[mes-1]
            super().add(data, tarefa)

    def get(self, dia: int, mes: int):
        cond = isinstance(dia, int)
        cond = cond and isinstance(mes, int)
        if cond:
            data = self.dias[dia-1] + self.meses[mes-1]
            return super().get(data)
        return None

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
        return None

    def __instanciar(self):
        for mes in range(12):
            for dia in range(31):
                data = self.dias[dia-1] + self.meses[mes-1]
                if super().get(data) is None:
                    super().add(data, self.diario[dia-1])
