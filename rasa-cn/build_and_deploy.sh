docker build -t 172.30.3.211:30003/rasa-cn .
docker push 172.30.3.211:30003/rasa-cn:latest
kubectl delete -f rasa.yml
kubectl apply -f rasa.yml

curl --request POST \
  --url http://rasa.leandata.top/webhooks/rest/webhook \
  --header 'content-type: application/json' \
  --data '{
    "message": "今天天气真好"
  }'