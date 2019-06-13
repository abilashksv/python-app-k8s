# Flask RESTful API  example Kubernetes Deployment

## Install guide

##### Clone the repo

```bash
$ git clone https://github.com/abilashksv/python-flask-k8s.git
$ cd python-flask-k8s
```

##### Create the Docker image for python app 1
change the value service_name line 18 to backend-(1 or 2 or 3) in the file api/_01_manual_response_class.py
create respective docker image for each modification
```bash
$ docker build -t "registry:5000/username/python-app(1 or 2 or 3)" .
```
change registry url above accordingly and push the docker image using docker push <image_name>

##### Run the app
```bash
$ cd k8s/app
change the 3 docker image created in python-app*.yml respectively
$ kubectl apply -f .
```

## Running the load balancer

```bash
$ cd k8s/haproxy
$ kubectl create namespace ingress-controller
$ kubectl create configmap -n ingress-controller haproxy-templates --from-file=./files/haproxy.tmpl
$ kubectl create configmap -n ingress-controller haproxy-json-lua --from-file=./files/json.lua 
$ kubectl create configmap -n ingress-controller haproxy-json-test-lua --from-file=./files/test.lua
$ kubectl apply -f .
```
Edit the ingress-controller configmap and add the below entry
```bash
$ kubectl edit configmaps haproxy-ingress  --namespace=ingress-controller
data:
  config-frontend: |
    acl host-python-app.com var(txn.hdr_host) -i python-app.com python-app.com:80 python-app.com:443
    acl is_backend-1 req.hdr(X-Message-Type) backend-1
    acl is_backend-2 req.hdr(X-Message-Type) backend-2
    acl is_backend-3 req.hdr(X-Message-Type) backend-3
    use_backend default-python-app1-8080 if is_backend-1  host-python-app.com { var(txn.path) -m beg /hit_backend }
    use_backend default-python-app2-8080 if is_backend-2  host-python-app.com { var(txn.path) -m beg /hit_backend }
    use_backend default-python-app3-8080 if is_backend-3  host-python-app.com { var(txn.path) -m beg /hit_backend }
  config-global: lua-load /etc/haproxy/test.lua
```
add /etc/host entry for python-app.com with ip address of host where haproxy app is running
if using kubeadm enter the current host ip

## Test
curl --header "X-Message-Type: backend-2" -H "Content-Type: application/json" -d '{"username": "user1", "target":"backend-2"}'  http://python-app.com/hit_backend
```bash
```
