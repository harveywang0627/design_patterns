class EndHandler(object):

    def __init__(self):
        self.next_executor = None

    def handle_request(self, request):
        print(request)


class Handler1(object):

    def __init__(self):
        self.next_handler = EndHandler()

    def handle_request(self, request):
        print(request)
        self.next_handler.handle_request(request)


class Handler2(object):

    def __init__(self):
        self.next_handler = EndHandler()

    def handle_request(self, request):
        print(request)
        self.next_handler.handle_request(request)


def main_handler(handler, request):

    handler.handle_request(request)


if __name__ == "__main__":

    hd = Handler1()

    current = hd
    current.next_handler = Handler2()

    main_handler(hd, {"request_info": True})

