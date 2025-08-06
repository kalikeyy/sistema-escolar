def sistema_contato():
    print("=== Fale Conosco ===")
    email = input("Digite seu e-mail: ")
    mensagem = input("Digite sua mensagem ou pergunta: ")

    if not email or not mensagem:
        print("preencha todos os campos.")
    else:
        print("\nEnviando mensagem")
        print("Mensagem enviada com sucesso! Aguardaremos seu contato.")
        
if __name__ == "__main__":
    sistema_contato()
