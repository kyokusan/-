from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.forms import UserformModel


def login(request):
    return render(request,"login.html")
def reg(request):
    if request.method=="GET":
        return render(request,"reg.html")
    else:
        data=request.POST
        form=UserformModel(data)
        if form.is_valid():
            pass
        else:
            context={"errors":form.errors}
            return render(request,"reg.html",context=context)

        # data=request.POST
        # form=UserformModel(data)
        # if form.is_valid():
        #     return HttpResponse("OK")
        # else:
        #     context={"errors":form.errors}
        #     return request(request,"reg.html",context=context)