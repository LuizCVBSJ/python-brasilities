class AdressSearch:
    def __init__(self, cep):
        if self.cep_is_valid(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")

    def cep_is_valid(self, cep):
        return len(cep) == 8

    def format_cep(self):
        return "{}-{}".format(self.cep[0:5], self.cep[5:])

    def __str__(self):
        return self.format_cep()
