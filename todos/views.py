from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo


# Create your views here.


def list_todo_items(request):

    # fetch request for all todos
    context = {'todo_list': Todo.objects.all()}

    # returning the btained data as object
    return render(request, 'todos/todo_list.html', context)


def insert_todo_item(request: HttpRequest):

    # create operation adding new todotask
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')


def delete_todo_item(request, todo_id):
    # delete operation
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')
