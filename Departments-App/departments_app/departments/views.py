from random import choice

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect


# # Най-базовото View withouth render
# def show_departments(request: HttpRequest, *args, **kwargs):
#     # body = f"Hallo this is my first HttpResponse"
#
#     print(request.method)
#     print(request.GET)
#     print(request.get_port())
#     print(request.get_host())
#     print(request.headers)
#     order_by = request.GET.get("order_by", "name")
#     body = f"path: {request.path}, args= {args}, kwargs= {kwargs}, order_by: {order_by}"
#     return HttpResponse(body)
#     # return HttpResponse()

def show_departments(request: HttpRequest, *args, **kwargs):
    context = {
        "method": request.method,
        "order_by": request.GET.get("order_by", "name"),
    }

    return render(request, "departments/all.html", context)


def show_departments_details(request: HttpRequest, department_id):
    body = f"path: {request.path}, id: {department_id}"
    return HttpResponse(body)

def redirect_to_first_department(request):
    possible_order_by = [
        "name",
        "age",
        "id",
    ]

    order_by = choice(possible_order_by)
    # return redirect(f"/departments/?order_by={order_by}")
    return redirect("show departments details", department_id=13)

    # to = "https://softuni.bg"
    # return redirect(to)

def show_not_found(request):
    status_code = 400
    # status_code = 404
    # if status_code == 404:
    #     return HttpResponseNotFound("Page not found!")
    # elif status_code == 400:
    #     return HttpResponseBadRequest("This is bad!")
    # return HttpResponse("Error", status=status_code)
    raise Http404("Not found!")