docker build . -t app-inference
docker tag app-inference dalbamm/240109-app-inference
docker push dalbamm/240109-app-inference
