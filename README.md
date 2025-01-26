# 사용방법

1. 계정 관련

1) 계정 목록
   gcloud auth list

2) 계정 전환
   gcloud auth login
   계정 선택을 위한 브라우저가 출력됨

3) 현재 계정의 액세스 토큰을 표시
   gcloud auth print-access-token
   [중요] GCP access-token은 공식적으로 디코딩할 수 있는 방법이 없음
   https://www.googlecloudcommunity.com/gc/Apigee/Need-to-decrypt-access-token-to-set-in-env-variable-before/m-p/490036
   [질문01] 계정을 변경하면 access-token도 변경해야하는데 변경하는 방법은?
   > 사실 작업은 프로젝트 내 cloud shell에서 진행하므로 계정을 변경할 일이 없음(있어도 토큰이 자동으로 변경됨)

2. 프로젝트 관련

1) 프로젝트 목록
   gcloud projects list

2) 현재 사용중인 프로젝트
   gcloud config get project

3) 프로젝트 변경
   gcloud config set project PROJECT_ID
   gcloud config set project gen-lang-client-0274842719
   - 권한이 없는 경우 아래와 같은 메시지 발생
     Are you sure you wish to set property [core/project] to gen-lang-client-0480088393?
     Do you want to continue (Y/n)? Y

3. 이미지 배포 프로세스

1) 환경변수 설정
   export PROJECT_ID=$(gcloud config get-value project)
   export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
   <!-- export REGION="REGION" -->

   export REGION="us-central1"
   gcloud config set compute/region $REGION

2) API 활성화
   gcloud services enable artifactregistry.googleapis.com

3) Artifact Repository(도커 이미지 관리 서비스) 내 repository 생성
   gcloud artifacts repositories create container-dev-web --repository-format=docker --location=$REGION
   [중요] --location 옵션은 필수임(안하면 오류 발생)

4) git clone https://github.com/dannykil/Vertex_AI.git

5) cd Vertex_AI

6) 생성
   <!-- gcloud container clusters create container-dev-cluster --zone="ZONE" -->

   docker build -t docker.dev.web/$PROJECT_ID/container-dev-web/web:tag1 .

7) 빌드
8) 배포

# 이슈정리

1. ModuleNotFoundError: No module named 'google'
   pip3 install --upgrade google-api-python-client
   https://stackoverflow.com/questions/36183486/importerror-no-module-named-google

2. ImportError: cannot import name 'discoveryengine_v1' from 'google.cloud' (unknown location)
   pip3 install google-cloud-discoveryengine

<!-- pip3 install google-cloud-storage(필요없음) -->
