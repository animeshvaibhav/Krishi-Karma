from django.shortcuts import render
from . models import Crop,State,Farmer,District
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
#import urllib

# Create your views here.

def update_district(request):
    state = request.GET.get('state', None)
    districts = State.objects.get(name__iexact=state).districts.all()
    districts = [district.name for district in districts]
    data = {
        'districts': districts
    }
    print(districts)
    return JsonResponse(districts,safe = False)

def update_crop(request):
    district = request.GET.get('district', None)
    #crops = District.objects.get(name__iexact=district).crops.all()
    crops = Crop.objects.all()
    crops = [crop.name for crop in crops]
    data = {
        'crops': crops
    }
    return JsonResponse(crops,safe = False)    

def index(request):
    
    return render(request, 'krishiKarma/index.html')

def apply(request):
    # the whole content inside this if ....is to be written inside the a different view called farmer for rendering farmer.html which 
    # will then direct towards detail.html....and this html will have a view called detail to render the contents on detail.html... 
    
    states = State.objects.all()
    context = {
        'states' : states
    }    

    return render(request, 'krishiKarma/apply.html',context)

def dietician(request):

    return render(request, 'krishiKarma/dietician.html')


def donate(request):

    return render(request, 'krishiKarma/donate.html')

def login(request):

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(username=username,password=password)
            if user is not None :
                auth.login(request, user)
                return redirect('index')
            else:
                return redirect('login')    

        return  render(request, 'krishiKarma/login.html')    


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                return redirect('register') 
            else:
                print('*********************************************************')
                user = User.objects.create_user(username=username,password=password1,email=email)  
                user.save();     
                auth.login(request, user)

                return redirect('index')
        else:
            return redirect('register')

    return render(request, 'krishiKarma/login.html') 

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return redirect('index')       

# We will defife the view for farmerDetail.html for handling the invest and donate actions on that page 

def farmer(request):
    # the whole content inside this if ....is to be written inside the a different view called farmer for rendering farmer.html which 
    # will then direct towards detail.html....and this html will have a view called detail to render the contents on detail.html... 
    
    #farmer_list = farmers
    district = request.GET['district']
    crop = request.GET['crop']
    farmers = Farmer.objects.filter(crop__name=crop,location__name = district).all()
    
    paginator = Paginator(farmers, 4) # Show 4 farmers per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
            'page_obj': page_obj
        }
    return render(request, 'krishiKarma/farmer.html',context)


def detail(request, farmerId):
    
    farmer = Farmer.objects.get(id = farmerId)
    print(farmer)
    context={
            'farmer':farmer
        }    
    return render(request, 'krishiKarma/detail.html',context)