# Andares do hotel sem imprimir o andar 13

for andar in range(1, 21):
  if(andar == 13):
    continue
  else:
    print(andar)

  # Andares com o laço While.

  contador = 1
  while (contador <= 20):
    if(contador == 13):
      contador = contador + 1
      continue
    else:
      print(contador)
      contador = contador + 1

  # andares em ordem decrescente

for andar in range(20, 0 -1):
  if(andar == 13):
    continue
  else:
    print(andar)