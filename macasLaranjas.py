from sklearn import tree

lisa, irregular = 1, 0
maça, laranja = 1, 0

pomar = [
    [150, lisa], [130, lisa], [180, irregular], 
    [160, irregular], [140, irregular], [160, lisa], 
    [100, irregular]
]

resultado = [maça, maça, laranja, laranja, laranja, maça, maça]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

peso = input("Insira o peso: ")
superficie = input("Insira a superfície(1 lisa/ 0 irregular): ")

resultadoUsuario = clf.predict([[peso, superficie]])

if resultadoUsuario == 1:
    print("Maçã!")
else:
    print("Laranja!")