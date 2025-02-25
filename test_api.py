from flask import Flask, request, jsonify
import socket
from datetime import datetime
import json
import random
from datetime import date, timedelta

from typing import List
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine
from google.cloud import storage
# from google.oauth2 import credentials
from google.oauth2 import service_account
# import logger

import logging
# import google.cloud.logging 


# Cloud Storage 클라이언트 초기화
storage_client = storage.Client()
bucket_name = "dev-unstructured-with-metadata"  # 실제 버킷 이름으로 변경
bucket = storage_client.bucket(bucket_name)
destination_blob_name = "/"
source_blob_name = "metadata/metadata_metadata_board.ndjson"

# bucket_name = "your-bucket-name"
# The path to your file to upload
# source_file_name = "local/path/to/file"
# The ID of your GCS object
# destination_blob_name = "storage-object-name"

# storage_client = storage.Client()
# bucket = storage_client.bucket(bucket_name)
# blob = bucket.blob(destination_blob_name)
# bucket = storage_client.bucket("dev-unstructured-with-metadata")
# blob = bucket.blob(destination_blob_name)
# source_blob_name = "Contents/20250212.pdf"


now = datetime.now()

app = Flask(__name__)

# logger.LoggerFactory.create_logger()

# lsof -i : 포트번호
# FLASK_APP=test_api.py flask run
@app.route('/api/example', methods=['POST'])
def example_post():
    # JSON 데이터를 가져옵니다.
    data = request.get_json()
    print(data)
    # logger.LoggerFactory._LOGGER.info('ERP AR 발행 Process 및 현재 위치 - 5 depth')
    # logger.LoggerFactory._LOGGER.info(data)

    # 데이터 유효성 검사
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    # 데이터 처리 로직
    name = data['name']
    age = data['age']

    # 응답 반환
    return jsonify({
        'message': f'Hello, {name}! Your age is {age}.'
    }), 200

