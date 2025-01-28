from flask import Flask, request, jsonify
import socket
from datetime import datetime
import json

from typing import List
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

now = datetime.now()

app = Flask(__name__)

# FLASK_APP=test_api.py flask run
@app.route('/api/example', methods=['POST'])
def example_post():
    # JSON 데이터를 가져옵니다.
    data = request.get_json()
    print(data)

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

    return host + "_v2_" + now.strftime('%Y-%m-%d %H:%M:%S')



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
    engine_id = 'app-unstructured-data_1737791181790'
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


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')


# port 지정하는 방법 찾아야함(현재 5000포트 고정)