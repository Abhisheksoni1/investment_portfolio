from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Fund(models.Model):
    fund_type = models.CharField(max_length=32, choices=[('crypto', 'Crypto'), ('stocks', 'Stock')])
    portfolio = models.ForeignKey(Portfolio)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    buying = models.DecimalField(max_digits=32, decimal_places=5)
    redemption = models.DecimalField(max_digits=32, decimal_places=5)
    dividends = models.DecimalField(max_digits=32, decimal_places=5)
    total_injected = models.DecimalField(max_digits=32, decimal_places=5)
    cash_balance = models.DecimalField(max_digits=32, decimal_places=5)
    cost = models.DecimalField(max_digits=32, decimal_places=5)
    market_value = models.DecimalField(max_digits=32, decimal_places=5)
    total_asset = models.DecimalField(max_digits=32, decimal_places=5)
    unrealized = models.DecimalField(max_digits=32, decimal_places=5)
    per_unrealized = models.DecimalField(max_digits=32, decimal_places=5)
    realized = models.DecimalField(max_digits=32, decimal_places=5)
    cumul_realized = models.DecimalField(max_digits=32, decimal_places=5)
    gross_nav = models.DecimalField(max_digits=32, decimal_places=5)
    expenses = models.DecimalField(max_digits=32, decimal_places=5)
    net_nav = models.DecimalField(max_digits=32, decimal_places=5)
    shares = models.DecimalField(max_digits=32, decimal_places=5)
    nav_share = models.DecimalField(max_digits=32, decimal_places=5)
    per_variation = models.DecimalField(max_digits=32, decimal_places=5)
    cumul_variation = models.DecimalField(max_digits=32, decimal_places=5)
    set = models.DecimalField(max_digits=32, decimal_places=5)
    set_var = models.DecimalField(max_digits=32, decimal_places=5)
    note = models.CharField(max_length=1000)

    class Meta:
        ordering = ('date', 'portfolio')

    def __str__(self):
        return self.fund_type + "_" + self.portfolio.name

