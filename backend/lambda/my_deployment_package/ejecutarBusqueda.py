import json
import requests


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    messages = event['Records']
    for message in messages:
        messageAttributes = message['messageAttributes']
        busqueda = messageAttributes['busquedaId']
        empresa = messageAttributes['empresaId']
        proyecto = messageAttributes['proyectoId']
        perfil = messageAttributes['perfilId']

        print("empresaId = " + empresa['stringValue'])
        print("proyectoId = " + proyecto['stringValue'])
        print("perfilId = " + perfil['stringValue'])
        print("busquedaId = " + busqueda['stringValue'])
        #response = requests.get("http://k8s-proyecto-ingressp-eb59205740-1747100398.us-east-1.elb.amazonaws.com/empresa/" + empresa['stringValue'] + "/proyecto/" + proyecto['stringValue'] + "/perfil/" + perfil['stringValue'] + "/busqueda/" + busqueda['stringValue'] + "/run")

    return "Finaliza" # Echo back the first key value
    #raise Exception('Something went wrong')
