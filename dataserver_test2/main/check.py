from os import path
from kubernetes import client, config

import ssl
import ipaddress

def main2():
    config = client.Configuration()

    config.api_key['authorization'] = open('/var/run/secrets/kubernetes.io/serviceaccount/token').read()
    config.api_key_prefix['authorization'] = 'Bearer'
    config.host = 'https://kubernetes.default'
    config.ssl_ca_cert = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
    config.verify_ssl=True

    api_client = client.CoreV1Api(client.ApiClient(config))
    api_response = api_client.list_namespaced_service(namespace="default")    

    j = 0
    flag = 0

    for i in api_response.items:
        if i.metadata.name == "jupyternb-svc":
            flag = 1

            try:
                ip = i.status.load_balancer.ingress[j].ip
                ipaddress.ip_address(ip)
            except:
                ip = "Pod / Service is not created yet. Creating Service needs some time. Please wait and try again."

            break
        j = j + 1
    
    if flag == 0:
        ip = "Pod / Service is not created yet. Please create Pod / Service first."

    return ip

    
if __name__ == '__main__':
    main2()