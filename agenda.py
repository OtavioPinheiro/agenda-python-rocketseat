import re

contatos = []
favoritos = []

def exibir_menu() -> None:
    """
    Função responsável por exibir o menu de opções
    """

    opcoes = {
        "1": "Adicionar contato",
        "2": "Exibir lista de contatos",
        "3": "Editar um contato",
        "4": "Adicionar aos favoritos",
        "5": "Remover dos favoritos",
        "6": "Ver favoritos",
        "7": "Apagar um contato",
        "0": "Sair"
    }
    menu = "******** AGENDA ********\n"
    for key in opcoes.keys():
        menu += f"{key} - {opcoes.get(key)}\n"

    print(menu)
    opcao = input("Informe uma opção do menu: ")

    match opcao:
        case "1":
            adicionar_contato()
            exibir_menu()
        case "2":
            exibir_contatos()
            exibir_menu()
        case "3":
            editar_contato()
            exibir_menu()
        case "4":
            adicionar_favoritos()
            exibir_menu()
        case "5":
            remover_favoritos()
            exibir_menu()
        case "6":
            ver_favoritos()
            exibir_menu()
        case "7":
            apagar_contato()
            exibir_menu()
        case "0":
            print("Encerrando...")
            exit(0)
        case _:
            print(f"Opção {opcao} inválida")
            exibir_menu()     


def __validar_nome(nome: str) -> bool:
    """
    Função que valida se o nome informado é válido.

    Argumentos:
        nome: String contendo o nome a ser validado.

    Retorno:
        True se o nome for válido, False caso contrário.
    """

    # Expressão regular que define o padrão de um nome válido
    regex = r'^[a-zA-Zà-úÀ-ÚçÇãÃõÕÓêÊíÍôÔúÚ ]{3,50}$'

    # Valida o nome usando a expressão regular
    return bool(re.match(regex, nome))


def __validar_telefone(telefone: str) -> bool:
    """
    Função que valida se o telefone informado é válido.

    Argumentos:
        telefone: String contendo o telefone a ser validado.

    Retorno:
        True se o telefone for válido, False caso contrário.
    """

    # Padrão regex para validar números de telefone
    padrao = r'^\(\d{2}\) \d{4,5}-\d{4}$|^\(\d{2}\)\d{4,5}-\d{4}$|^\(\d{2}\)\d{8,9}$|^\d{2} \d{4,5} \d{4}$|^\d{6,7} \d{4}$|^\d{2} \d{4,5}-\d{4}$|^\d{6,7}-\d{4}$|^\d{8,11}$'
    
    # Verifica se o número de telefone corresponde ao padrão regex
    return bool(re.match(padrao, telefone))


def __formatar_telefone(telefone: str) -> str|None:
    """
    Função que formata o número de telefone.

    Argumentos:
        telefone: String contendo o telefone a ser formatado.

    Retorno:
        Telefone formatado.
    """
    
    # Remove todos os caracteres que não são dígitos
    telefone = ''.join(filter(str.isdigit, telefone))

    if len(telefone) == 0:
        return None

    # Se o número de dígitos for 8, adiciona o DDD 19 por padrão
    if len(telefone) >= 8 and len(telefone) < 10:
        telefone = '19' + telefone

    if len(telefone) == 10:
        # Insere a máscara (XX) XXXX-XXXX
        telefone_formatado = '({}) {}-{}'.format(telefone[:2], telefone[2:6], telefone[6:])
    
    if len(telefone) == 11:
        # Insere a máscara (XX) XXXXX-XXXX
        telefone_formatado = '({}) {}-{}'.format(telefone[:2], telefone[2:7], telefone[7:])

    return telefone_formatado


def __validar_email(email: str) -> bool:
    """
    Função que valida o email.

    Argumentos:
        email: String contendo o email a ser validado.

    Retorno:
        True se o email for válido, False caso contrário.
    """
    # Padrão regex para validar números de telefone
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Verifica se o número de telefone corresponde ao padrão regex
    return bool(re.match(padrao, email))


