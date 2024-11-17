class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            return print(f"{self.nome} já está filmando...")
        print(f'{self.nome} filmando...')
        self.filmando = True

    def para_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando!")
            return
        
        print(f"{self.nome} está parando de filmar...")
        self.filmando = False

        
    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar quando estiver filmando!")
            return
        print(f'{self.nome} está fotografando!')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.para_filmar()
c1.fotografar()
# print(c1.filmando)
# print(c2.filmando)