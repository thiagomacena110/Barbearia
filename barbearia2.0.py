import pickle


try:
    arq = open("barbearia.dat", "rb")
    dados = pickle.load(arq)

    usuarios = dados["usuarios"]
    cortes = dados["cortes"]
    horarios = dados["horarios"]
    agendamentos = dados["agendamentos"]

    arq.close()

except:
    usuarios = {}
    cortes = {}
    horarios = {}
    agendamentos = {}

m = ""

print("""
Seja bem-vindo à Barbearia!

Aqui temos:
- Cadastro de usuários
- Gerência de cortes
- Agenda de horários
- Relatórios
""")

while m != "0":

    print("""
----- Sistema de Gestão para Barbearia -----

1 - Usuários
2 - Cortes
3 - Agenda de Horários
4 - Relatório
0 - Sair
""")

    m = input("Escolha uma opção: ")

    # ==========================
    # USUÁRIOS
    # ==========================

    if m == "1":

        n = ""

        while n != "0":

            print("""
----- Módulo Usuários -----

1 - Cadastrar usuário
2 - Alterar usuário
3 - Listar usuários
4 - Remover usuário
0 - Voltar
""")

            n = input("Escolha uma opção: ")

            # CADASTRAR
            if n == "1":

                cpf = input("Digite o CPF: ")
                nome = input("Digite o nome: ")
                telefone = input("Digite o telefone: ")

                usuarios[cpf] = [nome, telefone]

                print("Usuário cadastrado com sucesso!")

            # ALTERAR
            elif n == "2":

                if len(usuarios) == 0:
                    print("Nenhum usuário cadastrado.")

                else:

                    for cpf in usuarios:
                        print(
                            "CPF:", cpf,
                            "| Nome:", usuarios[cpf][0],
                            "| Telefone:", usuarios[cpf][1]
                        )

                    cpf = input("Digite o CPF do usuário: ")

                    if cpf in usuarios:

                        nome = input("Digite o novo nome: ")
                        telefone = input("Digite o novo telefone: ")

                        usuarios[cpf] = [nome, telefone]

                        print("Usuário alterado com sucesso!")

                    else:
                        print("CPF não encontrado.")

            # LISTAR
            elif n == "3":

                if len(usuarios) == 0:
                    print("Nenhum usuário cadastrado.")

                else:

                    print("\nUsuários cadastrados:")

                    for cpf in usuarios:
                        print(
                            "CPF:", cpf,
                            "| Nome:", usuarios[cpf][0],
                            "| Telefone:", usuarios[cpf][1]
                        )

            # REMOVER
            elif n == "4":

                if len(usuarios) == 0:
                    print("Nenhum usuário cadastrado.")

                else:

                    cpf = input("Digite o CPF do usuário: ")

                    if cpf in usuarios:

                        usuarios.pop(cpf)

                        print("Usuário removido com sucesso!")

                    else:
                        print("CPF não encontrado.")

    # ==========================
    # CORTES
    # ==========================

    elif m == "2":

        n = ""

        while n != "0":

            print("""
----- Módulo Cortes -----

1 - Cadastrar corte
2 - Listar cortes
3 - Remover corte
0 - Voltar
""")

            n = input("Escolha uma opção: ")

            if n == "1":

                codigo = len(cortes) + 1

                corte = input("Digite o nome do corte: ")

                cortes[codigo] = corte

                print("Corte cadastrado com sucesso!")

            elif n == "2":

                if len(cortes) == 0:
                    print("Nenhum corte cadastrado.")

                else:

                    print("\nCortes cadastrados:")

                    for codigo in cortes:
                        print(codigo, "-", cortes[codigo])

            elif n == "3":

                if len(cortes) == 0:
                    print("Nenhum corte cadastrado.")

                else:

                    for codigo in cortes:
                        print(codigo, "-", cortes[codigo])

                    codigo = int(input("Digite o código do corte: "))

                    cortes.pop(codigo)

                    print("Corte removido com sucesso!")

    # ==========================
    # Agenda de Horários 
    # ==========================

    elif m == "3":

        n = ""

        while n != "0":

            print("""
----- Agenda de Horários -----

1 - Cadastrar horário
2 - Listar horários
3 - Remover horário
4 - Agendar corte
0 - Voltar
""")

            n = input("Escolha uma opção: ")

            if n == "1":

                codigo = len(horarios) + 1

                horario = input("Digite o horário: ")

                horarios[codigo] = horario

                print("Horário cadastrado com sucesso!")

            elif n == "2":

                if len(horarios) == 0:
                    print("Nenhum horário cadastrado.")

                else:

                    print("\nHorários cadastrados:")

                    for codigo in horarios:
                        print(codigo, "-", horarios[codigo])

            elif n == "3":

                if len(horarios) == 0:
                    print("Nenhum horário cadastrado.")

                else:

                    for codigo in horarios:
                        print(codigo, "-", horarios[codigo])

                    codigo = int(input("Digite o código do horário: "))

                    horarios.pop(codigo)

                    print("Horário removido com sucesso!")

            elif n == "4":

                if len(usuarios) == 0:
                    print("Cadastre usuários primeiro.")

                elif len(cortes) == 0:
                    print("Cadastre cortes primeiro.")

                elif len(horarios) == 0:
                    print("Cadastre horários primeiro.")

                else:

                    print("\nUsuários:")

                    for cpf in usuarios:
                        print(
                            "CPF:", cpf,
                            "| Nome:", usuarios[cpf][0]
                        )

                    cpf = input("Digite o CPF do cliente: ")

                    if cpf in usuarios:

                        print("\nCortes:")

                        for codigo in cortes:
                            print(codigo, "-", cortes[codigo])

                        cod_corte = int(input("Código do corte: "))

                        print("\nHorários:")

                        for codigo in horarios:
                            print(codigo, "-", horarios[codigo])

                        cod_horario = int(input("Código do horário: "))

                        codigo = len(agendamentos) + 1

                        agendamentos[codigo] = {
                            "cpf": cpf,
                            "cliente": usuarios[cpf][0],
                            "telefone": usuarios[cpf][1],
                            "corte": cortes[cod_corte],
                            "horario": horarios[cod_horario]
                        }

                        print("Agendamento realizado com sucesso!")

                    else:
                        print("CPF não cadastrado.")

    # ==========================
    # RELATÓRIO
    # ==========================

    elif m == "4":

        print("""
---------------------------
-------- RELATÓRIO --------
---------------------------
""")

        print("\nUSUÁRIOS")

        for cpf in usuarios:
            print(
                "CPF:", cpf,
                "| Nome:", usuarios[cpf][0],
                "| Telefone:", usuarios[cpf][1]
            )

        print("\nCORTES")

        for codigo in cortes:
            print(codigo, "-", cortes[codigo])

        print("\nHORÁRIOS")

        for codigo in horarios:
            print(codigo, "-", horarios[codigo])

        print("\nAGENDAMENTOS")

        if len(agendamentos) == 0:

            print("Nenhum agendamento realizado.")

        else:

            for codigo in agendamentos:

                print(
                    codigo,
                    "| CPF:", agendamentos[codigo]["cpf"],
                    "| Cliente:", agendamentos[codigo]["cliente"],
                    "| Telefone:", agendamentos[codigo]["telefone"],
                    "| Corte:", agendamentos[codigo]["corte"],
                    "| Horário:", agendamentos[codigo]["horario"]
                )

    # ==========================
    # SAIR E SALVAR
    # ==========================

    elif m == "0":

        dados = {
            "usuarios": usuarios,
            "cortes": cortes,
            "horarios": horarios,
            "agendamentos": agendamentos
        }

        arq = open("barbearia.dat", "wb")
        pickle.dump(dados, arq)
        arq.close()

        print("""
Obrigado pela preferência!
Até a próxima!
""")

    else:
        print("Opção inválida!")

