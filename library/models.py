from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    year_published = models.DateTimeField('Date Published')
    copies = models.IntegerField()
    loan_type = models.IntegerField()

    def __str__(self):
        return self.book_name

class Customer(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    customer_surname = models.CharField(max_length=200)
    customer_age = models.IntegerField()
    customer_city = models.CharField(max_length=200)
    customer_books_loaned = models.IntegerField(default=0)

    def __str__(self):
        return self.customer_name + self.customer_surname

class Loan(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateTimeField('Loan Date')