def adicionar_contato() -> None:
    """
    Função responsável por adicionar um contato à lista de contatos
    """

    print("1 - Adicionar contato\n")
    
    nome = input("Informe o nome do contato: ")
    while not __validar_nome(nome):
        print("Nome inválido")
        nome = input("Informe o nome do contato: ")

    adicionar_mais = True
    telefones = []
    while adicionar_mais:
        telefone = input("Informe o telefone do contato: ")
        while not __validar_telefone(telefone):
            print("Telefone inválido")
            telefone = input("Informe o telefone do contato: ")
        telefone = __formatar_telefone(telefone)
        telefones.append(telefone)
        
        mais_telefone = input("Quer adicionar outro telefone?(s/n) ")
        if mais_telefone.strip() == "n":
            adicionar_mais = False

    adicionar_mais = True
    emails = []
    while adicionar_mais:
        email = input("Informe o email do contato: ")
        while not __validar_email(email):
            print("Email inválido")
            email = input("Informe o email do contato: ")
        emails.append(email)

        mais_email = input("Quer adicionar outro email?(s/n) ")
        if mais_email.strip() == "n":
            adicionar_mais = False

    favorito = input("Favoritar o contato?(s/n) ")
    while favorito.strip() != "s" and favorito.strip() != "n":
        print("O valor informado é inválido")
        favorito = input("Favoritar o contato?(s/n) ")

    contato = {
        "nome": nome,
        "telefones": telefones,
        "emails": emails,
        "favorito": favorito
    }

    if favorito == "s":
        favoritos.append(contato)

    contatos.append(contato)

    print("\nContato adicionado com sucesso!\n")


def exibir_contatos() -> None:
    """
    Função responsável por exibir a lista de contatos
    """

    print("2 - Exibir lista de contatos\n")

    if len(contatos) == 0:
        print("Lista de contatos vazia!")
    else:
        lista_de_contatos = ""

        for index, contato in enumerate(contatos):
            if contato["favorito"] == "s":
                lista_de_contatos += f"{index+1}-\n ⭐ Nome: {contato["nome"]}\n    Telefone(s): {", ".join(contato["telefones"])}\n    Email(s): {", ".join(contato["emails"])}\n"
            else:
                lista_de_contatos += f"{index+1}-\n    Nome: {contato["nome"]}\n    Telefone(s): {", ".join(contato["telefones"])}\n    Email(s): {", ".join(contato["emails"])}\n"
        print(lista_de_contatos)


def __exibir_um_contato(contato: dict) -> None:
    
    if contato["favorito"] == "s":
        lista_de_contatos = f" ⭐ Nome: {contato["nome"]}\n    Telefone(s): {", ".join(contato["telefones"])}\n    Email(s): {", ".join(contato["emails"])}\n"
    else:
        lista_de_contatos = f"    Nome: {contato["nome"]}\n    Telefone(s): {", ".join(contato["telefones"])}\n    Email(s): {", ".join(contato["emails"])}\n"
    
    print(lista_de_contatos)


def __editar_nome(contato: dict) -> None:
    contato["nome"] = input("Informe o nome do contato: ")
    while not __validar_nome(contato["nome"]):
        print("Nome inválido")
        nome = input("Informe o nome do contato: ")


def __editar_telefone(contato: dict) -> None:
    adicionar_mais = True
    contato["telefones"] = []
    while adicionar_mais:
        telefone = input("Informe o telefone do contato: ")
        while not __validar_telefone(telefone):
            print("Telefone inválido")
            telefone = input("Informe o telefone do contato: ")
        telefone = __formatar_telefone(telefone)
        contato["telefones"].append(telefone)
        
        mais_telefone = input("\nQuer adicionar outro telefone?(s/n) ")
        if mais_telefone.strip() == "n":
            adicionar_mais = False


def __editar_email(contato: dict) -> None:
    adicionar_mais = True
    contato["emails"] = []
    while adicionar_mais:
        email = input("Informe o email do contato: ")
        while not __validar_email(email):
            print("Email inválido")
            email = input("Informe o email do contato: ")
        contato["emails"].append(email)

        mais_email = input("Quer adicionar outro email?(s/n) ")
        if mais_email.strip() == "n":
            adicionar_mais = False


def __editar_favorito(contato: dict) -> None:
    contato["favorito"] = input("Favoritar o contato?(s/n) ")
    while contato["favorito"].strip() != "s" and contato["favorito"].strip() != "n":
        print("O valor informado é inválido")
        contato["favorito"] = input("Favoritar o contato?(s/n) ")

    if contato["favorito"] == "s":
        if contato not in favoritos:
            favoritos.append(contato)
    else:
        if contato in favoritos:
            favoritos.remove(contato)


