from django.db import models

# admin model
class AdminData(models.Model):
    admin_name = models.CharField(max_length=255)
    admin_email = models.CharField(max_length=255, blank=True, null=True)
    admin_password = models.CharField(max_length=100, blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'admindata'


# book model
class BookData(models.Model):
    book_id = models.CharField(max_length=255)
    book_name = models.CharField(max_length=455)
    book_price = models.CharField(max_length=255)
    book_author = models.CharField(max_length=455)
    book_dateOfPublication = models.CharField(max_length=455)
    book_inlanguage = models.CharField(max_length=455)
    
    class Meta:
        managed = True
        db_table = 'bookdata'