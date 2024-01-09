VERSION=$(git rev-parse --short $1)

docker build . -t app-inference
docker tag app-inference dalbamm/240109-app-inference:$VERSION
docker push dalbamm/240109-app-inference:$VERSION

