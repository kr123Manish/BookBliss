from django.shortcuts import render
from django.http.response import JsonResponse
from LIB_API.book_serializers import *
from django.views.decorators.csrf import csrf_exempt
from LIB_API.models import BookData

@csrf_exempt
def newEntry(request):
    if request.method == 'POST':
        Book_id = request.POST.get('book_id')
        Book_name = request.POST.get('book_name')
        Book_price = request.POST.get('book_price')
        Book_author = request.POST.get('book_author')
        Book_dateOfPublication = request.POST.get('book_dateOfPublication')
        Book_inlanguage = request.POST.get('book_inlanguage')
        try:
            book_details = BookData.objects.filter(book_id=Book_id).first()
            if(book_details):
                book_details_Serializer = book_Serializer(book_details,many=False)
                # print(book_details_Serializer.data)
                book_data = book_details_Serializer.data
                book_data['status']="Not Added, Book-Id Already Present"
                return JsonResponse(book_data,safe=False)
            else:
                newbook={}
                try:
                    
                    newbook['book_id'] = Book_id
                    newbook['book_name'] = Book_name
                    newbook['book_price'] = 'Rs '+Book_price+'/'
                    newbook['book_author'] = Book_author
                    newbook['book_dateOfPublication'] = Book_dateOfPublication
                    newbook['book_inlanguage'] = Book_inlanguage

                    book_details_Serializer = book_Serializer(data=newbook)
                    if book_details_Serializer.is_valid():
                        book_details_Serializer.save()
                        newbook['status']='Added'
                        return JsonResponse(newbook,safe=False)
                    else:
                        return JsonResponse("book_details_Serializer is not valid",safe=False)
                except Exception as e:
                    newbook['status']='Not Added'
                    return JsonResponse(newbook,safe=False)
        except Exception as e:
            # print("Error from server side ==> ",e)
            return JsonResponse("Something wents wrong",safe=False)
    return JsonResponse("newEntery endpoint",safe=False)



@csrf_exempt
def RetrieveAll(request):
    try:
        book_details = BookData.objects.all()
        book_details_Serializer = book_Serializer(book_details,many=True)
        # print(book_details_Serializer.data)
        book_data = book_details_Serializer.data
        return JsonResponse(book_data,safe=False)
    except Exception as e:
        return JsonResponse("Something wents wrong",safe=True)
    return JsonResponse("Retrieve all the books endpoint",safe=False)

@csrf_exempt
def Update(request):
    if request.method == 'POST':
        Book_id = request.POST.get('book_id')
        Book_name = request.POST.get('book_name')
        Book_price = request.POST.get('book_price')
        Book_author = request.POST.get('book_author')
        Book_dateOfPublication = request.POST.get('book_dateOfPublication')
        Book_inlanguage = request.POST.get('book_inlanguage')
        try:
            book_details = BookData.objects.filter(book_id=Book_id).first()
            if(book_details):
                try:
                    newbook={}
                    newbook['book_id'] = Book_id
                    newbook['book_name'] = Book_name
                    newbook['book_price'] = 'Rs '+Book_price+'/'
                    newbook['book_author'] = Book_author
                    newbook['book_dateOfPublication'] = Book_dateOfPublication
                    newbook['book_inlanguage'] = Book_inlanguage

                    book_details_Serializer = book_Serializer(instance=book_details,data=newbook)
                    if book_details_Serializer.is_valid():
                        book_details_Serializer.save()

                        updated_book_info_Serializer=book_Serializer(book_details,many=False)
                        book_data = updated_book_info_Serializer.data
                        book_data['status'] = "Updated"
                        return JsonResponse(book_data,safe=False)
                    else:
                        return JsonResponse("book_details_Serializer is not valid",safe=False)
                except Exception as e:
                    print("Book not updated ==>",e)
                    return JsonResponse("Book not Updated",safe=False)
                
            else:
                return JsonResponse("Book Not found",safe=False)
        except Exception as e:
            # print("Error from server side ==> ",e)
            return JsonResponse("Something wents wrong",safe=False)
    return JsonResponse("Update book endpoint",safe=False)

@csrf_exempt
def Delete(request):
    if request.method == 'POST':
        Book_id = request.POST.get('book_id')
        try:
            book_details = BookData.objects.filter(book_id=Book_id).first()
            if(book_details):
                book_details_Serializer = book_Serializer(book_details,many=False)
                # print(book_details_Serializer.data)
                book_data = book_details_Serializer.data
                try:
                    book_details.delete()
                    book_data['status'] = "Deleted"
                    return JsonResponse(book_data,safe=False)
                except Exception as e:
                    book_data['status'] = "Not Deleted"
                    return JsonResponse(book_data,safe=False)
            else:
                return JsonResponse("Book Not found",safe=False)
        except Exception as e:
            # print("Error from server side ==> ",e)
            return JsonResponse("Something wents wrong",safe=False)
    return JsonResponse("Delete book endpoint",safe=False)

# get single book info
@csrf_exempt
def singleBookInfo(request):
    if request.method == 'GET':
        Book_id = request.GET.get('book_id')
        # print("Book_id =======> ",Book_id)
        # return JsonResponse("Ready",safe=False)
        try:
            book_details = BookData.objects.filter(book_id=Book_id).first()
            book_details_Serializer = book_Serializer(book_details,many=False)
                    # print(book_details_Serializer.data)
            book_data = book_details_Serializer.data
            if book_data['book_name']:
                return JsonResponse(book_data,safe=False)
            else:
                return JsonResponse("Book Not found",safe=False)
        except Exception as e:
            # print("Error from server side ==> ",e)
            return JsonResponse("Something wents wrong",safe=False)
    return JsonResponse("Something wents wrong",safe=False)
        
