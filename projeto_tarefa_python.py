import os
from datetime import datetime
from pathlib import Path

ROOT_PATH = Path(__file__).parent #pegar o caminho da pasta que o arq. txt será armazenado
TAMANHO_CADA_TAREFA = 5
indice_tarefas = [] #indice onde inicia a tarefa

# Função para limpar a tela
def limpar_tela():
    if os.name == 'nt':
        _ = os.system('cls')  # Limpa a tela no Windows
    else:
        _ = os.system('clear')  # Limpa a tela em Unix/macOS


#verifica se as funções editar,exibir,excluir e completar podem ser executadas
def lista_vazia():
    try:
        with open(ROOT_PATH / "tarefas.txt", "r", encoding="utf-8") as arquivo:
            # Verifica se o arquivo está vazio lendo todo o conteúdo e removendo espaços em branco
            if arquivo.read().strip() != "":
                return False
    except Exception:
        return True
        

def apresentar_tarefas():
    numero_tarefa = 1
    contador = 0
    indice_tarefas.clear()  # Limpa a lista de índices antes de adicionar os novos
    try:
        with open(ROOT_PATH / "tarefas.txt", "r", encoding="utf-8") as arquivo:
            while len(linha := arquivo.readline()):  # Lê uma linha do arquivo
                linha = linha.strip()  # Remove espaços em branco no início e no fim da linha
                if linha and ((contador%5) == 0):  # Se linha não está em branco e é inicio de uma tarefa
                    indice_tarefas.append(contador) # Guarda em uma lista
                    print(f"{numero_tarefa} - {linha}")
                    numero_tarefa+=1
                contador += 1
    except IOError as exc:
         print(f"Erro ao abrir o arquivo: {exc}")
    except Exception as exc:
        print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")


# Função para criar uma tarefa e adicioná-la à lista de tarefas
def criar_tarefas(titulo, descricao="", data_maxima_tarefa=""):
    if descricao == "":
        descricao = "Não informado"
    if data_maxima_tarefa == "":
        data_maxima_tarefa = "Não informado"
    try:
        with open(ROOT_PATH / "tarefas.txt", "a", encoding="utf-8") as arquivo: 
            #gravar a tarefa no arquivo selecionado
            tarefa = ""
            tarefa +=f"Título: {titulo}\n"
            tarefa +=f"Descrição: {descricao}\n"
            tarefa +=f"Data Publicação:{datetime.now().strftime("%d/%m/%Y")}\n"
            tarefa +=f"Data máxima: {data_maxima_tarefa}\n"
            tarefa +=f"Completa: {"Pendente"}\n"
            arquivo.write(tarefa) #escrever no fim do arquivo
            print("Tarefa inserida na lista! ") #Apresentar no console apos as operações
    except IOError as exc:
         print(f"Erro ao abrir o arquivo: {exc}")
    except Exception as exc:
        print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")
        
    
# Função para exibir todas as tarefas
def exibir_tarefas(): 
    contador = 0 
    try:
        with open(ROOT_PATH / "tarefas.txt", "r", encoding="utf-8") as arquivo:
            while len(linha := arquivo.readline()):  # Lê uma linha do arquivo
                linha = linha.strip()  # Remove espaços em branco no início e no fim da linha
                if linha:  # Verifica se a linha não está em branco
                    print(linha)
                    contador += 1  
                if (contador%5) == 0: #Multiplo de 5, corresponde a uma nova tarefa no arquivo
                    print("-" * 80) 
    except IOError as exc:
         print(f"Erro ao abrir o arquivo: {exc}")
    except Exception as exc:
        print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")
    
            
