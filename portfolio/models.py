from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Portfolio(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Fund(models.Model):
    fund_type = models.CharField(max_length=32, choices=[('crypto', 'Crypto'), ('stocks', 'Stock')])
    portfolio = models.ForeignKey(Portfolio)
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    buying = models.DecimalField(max_digits=32, decimal_places=5)
    redemption = models.DecimalField(max_digits=32, decimal_places=5)
    dividends = models.DecimalField(max_digits=32, decimal_places=5)
    total_injected = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    cash_balance = models.DecimalField(max_digits=32, decimal_places=5)
    cost = models.DecimalField(max_digits=32, decimal_places=5)
    market_value = models.DecimalField(max_digits=32, decimal_places=5)
    total_asset = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    unrealized = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    per_unrealized = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    realized = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    cumul_realized = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    gross_nav = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    expenses = models.DecimalField(max_digits=32, decimal_places=5)
    net_nav = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    shares = models.DecimalField(max_digits=32, decimal_places=5, default=1)
    nav_share = models.DecimalField(max_digits=32, decimal_places=5, default=1)
    per_variation = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    cumul_variation = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    set = models.DecimalField(max_digits=32, decimal_places=5)
    set_var = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    note = models.CharField(max_length=1000)

    class Meta:
        ordering = ('date', 'portfolio')

    def __str__(self):
        return self.fund_type + "_" + self.portfolio.name + "_" + self.user.username + "_" + str(self.date)

    def save(self, *args, **kwargs):
        data = Fund.objects.filter(portfolio=self.portfolio)
        data = data[::-1]
        total_injected_previous = 0
        total_asset_previous = 0
        cumul_previous = 0
        shares_previous = 1
        nav_share_previous = 1
        set_previous = 1
        sum_of_per_veriation = 0
        if len(data) > 0:
            total_injected_previous = data[0].total_injected
            total_asset_previous = data[0].total_asset
            cumul_previous = data[0].cumul_realized
            shares_previous = data[0].shares
            nav_share_previous = data[0].nav_share
            set_previous = data[0].set
            sum_of_per_veriation = sum(map(lambda i: i.per_variation, data))

            if set_previous == 0:
                set_previous = 1
            if nav_share_previous == 0:
                nav_share_previous = 1
            if shares_previous == 0:
                shares_previous = 1
        if self.fund_type == 'crypto':
            self.dividends = 0
            self.set = 0
            self.set_var = 0
        self.total_injected = total_injected_previous + self.buying - self.redemption - self.dividends
        self.total_asset = self.cash_balance + self.cost
        self.unrealized = self.market_value - self.cost
        self.per_unrealized = self.unrealized/self.cost
        self.realized = self.total_asset - total_asset_previous - self.buying + self.redemption + self.dividends
        self.cumul_realized = cumul_previous + self.realized
        self.gross_nav = self.cash_balance + self.market_value
        self.net_nav = self.gross_nav - self.expenses

        self.shares = shares_previous + ((self.buying - self.dividends) / nav_share_previous) - (self.redemption / nav_share_previous)
        self.nav_share = self.net_nav / self.shares
        self.per_variation = self.nav_share / nav_share_previous - 1
        self.cumul_variation = sum_of_per_veriation
        self.set_var = (self.set - set_previous)/set_previous
        if self.fund_type == "crypto":
            self.set_var = 0
        super(Fund, self).save(*args, **kwargs)
