# Flask-kubernetes

## Docker installation steps:
    1) sudo apt-get update
    2) sudo apt-get install \ca-certificates \curl \gnupg \lsb-release
    3) curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    4) echo \ "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyring docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    5) sudo apt-get update
    6) sudo apt-get install docker-ce docker-ce-cli containerd.io

## KubeCTL installation steps:
    1) curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux amd64/kubectl"
    2) curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
    3) echo "$(<kubectl.sha256) kubectl" | sha256sum --check
    4) sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    5) kubectl version --client
    6) kubectl cluster-info
    
    If you see a message similar to the following, kubectl is not configured correctly or is not able to connect to a Kubernetes cluster.
        The connection to the server <server-name:port> was refused - did you specify the right host or port?
    if you are intending to run a Kubernetes cluster on your laptop (locally), you will need a tool like Minikube to be installed first and then re-run the commands stated above.

## MiniKube installation steps:
    1) curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    2) sudo install minikube-linux-amd64 /usr/local/bin/minikube
    3) minikube start
    4) eval $(minikube docker-env)  #this code build image in Minikube
    5) minikube start

### After installation, build docker image:
    docker build -t flask-kubernetes .

### Deploy service and deployment to kubernetes:
    kubectl apply -f deployment.yaml

### Open minikube dashboard:
    minikube dashboard

### Run service(app):
    minikube service flask-test-service

### If the pods are unhealthy(red or orange):
    minikube tunnel
