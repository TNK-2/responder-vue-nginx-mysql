import responder

api = responder.API()

@api.route("/api")
def hello_world(req, resp):
    resp.text = "hello world!!"

if __name__ == '__main__':
    api.debug = True
    api.run()