from modelo import Filme, Serie, Playlist

filme1 = Filme("Vingadores", 2018, 240)
filme2 = Filme("Thor", 2012, 175)
filme3 = Filme("Matrix", 1999, 231)


serie1 = Serie("Friends", 2018, 12)
serie2 = Serie("SOS Malibu", 2018, 5)

filme1.dar_likes()
filme1.dar_likes()
filme1.dar_likes()

filme2.dar_likes()
filme2.dar_likes()
filme3.dar_likes()
filme3.dar_likes()

serie1.dar_likes()
serie1.dar_likes()
serie1.dar_likes()
serie1.dar_likes()
serie1.dar_likes()

serie2.dar_likes()
serie2.dar_likes()

filmes_e_series = [filme1, filme2, serie1, serie2]

fim_de_semana = Playlist("Fim de semana", filmes_e_series)

# Verificando se um item está na playlist
print(filme3 in fim_de_semana)

# Mostrando o primeiro item da playlist
print(fim_de_semana[0])

print("----------------------------------------------")

# Mostrando a playlist
for programa in fim_de_semana:
    print(programa)


