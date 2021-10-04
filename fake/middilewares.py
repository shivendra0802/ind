from django.http import response, HttpResponse

# def my_middileware(get_response):
#     print("One time Initialization")
#     def my_function(request):
#         print("This is before view")
#         response = get_response(request)
#         print("This is after view")
#         return response
#     return my_function    


class MyMiddileware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('one time initialization')

    def __call__(self, request):
        print('This is before view')
        response = self.get_response(request)
        print('This is after view') 
        return response       
    
    def process_view(request, *args, **kwargs):
        print("This is process before view")
        return HttpResponse("This is before view")


class MyExceptionMiddileware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('one time initialization')

    def __call__(self, request):
        print('This is before view')
        response = self.get_response(request)
        print('This is after view') 
        return response       
    
    def process_exception(self,request, exception):
        print("exception occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)

class MyTemplateResponseMiddileware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('one time initialization')
    
    def __call__(self, request):
        print('This is before view')
        response = self.get_response(request)
        print('This is after view') 
        return response       

    def process_templates_response(self,request,response):
        print('Process Template Response middileware')
        response.context_data['name']
        # print('')    
