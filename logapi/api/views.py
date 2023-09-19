from rest_framework import viewsets
from rest_framework.views import APIView, Response
from .serializer import *
from .models import *
from django.contrib.auth import login
import random
import datetime
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# from rest_framework import status


# Create your views here.
@api_view(["POST"])
@csrf_exempt
def log(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = Customers.objects.get(username=username, password=password)
            if user:
                print(user)
                if user.session is not None:
                    return Response(user.session)
                else:
                    randint = str(random.randint(1, 100))
                    user.session = randint
                    user.save()
                    return Response({"msg": randint})
            else:
                return Response("user not registerd")
        except:
            return Response({"msg": "failed"})


@api_view(["POST"])
@csrf_exempt
def Registr(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = Customers.objects.filter(username=username, password=password).exists()
        if user:
            # otp=request.data.get('otp')
            # otps=Customers.objects.get(otp=otp)
            print(user)
            return Response({"otp": "user already taken"})
        else:
            user = Customers.objects.create(username=username, password=password)
            randint = str(random.randint(1000, 9999))
            user.otp = randint
            user.save()
            return Response({"otp": user.otp})


@api_view(["POST"])
@csrf_exempt
def verify(request):
    if request.method == "POST":
        username = request.data.get("username")
        otp = request.data.get("otp")
        user = Customers.objects.filter(username=username, otp=otp).first()
        print(user)
        if user:
            print(user)
            user.status = True
            user.save()
            return Response({"msg": "user verified"})
        else:
            return Response({"msg": "try again..."})


# class CustView(APIView):
#     def post(self,request,*args,**kwargs):
#         ser=CustSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response({"msg":"OK"})
#         return Response({"msg":"FAILED"})


class ProductModelView(viewsets.ModelViewSet):
    model = Products
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    # http://127.0.0.1:8000/prod/

    def list(self, request, *args, **kwargs):
        allitems = Products.objects.all()
        if "ct_id" in request.query_params:
            allitems = allitems.filter(ct_id=request.query_params.get("ct_id"))

        # http://127.0.0.1:8000/prod/?ct_id=1

        if "br_id" in request.query_params:
            allitems = allitems.filter(br_id=request.query_params.get("br_id"))

        # http://127.0.0.1:8000/prod/?br_id=1

        ser = ProductSerializer(allitems, many=True)
        return Response(data=ser.data)

    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]


class categoryModelView(viewsets.ModelViewSet):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        allitems = Category.objects.all()
        if "ct_name" in request.query_params:
            allitems = allitems.filter(ct_name=request.query_params.get("ct_name"))
        ser = CategorySerializer(allitems, many=True)
        return Response(data=ser.data)


class BrandModelView(viewsets.ModelViewSet):
    model = Brand
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class BannerModelView(viewsets.ModelViewSet):
    model = Banner
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


# def get_brand(self,request,**kwargs):
#     br_name=kwargs.get("br_name")
#     brand=Brand.objects.get(br_name=br_name)
#     ser=BrandSerializer(brand)
#     return Response(data=ser.data)
# class categoryView(APIView):
#     def get(self,request,*args,**kwargs):
#         res=Category.objects.all()
#         ser=CategorySerializer(res,many=True)
#         return Response(data=ser.data)


# class ProductView(APIView):
#     def get(self,request,*args,**kwargs):
#         res=Products.objects.all()
#         ser=ProductSerializer(res,many=True)
#         return Response(data=ser.data)
#     def post(self,request,*args,**kwargs):
#         ser=ProductSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response({"msg":"Ok"})
#         else:
#             return Response({"msg":"FAILED"})


# class SpecificProView(APIView):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("pid")
#         item=Products.objects.get(id=id)
#         ser=ProductSerializer(item)
#         return Response(data=ser.data)
