#!/usr/bin/python3
# coding: UTF-8

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import sys
import json

responses = []
response = {"id": 1, "deadline": "2019-06-11T14:00:00+09:00", "title": "Report submission", "memo": ""}
response2 = {"id": 2, "deadline": "2019-06-11T14:00:00+09:00", "title": "222", "memo": ""}
responses.append(response)
responses.append(response2)

class RequestHandler(BaseHTTPRequestHandler):

    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path_elements = parsed_path.path.split('/')[1:]

        #APIから外れている
        if path_elements[0] != 'api' or path_elements[1] != 'v1' or path_elements[2] != 'todo':
            self.send_response(404)
            self.end_headers()
            return
        

        #全取得の条件分岐
        if len(path_elements)==3:
            self.send_response(200)
            self.end_headers()

            #全リストを作成
            all_responses = {"events":responses}

            responseBody = json.dumps(all_responses)
            self.wfile.write(responseBody.encode('utf-8'))
            return

        #idが存在しない
        if  int(path_elements[3]) > len(responses):
            self.send_response(404)
            self.end_headers()
            return

        #1つ取得
        try:
            self.send_response(200)
            self.end_headers()

            responseBody = json.dumps(responses[int(path_elements[3])-1])

            self.wfile.write(responseBody.encode('utf-8'))
            return
        except Exception as e:
            print(e)
            self.send_response(500)
            self.end_headers()
            return


    def do_POST(self):
        parsed_path = urlparse(self.path)
        path_elements = parsed_path.path.split('/')[1:]


        #APIから外れている
        if path_elements[0] != 'api' or path_elements[1] != 'v1' or path_elements[2] != 'todo':
            self.send_response(400)
            self.end_headers()
            return
        
        #json取得
        content_len=int(self.headers.get('content-length'))
        requestBody = json.loads(self.rfile.read(content_len).decode('utf-8'))


        #titleがない
        if 'title' not in requestBody:
            self.send_response(400)
            self.end_headers()

            post_response = {"status": "failure", "message": "no title"}
            responseBody = json.dumps(post_response)
            self.wfile.write(responseBody.encode('utf-8'))
            
            return
        
        #deadlineがない
        if 'deadline' not in requestBody:
            self.send_response(400)
            self.end_headers()

            post_response = {"status": "failure", "message": "no deadline"}
            responseBody = json.dumps(post_response)
            self.wfile.write(responseBody.encode('utf-8'))
            
            return
        
        #memoがない
        if 'memo' not in requestBody:
            self.send_response(400)
            self.end_headers()

            post_response = {"status": "failure", "message": "no memo"}
            responseBody = json.dumps(post_response)
            self.wfile.write(responseBody.encode('utf-8'))
            
            return
  
        try:
            self.send_response(200)
            self.end_headers()

            add_json_data = {}
            add_json_data["id"] = len(responses)+1
            add_json_data.update(requestBody)

            #requestBody["id"] = len(responses)
            responses.append(add_json_data)

            post_response = {"status": "success", "message": "registered", "id": len(responses)}
            responseBody = json.dumps(post_response)
            self.wfile.write(responseBody.encode('utf-8'))
            return
        except Exception as e:
            print(e)
            self.send_response(500)
            self.end_headers()
            return

def main():
    print ("server starting")
    sys.stderr.write("test\n")
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
