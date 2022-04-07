from urllib import response
from django.shortcuts import render
from .models import Todo
from rest_framework.views import APIView
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.


class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo_item = serializer.save()
            todo_item.url = reverse(
                'todo_one', args=[todo_item.id], request=request)
            todo_item.save()
            return Response(serializer.data, status=201)
        return Response(None, status=400)

    def delete(self, request):
        Todo.objects.all().delete()
        return Response(None, status=204)


class TodoOne(APIView):
    def get(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)
            serializer = TodoSerializer(todo)

            return Response(serializer.data, status=200)
        except Todo.DoesNotExist:
            return Response(None, status=400)

    def patch(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)
            serializer = TodoSerializer(
                data=request.data, instance=todo, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(None, status=400)
        except Todo.DoesNotExist:
            return Response(None, status=400)

    def delete(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)
            todo.delete()
            return Response(None, status=204)
        except Todo.DoesNotExist:
            return Response(None, status=400)