@app.route('/api/getIP', methods=['GET'])
def example_get():
    host = socket.gethostbyname(socket.gethostname()) 
    print(host)
    # print(socket.gethostname())


    # 확인사항 및 추가작업 내용
    # 1) 각 핸들러/메서드 설정은 왜 하는지? + 없어도 되는지
    # 2) 통합검색 resource 정리 문서에 bigquery, logging 정리할 것
    # 3) 리소스, 어플리케이션 로그 외 다른 내용은 필터로 제외하기(제외하기 전 현차장님 확인)
    # 4) 로깅 정책

    # 5) log router sink에서 sink의 의미는 무엇인지
    # > 로그 데이터는 라우터를 통해 싱크로 흘러 들어가 저장되거나 처리됩니다.


    # 6) bigquery sink로 생성된 테이블들의 의미 확인(개인적으로 필터 가능한 테이블이 있는지까지 확인)
    # select * from `gen-lang-client-0274842719.logs.cloudaudit_googleapis_com_activity_20250218`;
    # > 생성 이유: Cloud Audit Logs의 Activity 로그를 저장(GCP 리소스에 대한 관리 작업 (생성, 수정, 삭제 등) 기록)

    # select * from `gen-lang-client-0274842719.logs.cloudaudit_googleapis_com_data_access_20250218`;
    # > 생성 이유: Cloud Audit Logs의 Data Access 로그를 저장(사용자 데이터에 대한 접근 기록)

    # select * from `gen-lang-client-0274842719.logs.cloudaudit_googleapis_com_system_event_20250218`;
    # > 생성 이유: Cloud Audit Logs의 System Event 로그를 저장(GCP 서비스 자체의 이벤트 기록)

    # select * from `gen-lang-client-0274842719.logs.cloudbuild_20250218`;
    # > 생성 이유: Cloud Build 작업 로그를 저장(빌드 작업 단계별 실행 결과, 오류 메시지 등)

    # select * from `gen-lang-client-0274842719.logs.cloudsql_googleapis_com_postgres_log_20250218`;
    # > 생성 이유: Cloud SQL for PostgreSQL 데이터베이스 로그를 저장(데이터베이스 서버의 동작 기록, 쿼리 실행 결과 등)

    # select * from `gen-lang-client-0274842719.logs.run_googleapis_com_stderr_20250218`;
    # > 생성 이유: Cloud Run 서비스에서 발생하는 표준 에러(stderr) 로그를 저장(애플리케이션 실행 중 발생한 오류 메시지)
    # >>> select textPayload, resource.labels.location, timestamp from `gen-lang-client-0274842719.logs.run_googleapis_com_stderr_20250219` where textPayload LIKE '%Application started.%' order by timestamp desc;

    # select * from `gen-lang-client-0274842719.logs.run_googleapis_com_varlog_system_20250218`;
    # > 생성 이유: Cloud Run 서비스의 시스템 로그를 저장(Cloud Run 플랫폼 자체의 동작 기록)


    # 7) 테이블들이 자동으로 생성되는데 네이밍을 정할 수 있는지?

    # 8) cloud auth log는 무엇인지
    # 

    # 9) UTC > KST 변경(Region - us-central1이 원인인 것 같음...)
    # asia-east1로 변경했는데도 UTC로 출력됨....데이터 조회하는 API개발 시 쿼리 변경
    



    # # Cloud Logging 클라이언트 초기화
    # client = google.cloud.logging.Client()

    # # 로거 설정
    # logger = logging.getLogger(__name__)
    # logger.setLevel(logging.INFO)  # 로그 레벨 설정 (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    # # Cloud Logging 핸들러 추가
    # handler = client.get_default_handler()
    # logger.addHandler(handler)

    # # 로그 메시지 기록
    # logger.info("Application started.")  # INFO 레벨 로그
    # print("This message will also be logged.")  # print() 문으로 출력된 메시지도 로그에 포함 가능

    # try:
    #     result = 10 / 0
    # except ZeroDivisionError as e:
    #     logger.exception("An error occurred: %s", e)  # 에러 발생 시 traceback과 함께 로그 기록

    # logger.warning("Application is running low on resources.")  # WARNING 레벨 로그
    # logger.critical("A critical error occurred. Shutting down.")  # CRITICAL 레벨 로그

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("This is an info mesage")

    # response = {
    #     "message": "Success",
    #     "timestamp": now.strftime('%Y-%m-%d %H:%M:%S')
    # }
    # return jsonify(response), 200  # JSON 응답과 200 OK 상태 코드 반환

    num_records=20
    start_date="2025-07-26"
    num_users=3

    data = []
    current_date = date.fromisoformat(start_date)
    users = [chr(ord('A') + i) for i in range(num_users)]  # 사용자 A, B, C... 생성
    events = ["Login", "View Product", "Add to Cart", "Purchase"]

    for _ in range(num_records):
        user = random.choice(users)
        event = random.choice(events)
        data.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "user": user,
            "event": event
        })

        # 날짜를 랜덤하게 증가시킴 (최대 3일)
        days_to_add = random.randint(0, 2)
        current_date += timedelta(days=days_to_add)

    return data
    # return host + "_" + now.strftime('%Y-%m-%d %H:%M:%S') + "_v9"



# def search_sample(
#     project_id: str,
#     location: str,
#     engine_id: str,
#     search_query: str,
# ) -> List[discoveryengine.SearchResponse]:

@app.route('/api/vertexai/search', methods=['POST'])
def search_sample():

    project_id = 'gen-lang-client-0274842719'
    location = 'global'
    # engine_id = 'app-unstructured-data_1737791181790'
    engine_id = 'app-unstructured-data_1738996146048'
    search_query = 'google'

    # data = request.get_json()

    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.SearchServiceClient(client_options=client_options)

    # The full resource name of the search app serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_config"

    # Optional - only supported for unstructured data: Configuration options for search.
    # Refer to the `ContentSearchSpec` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec
    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        # For information about snippets, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/snippets
        snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
            return_snippet=True
        ),
        # For information about search summaries, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries
        summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
            summary_result_count=5,
            include_citations=True,
            ignore_adversarial_query=True,
            ignore_non_summary_seeking_query=True,
            model_prompt_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec(
                preamble="YOUR_CUSTOM_PROMPT"
            ),
            model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                version="stable",
            ),
        ),
    )

    # Refer to the `SearchRequest` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
        page_size=10,
        content_search_spec=content_search_spec,
        query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
            condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
        ),
        spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
            mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
        ),
    )

    response = client.search(request)

    # responses = response.pages
    # for document in responses:
    #     # Process each document 
    #     print(document) 
    
    # print(response)

    # TypeError: The view function did not return a valid response. 
    # The return type must be a string, dict, list, tuple with headers or status, Response instance, or WSGI callable, but it was a SearchPager.
    # return response

    # TypeError: Object of type SearchPager is not JSON serializable
    # return jsonify(response)

    # TypeError: Object of type SearchPager is not JSON serializable
    # return json.dumps(response)

    # return [response]
    # return type(response)
    # return response.SearchPager
    # return response.SearchResponse
    # return search_pager_to_json(response)
    # return json.dumps(response.pages)

    # succeed
    # return str(response)
    # return str(response.pages)
    return search_pager_to_json(response.pages)
    
    


