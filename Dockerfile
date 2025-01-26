# 간단한 텍스트 출력이므로 가장 가벼운 apline버전을 사용하였다.
FROM python:3.9-alpine			
RUN pip3 install flask
# WORKDIR /root
WORKDIR /app
COPY . /app
# RUN cd /app/Vertex_AI
RUN pwd
RUN ls -al
# RUN FLASK_APP=test_api.py flask run

# working directory를 지정했으므로 그 디렉토리인 . 을 잊지말고 꼭 입력해주자.
# ADD test_api.py .
CMD ["python3", "test_api.py"]
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
# FLASK_APP=test_api.py flask run
# CMD ["FLASK_APP=test_api.py", "flask", "run"]
# docker build -t docker.dev.web/$PROJECT_ID/container-dev-web/web:tag1 .