from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
import time
from CeleryTask.tasks import sendDing
class MiddleWareTest(MiddlewareMixin):
    def process_request(self,request):
        request_ip=request.META['REMOTE_ADDR']
        if request_ip == '10.10.14.74':
            return HttpResponse('非法IP地址')

    # def process_view(self,request,callback,callback_args,callback_kwargs):
    #     print('i am process_view')
    #
    # def process_exception(self,request,exception):
    #     if exception:
    #         with open('ERROR_PATH','a') as f:
    #             now=time.strftime('%Y-%m-%d %h-%M-%S',time.localtime())
    #             content='[%s]:%s\n'%(now,exception)
    #             f.write(content)
    #             sendDing.delay(content)
    #         return HttpResponse('有错误出现，改一改代码<br> %s'%exception)
    #
    # def process_template_response(self,request,response):
    #     print('我是 process_template_response')
    #     return HttpResponse('hi hi hi')
    #
    # def process_response(self,request,response):
    #     print('我是 process_response')
    #     return response
    #
