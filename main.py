from rich import print 
from time import sleep 
import os 
import base 
import inquirer 
 
tarefas = base.ListaTarefas() 
 
questions = [ 
    inquirer.List( 
        'opcao', 
        message='Selecione a opção desejada', 
        choices=[ 
            'Adicionar tarefa', 
            'Alterar o status da tarefa', 
            'Remover tarefa', 
            'Visualizar tarefas', 
            'Limpar o console', 
            'Fechar'] 
    ) 
] 
 
opcoes = [ 
    'Adicionar tarefa', 
    'Alterar o status da tarefa', 
    'Remover tarefa', 
    'Visualizar tarefas', 
    'Limpar o console', 
    'Fechar' 
] 
 
def valida_data(): 
    while True: 
        data = input('Digite a data da tarefa [DD/MM/AAAA]: ') 
        if data == '': 
            break 
        try: 
            dia, mes, ano = map(int, data.split('/')) 
            if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and  ano >= 2021 and ano <= 2100: 
                break 
            else: 
               print('[red]Digite uma data no formato[/] [green][DIA/MÊS/ANO][/]') 
        except: 
            print('[red]Digite uma data no formato[/] [green][DIA/MÊS/ANO][/]') 
    return data 
 
while True: 
    resposta = inquirer.prompt(questions) 
    if resposta['opcao'] == opcoes[0]: 
        nome = input('Digite o nome da tarefa: ') 
        data = valida_data() 
        categoria = input('Digite a categoria da tarefa: ') 
        tarefas.adicionar_tarefa(nome, data, categoria) 
        print('Adicionando tarefa...') 
        sleep(1) 
        print('[bold green]Tarefa cadastrada com sucesso![/]') 
    elif resposta['opcao'] == opcoes[1]: 
        nome = input('Digite o nome da tarefa que deseja alterar: ') 
        tarefas.alterar_status(nome) 
    elif resposta['opcao'] == opcoes[2]: 
        nome = input('Digite o nome da tarefa que deseja remover: ') 
        tarefas.remover_tarefa(nome) 
    elif resposta['opcao'] == opcoes[3]: 
        data = input('Digite a data do vencimento das tarefas que deseja imprimir: ') 
        tarefas.imprimir_tarefas(data) 
    elif resposta['opcao'] == opcoes[4]: 
        os.system('clear') 
    else: 
        print('[white]Finalizando...[/]') 
        sleep(2) 
        break 
print('[bold]Partiu concluir as tarefas pendentes![/]')