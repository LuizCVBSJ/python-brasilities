from validate_docbr import CPF, CNPJ


class Document:
    @staticmethod
    def create_document(document):
        document = str(document)
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Document length invalid!")


class DocCpf:
    def __init__(self, document):
        document = str(document)
        if self.validate(document):
            self.cpf = document
        else:
            raise ValueError("CPF Invalid!")

    def __str__(self):
        return self.format()

    def validate(self, document):
        if len(document) == 11:
            validator = CPF()
            return validator.validate(document)
        else:
            raise ValueError("Number of digits invalid!")

    def format(self):
        mask = CPF()
        return mask.mask(self.cpf)


class DocCnpj:

    def __init__(self, document):
        if self.validate(document):
            self.cnpj = document
        else:
            raise ValueError("CNPJ invalid!")

    def validate(self, document):
        validator = CNPJ()
        return validator.validate(document)

    def __str__(self):
        return self.format()

    def format(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)
