class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.cpf_validate(document):
            self.cpf = document
        else:
            raise ValueError("CPF Invalid!")

    def __str__(self):
        return self.cpf_format()

    def cpf_validate(self, document):
        if len(document) == 11:
            return True
        else:
            return False

    def cpf_format(self):
        return "{}.{}.{}-{}".format(self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:])
