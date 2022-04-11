from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def doneTodo(request):
    done_todo_id = request.POST['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
