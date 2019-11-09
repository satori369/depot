from goodslist.models import Goods_sort
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# 增加商品类别
def goodslist_addsort(request):

    if request.method == 'GET':
        # get获取到页面
        return render(request, 'goodslist_addsort.html')

    if request.method == 'POST':
        #收到页面提交来的信息
        spname = request.POST.get('spname')
        if not spname:
            result = {'code':10101,'error':'Please give me 商品类别名~'}
            return JsonResponse(result)

        spms = request.POST.get('spms')
        if not spms:
            result = {'code':10102,'error':'Please give me 商品描述~'}
            return JsonResponse(result)
        #查询有没有这个类别,有则不添加
        old_sps = Goods_sort.objects.filter(name=spname)
        if old_sps:
            result = {'code': 10103, 'error': 'The spname is already existed,商品类别已存在 !'}
            return JsonResponse(result)
        #判定完成,可以入库
        try:
            Goods_sort.objects.create(name=spname,introduce=spms)
        except Exception as e:
            #入库出现错误,返回页面商品已存在,后台打印错误类型方便排除
            print('----create error----')
            print(e)
            result = {'code': 10104, 'error': '添加商品失败,商品类别已存在 !!'}
            return JsonResponse(result)
        #完成入库,返回200给页面
        result = {'code': 200, 'data': 'code200 添加 ok'}
        return JsonResponse(result)

def goodslist_addsort_server(request):
    #xhr动态查询
    spname = request.GET.get('spname')
    #商品是否存在
    old_sps = Goods_sort.objects.filter(name=spname)
    #商品类别存在则返回1,返回提示和按钮禁用
    if old_sps:
        return HttpResponse('1')
    #商品类别可以添加返回0
    return HttpResponse('0')


# 增加商品
def goodslist_addinfo(request):



    return render(request, 'goodslist_addinfo.html')

# 获取全部  删除商品
# def goodslist(request):
#
#     top_all = Goods_sort.objects.all()
#
#     return render(request, 'goodslist_add.html')