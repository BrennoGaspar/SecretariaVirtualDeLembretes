# Objetivo: Um sistema que envia notificações (via email, WhatsApp ou pop-ups) com base em tarefas ou eventos agendados.

# Bibliotecas: smtplib (para emails), pywhatkit (para WhatsApp), schedule ou apscheduler

# Funcionalidades:
# Configura tarefas recorrentes ou eventos únicos.
# Integração com um calendário (ex: Google Calendar via API).
# Envia notificações personalizadas.

import schedule as sc
import time
import os
import pywhatkit as what

tarefas = []
horarios = []

##### FUNÇÕES #####
try:
    def add_task():
        os.system('cls')
        add = input('Digite a atividade que você deseja adicionar: ')
        addh = input('Digite o horário da tarefa: ')
        if add in tarefas:
            print('Você já adicionou esta tarefa à sua lista!')
        else:
            tarefas.append(add)
            horarios.append(addh)
            time.sleep(1)
            os.system('cls')
            print('Tarefa adicionada com sucesso!')

    def rem_task():
        os.system('cls')
        rem = input('Digite a atividade que você deseja remover: ')
        if rem not in tarefas:
            print('Não tem nenhuma atividade com esse nome na lista!')
        else:
            index = tarefas.index(rem)
            tarefas.pop(index)
            horarios.pop(index)
            time.sleep(1)
            os.system('cls')
            print('Tarefa removida com sucesso!')

    def view_task():
        os.system('cls')
        print('Tarefas agendadas!\n')
        for tarefa, horario in zip(tarefas,horarios):
            print(f'{tarefa} - {horario}')
        time.sleep(5)

    def edit_task():
        os.system('cls')
        print(tarefas)
        edit = input('Digite qual tarefa deseja editar: ')
        if edit in tarefas:
            new_task = input('Digite como deseja salvar tal tarefa: ')
            new_taskh = input('Digite qual horário deseja salvar para tal tarefa: ')
            time.sleep(1)
            index = tarefas.index(edit)
            tarefas[index] = new_task
            horarios[index] = new_taskh
            os.system('cls')
            print("Tarefa atualizada com sucesso!")
        else: 
            print('Você digitou errado o nome da tarefa da lista!')

##### VERIFICAÇÃO DE TAREFAS A CADA 5 SEGUNDOS #####

    def aviso():
        number = input('Digite o seu número (modelo 11950612743): ')
    
        def tasks():
            os.system('cls')
            print("Enviando mensagens para todas as tarefas...")

            for t, h in zip(tarefas, horarios):
                try:
                    # Envia mensagem instantaneamente
                    what.sendwhatmsg_instantly(f"+55{number}", f'Você tem a tarefa "{t}" às {h}', 7)
                    time.sleep(2) 
                except Exception as e:
                    print(f"Erro ao enviar mensagem para '{t}': {e}")

            print("Mensagens enviadas!")
        tasks()

##### MENU #####

    while 1:
        os.system('cls')
        print('Bem-vindo ao nosso sistema de assistente virtual!\n')
        print('Essas são nossas funções que estão disponíveis atualmente: ')
        print('1\tAdicionar tarefa\n2\tRemover tarefa\n3\tEditar tarefa\n4\tVisualizar tarefas\n5\tMandar mensagem como aviso')
        escolha = int(input('Qual opção você deseja executar? '))
        if escolha == 1:
            add_task()
        elif escolha == 2:
            rem_task()
        elif escolha == 3:
            edit_task()
        elif escolha == 4:
            view_task()
        elif escolha == 5:
            aviso()
        else: 
            print('Você digitou errado, tente novamente!')

except Exception as err:
    print(f'Algo deu errado. Erro: {err}')