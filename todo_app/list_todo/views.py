from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def list_index(req: HttpRequest) -> HttpResponse:
  
  print(f"HOST -> {req.headers.get('Host')}")

  return render(req, 'list_todo/index.html')
