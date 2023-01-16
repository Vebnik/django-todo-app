from django.http import HttpResponse, HttpRequest
import json

# models
from .models import TodoItem

def get_todo(req: HttpRequest) -> HttpResponse:
  if req.method == 'GET':

    data = TodoItem.objects.all()
    
    return HttpResponse(json.dumps({'ok': True, 'message': [item.to_dict() for item in data]}, default=str))
  return HttpResponse(json.dumps({'ok': False, 'message': 'Not allowed method'}))
