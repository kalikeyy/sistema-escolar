def sistema_agenda():
    agenda = {}  

    while True:
        print("\nSistema de Agenda Escolar")
        print("1 - Professor (Postar atividade)")
        print("2 - Aluno (Ver atividades)")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_prof = input("\nNome do professor: ")
            materia = input("Matéria: ").strip().title()
            data = input("Data da atividade: ").strip()
            descricao = input("Descrição da atividade: ").strip()

            atividade = {"data": data, "descricao": descricao}

            if materia not in agenda:
                agenda[materia] = []
            agenda[materia].append(atividade)

            print(f"Atividade foi adicionada para {materia}.")

        elif escolha == "2":
            print("\nConsulta de Atividades")
            materia = input("Digite a matéria: ").strip().title()

            if materia in agenda and agenda[materia]:
                print(f"\n Atividades de {materia}:")
                for i, atividade in enumerate(agenda[materia], start=1):
                    print(f"{i}. Data: {atividade['data']} - {atividade['descricao']}")
            else:
                print("Nenhuma atividade registrada para essa matéria.")

        elif escolha == "3":
            print("Saindo do sistema de agenda.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema_agenda()
