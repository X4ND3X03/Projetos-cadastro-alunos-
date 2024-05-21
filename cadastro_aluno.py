class Aluno:
    def __init__(self, nome, idade, cpf, endereco, email, contato):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.email = email
        self.contato = contato

def cadastrar_aluno():
    print("Por favor, insira os dados do aluno:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    email = input("Email: ")
    contato = input("Contato: ")

    return Aluno(nome, idade, cpf, endereco, email, contato)

def verificar_matricula(aluno):
    if 15 <= aluno.idade <= 29:
        print(f"O aluno {aluno.nome} foi matriculado no curso de Front-End!")
    else:
        print(f"Desculpe, o aluno {aluno.nome} não atende aos requisitos de idade para matrícula.")

def main():
    print("Bem-vindo ao Sistema de Matrícula para o Curso de Front-End!")

    aluno = cadastrar_aluno()
    verificar_matricula(aluno)

if __name__ == "__main__":
    main()