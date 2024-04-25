import os

# Inicialização da lista de tarefas vazia
tarefas = []

#cores do print
VERMELHO = "\033[31m" 
COR_PADRAO = "\033[0m" 
VERDE = "\033[32m"

# Função para limpar a tela
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')  # Limpa a tela no Windows
    else:
        os.system('clear')  # Limpa a tela em Unix/macOS

#verifica se as funções editar,exibir,excluir e completar podem ser executadas
def lista_vazia():
    if not tarefas:
        return False
    else: 
        return True


# Função para criar uma tarefa e adicioná-la à lista de tarefas
def criar_tarefas(titulo, descricao="", data_maxima_tarefa=""):
    if descricao == "":
        descricao = "Não informado"
    if data_maxima_tarefa == "":
        data_maxima_tarefa = "Não informado"

    tarefas.append({ #adicionar o dicionário, relacionado a tarefa, na lista.
        "titulo": titulo.title(),
        "descricao": descricao.title(),
        "data_max_tarefa": data_maxima_tarefa.title(),
        "completa": False,
    })
    print("Tarefa inserida na lista!")

# Função para exibir todas as tarefas
def exibir_tarefas():
    if tarefas:  
        entrada_tarefas = "" #variavel que será retornado, com as informações da lista
        # Se a lista não estiver vazia, exibe as tarefas
        for indice, tarefa in enumerate(tarefas):
            entrada_tarefas += f"{VERMELHO}\t\t{indice + 1}° tarefa:{COR_PADRAO}\n"
            entrada_tarefas += f"Título:{tarefa['titulo']}\n"
            entrada_tarefas += f"Descrição:{tarefa['descricao']}\n"
            entrada_tarefas += f"Conclusão:{tarefa['data_max_tarefa']}\n"
            entrada_tarefas += f"Status:{'Completo' if tarefa['completa'] else 'Pendente'}\n\n"
        return entrada_tarefas
            
def editar_tarefas(titulo="", descricao="", data_maxima_tarefa=""):
    print("---------------------------------------------------------")     
    print(f"{VERMELHO}\t\tQUAL DAS TAREFAS VOCÊ DESEJA EDITAR:{COR_PADRAO}")
    for indice,tarefa in enumerate(tarefas):
        print(f"{indice + 1}. {tarefa['titulo']}\n") # talvez apague depois
    print("---------------------------------------------------------")      
    op=int(input("-Digite o número da tarefa à ser editada:")) #transforma input em inteiro
    if op < 1 or op > len(tarefas):
        return print("Está tarefa não existe.")  
    else:
        tarefa = tarefas[op - 1]
        if titulo != "":
            tarefa["titulo"] = titulo
        if descricao != "":
            tarefa["descricao"] = descricao
        if data_maxima_tarefa != "":
            tarefa["data_max_tarefa"] = data_maxima_tarefa
        return print(f"Tarefa {op} atualizada com sucesso!")
        
         
def concluir_tarefa(indice):
    if indice < 0 or indice > len(tarefas):
        print("Está tarefa não existe.")
        return
    else:
        tarefa = tarefas[indice - 1]
        tarefa["completa"] = True
        return print(f"Tarefa {indice} finalizada com sucesso!")
        

def excluir_tarefa(indice):
    if not tarefas:  # Verifica se a lista de tarefas está vazia
        print("Não há tarefas para exibir.")
        return
        
    if indice < 0 or indice > len(tarefas):
        print("Está tarefa não existe.")
        return
    else:
        tarefas.pop(indice - 1)
        return f"Tarefa {indice} foi excluída."
    
def  menu():
    while(True):
        mensagem = f''' 
        ----------------------------------------
                GERENCIADOR DE TAREFAS
             1- Criar tarefas
             2- Exibir tarefas
             3- Editar tarefas
             4- Concluir tarefas
             5- Excluir tarefas
             6- Sair do programa
        ----------------------------------------'''
        print(mensagem)
        opcao = int(input("Digite uma opção:"))
        limpar_tela()
        if opcao == 1:
            print(f"{VERMELHO}ATENÇÃO: Caso optar por não colocar descrição ou data, pressione ENTER{COR_PADRAO}")
            while(1):
                titulo = input("Digite um título para a tarefa:")
                if titulo != "":
                    break
            descricao = input("Digite uma descrição para a tarefa(opcional):")
            data = input("Digite uma data para você finalizar a tarefa(opcional):")
            criar_tarefas(titulo,descricao,data)

        elif opcao == 2:
            valido = lista_vazia()
            if valido:
                exibicao = exibir_tarefas()
                if exibicao:
                    print(exibicao)
            else:
                print("Não há tarefas na lista!")

        elif opcao == 3:
            valido = lista_vazia()
            if valido:
                print(f"{VERMELHO}ATENÇÃO: Caso optar por não mudar algum campo, pressione ENTER{COR_PADRAO}")
                titulo = input("Digite um título para a tarefa(opcional):")
                descricao = input("Digite uma descrição para a tarefa(opcional):")
                data = input("Digite uma data para você finalizar a tarefa(opcional):")
                if titulo == "" and descricao == "" and data == "":
                    print(f"Você precisa editar algo para atualizar a tarefa")                    
                else:
                    exibicao = editar_tarefas(titulo.title(),descricao.title(),data.title())
                    if exibicao: #se existe algum valor retornado
                        print(exibicao)
            else:
                print("Não há tarefas na lista!")

        elif opcao == 4:
            valido = lista_vazia()
            if valido:
                for indice,tarefa in enumerate(tarefas):
                    print(f"{indice + 1}° tarefa: {tarefa['titulo']}")
                opcao = int(input("Digite o número da tarefa para concluir:"))
                exibicao = concluir_tarefa(opcao)
                if exibicao: 
                    print(exibicao)
            else:
                print("Não há tarefas na lista!")

        elif opcao == 5:
            valido = lista_vazia()
            if valido:
                for indice,tarefa in enumerate(tarefas):
                    print(f"{indice + 1}° tarefa: {tarefa['titulo']}")
                    opcao = int(input("Digite o número da tarefa para excluir:"))
                    exibicao = excluir_tarefa(opcao)
                    if exibicao:
                        print(exibicao)
            else:
                print("Não há tarefas na lista!")

        else:
            break
        input(f"{VERDE}PRESSIONE ENTER PARA CONTINUAR...{COR_PADRAO}")
        limpar_tela()

#"main()"                
menu()
       

    