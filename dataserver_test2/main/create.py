"""
Creates a Service using AppsV1Api from file jupyternb-svc.yaml.
"""

from os import path
from kubernetes import client, config
from tkinter import *

import ssl
import yaml
import time

def maindel():
    config = client.Configuration()

    config.api_key['authorization'] = open('/var/run/secrets/kubernetes.io/serviceaccount/token').read()
    config.api_key_prefix['authorization'] = 'Bearer'
    config.host = 'https://kubernetes.default'
    config.ssl_ca_cert = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
    config.verify_ssl=True

    try:
        api_client = client.CoreV1Api(client.ApiClient(config))
        resp = api_client.delete_namespaced_service(name="jupyternb-svc", namespace="default")
    except:
        pass

    try:
        api_client = client.AppsV1Api(client.ApiClient(config))
        resp = api_client.delete_namespaced_deployment(name="jupyternb-dp", namespace="default")
    except:
        pass

def maincre():
    config = client.Configuration()

    config.api_key['authorization'] = open('/var/run/secrets/kubernetes.io/serviceaccount/token').read()
    config.api_key_prefix['authorization'] = 'Bearer'
    config.host = 'https://kubernetes.default'
    config.ssl_ca_cert = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
    config.verify_ssl=True
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.

    # config.load_kube_config()
    with open(path.join(path.dirname(__file__), "jupyternb-dp.yaml")) as f:
        dep = yaml.safe_load(f)
        api_client = client.AppsV1Api(client.ApiClient(config))
        resp = api_client.create_namespaced_deployment(body=dep, namespace="default")
        s1 = "Deployment created. status=" + resp.metadata.name
    
    while 1:
        try:
            with open(path.join(path.dirname(__file__), "jupyternb-svc.yaml")) as f:
                dep = yaml.safe_load(f)
                api_client = client.CoreV1Api(client.ApiClient(config))
                resp = api_client.create_namespaced_service(body=dep, namespace="default")
                s1 = s1 + " Service created. status=" + resp.metadata.name
        except:
            pass
        else:
            break

    return s1

def main():
    maindel()

    time.sleep(3)

    return maincre()


if __name__ == '__main__':
    main()