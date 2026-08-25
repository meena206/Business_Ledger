from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="customers"
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @property
    def total_credit(self):
        return sum(
            t.amount
            for t in self.transactions.all()
            if t.transaction_type == "CREDIT"
        )

    @property
    def total_debit(self):
        return sum(
            t.amount
            for t in self.transactions.all()
            if t.transaction_type == "DEBIT"
        )

    @property
    def balance(self):
        return self.total_credit - self.total_debit


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("CREDIT", "Credit"),
        ("DEBIT", "Debit"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return (
            f"{self.customer.name} - "
            f"{self.get_transaction_type_display()} - "
            f"{self.amount}"
        )