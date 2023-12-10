from modelo import Filme, Serie

filme1 = Filme("Vingadores", 2018, 240)
filme2 = Filme("Thor", 2012, 175)

serie1 = Serie("Friends", 2018, 12)
serie2 = Serie("SOS Malibu", 2018, 5)

filme1.dar_likes()
filme1.dar_likes()
filme1.dar_likes()

filme2.dar_likes()

serie1.dar_likes()

serie2.dar_likes()
serie2.dar_likes()

filmes_e_series = [filme1, filme2, serie1, serie2]

for programa in filmes_e_series:
    programa.imprime()


