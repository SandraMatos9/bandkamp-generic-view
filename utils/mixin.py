# #mixin é uma classe que não herda de ninguém. O único objetivo dela é ser herdada para passar métodos.
# from django.shortcuts import get_object_or_404
# from rest_framework.views import  Request,Response, status

# class ListModelMixin:

#     def list(self, request: Request, pk: int) -> Response:
#         queryset=self.queryset.all()
#         serializer= self.serializer_class(queryset,many=True)
#         return Response(serializer.data, status.HTTP_200_OK)

# class CreateModelMixin:
 
#     def create(self, request:Request) -> Response:
#         serializer= self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status.HTTP_201_CREATED)
        
# class RetrieveModelMixin:
#     def get(self, request:Request,*args:tuple,**kwargs: dict) -> Response:
#         lookup_field= kwargs.get(self.lookup_field, pk=lookup_field)
#         obj = get_object_or_404(self.queryset, pk=lookup_field)
#         serializer = self.serializer_class(obj)
#         return Response(serializer.data, status.HTTP_200_OK)

# class UpdateModelMixin:
#     def patch(self, request:Request,*args:tuple,**kwargs: dict) -> Response:
#         lookup_field= kwargs.get(self.lookup_field, pk=lookup_field)
#         obj = get_object_or_404(self.queryset, pk=lookup_field)
#         serializer = self.serializer_class(obj, request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)


# class DestroyModelMixin:
#     def delete(self, request:Request,*args:tuple,**kwargs: dict) -> Response:
#         lookup_field= kwargs.get(self.lookup_field)
#         obj = get_object_or_404(self.queryset,pk=lookup_field)
#         obj.delete()
#         return Response(status.HTTP_204_NO_CONTENT)

