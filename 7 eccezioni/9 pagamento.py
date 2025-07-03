# Crea una classe Pagamento che gestisce transazioni.
# Definisci e gestisci le seguenti eccezioni personalizzate:
# - SaldoInsufficienteException
# - MetodoPagamentoNonSupportatoException
# - TransazioneFallitaException
# Implementa un metodo effettua_pagamento() che solleva queste eccezioni quando necessario.

from random import choice


class SaldoInsufficienteException(Exception):
    def __init__(self, saldo, importo):
        super().__init__(f"Saldo insufficiente: saldo disponibile {saldo}, importo richiesto {importo}")


class MetodoPagamentoNonSupportatoException(Exception):
    def __init__(self, metodo):
        super().__init__(f"Metodo di pagamento non supportato: '{metodo}'")


class TransazioneFallitaException(Exception):
    def __init__(self, messaggio="La transazione è fallita per motivi sconosciuti."):
        super().__init__(messaggio)


# Classe Pagamento

class Pagamento:

    metodi_supportati = ["carta_credito", "paypal", "bonifico"]

    def __init__(self, saldo_iniziale):
        self.saldo = saldo_iniziale

    def effettua_pagamento(self, importo, metodo):
        print(f"➡️ Tentativo di pagamento di €{importo} con metodo '{metodo}'")

        if metodo not in self.metodi_supportati:
            raise MetodoPagamentoNonSupportatoException(metodo)

        if importo > self.saldo:
            raise SaldoInsufficienteException(self.saldo, importo)

        try:
            # Simulazione di una possibile eccezione generica (es. errore di rete, banca offline, ecc.)
            if choice([True, False]):
                raise RuntimeError("Errore imprevisto nel sistema bancario")

            # Esecuzione del pagamento
            self.saldo -= importo
            print(f"✅ Pagamento riuscito. Nuovo saldo: €{self.saldo}")

        except RuntimeError as e:
            raise TransazioneFallitaException(str(e))


# Esempio di utilizzo

account = Pagamento(saldo_iniziale=100)

try:
    account.effettua_pagamento(50, "paypal")
    account.effettua_pagamento(70, "carta_cripto")  # metodo non supportato
except MetodoPagamentoNonSupportatoException as e:
    print(f"❌ Errore: {e}")
except SaldoInsufficienteException as e:
    print(f"❌ Errore: {e}")
except TransazioneFallitaException as e:
    print(f"❌ Errore: {e}")