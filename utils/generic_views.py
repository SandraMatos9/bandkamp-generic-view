# from rest_framework.views import  Request,Response, APIView
# from utils.mixin import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin

# class GenericApiView(APIView):
#     queryset=None
#     serializer_class=None
#     lookup_field = "pk"

# class ListApiView(GenericApiView, ListModelMixin):
#     def get(self, request:Request, *args, **kwargs) ->Response:
#         return super().list(request)

# class CreateApiView(GenericApiView, CreateModelMixin):
#     def post(self, request: Request) -> Response:
#         return super().create(request)
    
# #*****

# class RetrieveApiView(GenericApiView, RetrieveModelMixin):
#     def get(self, request: Request, *args, **kwargs) -> Response:
#         return super().retrieve(request, *args, **kwargs)
    

# class UpdateApiView(GenericApiView, UpdateModelMixin):
#     def patch(self, request: Request, *args, **kwargs) -> Response:
#         return super().update(request,*args,**kwargs)
    

# class DestroyApiView(GenericApiView, DestroyModelMixin):
#     def delete(self, request: Request, *args, **kwargs) -> Response:
#         return super().delete(request, *args, **kwargs)
    
# #****
    
# class ListCreateApiView(ListApiView,CreateApiView):
#     ...

# class RetrieveUpdateDestroyAPIView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     ...
