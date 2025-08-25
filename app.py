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
    


contatos = []
while True:
    print("\ncadastro e visualizalçao de contatos")
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
    
    elif escolha == "7":
        break
        
print("programa finalizado")