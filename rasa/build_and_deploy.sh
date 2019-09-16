docker build -t 172.30.3.211:30003/rasa-cn .
docker push 172.30.3.211:30003/rasa-cn:latest
kubectl delete -f action.yml
kubectl delete -f rasa.yml
kubectl apply -f action.yml
kubectl apply -f rasa.yml