from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction as db_transaction
from django.db.models import Q, Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomerForm, RegisterForm, TransactionForm
from .models import Customer, Transaction


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("dashboard")
    else:
        form = RegisterForm()

    return render(request, "ledger/register.html", {"form": form})


@login_required
def dashboard(request):
    customers = Customer.objects.filter(owner=request.user)
    transactions = Transaction.objects.filter(customer__owner=request.user)

    total_credit = (
        transactions.filter(transaction_type="CREDIT").aggregate(total=Sum("amount"))["total"]
        or Decimal("0")
    )

    total_debit = (
        transactions.filter(transaction_type="DEBIT").aggregate(total=Sum("amount"))["total"]
        or Decimal("0")
    )

    context = {
        "customer_count": customers.count(),
        "transaction_count": transactions.count(),
        "total_credit": total_credit,
        "total_debit": total_debit,
        "balance": total_credit - total_debit,
        "recent_transactions": transactions.select_related("customer")[:8],
    }
    return render(request, "ledger/dashboard.html", context)


@login_required
def customer_list(request):
    customers = Customer.objects.filter(owner=request.user)

    search = request.GET.get("search", "").strip()
    if search:
        customers = customers.filter(
            Q(name__icontains=search)
            | Q(phone__icontains=search)
            | Q(city__icontains=search)
        )

    return render(request, "ledger/customer_list.html", {"customers": customers, "search": search})


@login_required
def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        transaction_form = TransactionForm(request.POST)
        if form.is_valid() and transaction_form.is_valid():
            with db_transaction.atomic():
                customer = form.save(commit=False)
                customer.owner = request.user
                customer.save()
                new_transaction = transaction_form.save(commit=False)
                new_transaction.customer = customer
                new_transaction.save()
            messages.success(request, "Customer added successfully.")
            return redirect("customer_detail", customer_id=customer.id)
    else:
        form = CustomerForm()
        transaction_form = TransactionForm()

    return render(
        request,
        "ledger/customer_form.html",
        {"form": form, "transaction_form": transaction_form, "title": "Add Customer"},
    )


@login_required
def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id, owner=request.user)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully.")
            return redirect("customer_detail", customer_id=customer.id)
    else:
        form = CustomerForm(instance=customer)

    return render(
        request, "ledger/customer_form.html", {"form": form, "title": "Edit Customer", "customer": customer}
    )


@login_required
def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id, owner=request.user)

    if request.method == "POST":
        customer.delete()
        messages.success(request, "Customer deleted successfully.")
        return redirect("customer_list")

    return render(
        request,
        "ledger/customer_detail.html",
        {"customer": customer, "transactions": customer.transactions.all(), "confirm_delete": True},
    )


@login_required
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id, owner=request.user)
    transactions = customer.transactions.all()
    return render(request, "ledger/customer_detail.html", {"customer": customer, "transactions": transactions})


@login_required
def transaction_add(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id, owner=request.user)

    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.customer = customer
            transaction.save()
            messages.success(request, "Transaction added successfully.")
            return redirect("customer_detail", customer_id=customer.id)
    else:
        form = TransactionForm()

    return render(request, "ledger/transaction_form.html", {"form": form, "customer": customer})


@login_required
def ledger_history(request):
    transactions = Transaction.objects.filter(customer__owner=request.user).select_related("customer")

    search = request.GET.get("search", "").strip()
    transaction_type = request.GET.get("type", "").strip()

    if search:
        transactions = transactions.filter(
            Q(customer__name__icontains=search) | Q(description__icontains=search)
        )

    if transaction_type in ("CREDIT", "DEBIT"):
        transactions = transactions.filter(transaction_type=transaction_type)

    return render(
        request,
        "ledger/ledger_history.html",
        {"transactions": transactions, "search": search, "transaction_type": transaction_type},
    )


@login_required
def reports(request):
    transactions = Transaction.objects.filter(customer__owner=request.user)

    total_credit = (
        transactions.filter(transaction_type="CREDIT").aggregate(total=Sum("amount"))["total"] or Decimal("0")
    )

    total_debit = (
        transactions.filter(transaction_type="DEBIT").aggregate(total=Sum("amount"))["total"] or Decimal("0")
    )

    return render(
        request,
        "ledger/reports.html",
        {
            "total_credit": total_credit,
            "total_debit": total_debit,
            "balance": total_credit - total_debit,
            "transaction_count": transactions.count(),
        },
    )