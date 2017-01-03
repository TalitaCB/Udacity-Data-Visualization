## P6. Data Visualization: Titanic Data Exploration

### Resumo
The scatter chart shows the survival rates as per the age of the passengers. 
O gráfico de bolhas mostra a taxa de sobrevivência por faixa de idade, sexo e classe social. 

### Design
Eu escolhi a base de dados do Titanic que contém informações sobre os passageiros a bordo do Titanic e quais passageiros sobreviveram ou não ao acidente que afundou o navio.
Ao analisar os dados procurei padrões que pudessem explicar que tipo de passageiro sobreviveu e qual não sobreviveu. Durante a analise pude perceber que menos que 20% dos passageiros totais que estavam no navio sobreviveram.
Desses passageiro a maior parte é composta por mulheres e crianças, ou sejam, mulheres e crianças tiveram uma maior taxa de sobrevivência que os homens. Também percebi que o índice de sobrevivência de passageiros da 1 classe foi maior do que de passageiros da terceira classe.

Para a visualização dos dados utilzei um gráfico de bolhas com três variáveis categóricas. Eu queria um gráfico que pudesse mostrar a relação de sobrevivência entre vários grupos como mulheres adultas de classe baixa, homens adultos de classe alta, crianças de classe alta etc.
Esse tipo de visualização me permitiu fazer isso mesmo tendo trabalhado com três variáveis categóricas. 

As variáveis utilizadas foram:

Idade: Está representada no eixo Y. É uma  variável categórica, dividida em 4 faixas para melhor representar cada fase da vida como crianças, jovens adultos, adultos e idosos.
Sexo: Variável catégorica representada por dois códigos visuais no eixo x. As cores foram utilizadas foram em tons pasteis, vermelho para mulher e azul para homem já que são cores que pelo senso comum identificam esses generos
Classe Social: Variável categorica representada no eixo x.
% Sobreviventes: Variavel quantitativa calculada para cada grupo com a seguinte formula: (total de sobreviventes do grupo / total de pessoas no grupo) * 100. Esta exibida em %. A medida foi representada pelo tamanho das bolhas.

### Transformação Dados
Realizei algumas transformações no arquivo original recebido. Primeiramente eliminei todas as colunas que não iria utilizar deixando apenas as colunas Idade, Sexo, Classe social e o indicador de sobrevivência. 
Após isso gerei faixas de idade:

< 14 anos
entre 14 e 30 anos
entre 31 e 50 anos
acima de 51 anos

Também renomeei as classes sociais e o sexo para que ficassem mais legiveis. Calculei o percentual de sobreviventes em cada grupo composto de faixa de idade, sexo e classe social.
A transformação da base de dados foi feita em python e pode ser consultada no arquivo titanic_csv_change.py. 


### Antes do feedback:
O html feito antes do feedback foi nomeado de index_initial.html

### Feedback

Segue abaixo o feedback recebido:

#### #1

> O gráfico não tem nenhuma explicação sobre o que está sendo analisado e o que é essa taxa de sobrevivência. 


#### #2

> Gostei muito da forma como o gráfico foi utilizado, está muito fácil de visualizar as diferenças entre os grupos. No entanto acho que o título está muito grande e não está centralizado com o gráfico. 

####  #3

> Gostei das cores utilizadas no gráfico e quão fácil está a visualização da informação. Apenas um ponto a melhorar é o titulo dos eixos está da mesma cor do eixo dificultando a leitura.


### After Feedback:
As mudanças realizadas foram:

- Título dos eixos ficou em negrito
- Alterado tamanho de letra e tipo de letra do título.
- Inserido alguns textos explicando melhor sobre a base de dados e o que foi analisado.


O html após o feedback é o index_final.html


### Recursos

http://stackoverflow.com/questions/21206395/write-to-csv-from-dataframe-python-pandas
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html
http://stackoverflow.com/questions/25478673/add-colors-to-dimple-js-bar-chart-based-on-value-and-add-goal-line
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.chart#assignColor
http://stackoverflow.com/questions/25416063/title-for-charts-and-axes-in-dimple-js-charts
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.axis#title
http://dimplejs.org/advanced_examples_viewer.html?id=advanced_custom_styling
http://dimplejs.org/adhoc_viewer.html?id=adhoc_bar_custom_tooltips
http://stackoverflow.com/questions/25334677/override-d3-dimple-tooltips-with-chart-data
http://bl.ocks.org/tybyers/736da90eefe0c347a1d6