# def search_pager_to_json(search_pager: SearchPager) -> list[dict]:
# #   """
# #   Converts a SearchPager object to a list of dictionaries.

# #   Args:
# #     search_pager: The SearchPager object to convert.

# #   Returns:
# #     A list of dictionaries, where each dictionary represents a document.
# #   """

#   results = []

#   for document in search_pager:

#     document_dict = {
#         "content": document.content,
#         "id": document.id,
#         "metadata": document.metadata,
#         "mime_type": document.mime_type,
#         "score": document.score, 
#     }

#     results.append(document_dict)

#   return results



def search_pager_to_json(search_pager):

  results = []

  for document in search_pager:

    document_dict = {
        "content": str(document.results)
    }

    results.append(document_dict)

  return json.dumps(results[0])

# 방법2
# def search_pager_to_json(search_pager):

#   results = []

#   for depth1 in search_pager:
#     for depth2 in depth1.results:

#         document_dict = {
#             "id": str(depth2.id)
#         }

#     results.append(document_dict)

#   return json.dumps(results)

# 방법1
# def search_pager_to_json(search_pager):

#   results = []

#   for document in search_pager:

#     document_dict = {
#         "content": str(document.results)

#         # backup
#         # "content": document.content,
#         # "id": document.id,
#         # "metadata": document.metadata,
#         # "mime_type": document.mime_type,
#         # "score": document.score, 
#     }

#     results.append(document_dict)

#   return json.dumps(results)


@app.route('/eventarc/finalized', methods=['POST'])
def process_event():
    event = request.get_json()

    # CloudEvent 속성 확인
    print('Event Type:', event.get('type'))
    print('Event Source:', event.get('source'))
    print('request : ', request)
    print('request.headers : ', request.headers)

    file = event.get('data')

    if file and file.get('name') == 'metadata.ndjson':
        print('metadata.ndjson 파일이 업로드 요청되었습니다.')

        # 1. 기본 사용자 인증 정보 가져오기
        # creds, _ = credentials.default() # 오류
        # creds = service_account.Credentials.from_service_account_file(credentials_file_path)

        # # 2. 액세스 토큰 확인
        # access_token = creds.token

        # # 3. 이메일 계정 확인
        # email = creds.service_account_email

        # print('access_token : ', access_token)
        # print('email : ', email)

        # 원하는 작업 수행
        # Cloud Run response 데이터 가져오기 (예시)
        # response_data = {
        #     "message": "Data processed successfully",
        #     "result": file.get('name')
        # }

        # # JSON 데이터를 Cloud Storage에 저장
        # blob = bucket.blob("response.json")  # 저장할 파일 이름
        # blob.upload_from_string(json.dumps(response_data), content_type="application/json")
        # print(response_data)

        # blob = bucket.blob(source_blob_name)
        blob = bucket.blob("/metadata/metadata_metadata_board.ndjson")
        blob.download_to_filename("response.ndjson")
        # blob = bucket.blob("metadata")
        # blob.download_to_filename("metadata")

        return jsonify({'message': 'Event received and processed and file name is : {}'.format(file.get('name'))}), 200
    else:
        # metadata.ndjson 파일이 아닌 경우
        if file:
            print('업로드된 파일: ', file.get('name'))
        return jsonify({'message': 'Event received but not processed.'}), 200



if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')


# port 지정하는 방법 찾아야함(현재 5000포트 고정)