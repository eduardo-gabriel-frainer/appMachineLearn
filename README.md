# Projeto Machine Learn Calcular o valor de uma pizza com o diâmetro 🍕🍕

Linguagens e tecnologias utilizadas:
*  Python
*  Pandas
*  scikit-learns
*  streamlit
*  matplotlib

## Funcionamento

Através de um planilha em formato csv, que contêm tamanhos de pizzas e seus respectivos valores, a maquina através de uma análise consegue ver o padrão linear, a cada 2 cm de diâmetro a pizza aumenta 5 Reais, sendo assim consegue realizar um Predict do valor independentemente do diametro.

Dessa forma conseguimes realizar cálculos sem realmente colocar formulas no Programa.

A fórmula seria:
<br>
VALOR DA PIZZA = 5 x (DIÂMETRO/2)

<hr>

## Fotos do Sistema

![image](https://github.com/user-attachments/assets/b9c6b63c-5df3-48bc-9179-096787d81fb4)
<br>
Esse código é resposavel por carregar os dados da tabela CSV 
<hr>

![image](https://github.com/user-attachments/assets/9584acc4-5e49-4aea-8b6d-a50666ac40d6)
<br>
Esse código cria um gráfico com o eixo X representando o "diâmetro" das pizzas e o eixo Y representando o "preço", permitindo visualizar a relação entre essas duas variáveis. Assim podemos entender que existe uma relação proporcinal por que a linha é reta.
<hr>

![image](https://github.com/user-attachments/assets/1420e664-039f-46b6-a812-3f28a75d8065)
<br>
O treinamento acontece aqui, o código treina um modelo de regressão linear para prever o preço das pizzas com base no seu diâmetro.
<hr>

![image](https://github.com/user-attachments/assets/16385ece-5d1f-4ac3-8813-5c72a6f4a4c7)
<br>
O código faz uma previsão do preço de uma pizza com diâmetro de 50 cm, retornando o valor estimado.
<hr>

![image](https://github.com/user-attachments/assets/0bc4c8be-3156-4159-82ba-593b3867667d)
<br>
Esse bloco de código é reposável por criar uma interface gráfica utilizando a dependência do StremLit
<hr>

![image](https://github.com/user-attachments/assets/f6c7d14f-78e2-4c46-9398-1c94074b0acf)
<br>
Ao executar o código, o Streamlit automaticamente cria uma aplicação web local, que pode ser acessada no navegador
<hr>

## Para rodar a Aplicação

1. Instalar as dependências: Primeiro, instale as bibliotecas necessárias com o seguinte comando no terminal:
* pip install streamlit scikit-learn pandas

2. Fazer o Dowload de todo o Código, juntamente com o Arquivo CSV com os dados

3. Rodar o serviço Stremlit
* streamlit run previsao_pizza.py

* 4 Se a página Web nao se abrir automaticamente acesse o serviço com:
* geralmente http://localhost:8501
   










  
