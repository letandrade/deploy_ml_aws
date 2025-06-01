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

**4.1 Criação e serialização do modelo**

Todo o processo de criação do modelo está disponível no notebook. Trata-se de um modelo de propensão ao absenteísmo de um funcionário em um dia de trabalho. 

Como o foco deste projeto é o deploy do modelo, não vou entrar em detalhes sobre o processo de modelagem. 

É importante dizer que o modelo foi criado e gerado um arquivo picle que será usado no deploy.

**4.2 Iniciando com o Lambda**

Logado na conta AWS e no console do Lambda, seguir os passos:

- Criar função;
- Criar do zero;
- Digitar nome da função (ex: api_predicao_diabetes_ml);
- Versão da linguagem Python 3.10.

  ![image](https://github.com/user-attachments/assets/eabdf9af-3525-4586-85b6-f6e8e0130407)

Neste momento, criei uma permissão, onde o Lambda possa acessar o S3 internamente. Então em permissões, segui os passos:

- Criar uma função a partir da política da AWS templates;
- Nome da função (ex: access_lambda_to_s3);
- Selecionar permissões de somente leitura de objetos do Amazon S3.

![image](https://github.com/user-attachments/assets/d776b37d-4957-45ef-8993-7c68ed024a65)

Com a função criada, escolhi fazer o deploy do código através de um arquivo zip armazenado no S3 pelo fato do arquivo zip ser maior que 10mb.

**Criando a função Lambda**

Agora o passo é criar um arquivo com o nome lambda_funcao.py, disponível no repositório. Basicamente, a função importa o modelo .pckl e faz a previsão via modelo.

O próximo passo é criar o pacote zip de implantação do Lambda, para este exemplo o nome será funcao.zip, disponível no repositório.

O pacote deve conter as dependências das bibliotecas pandas, sckitlearn e numpy, usadas para criação do modelo. E a função Python que escrevemos. É importante dizer que precisam estar no mesmo nível de estruturas de pastas.

**Deploy da função Lambda**

Com o zip criado, precisamos realizar o upload do mesmo em um bucket no S3, para este exemplo foi criado um bucket chamado modelo-producao-diabetes e nele feito o upload do pacote que contém a função Lambda, o function.zip e o arquivo do nosso modelo, chamado modelo.pkl. Lembrando que o bucket não precisa ser público.

![image](https://github.com/user-attachments/assets/79a7c99f-ef9a-4647-97ea-a7fd366b2093)


Para fazer o deploy da aplicação no Lambda precisamos do link do arquivo funcao.zip e depois no painel do Lambda deve escolher a opção “Fazer upload de um arquivo do Amazon S3”, colar o link no espaço destinado e salvar a função.

![1](https://github.com/user-attachments/assets/1a04b500-ce6e-41ba-ad26-e13198c3887c)

**Configurando o API Gateway**

Agora estamos na parte final, uma última configuração deve ser realizada. Disponibilizar a solução para o mundo externo ou interno, através de uma API.

Neste exemplo será utilizado uma API do tipo HTTP, que é muito simples de configurar.

Acesse o console do API Gateway e depois cliquei em API HTTP. Escolhi o nome e o tipo de integração, que no caso é com o Lambda. Quando selecionei Lambda, escolhi na lista a função desejada.

![image](https://github.com/user-attachments/assets/2c65c89f-b7d6-45f4-810c-9462d57c0eda)

No próximo passo, criei um endpoint chamado/predict e defini a requisição como sendo do tipo POST.

![image](https://github.com/user-attachments/assets/df39e133-7a89-4483-9bd9-3c2169b6d82e)

Avancei e finalizei os passos. A API foi criada com sucesso e a Amazon forneceu uma DNS para acessá-la.

![image](https://github.com/user-attachments/assets/1b3e4fb6-98d9-442e-84c9-f6a9d74e9762)

## **5.0 Resultados**

