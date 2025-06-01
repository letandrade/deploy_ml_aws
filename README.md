<h1 align="center"> Deploy de um modelo de machine learning utilizando uma Arquitetura Serverless com AWS <br /> </h1>
<h3 align="center"> S3, Lambda e API Gateway</h3>

## **1.0 Visão geral**

Este projeto tem como objetivo demonstrar o deploy de um modelo de machine learning em uma arquitetura serverless utilizando os serviços da AWS: S3, Lambda e API Gateway.

O modelo desenvolvido é supervisionado e utiliza o algoritmo de Regressão Logística para realizar uma tarefa de classificação. Seu propósito é prever a probabilidade de absenteísmo de um funcionário em um dia de trabalho, auxiliando na identificação de padrões de ausência e possibilitando ações proativas por parte da empresa.

A proposta destaca não apenas a construção do modelo, mas também a importância de uma infraestrutura escalável, de baixo custo e com fácil manutenção, característica das arquiteturas serverless.

A base de dados utilizada neste projeto foi obtida no repositório da UCI, através do seguinte link:

🔗 [Absenteísmo no trabalho](https://archive.ics.uci.edu/dataset/445/absenteeism+at+work)

> ⚠️ **Observação:** O banco de dados foi criado com registros de absenteísmo no trabalho no período de julho de 2007 a julho de 2010 em uma empresa de courier no Brasil.

## **2.0 Objetivos técnicos**

Realizar o deploy de um modelo de classificação utilizando uma arquitetura serverless com os seguintes serviços da AWS:

Amazon S3: Armazenamento do modelo treinado e de arquivos auxiliares necessários para a execução da função.

AWS Lambda: Execução do modelo de forma escalável e sob demanda, sem necessidade de provisionamento de servidores.

API Gateway: Exposição de uma API REST para consumo externo, permitindo a comunicação entre o usuário e a função Lambda responsável pela inferência do modelo.

![image](https://github.com/user-attachments/assets/cdf9829a-a458-4ff8-8342-b1a5678d31b9)

## **3.0 Ferramentas utilizadas**

- Jupyter notebook: Ambiente de desenvolvimento.
- Python: Pré-processamento, modelagem e avaliação.
- Console AWS: S3, Lambda e API Gateway.

## **4.0 Desenvolvimento**



## **5.0 Resultados**

