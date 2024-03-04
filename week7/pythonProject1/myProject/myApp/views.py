from django.shortcuts import render, redirect
from .models import Works, Lives, Product

def ques2(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        salary = request.POST['salary']

        street = request.POST['street']
        city = request.POST['city']

        new_works = Works.objects.create(name=name, company=company, salary=salary)
        new_works.save()

        new_lives = Lives.objects.create(name=name, street=street, city=city)
        new_lives.save()
        
        return redirect('/')
    else:
        return render(request, 'index.html')
    

def find_people(request):
    if request.method == 'POST':
        company = request.POST.get('companyF')
        if company:
            employees = Works.objects.filter(company=company)
            cities = []
            for emp in employees:
                temp = Lives.objects.filter(name=emp.name)
                if temp.exists():
                    cities.extend(temp.values_list('city', flat=True))
            print(cities)  # This prints list of cities of employees for debugging
            return render(request, 'employees.html', {'employees': employees, 'cities': cities})
        else:
            # Handle case where no company is provided
            return redirect('/')
    else:
        return redirect('/')
    
def ques4(request):
    all_products = Product.objects.all()
    return render(request, 'ques4.html', {'all_products': all_products})

def q4form(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        desc = request.POST['desc']
        new_product = Product.objects.create(title=title, price = price, description= desc)
        new_product.save()
        return redirect('/q4')
    else:
        return render(request, 'q4_form.html')