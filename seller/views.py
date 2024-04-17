from django.shortcuts import render, redirect
from .models import Food
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

# 자신이 판매하는 상품 리스트를 보여주기
# Food 전체에서 User가 판매자인 Food만 가져온다
# 전체 Food에서 내가 올린 food만 filter한다
# Food.objects.all().filter(조건)
# 상품 등록 기능

@login_required
def seller_index(request):
    foods = Food.objects.filter(user=request.user)
    context={
        'object_list': foods
    }
    return render(request, 'seller/seller_index.html', context)

@login_required
def add_food(request):
    # GET
    if request.method=='GET':
        return render(request, 'seller/seller_add_food.html')
    # POST
    elif request.method=='POST':
        # form에서 전달되는 각 값을 가져와서 DB에 저장
        # name, price, description
        user = request.user
        food_name = request.POST['name']
        food_price = request.POST['price']
        food_description = request.POST['description']

        # 이미지 저장 및 url 설정 내용
        fs=FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        
        Food.objects.create(user=user ,name=food_name, price=food_price , description=food_description, image_url=url)        
        return redirect('seller:seller_index')

@login_required
def food_detail(request, pk):
    object = Food.objects.get(pk=pk)
    context = {
        'object':object
    }
    return render(request, 'seller/seller_detail.html', context)

@login_required
def food_delete(request, pk):
    object = Food.objects.get(pk=pk)
    object.delete()
    return redirect('seller:seller_index')  