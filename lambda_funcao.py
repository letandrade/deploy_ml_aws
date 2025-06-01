
import pandas as pd
import pickle
import boto3
import json
import sklearn

def lambda_handler(event, context):
    # Permite acesso pela configuração de permissão que realizamos
    s3 = boto3.client('s3')
    
    # Nome do bucket e arquivo que serão carregados do S3
    bucket_name = 'modelo-abssenteismo'
    object_name = 'best_model_rl.pkl'
    
    # Carregando o arquivo do modelo em memória
    response = s3.get_object(Bucket=bucket_name, Key=object_name)
    model = pickle.loads(response['Body'].read())

    # Recebendo os parâmetros passados pelo cliente por POST
    data = json.loads(event['body'])  # Deve ser um dicionário com os nomes das features
    
    # Convertendo para DataFrame com nomes de colunas
    df = pd.DataFrame([data])  # Coloca dentro de uma lista para manter como 1 amostra

    # Realizando a predição
    prediction = model.predict(df)
    output = prediction[0]

    resposta = {'ABSSENTEISMO': int(output)}
    
    # Retornando a resposta para o cliente
    return {
        'statusCode': 200,
        'body': json.dumps(resposta)
    }
