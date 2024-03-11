from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Works, Lives, Product, Category, Page

from .models import Human
from .forms import HumanForm




def ques1(request):
    if request.method == 'POST':
        cat_name = request.POST.get('add1')  # Get the category name from the form
        try:
            category = Category.objects.get(name=cat_name)  # Get the category object
            category.likes += 1  # Increment likes
            category.save()  # Save the updated category
            print(category.likes)  # Print updated likes
        except Category.DoesNotExist:
            print("Category does not exist")
        return redirect('/q1')  # Redirect after processing POST request
    else:
        all_pages = Page.objects.all()
        all_categories = Category.objects.all()
        return render(request, 'q1.html', {'all_pages': all_pages, 'all_categories': all_categories})




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
    
def index(request):
    humans = Human.objects.all()
    form = HumanForm()
    return render(request, 'q5.html', {'humans': humans, 'form': form})

def update_human(request, human_id):
    human = Human.objects.get(pk=human_id)
    form = HumanForm(request.POST, instance=human)
    if form.is_valid():
        form.save()
    return redirect('index')

def delete_human(request, human_id):
    human = Human.objects.get(pk=human_id)
    human.delete()
    return redirect('index')