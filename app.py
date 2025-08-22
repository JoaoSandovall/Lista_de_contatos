def adicionar_contato(nome, telefone, email):
    contatos_exemplo = {
        "nome": "joao",
        "telefone": "6191895543",
        "e-mail": "joao@emailcom",
        "favorito": False
        }
    contatos.append(contatos_exemplo)
    print(f"contato {nome} foi adicionado")
    return
    
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
        adicionar_contato = input("Digite o nome da pessoa")
    
    break

print("programa finalizado")