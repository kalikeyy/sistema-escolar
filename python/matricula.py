def main():
    print("Sistema de Matrícula Escolar")
    alunos = []
    
    while True:
        print("\nMenu Principal:")
        print("1 - Matricular aluno")
        print("2 - Rematricular aluno")
        print("3 - Sair do sistema")
        
        try:
            opcao = int(input("\nEscolha uma opção (1-3): "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
            
        if opcao == 3:
            print("Saindo do sistema...")
            break
        elif opcao not in [1, 2]:
            print("Opção inválida. Por favor, escolha entre 1 e 3.")
            continue
            
        if opcao == 1:
            print("\n Matricular Aluno")
            nome = input("Nome completo do aluno: ")
            cpf = input("CPF do aluno: ")
            serie = input("Série/Ano: ")
            turma = input("Turma: ")
            
            alunos.append({
                "nome": nome,
                "cpf": cpf,
                "serie": serie,
                "turma": turma,
                "situacao": "Matriculado"
            })
            print(f"\nAluno {nome} matriculado com sucesso na turma {turma}!")
            
        elif opcao == 2:
            print("\nRematricular Aluno")
            cpf = input("Digite o CPF do aluno: ")
            
            encontrado = False
            for aluno in alunos:
                if aluno["cpf"] == cpf:
                    nova_serie = input(f"Nova série para {aluno['nome']}: ")
                    nova_turma = input("Nova turma: ")
                    aluno["serie"] = nova_serie
                    aluno["turma"] = nova_turma
                    print(f"\n{aluno['nome']} rematriculado para {nova_serie}, turma {nova_turma}!")
                    encontrado = True
                    break
                    
            if not encontrado:
                print("\nAluno não encontrado!")
                

if __name__ == "__main__":
    main()
