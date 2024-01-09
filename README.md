# mnist-inference-app

## 1-1. 로컬 실행 방법(가상환경)
### 실행 조건
- python3 설치 필요

### Command
```
pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
cd app
pip install -r requirements.txt
python application.py
```
### Endpoint
- http://localhost:8000

## 1-2. 로컬 실행 방법(도커)
### 실행 조건
docker desktop 설치 필요

### Command
```
./build_local.sh && ./run.sh
```
### Endpoint
http://localhost:8000

# 세부 사항
[노션 페이지 참조(클릭))](https://primstryn.notion.site/CI-CD-b86b73e478c0422487f347d15685927e)
