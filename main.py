from rich import print
from time import sleep
import base
 
tarefas = base.ListaTarefas() 
 
while True: 
    print(''' 
    1 - Adicionar tarefa. 
    2 - Alterar o status da tarefa. 
    3 - Remover tarefa. 
    4 - Visualizar tarefas. 
    5 - Fechar. 
    ''') 
    try: 
        opcao = int(input('Digite a opção desejada: ')) 
    except ValueError: 
        print('Digite um número!') 
        continue 
    print(f'>>> Opção escolhida: {opcao} <<<') 
    if opcao == 1: 
        nome = input('Digite o nome da tarefa: ') 
        data = input('Digite a data da tarefa: ') 
        categoria = input('Digite a categoria da tarefa: ') 
        tarefas.adicionar_tarefa(nome, data, categoria) 
        print('Adicionando tarefa...') 
        sleep(1) 
        print('[bold green]Tarefa cadastrada com sucesso![/]')
    elif opcao == 2: 
        nome = input('Digite o nome da tarefa que deseja alterar: ') 
        tarefas.alterar_status(nome) 
    elif opcao == 3: 
        nome = input('Digite o nome da tarefa que deseja remover: ') 
        tarefas.remover_tarefa(nome) 
    elif opcao == 4: 
        data = input('Digite a data do vencimento das tarefas que deseja imprimir: ')
        tarefas.imprimir_tarefas(data)
    elif opcao == 5: 
        break 
    else: 
        print('[bold red]Digite uma opção válida![/]') 
print('[bold]Partiu concluir as tarefas pendentes![/]')