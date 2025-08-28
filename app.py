# funções
def adicionar_contato(lista_de_contatos):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    
    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    
    lista_de_contatos.append(novo_contato)
    
    print(f"O contato {nome} foi adicionado com sucesso.")
    pass

def visualizar_contato(lista_de_contatos):
    print("\n Lista de contatos")
    
    if not lista_de_contatos:
        print("Sua lista de contatos está vazia.")
        return
    for indice, contato in enumerate(lista_de_contatos):
        status_favorito = "★" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        
        print(f"{indice + 1}. [{status_favorito}] Nome: {nome_contato} - Tel: {telefone_contato} - Email: {email_contato}")
print("---------------------")

def editar_contato(lista_de_contatos):
    visualizar_contato(lista_de_contatos)
    if not lista_de_contatos:
        return
    try:
        escolha = input("\nDigite o número do contato que deseja editar: ")
        escolha_int = int(escolha)
        
        if 1 <= escolha_int <= len(lista_de_contatos):
            indice_contato = escolha_int - 1
            
            contato_a_editar = lista_de_contatos[indice_contato]
            
            print(f"\nEditando contato: {contato_a_editar['nome']}")
            
            novo_nome = input(f"novo nome (atual: {contato_a_editar['nome']}): ")
            novo_telefone = input(f"novo telefone (atual: {contato_a_editar['telefone']}): ")
            novo_email = input(f"novo email (atual: {contato_a_editar['email']}): ")            
            
            contato_a_editar['nome'] =  novo_nome
            contato_a_editar['telefone'] = novo_telefone
            contato_a_editar['email'] = novo_email
            
            print("\n✅ Contato atualizado com sucesso!")
            
        else:
            print("❌ Erro: Número inválido. Escolha um contato da lista.")
            
    except ValueError:
        print("❌ Erro: Por favor, digite apenas o número do contato.")
        
def favoritar_contato(lista_de_contatos):
    visualizar_contato(lista_de_contatos)
    if not lista_de_contatos:
        return
    try:
        escolha = input("\nDigite o contato que deseja favoritar: ")
        escolha_int = int(escolha)
        
        if 1 <= escolha_int <= len (lista_de_contatos):
            indice_contato = escolha_int - 1
            
            favoritar_contato = lista_de_contatos[indice_contato]
            
            favoritar_contato['favorito'] = not favoritar_contato['favorito']
            
            nome_contato = favoritar_contato['nome']
            if favoritar_contato['favorito']:
                print(f"\n✅ Contato '{nome_contato}' marcado como favorito ★.")
            else:
                print(f"\n🗑️ Contato '{nome_contato}' desmarcado como favorito.")
        
        else:
            print("❌ Erro: Número inválido. Escolha um contato da lista.")
            
    except ValueError:
        print("❌ Erro: Por favor, digite apenas o número do contato.")
        
def visualizar_contato_favorito(lista_de_contatos):
    print("\n Lista de contatos favoritos")
    
    favoritos_encontrados = []
    
    for contato in lista_de_contatos:
        
        if contato["favorito"]:
            favoritos_encontrados.append(contato)
     
    if not favoritos_encontrados:
        print("Você ainda não marcou nenhum contato como favorito.")
        return
    
        
    for indice, contato in enumerate (favoritos_encontrados):
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            
            print(f"{indice + 1}. [★] Nome: {nome_contato} - Tel: {telefone_contato} - Email: {email_contato}")
print("---------------------")
    
def deletar_contato(lista_de_contatos):
    visualizar_contato(lista_de_contatos)
    if not lista_de_contatos:
        return
    
    try:
        escolha = input("\nDigite o número do contato que deseja deletar: ")
        escolha_int = int(escolha)
        
        if 1 <= escolha_int <= len (lista_de_contatos):
            indice_contato = escolha_int - 1
            
            nome_removido = lista_de_contatos[indice_contato]['nome']
            
            lista_de_contatos.pop(indice_contato)
            print(f"\n✅ Contato '{nome_removido}' foi deletado com sucesso!")
            
        else:
            print("❌ Erro: Número inválido. Escolha um contato da lista.")

    except ValueError:
        print("❌ Erro: Por favor, digite apenas o número do contato.")
    
contatos = []
while True:
    print("\ncadastro e visualização de contatos")
    print("1 - Adicionar contato novo")
    print("2 - Visualizar toda a lista de contatos")
    print("3 - Editar contato existente")
    print("4 - Marcar ou desmarcar contato favorito")
    print("5 - Visualizar lista de contatos favoritos")
    print("6 - Deletar contato existente")
    print('7 - Sair')
    
    escolha = input("Digite a sua escolha: ")

# escolhas

    if escolha == "1":
        adicionar_contato(contatos)
        
    elif escolha == "2":
        visualizar_contato(contatos)
    
    elif escolha == "3":
        editar_contato(contatos)
        
    elif escolha == "4":
        favoritar_contato(contatos)
        
    elif escolha == "5":
        visualizar_contato_favorito(contatos)
        
    elif escolha == "6":
        deletar_contato(contatos)
        
    elif escolha == "7":
        break
        
print("programa finalizado")