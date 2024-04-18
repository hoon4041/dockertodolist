from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import TodoItem

def index(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todo_items': todo_items})

def add_todo_item(request):
    due_date = request.GET.get('due_date')
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date')
        TodoItem.objects.create(title=title, description=description, due_date=due_date)
        return redirect('calendar_view')
    
    return render(request, 'todo/add_todo_item.html', {'due_date': due_date})

def toggle_todo_item(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('index')

def calendar_view(request):
    # 모든 To-do 항목을 JSON 형식으로 캘린더에 전달할 이벤트 목록을 생성합니다.
    todo_items = TodoItem.objects.all()
    events = []
    for item in todo_items:
        if item.due_date:
            events.append({
                'title': item.title,
                'start': item.due_date.isoformat(),
                'url': f'/toggle/{item.id}/'  # 각 항목을 토글하는 URL
            })

    return render(request, 'todo/calendar.html', {'events': events})