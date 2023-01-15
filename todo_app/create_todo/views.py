from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def create_index(req: HttpRequest) -> HttpResponse:

  print(f"HOST -> {req.headers.get('Host')}")

  return HttpResponse('create page')
