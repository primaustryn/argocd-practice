# 문자열 치환
IMAGE_REPOSITORY="dalbamm/240109-app-inference"
DEPLOYMENT_YAML="deployments.yaml"
VERSION=$(git rev-parse --short $1)
# echo $VERSION
# docker build . -t app-inference
# docker tag app-inference dalbamm/240109-app-inference:$VERSION
# docker push dalbamm/240109-app-inference:$VERSION


# sed를 사용하여 파일 내에서 문자열 치환
git clone git@github.com:primaustryn/argocd-k8s-configs.git
cd argocd-k8s-configs && sed -i "s/$IMAGE_REPOSITORY/$IMAGE_REPOSITORY:$VERSION/g" $DEPLOYMENT_YAML
git add $DEPLOYMENT_YAML && git commit -m "update commit hash: $VERSION($DEPLOYMENT_YAML)"
git push origin main
