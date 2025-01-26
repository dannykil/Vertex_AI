# 간단한 텍스트 출력이므로 가장 가벼운 apline버전을 사용하였다.
FROM python:3.9-alpine			
RUN pip3 install flask
WORKDIR /root

# working directory를 지정했으므로 그 디렉토리인 . 을 잊지말고 꼭 입력해주자.
ADD test_api.py .
CMD ["python3", "test_api.py"]