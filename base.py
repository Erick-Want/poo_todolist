import csv 
import datetime 
from rich import print 
from time import sleep 
 
class ListaTarefas (): 
    def __init__(self): 
        self.lista_tarefas = [] 
        with open('File.csv', 'a') as arquivo: 
            csv.writer(arquivo, delimiter=',', lineterminator='\n') 
 
    def adicionar_tarefa (self, nome_tarefa, data_vencimento, categoria = 'Nenhuma'): 
        tarefa = [nome_tarefa, self.converter_data(data_vencimento), categoria, 'Pendente'] 
         
        with open('File.csv', 'a') as arquivo: 
            escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n') 
            escritor.writerow(tarefa) 
 
    def remover_tarefa (self, nome_tarefa): 
        self.ler_csv() 
        if len(self.lista_tarefas) == 0: 
            print('[bold red]Sem tarefas para alterar, adicione alguma![/]') 
        else: 
            for tarefa in self.lista_tarefas: 
                if tarefa[0] == nome_tarefa: 
                    print(f'''[white] 
                    Tarefa a ser removida: 
                    Nome: {tarefa[0]} 
                    Data de vencimento: {tarefa[1]} 
                    Categoria: {tarefa[2]} 
                    Status: {tarefa[3]} 
 
                    Removendo...[/] 
                    ''') 
                    sleep(2) 
                    self.lista_tarefas.remove(tarefa) 
                    print('[bold green] Removido com sucesso![/]') 
        self.atualizar_csv() 
 
    def alterar_status (self, nome_tarefa): 
        self.ler_csv() 
        if len(self.lista_tarefas) == 0: 
            print('[bold red]Sem tarefas para alterar, adicione alguma![/]') 
        else: 
            for index, tarefa in enumerate(self.lista_tarefas): 
                if tarefa[0] == nome_tarefa: 
                    if tarefa[3] ==  'Pendente': 
                        self.lista_tarefas[index][3] = 'Concluido' 
                    else: 
                        self.lista_tarefas[index][3] = 'Pendente' 
        self.atualizar_csv() 
     
    def imprimir_tarefas (self, data_vencimento): 
        self.ler_csv() 
        if len(self.lista_tarefas) == 0: 
            print('[bold red]Sem tarefas para alterar, adicione alguma![/]') 
        else: 
            encontradas = [] 
 
            data = self.converter_data(data_vencimento) 
            for tarefa in self.lista_tarefas: 
                if tarefa[1] == str(data): 
                    encontradas.append(tarefa) 
            if len(encontradas) > 0: 
                for index, tarefa in enumerate(encontradas): 
                    print(f'''[white] 
                    Tarefa {index + 1} encontrada: 
                        Nome: {tarefa[0]} 
                        Data de vencimento: {tarefa[1]} 
                        Categoria: {tarefa[2]} 
                        Status: {tarefa[3]} 
                    [/]''') 
            else: 
                print(f'[bold red]Não foi encontrada nenhuma tarefa na data: {data}[/]') 
 
    def atualizar_csv (self): 
        with open('File.csv', 'w') as arquivo: 
            escritor = csv.writer(arquivo, delimiter=',', lineterminator='\n') 
            escritor.writerows(self.lista_tarefas) 
 
    def ler_csv (self): 
        with open('File.csv') as arquivo: 
            self.lista_tarefas = list(csv.reader(arquivo, delimiter=',', lineterminator='\n')) 
 
    @staticmethod 
    def converter_data (data_entrada): 
        if data_entrada == '': 
            data_entrada = datetime.date.today() 
            return data_entrada 
        dia, mes, ano = map(int, data_entrada.split('/')) 
        data_entrada = datetime.datetime(ano, mes, dia) 
