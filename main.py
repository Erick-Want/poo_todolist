from rich import print 
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
        pass
    elif opcao == 2: 
        pass
    elif opcao == 3: 
        pass
    elif opcao == 4: 
        pass
    elif opcao == 5: 
        break 
    else: 
        print('[bold red]Digite uma opção válida![/]') 
print('[bold]Partiu concluir as tarefas pendentes![/]')