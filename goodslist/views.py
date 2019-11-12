from goodslist.models import Goods_sort,Goods_info
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# 增加商品类别  http://127.0.0.1:8000/goodslist/addsort/
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
            result = {'code': 10104, 'error': '添加商品类别失败,商品类别已存在 !!'}
            return JsonResponse(result)
        #完成入库,返回200给页面
        result = {'code': 200, 'data': 'code200 添加 ok'}
        return JsonResponse(result)

# xhr检测
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


# 增加商品 http://127.0.0.1:8000/goodslist/addinfo/
def goodslist_addinfo(request):

    if request.method == 'GET':
        # 给下拉列表返回对象[{'name':水果},{'name':手机},{'name':零食}]
        sorts = Goods_sort.objects.all()
        arr = []
        for sort in sorts:
            dic={}
            dic['name'] = sort.name
            arr.append(dic)

        return render(request, 'goodslist_addinfo.html',locals())

    if request.method == 'POST':
        # 收到页面提交来的信息
        splb = request.POST.get('splb')
        splbs = Goods_sort.objects.filter(name=splb)
        splb_id = int(splbs[0].id)
        spxx = request.POST.get('spxx')
        if not spxx:
            result = {'code':10105,'error':'Please give me 商品信息~'}
            return JsonResponse(result)
        spcd = request.POST.get('spcd')
        spdw = request.POST.get('spdw')
        spgg = request.POST.get('spgg')
        spbz = request.POST.get('spbz')
        spsl = request.POST.get('spsl')
        try:
            Goods_info.objects.create(goods_sort_id=splb_id,name=spxx,area=spcd,unit=spdw,spec=spgg,remark=spbz,number=spsl)
        except Exception as e:
            #入库出现错误,返回页面商品已存在,后台打印错误类型方便排除
            print('----create error----')
            print(e)
            result = {'code': 10106, 'error': '添加商品信息失败,请确认信息后重试 !!'}
            return JsonResponse(result)
        #完成入库,返回200给页面
        result = {'code': 200, 'data': 'code200 添加 ok'}
        return JsonResponse(result)

# 获取全部商品http:127.0.0.1:8000/goodslist/all/
def goodslist(request):

    print('获取全部商品 ok')
    goods_all = Goods_info.objects.all()

    return render(request, 'goodslist.html', locals())

# 删除商品#http:127.0.0.1:8000/goodslist/delete/
def goodslist_delete(request,goods_id):

    try:
        upd = Goods_info.objects.get(id=goods_id)
        upd.delete()
    except Exception as e:
        # 删除商品出现错误,后台打印错误类型方便排除
        print('----delete error----')
        print(e)
        return HttpResponse('删除商品信息失败,请确认信息后重试 !!')

    return HttpResponseRedirect('/goodslist/all/')