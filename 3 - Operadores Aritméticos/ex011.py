larg = float(input("Digite a largura da parede: "))
altu = float(input("Digite a altura da parede: "))
area = larg * altu
tint = area / 2

print("Sua parede tem dimensão de {} x {} e sua área é de {:.2f} metros quadrados" .format(larg, altu, area))
print("Para pintar essa parede, você precisará de {:.2f}l de tinta." .format(tint))
