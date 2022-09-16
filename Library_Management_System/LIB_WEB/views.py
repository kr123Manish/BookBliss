from django.shortcuts import render,HttpResponse,redirect
import requests
import json
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.cache import cache_control
# Create your views here.
@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.method=="POST":
        admin_email = request.POST["email"]
        # print("admin_email ",admin_email)
        admin_password = request.POST["password"]
        # print("admin_Password ",admin_password)
        url = "http://127.0.0.1:8000/admin/login"

        payload={'admin_email': admin_email,'admin_password': admin_password}
        files=[

        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        # print(response.text)
        data =  json.loads(response.text)
        print("data ::",data)
        if data == 'Password did not matched' or data == 'Admin is not present' :
            context={
                'email':admin_email,
                'password':admin_password,
                'error': data,
            }
            print("context ::",context)
            return render(request,"adminLogin.html",{'detail':context})
            # return HttpResponse(detail['email'])
        else:
            # return HttpResponse("<h1>Admin login sucessfully</h1>")
            url = "http://127.0.0.1:8000/book/retrieveall"

            payload={}
            files={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload, files=files)

            data = json.loads(response.text)
            request.session['admin_email'] = admin_email
            return render(request,"adminPage.html",{'books':data})
    return render(request,"adminLogin.html")

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Admin Register
def adminRegister(request):
    if request.method=="POST":
        admin_name = request.POST["name"]
        admin_email = request.POST["email"]
        admin_password = request.POST["password"]
        admin_confirm_password = request.POST["confirm_password"]
        if admin_password != admin_confirm_password:
            context={
                'name':admin_name,
                'email':admin_email,
                'password':admin_password,
                'confirm_password':admin_confirm_password,
                'error': "Password did not matched with Confirmed Password"
            }
            return render(request,"adminRegister.html",{'detail':context})
        else:
            url = "http://127.0.0.1:8000/admin/signup"

            payload={'admin_email': admin_email,
            'admin_password': admin_password,
            'admin_name': admin_name}
            files=[

            ]
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            data = json.loads(response.text)
            # print("data::",data['Status'])
            if data['Status']=='Already Present':
                context={
                    'name':admin_name,
                    'email':admin_email,
                    'password':admin_password,
                    'confirm_password':admin_confirm_password,
                    'error': "Admin already registered"
                }
                return render(request,"adminRegister.html",{'detail':context})
            else:
                # return HttpResponse("<h1>Admin Registered sucessfully</h1>")
                request.session['admin_email'] = admin_email
                url = "http://127.0.0.1:8000/book/retrieveall"

                payload={}
                files={}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload, files=files)

                data = json.loads(response.text)
                return render(request,"adminPage.html",{'books':data})
    return render(request,"adminRegister.html")

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# delete book
def deleteBook(request,book_id):
    if 'admin_email' in request.session:
        url = "http://127.0.0.1:8000/book/delete"

        payload={'book_id': book_id}
        files=[]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        data = json.loads(response.text)
        return render(request,"singlebook.html",{'details':data})
    else:
        redirect_url = "http://127.0.0.1:8000"
        return redirect(redirect_url)

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# retrive all book
def showAllBooks(request):
    if 'admin_email' in request.session:
        url = "http://127.0.0.1:8000/book/retrieveall"

        payload={}
        files={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload, files=files)

        data = json.loads(response.text)
        return render(request,"adminPage.html",{'books':data})
    else:
        redirect_url = "http://127.0.0.1:8000"
        return redirect(redirect_url)


@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addBook(request):
    if 'admin_email' in request.session:
        if request.method=="POST":
            Book_id = request.POST.get('book_id')
            Book_name = request.POST.get('book_name')
            Book_price = request.POST.get('book_price')
            Book_author = request.POST.get('book_author')
            Book_dateOfPublication = request.POST.get('book_dateOfPublication')
            Book_inlanguage = request.POST.get('book_inlanguage')
            
            url = "http://127.0.0.1:8000/book/newentry"

            payload={
            'book_id': Book_id,
            'book_name': Book_name,
            'book_price': Book_price,
            'book_author': Book_author,
            'book_dateOfPublication': Book_dateOfPublication,
            'book_inlanguage': Book_inlanguage}
            files=[

            ]
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            data = json.loads(response.text)
            return render(request,"singlebook.html",{'details':data})
        else:
            return render(request,'addnewbook.html')
    else:
        redirect_url = "http://127.0.0.1:8000"
        return redirect(redirect_url)


@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateBook(request,book_id):
    if 'admin_email' in request.session:
        if request.method=="POST":
            Book_id = book_id
            Book_name = request.POST.get('book_name')
            Book_price = request.POST.get('book_price')
            Book_author = request.POST.get('book_author')
            Book_dateOfPublication = request.POST.get('book_dateOfPublication')
            Book_inlanguage = request.POST.get('book_inlanguage')
            
            url = "http://127.0.0.1:8000/book/update"

            payload={
                'book_id': Book_id,
                'book_name': Book_name,
                'book_price': Book_price,
                'book_author': Book_author,
                'book_dateOfPublication': Book_dateOfPublication,
                'book_inlanguage': Book_inlanguage
            }
            # print("payload ===>",payload)
            files=[

            ]
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            
            data = json.loads(response.text)
            # print("data ===>",data)
            return render(request,"singlebook.html",{'details':data})
        else:
            url = "http://127.0.0.1:8000/book/singlebookInfo?book_id="+book_id

            payload={}
            files={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload, files=files)

            
            data = json.loads(response.text)
            book_price = data['book_price']
            book_price=book_price.split("Rs",1)[1]
            book_price=float(book_price[:-1])
            data['book_price']=book_price
            print("data :: ",book_price)
            return render(request,'updatebook.html',{'details':data})
    else:
        redirect_url = "http://127.0.0.1:8000"
        return redirect(redirect_url)

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    try:
        del request.session['admin_email']
        print("Deleted sessions...")
    except Exception as e:
        pass
    redirect_url = "http://127.0.0.1:8000"
    return redirect(redirect_url)

@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def studentView(request):
    if request.method=="POST":
        Book_Id = request.POST["book_id"]
        url = "http://127.0.0.1:8000/book/singlebookInfo?book_id="+Book_Id

        payload={}
        files={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        data = json.loads(response.text)
        print("data : ",data)
        if data!="Book Not found":
            return render(request,'singlebook.html',{'details':data})
        else:
            data={}
            data['error']=True
            data['book_id'] = Book_Id
            return render(request,'studentPage.html',{'details':data})
    else:
        return render(request,"studentPage.html")
