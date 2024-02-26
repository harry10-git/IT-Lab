from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


# 1) Develop a web application using Django framework to demonstrate the transfer of
# multiple parameters between web pages. User should be presented with a dropdown
# list containing car manufacturers, a text box which takes model name of the
# manufacturer and a submit button. On submitting the web page, the user is forwarded
# to a new page. This new page should display the selected car manufacturer name and
# the model name
def q1(request):
    if request.method == 'POST':
        company = request.POST['car-manufacturer']
        model = request.POST['model']
        return render(request, 'q1_res.html', {'company': company, 'model':model})
    else:
        return render(request, 'q1.html')


def q3(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']

        context = {
            'username': username,
            'email': email,
            'contact': contact,
        }

        return render(request, 'q3_res.html', context)
    else:
        return render(request, 'q3.html')


def q4(request):
    if request.method == 'POST':
        brand = request.POST['radio']
        mobile = 'mobile' in request.POST.getlist('mobile')
        laptop = 'laptop' in request.POST.getlist('laptop')
        quantity = request.POST['quantity']
        quantity = int(quantity)
       
        cost = 0
        if mobile is True:
            cost += 1000*quantity
        if laptop is True:
            cost += 10000*quantity

        context = {
            'cost': cost,
            'brand': brand,
            'laptop': laptop,
            'mobile': mobile
        }
       
        return render(request, 'q4_res.html', context)
    else:
        return render(request, 'q4.html')