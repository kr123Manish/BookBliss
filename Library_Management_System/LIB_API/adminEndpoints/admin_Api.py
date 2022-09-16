from django.shortcuts import render
from django.http.response import JsonResponse
from LIB_API.admin_serializers import *
from django.views.decorators.csrf import csrf_exempt
from LIB_API.models import AdminData

@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        name = request.POST.get('admin_name')
        email = request.POST.get('admin_email')
        password = request.POST.get('admin_password')
        # print("admin_name => ",name)
        # print("admin_email => ",email)
        # print("admin_password => ",password)
        try:
            #for get all data
            # admin_details = AdminData.objects.all()
            # admin_details_Serializer = signUp_Serializer(admin_details,many=True)
            # print(admin_details_Serializer.data)
            # return JsonResponse(admin_details_Serializer.data,safe=False)
            admin_details = AdminData.objects.filter(admin_email=email).first()
            if(admin_details):
                admin_details_Serializer = signUp_Serializer(admin_details,many=False)
                # print(admin_details_Serializer.data)
                admin_data = admin_details_Serializer.data
                admin_data['Status']="Already Present"
                return JsonResponse(admin_data,safe=False)
            else:
                # print("Admin not present")
                # return JsonResponse("Admin not present",safe=False)
                try:
                    newAdmin={}
                    newAdmin['admin_name']=name
                    newAdmin['admin_email']=email
                    newAdmin['admin_password']=password
                    # print("newAdmin",newAdmin)
                    admin_details_Serializer = signUp_Serializer(data=newAdmin)
                    if admin_details_Serializer.is_valid():
                        admin_details_Serializer.save()
                        newAdmin['Status']='New Admin Added'
                        return JsonResponse(newAdmin,safe=False)
                    else:
                        return JsonResponse("admin_details_Serializer is not valid",safe=False)
                except Exception as e:
                    return JsonResponse("New Admin Does not Added",safe=False)
                

        except Exception as e:
            # print("Error from server side ==> ",e)
            return JsonResponse("Something wents wrong",safe=False)
        
        
    return JsonResponse("signUp Endpoint",safe=False)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('admin_email')
        password = request.POST.get('admin_password')
        # print("admin_email => ",email)
        # print("admin_password => ",password)
        try:
            admin_details = AdminData.objects.filter(admin_email=email).first()
            if(admin_details):
                admin_details_Serializer = signUp_Serializer(admin_details,many=False)
                # print(admin_details_Serializer.data)
                admin_data = admin_details_Serializer.data
                admin_data['Status']="Present"
                if(admin_data['admin_password']==password):
                   return JsonResponse(admin_data,safe=False)
                else:
                    return JsonResponse("Password did not matched",safe=False)
            else:
                # print("Admin not present")
                return JsonResponse("Admin is not present",safe=False)
                
                

        except Exception as e:
            # print("Error from server side ==> ",e)
            return JsonResponse("Something wents wrong",safe=False)

    return JsonResponse("login Endpoint",safe=False)


    
