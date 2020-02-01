from httpy import HTTPy
from httpy.environment import global_environment


global_environment.set('endpoint', 'response-headers')

httpy_api = HTTPy.load('test_request.yml')
print(global_environment.get())
get_request_response = httpy_api.response_headers.run()

