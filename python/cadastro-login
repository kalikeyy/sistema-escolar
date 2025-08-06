def sistema():
    usuarios = {}  

    while True:
        print("\n=== Sistema Escolar ===")
        print("1 - Cadastro")
        print("2 - Login")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("\n--- Cadastro ---")
            print("Escolha o tipo de perfil:")
            print("1 - Responsável")
            print("2 - Aluno")
            print("3 - Professor")
            opcao = input("Opção: ")

            tipos = {"1": "responsável", "2": "aluno", "3": "professor"}
            if opcao not in tipos:
                print("Opção inválida.")
                continue
            perfil = tipos[opcao]

            nome = input("Nome completo: ").strip()
            email = input("E-mail: ").strip().lower()
            cpf = input("CPF: ").strip()
            telefone = input("Telefone: ").strip()
            endereco = input("Endereço: ").strip()
            senha = input("Senha: ").strip()

            dados_extra = {}
            if perfil == "responsável":
                dados_extra["nome_aluno"] = input("Nome completo do aluno: ").strip()
                dados_extra["cgm_aluno"] = input("CGM do aluno: ").strip()
            elif perfil == "aluno":
                dados_extra["cgm"] = input("CGM do aluno: ").strip()

            if email in usuarios:
                print(" Esse e-mail já está cadastrado!")
            else:
                usuarios[email] = {
                    "senha": senha,
                    "perfil": perfil,
                    "dados": {
                    "nome": nome,
                    "cpf": cpf,
                    "telefone": telefone,
                    "endereco": endereco,
                        **dados_extra
                    }
                }
                print(f"cadastro concluído para {nome} ({perfil}).")

        elif escolha == "2":
            print("\n--- Login ---")
            print("Escolha o tipo de perfil para login:")
            print("1 - Responsável")
            print("2 - Aluno")
            print("3 - Professor")
            opcao_login = input("Opção: ")

            tipos = {"1": "responsável", "2": "aluno", "3": "professor"}
            if opcao_login not in tipos:
                print("Opção inválida.")
                continue
            perfil_login = tipos[opcao_login]

            nome_login = input("Nome completo: ").strip()
            senha_login = input("Senha: ").strip()

            encontrado = None
            for usuario in usuarios.values():
                if (usuario["dados"]["nome"].lower() == nome_login.lower() and
                    usuario["senha"] == senha_login and
                    usuario["perfil"] == perfil_login):
                    encontrado = usuario
                    break

            if encontrado:
                if perfil_login == "aluno":
                    cgm_login = input("Digite seu CGM: ").strip()
                    if cgm_login != encontrado["dados"].get("cgm"):
                        print(" CGM incorreto.")
                        continue
                elif perfil_login == "responsável":
                    cpf_login = input("Digite seu CPF: ").strip()
                    cgm_aluno_login = input("Digite o CGM do aluno: ").strip()
                    if cpf_login != encontrado["dados"].get("cpf") or cgm_aluno_login != encontrado["dados"].get("cgm_aluno"):
                        print(" CPF ou CGM do aluno incorretos.")
                        continue
                elif perfil_login == "professor":
                    cpf_login = input("Digite seu CPF: ").strip()
                    if cpf_login != encontrado["dados"].get("cpf"):
                        print(" CPF incorreto.")
                        continue

                print(f" Login bem-sucedido! Bem-vindo(a), {encontrado['dados']['nome']} ({perfil_login}).")
            else:
                print("Nome, senha ou perfil incorretos.")

        elif escolha == "3":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema()
