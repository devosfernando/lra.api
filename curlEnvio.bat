@echo off

curl -H "Content-Type: application/json" -X POST http://localhost:8080/dispacher/notification/topic -d "{\"registrationTopic\":\"weather\"}"

