from pprint import pprint


class EndHandler(object):

    def __init__(self):
        self.next_executor = None

    def handle_request(self, request):
        pprint("End")


class Handler1(object):

    def __init__(self):
        self.next_handler = EndHandler()

    def handle_request(self, request):
        request["header"] = "A"
        pprint(request)
        self.next_handler.handle_request(request)


class Handler2(object):

    def __init__(self):
        self.next_handler = EndHandler()

    def handle_request(self, request):
        request["auth"] = "pass"
        pprint(request)
        self.next_handler.handle_request(request)


def main_handler(handler, request):
    handler.handle_request(request)

