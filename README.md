# 사용방법

1. 계정 관련

1) 계정 목록
   gcloud auth list

2) 계정 전환(계정 선택을 위한 브라우저가 출력됨)
   gcloud auth login

3) 현재 계정의 액세스 토큰을 표시
   gcloud auth print-access-token
   [중요] GCP access-token은 공식적으로 디코딩할 수 있는 방법이 없음
   https://www.googlecloudcommunity.com/gc/Apigee/Need-to-decrypt-access-token-to-set-in-env-variable-before/m-p/490036
   [질문] 계정을 변경하면 access-token도 변경해야하는데 변경하는 방법은?

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

# 이슈정리

1. ModuleNotFoundError: No module named 'google'
   pip3 install --upgrade google-api-python-client
   https://stackoverflow.com/questions/36183486/importerror-no-module-named-google

2. ImportError: cannot import name 'discoveryengine_v1' from 'google.cloud' (unknown location)
   pip3 install google-cloud-discoveryengine

<!-- pip3 install google-cloud-storage(필요없음) -->
