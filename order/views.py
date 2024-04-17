from django.shortcuts import render

def order_detail(request, pk):
    return render(request, 'order/order_detail.html')
