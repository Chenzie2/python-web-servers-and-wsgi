from werkzeug.wrappers import Request, Response
# Function to handle incoming requests
@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    # RUn server for the one page application
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )
