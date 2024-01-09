# 문자열 치환
IMAGE_REPOSITORY="dalbamm/240109-app-inference"
DEPLOYMENT_YAML="deployments.yaml"
VERSION=$(git rev-parse --short $1)

# echo $VERSION
docker build . -t app-inference
docker tag app-inference dalbamm/240109-app-inference:$VERSION
docker push dalbamm/240109-app-inference:$VERSION

