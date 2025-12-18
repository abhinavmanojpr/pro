from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# 1️⃣ Display all to-do items
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list.html', {'todos': todos})

# 2️⃣ Create new to-do
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/form.html', {'form': form})

# 3️⃣ Update existing to-do
def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/form.html', {'form': form})

# 4️⃣ Delete to-do
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')