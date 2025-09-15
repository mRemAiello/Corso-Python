class Calcolatrice:
    uso_counter = 0

    @staticmethod
    def somma(a, b):
        return a + b

    @classmethod
    def incrementa_uso(cls):
        cls.uso_counter += 1
        print(f"La calcolatrice è stata usata {cls.uso_counter} volte")


if __name__ == "__main__":
    print(f"Uso iniziale: {Calcolatrice.uso_counter}")
    Calcolatrice.incrementa_uso()
    risultato = Calcolatrice.somma(5, 7)
    print(f"Risultato della somma: {risultato}")
    Calcolatrice.incrementa_uso()
    print(f"Uso finale: {Calcolatrice.uso_counter}")
