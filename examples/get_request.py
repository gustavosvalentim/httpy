from httpy import HTTPy


httpy_api = HTTPy.load('test_request.yml')
get_request_response = httpy_api.get_request.run()

print(get_request_response.content.decode('utf-8'))
