from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import(
    HTTP_400_BAD_REQUEST,
#    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import MedicineSerializer
from medicine.models import Medicine
from django.shortcuts import get_object_or_404

# Create your views here.
#signup
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if username and password and email:
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'Signup successful'})
    else:
        return Response({'error': 'Invalid data'}, status=400)
    
#login
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'message': 'Login successful'}, status=HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=400)

    

# logout
@csrf_exempt
@api_view(["POST"])
def logout(request):
    request.user.auth_token.delete()

    return Response({"Sataus":"User Logout Successfully"},status=HTTP_200_OK)

# medicines list
@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def medicinelist(request):
    user = request.user
    medicines = Medicine.objects.all()
    if not user.is_authenticated:
        return Response({"Error":"User Need To Login"},status=HTTP_400_BAD_REQUEST)

    else:
        

        medicines_list = MedicineSerializer(medicines,many=True)

        return Response(medicines_list.data,status=HTTP_200_OK)    

#delete
@csrf_exempt
@api_view(["DELETE"])
@permission_classes((AllowAny,))
def delete(request,id):
    dele = Medicine.objects.filter(pk=id)
    dele.delete()
    return Response({"status":"Delete Sucessfully"},status=HTTP_200_OK)

#search
@csrf_exempt
@api_view(["GET"])

def search(request,mname):
    searchdetails = Medicine.objects.filter(mname=mname)
    search=MedicineSerializer(searchdetails,many=True)
    return Response(search.data,status=HTTP_200_OK)

#add
@csrf_exempt
@api_view(["POST"])

def add(request):
    
    serializer = MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status":"Medicine Added sucessfully"}, status=201)
    return Response(serializer.errors, status=400)
    

#update      
@csrf_exempt
@api_view(["PUT"])

def update(request, pk):
    instance = get_object_or_404(Medicine, pk=pk)
    serializer = MedicineSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
    

    
