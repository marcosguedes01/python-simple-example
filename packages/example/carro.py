class Carro():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    
    def exibirDescricao(self):
        print(f'Carro {self.nome} de cor {self.cor}')

    def exibirMotor(self):
        print("1.0")

class HB20(Carro):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    
    def exibirMotor(self):
        print("1.6")