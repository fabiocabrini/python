#Fábio Henrique Cabrini
#Check point 2 - Diagnóstico de Diabétes Mellitus
#Maio de 2020
from sklearn import tree #importa o módulo "tree" do Sklearn Árvore de Decisão
features = [[90, 140, 150], [89, 135, 140], [85, 140, 100], [100, 145, 150], [110, 200, 180], [126, 142, 160], [126, 200, 201], [128, 201, 210], [134,201, 250]]
#labels = [normal, normal, normal, tolerancia, tolerancia, tolerancia, mellitus, mellitus, mellitus]
labels = [0, 0, 0, 1, 1, 1, 2, 2, 2]
classif = tree.DecisionTreeClassifier() #Classificador
classif.fit(features, labels)
jejum = float(input("Digite a glicemia em mg/dL Jejum:"))
sobrecarga = float(input("Digite a glicemia em mg/dL Pós-Sobrecarga:"))
qualquer = float(input("Digite a glicemia em mg/dL Casual:"))
x = classif.predict([[jejum, sobrecarga, qualquer]])
if x == 0:
    print("Glicemia está normal!")
elif x == 1:
    print("Tolerância à glicose diminuida!") 
else:
    print("Diagnóstico de Diabetes Mellitus")
print("Esses valores não devem ser aceitos como diagnóstico, procure um médico!")
