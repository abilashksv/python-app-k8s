# Flask RESTful API example
_(This repo is part of our [Free Flask Tutorial](https://flask-tutorial.com))_

This repo shows how to create a simple RESTful API using the Flask web framework. Among the included features, you'll see how to:
* Return custom status codes and headers ⚡️
* Create resources using POST requests 📬
* Deleting resources using DELETE requests 📭
* Test the application using Flask's [test client](http://flask.pocoo.org/docs/latest/testing) 🔮

## Install guide

##### Clone the repo

```bash
$ git clone https://github.com/abilashksv/python-flask-k8s.git
$ cd python-flask-k8s
```

##### Create the Docker image for python app 1
```bash
change the value service_name line 18 to backend-(1 or 2 or 3) in the file api/_01_manual_response_class.py
create respective docker image for each modification
$ docker build -t "registry:5000/username/python-app(1 or 2 or 3)" .
change registry url above accordingly and push the docker image using docker push <image_name>
```

##### Install dependencies
```bash
$ 
```

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
add /etc/host entry for python-app.com with ip address of host where haproxy app is running
if using kubeadm enter the current host ip
```


## Test
curl --header "X-Message-Type: backend-2" -H "Content-Type: application/json" -d '{"username": "user1", "target":"backend-2"}'  http://python-app.com/hit_backend
```bash
```
