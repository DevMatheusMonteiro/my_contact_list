def enterNumber(mensagem:str):
    while True:
        try:
            number = float(input(mensagem))
            return number
        except ValueError:
            print("Erro: número inválido.")

def enterText(mensagem:str):
    while True:
        text = input(mensagem)
        if text != None and text.strip() != "":
            return text
        print("Erro: texto nulo ou vazio.")