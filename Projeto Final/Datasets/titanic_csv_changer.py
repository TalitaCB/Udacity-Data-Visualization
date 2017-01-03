# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np


df = pd.read_csv("D:/Talita/Pessoal/Udacity/Data Visualization/bar_charts/Projeto Final/titanic_data.csv")

#retira nulo da variavel idade inserindo a media por classe e sexo
sexo = ['female','male']

mediana_idade = np.zeros((2,3))


for i in sexo:

    if i == 'female':
        cod_sexo = 0
    else:
        cod_sexo = 1
    for j in range(0, 3):
        mediana_idade[cod_sexo,j] = df[(df['Sex'] == i) & (df['Pclass'] == j+1)]['Age'].dropna().median()


df['Idade_preenchimento'] = df['Age']

for i in sexo:
    if i == 'female':
        cod_sexo = 0
    else:
        cod_sexo = 1

    for j in range(0, 3):
        df.loc[(df.Age.isnull()) & (df.Sex == i) & (df.Pclass == j+1),'Idade_preenchimento'] = mediana_idade[cod_sexo,j]

df['Age'] = df['Idade_preenchimento']

#Criando faixa de idade
df.loc[(df.Age >= 0) & (df.Age <=14), 'Age'] = ' <14'
df.loc[(df.Age > 14) & (df.Age <=30), 'Age'] = '14-30'
df.loc[(df.Age > 30) & (df.Age <=50), 'Age'] = '31-50'
df.loc[(df.Age > 50) & (df.Age <=80), 'Age'] = '>51'
df.Age.fillna('NA', inplace=True)
df.loc[(df.Age == 'NA'), 'Age'] = 'Nâo Registrado'

#print df['Survived'].sum()

#Renomeando classe
df.loc[(df.Pclass == 1), 'Classe'] = '1ª Classe'
df.loc[(df.Pclass == 2), 'Classe'] = '2ª Classe'
df.loc[(df.Pclass == 3), 'Classe'] = '3ª Classe'

#Renomeando sexo
df.loc[(df.Sex == 'male'), 'Sexo'] = 'Masculino'
df.loc[(df.Sex == 'female'), 'Sexo'] = 'Feminino'

#drop colunas desnecessarias
df.pop('Name')
df.pop('Fare')
df.pop('Cabin')
df.pop('Ticket')
df.pop('SibSp')
df.pop('Parch')
df.pop('Embarked')
df.pop('Sex')
df.pop('Pclass')
df.pop('PassengerId')
df.pop('Idade_preenchimento')


agrupamento_quantidade = df.groupby(['Age','Classe','Sexo'])['Survived'].count()
agrupamento_sobreviventes = df.groupby(['Age','Classe','Sexo'])['Survived'].sum()
agrupamento_sobreviventes_taxa = (agrupamento_sobreviventes / agrupamento_quantidade)* 100


agrupamento_sobreviventes_taxa.to_csv('titanic_final.csv', header='True')