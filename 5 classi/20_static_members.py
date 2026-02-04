class Calcolatrice:
    uso_counter = 0

    def sottrazione(self, a, b):
        return a - b

    @staticmethod
    def somma(a, b):
        return a + b

    @classmethod
    def incrementa_uso(cls, valore):
        cls.uso_counter += valore
        print(f"La calcolatrice è stata usata {cls.uso_counter} volte")


print(f"Uso iniziale: {Calcolatrice.uso_counter}")
Calcolatrice.incrementa_uso(2)
risultato = Calcolatrice.somma(5, 7)
print(f"Risultato della somma: {risultato}")
Calcolatrice.incrementa_uso(2)
print(f"Uso finale: {Calcolatrice.uso_counter}")

calcolatrice = Calcolatrice()
risultato = calcolatrice.sottrazione(1, 2)
print(f"Risultato della sottrazione: {risultato}")

print(f"Uso: {calcolatrice.uso_counter}")
print(f"Uso finale: {Calcolatrice.uso_counter}")

calcolatrice.uso_counter += 1
print(f"Uso: {calcolatrice.uso_counter}")
print(f"Uso finale: {Calcolatrice.uso_counter}")