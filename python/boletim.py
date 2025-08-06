def sistema_boletim():
    notas_alunos = {}  

    while True:
        print("\nMenu Principal")
        print("1 - Professor (inserir notas)")
        print("2 - Aluno (ver boletim)")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_prof = input("\nNome do professor: ")
            while True:
                aluno = input("\nNome do aluno (ou 'voltar' para sair): ").strip().title()
                if aluno.lower() == "voltar":
                    break
                materia = input("Matéria: ").strip().title()
                try:
                    nota = float(input("Nota: "))
                except ValueError:
                    print("Nota inválida.")
                    continue

                if aluno not in notas_alunos:
                    notas_alunos[aluno] = {}
                notas_alunos[aluno][materia] = nota
                print(f"Nota registrada para {aluno} em {materia}.")

        elif opcao == "2":
            aluno = input("\nDigite seu nome: ").strip().title()
            if aluno not in notas_alunos:
                print("Nenhuma nota cadastrada para esse aluno.")
                continue

            materias = notas_alunos[aluno]
            print(f"\n Boletim de {aluno}")
            total = 0
            for materia, nota in materias.items():
                print(f"{materia}: {nota}")
                total += nota
            media = total / len(materias)
            print(f"Média final: {media:.2f}")

            if media >= 7:
                print(" Situação: Aprovado")
            elif media >= 5:
                print(" Situação: Recuperação")
            else:
                print("Situação: Reprovado")

        elif opcao == "3":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema_boletim()
