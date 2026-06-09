usuarios = []
cortes = []
horarios = []

m = ""
print("""Seja bem-vindo a Barbearia!
    Aqui temos: 
    Cadastro de usuário
    Gerencia de cortes 
    Agenda de cortes 
    Relatórios
    
    """)

while m != "0":
    
    print("""
    ----- Sistema de Gestão para Barbearia -----
    ----- 1 - Usuário --------------------------
    ----- 2 - Estilos de cortes ----------------
    ----- 3 - Agenda de Horários ---------------
    ----- 4 - Relatório ------------------------
    ----- 0 - Sair -----------------------------
    """)

    m = input("Escolha uma opção: ")

    
    # 1- Usuário
    
    if m == "1":

        n = ""

        while n != "0":

            print("""
            ----- Módulo de Usuário -----
            ----- 1 - Cadastrar usuário -
            ----- 2 - Alterar usuário ---
            ----- 3 - Listar usuários ---
            ----- 4 - Remover usuário ---
            ----- 0 - Voltar ------------
            """)

            n = input("Escolha uma opção: ")

            # Para cadastrar. usando o append para adiocinar na lista 
            if n == "1":
                nome = input("Digite o nome do usuário: ")
                usuarios.append(nome)
                print("Usuário cadastrado com sucesso.")

            # Alterar o usuário. o for é usando para olhar a lista e o len para contar quanto item na lista. o i para saber a posição. 
            elif n == "2":
                print("\nLista de usuários:")
                
                for i in range(len(usuarios)):
                    print(i, "-", usuarios[i])

                pos = int(input("Digite o número do usuário: "))
                novo_nome = input("Digite o novo nome: ")
            #pos é para mudar o nome na lista
                usuarios[pos] = novo_nome

                print("Usuário alterado com sucesso.")

            # Lista de Usuário 
            elif n == "3":
                print("""
                ----------------------------              
                --- Usuários cadastrados ---
                ----------------------------
                """)
                if len(usuarios) == 0:
                    print("Nenhum usuário encontrado.")
                else:
                    for usuario in usuarios:
                        print(usuario)

            # Remover usuário 
            elif n == "4":
                print("\nLista de usuários:")

                for i in range(len(usuarios)):
                    print(i, "-", usuarios[i])

                pos = int(input("Digite o número do usuário para remover: "))

                usuarios.pop(pos)
                #usado o pop para remover (pela a posição)

                print("Usuário removido com sucesso.")

    
    # 2- Estilos Cortes 
  
    elif m == "2":

        n = ""

        while n != "0":

            print("""
            ----- Estilos de Cortes -----
            ----- 1 - Cadastrar corte ---
            ----- 2 - Listar cortes -----
            ----- 3 - Remover corte -----
            ----- 0 - Voltar ------------
            """)

            n = input("Escolha uma opção: ")

            # Cadastrar Corte
            if n == "1":
                corte = input("Digite o nome do corte: ")
                cortes.append(corte)

                print("Corte cadastrado com sucesso.")

            # Lista Cortes
            elif n == "2":

                print("""
                ----------------------------              
                ---- Cortes cadastrados ----
                ----------------------------
                """)

                for corte in cortes:
                    print(corte)

            # Remover Corte
            elif n == "3":

                for i in range(len(cortes)):
                    print(i, "-", cortes[i])

                pos = int(input("Digite o número do corte: "))

                cortes.pop(pos)

                print("Corte removido.")

    
    # 3- Agenda de Horários
    
    elif m == "3":

        n = ""

        while n != "0":

            print("""
            ----- Agenda de Horários -----
            ----- 1 - Cadastrar horário --
            ----- 2 - Listar horários ----
            ----- 3 - Remover horário ----
            ----- 0 - Voltar -------------
            """)

            n = input("Escolha uma opção: ")

            # Cadastrar Horário
            if n == "1":

                horario = input("Digite o horário: ")

                horarios.append(horario)

                print("Horário cadastrado.")

            # Lista de Horários
            elif n == "2":

                print("""
                ----------------------------              
                --- Horários cadastrados ---
                ----------------------------
                """)
       

                if len(horarios) == 0:
                    print("Nenhum horário encontrado.")
                else:
                    for horario in horarios:
                        print(horario)

            # Remover Horários 
            elif n == "3":

                for i in range(len(horarios)):
                    print(i, "-", horarios[i])

                pos = int(input("Digite o número do horário: "))

                horarios.pop(pos)

                print("Horário removido.")

   
    # 4- Relatório
    
    elif m == "4":

        print("""
        ---------------------------
        -------- RELATÓRIO --------
        ---------------------------
        """)
      
        print("\nQuantidade de usuários:", len(usuarios))
        print("Usuários: ", usuarios)
        print("\nQuantidade de cortes:", len(cortes))
        print("Cortes: ", cortes)
        print("\nQuantidade de horários:", len(horarios))
        print("Horários: ", horarios)

    
    # Para Sair
    
    elif m == "0":
        print("""
        Obrigado pela a preferência. 
        Até a próxima! 
        """)

    else:
        print("Opção inválida!")