def editar_tarefas(titulo="", descricao="", data_maxima_tarefa=""):
    apresentar_tarefas()
    numero_tarefa = int(input("Digite a tarefa que será atualizada:"))
    indice = (numero_tarefa - 1) * TAMANHO_CADA_TAREFA  # Calcula o índice correto
    try:   
        with open(ROOT_PATH / "tarefas.txt", 'r', encoding="utf-8") as arquivo:
            linhas = arquivo.readlines() # Ler o arquivo referenciado(todo)
            if titulo != "":
                linhas[indice] = f"Título: {titulo}\n"
            if descricao != "":
                linhas[indice + 1] = f"Descrição: {descricao}\n"
            if data_maxima_tarefa != "":
                linhas[indice + 3] = f"Data máxima: {data_maxima_tarefa}\n"
                
        with open(ROOT_PATH / "tarefas.txt", 'w', encoding= "utf-8") as arquivo:
            arquivo.writelines(linhas)
        print("Tarefa editada com sucesso!")
    except IOError as exc:
         print(f"Erro ao abrir ou escrever no arquivo: {exc}")
    except Exception as exc:
        print(f"Algum problema ocorreu ao tentar editar a tarefa: {exc}")

                         
def concluir_tarefa():
    apresentar_tarefas()
    numero_tarefa = int(input("Digite a tarefa que será finalizada:"))
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines() #ler o arquivo referenciado
            indice = (numero_tarefa - 1) * TAMANHO_CADA_TAREFA + 4 #indice do status da tarefa
            if linhas[indice] == "Completa":
                print("Está tarefa já está marcada como concluída.")
            else:
                linhas[indice] = f"Status: Completa\n"
            with open('tarefas.txt', 'w', encoding= "utf-8") as arquivo:
                arquivo.writelines(linhas)       
    except IOError as exc:
         print(f"Erro ao abrir o arquivo: {exc}")
    except Exception as exc:
        print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")
    

def excluir_tarefa():    
    apresentar_tarefas()
    numero_tarefa = int(input("Digite a tarefa que será excluída:"))
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            #pega os indices correspondentes a tarefa
            indice_inicial = (numero_tarefa - 1) * TAMANHO_CADA_TAREFA
            indice_final = indice_inicial + 5
            del linhas[indice_inicial:indice_final] #deletar este intervalo do arquivo
        with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
            linhas = arquivo.writelines(linhas)
            print("Tarefa excluída com sucesso")
    except IOError as exc:
         print(f"Erro ao abrir ou escrever no arquivo: {exc}")
    except Exception as exc:
        print(f"Algum problema ocorreu ao tentar excluir a tarefa: {exc}")
    
def  menu():
    while(True):
        mensagem = ''' 
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
        if opcao == 1:
            print("ATENÇÃO: Caso optar por não colocar descrição ou data, pressione ENTER")
            while(1):
                titulo = input("Digite um título para a tarefa:").title()
                if titulo != "":
                    break
            descricao = input("Digite uma descrição para a tarefa(opcional):").title()
            data = input("Digite uma data para você finalizar a tarefa[dia/mês/ano] (opcional):")
            
            criar_tarefas(titulo,descricao,data)

        elif opcao == 2:
            vazio = lista_vazia()
            if not vazio:
                exibir_tarefas()
            else:
                print("Não há tarefas armazenadas!")

        elif opcao == 3:
            vazio = lista_vazia()
            if not vazio:
                print("ATENÇÃO: Caso optar por não mudar algum campo, pressione ENTER")
                titulo = input("Digite um título para a tarefa(opcional):").title()
                descricao = input("Digite uma descrição para a tarefa(opcional):").title()
                data = input("Digite uma data para você finalizar a tarefa(opcional):").title()
                if titulo == "" and descricao == "" and data == "": #se não tiver nenhuma mudança na tarefa
                    print(f"Você precisa editar algo para atualizar a tarefa")                    
                else:
                    editar_tarefas(titulo,descricao,data)
            else:
                print("Não há tarefas na lista!")

        elif opcao == 4:
            valido = lista_vazia()
            if not vazio:
                concluir_tarefa()
            else:
                print("Não há tarefas na lista!")

        elif opcao == 5:
            vazio = lista_vazia()
            if not vazio:
                excluir_tarefa()
            else:
                print("Não há tarefas na lista!")

        else:
            break
        input("PRESSIONE ENTER PARA CONTINUAR...")
        limpar_tela()
        #for i in range(0,100):
            #print("")

#"main()"                
menu()
       

    