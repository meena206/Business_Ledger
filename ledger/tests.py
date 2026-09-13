from decimal import Decimal
from django.db.models import Q
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Customer, Transaction


class ModelsTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username="test", password="pass")
		self.customer = Customer.objects.create(owner=self.user, name="ACME", phone="12345")

	def test_transaction_and_balance(self):
		Transaction.objects.create(customer=self.customer, transaction_type="CREDIT", amount=Decimal("100.00"), date="2026-01-01")
		Transaction.objects.create(customer=self.customer, transaction_type="DEBIT", amount=Decimal("40.00"), date="2026-01-02")

		self.assertEqual(self.customer.total_credit, Decimal("100.00"))
		self.assertEqual(self.customer.total_debit, Decimal("40.00"))
		self.assertEqual(self.customer.balance, Decimal("60.00"))


class CustomerSearchQueryTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username="search-user", password="pass")

	def test_query_matches_substrings_case_insensitively(self):
		customer = Customer.objects.create(
			owner=self.user,
			name="Alice Johnson",
			phone="555-1234",
			city="Springfield",
		)

		results = Customer.objects.filter(owner=self.user).filter(
			Q(name__icontains="john") | Q(phone__icontains="1234") | Q(city__icontains="SPRING")
		)

		self.assertEqual(list(results), [customer])


class CustomerSearchViewTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username="owner", password="pass")
		self.other_user = User.objects.create_user(username="other", password="pass")
		self.customer = Customer.objects.create(
			owner=self.user,
			name="Alice Johnson",
			phone="555-1234",
			city="Springfield",
		)
		Customer.objects.create(
			owner=self.other_user,
			name="Alice Johnson",
			phone="555-1234",
			city="Springfield",
		)
		self.client.login(username="owner", password="pass")

	def test_search_filters_by_customer_fields_and_keeps_customer_ownership_isolated(self):
		response = self.client.get(reverse("customer_list"), {"search": "john"})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, str(self.customer.name))
		self.assertEqual(list(response.context["customers"]), [self.customer])