def __editar_infos_contato(contato: dict) -> None:
    
    __editar_nome(contato)

    __editar_telefone(contato)

    __editar_email(contato)

    __editar_favorito(contato)

    print("\nContato editado com sucesso!\n")
    exibir_menu()


def __localizar_contato() -> dict|None:
    localizar = input("Informe o nome, telefone ou o email do contato: ")
        
    if __validar_nome(localizar) or __validar_telefone(__formatar_telefone(localizar)) or __validar_email(localizar):
        for index, contato in enumerate(contatos):
            if contato["nome"] == localizar or contato["telefones"] == __formatar_telefone(localizar) or contato["emails"] == localizar:
                print("Contato localizado:")
                __exibir_um_contato(contato)
                return contato
            elif index == len(contatos):
                print("Contato não localizado!\nVerifique a digitação e tente novamente.\n")
                return None
    else:
        print("Valor informado é inválido!\n")
        return None


def editar_contato() -> None:
    """
    Função responsável por editar um contato
    """

    print("3 - Editar um contato\n")

    if len(contatos) == 0:
        print("Lista de contatos vazia!\n")
    else:   
        localizar = input("Informe o nome, telefone ou o email do contato que deseja editar: ")
        
        if __validar_nome(localizar) or __validar_telefone(__formatar_telefone(localizar)) or __validar_email(localizar):
            for index, contato in enumerate(contatos):
                if contato["nome"] == localizar or contato["telefones"] == __formatar_telefone(localizar) or contato["emails"] == localizar:
                    print("Contato que será editado:")
                    __exibir_um_contato(contato)
                    
                    opcao_invalida = True
                    while opcao_invalida:
                        editar = input("O que deseja editar?(tudo/nome/telefone/email) ")
                        if editar == "tudo":
                            __editar_infos_contato(contato)
                            opcao_invalida = False
                        elif editar == "nome":
                            __editar_nome(contato)
                        elif editar == "telefone":
                            __editar_telefone(contato)
                        elif editar == "email":
                            __editar_email(contato)
                        else:
                            print("Opção inválida")
                elif index == len(contatos):
                    print("Contato não localizado!\nVerifique a digitação e tente novamente.\n")
        else:
            print("Valor informado é inválido!\n")
                    
                    
def adicionar_favoritos() -> None:
    """
    Esta função tem como objetivo adicionar um contato aos favoritos
    """
    print("4 - Adicionar aos favoritos\n")
    print("Qual contato deseja adicionar aos favoritos?")
    contato = __localizar_contato()
    if contato is not None:
        if contato["favorito"] == "s":
            if contato not in favoritos:
                favoritos.append(contato)
            print("Contato adicionado a lista de favoritos!\n")
        else:
            contato["favorito"] = "s"
            favoritos.append(contato)
            print("Contato adicionado a lista de favoritos!\n")
    else:
        print("Contato não localizado.\n")


def remover_favoritos() -> None:
    """
    Esta função tem como objetivo remover um contato dos favoritos
    """
    print("5 - Remover dos favoritos\n")
    print("Qual contato deseja remover dos favoritos?")
    contato = __localizar_contato()
    if contato is not None:
        if contato["favorito"] == "s":
            contato["favorito"] = "n"
            favoritos.remove(contato)
            print("Contato removido da lista de favoritos!\n")
        else:
            if contato in favoritos:
                favoritos.remove(contato)
            print("Contato removido da lista de favoritos!\n")
    else:
        print("Contato não localizado.\n")


def ver_favoritos() -> None:
    """
    Função tem o objetivo de exibir a lista de favoritos
    """

    print("6 - Ver favoritos\n")

    if len(favoritos) == 0:
        print("Lista de favoritos vazia!")
    else:
        lista_de_favoritos = ""

        for index, favorito in enumerate(favoritos):
            lista_de_favoritos += f"{index+1}-\n ⭐ Nome: {favorito["nome"]}\n    Telefone(s): {", ".join(favorito["telefones"])}\n    Email(s): {", ".join(favorito["emails"])}\n"

        print(lista_de_favoritos)


def apagar_contato() -> None:
    """
    Função tem o objetivo de apagar um contato
    """

    print("7 - Apagar um contato\n")
    print("Qual contato deseja apagar?")
    contato = __localizar_contato()
    if contato:
        contatos.remove(contato)
        if contato in favoritos:
            favoritos.remove(contato)
        print(f"Contato {contato["nome"]} removido!\n")
    else:
        print("Contato não localizado!\n")


exibir_menu()
