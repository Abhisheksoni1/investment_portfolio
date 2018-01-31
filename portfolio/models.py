from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Portfolio(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FundTypes(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shares = models.DecimalField(max_digits=32, decimal_places=4, default=0)
    portfolio = models.ForeignKey(Portfolio)
    nav = models.DecimalField(default=0, max_digits=32, decimal_places=4)
    value = models.DecimalField(decimal_places=4, max_digits=32, default=0)
    investor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investor')

    def __str__(self):
        return self.user.first_name + self.portfolio.name


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Fund(models.Model):
    fund_type = models.ForeignKey(FundTypes)
    portfolio = models.ForeignKey(Portfolio)
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    buying = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    redemption = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    dividends = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    total_injected = models.DecimalField(max_digits=32, decimal_places=5)
    cash_balance = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    cost = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    market_value = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    total_asset = models.DecimalField(max_digits=32, decimal_places=5)
    unrealized = models.DecimalField(max_digits=32, decimal_places=5)
    per_unrealized = models.DecimalField(max_digits=32, decimal_places=5)
    realized = models.DecimalField(max_digits=32, decimal_places=5)
    cumul_realized = models.DecimalField(max_digits=32, decimal_places=5)
    gross_nav = models.DecimalField(max_digits=32, decimal_places=5)
    expenses = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    net_nav = models.DecimalField(max_digits=32, decimal_places=5)
    shares = models.DecimalField(max_digits=32, decimal_places=5)
    nav_share = models.DecimalField(max_digits=32, decimal_places=5)
    per_variation = models.DecimalField(max_digits=32, decimal_places=5)
    cumul_variation = models.DecimalField(max_digits=32, decimal_places=5)
    set = models.DecimalField(max_digits=32, decimal_places=5, default=0)
    set_var = models.DecimalField(max_digits=32, decimal_places=5)
    note = models.CharField(max_length=1000, blank=True)

    class Meta:
        ordering = ('date', 'portfolio')

    def __str__(self):
        return "_" + self.portfolio.name + "_" + self.user.username + "_" + str(self.date)

    # def save(self, *args, **kwargs):
    #
    #     data = Fund.objects.filter(portfolio=self.portfolio, user=self.user, fund_type=self.fund_type,
    #                                date__lte=self.date.date())
    #
    #     data = data[::-1]
    #     print(data)
    #     total_injected_previous = 0
    #     total_asset_previous = 0
    #     cumul_previous = 0
    #     shares_previous = 1
    #     nav_share_previous = 1
    #     set_previous = 1
    #     sum_of_per_veriation = 0
    #     if data:
    #         total_injected_previous = data[0].total_injected
    #         total_asset_previous = data[0].total_asset
    #         cumul_previous = data[0].cumul_realized
    #         shares_previous = data[0].shares
    #         nav_share_previous = data[0].nav_share
    #         set_previous = data[0].set
    #         sum_of_per_veriation = sum(map(lambda i: i.per_variation, data))
    #
    #         if set_previous == 0:
    #             set_previous = 1
    #         if nav_share_previous == 0:
    #             nav_share_previous = 1
    #         if shares_previous == 0:
    #             shares_previous = 1
    #     if self.fund_type == 'crypto':
    #         self.dividends = 0
    #         self.set = 0
    #         self.set_var = 0
    #     self.total_injected = total_injected_previous + self.buying - self.redemption - self.dividends
    #     self.total_asset = self.cash_balance + self.cost
    #     self.unrealized = self.market_value - self.cost
    #     self.per_unrealized = self.unrealized/self.cost
    #     self.realized = self.total_asset - total_asset_previous - self.buying + self.redemption + self.dividends
    #     self.cumul_realized = cumul_previous + self.realized
    #     self.gross_nav = self.cash_balance + self.market_value
    #     self.net_nav = self.gross_nav - self.expenses
    #
    #     self.shares = shares_previous + ((self.buying - self.dividends) / nav_share_previous) - (self.redemption / nav_share_previous)
    #     self.nav_share = self.net_nav / self.shares
    #     self.per_variation = self.nav_share / nav_share_previous - 1
    #     if nav_share_previous == 1:
    #         self.per_variation = 0.0
    #     self.cumul_variation = sum_of_per_veriation + self.per_variation
    #     self.set_var = (self.set - set_previous)/set_previous
    #     if self.fund_type == "crypto":
    #         self.set_var = 0
    #     super(Fund, self).save(*args, **kwargs)
    #     # after saving the record update next record in the db to maintain changes
    #     try:
    #         d = Fund.objects.filter(portfolio=self.portfolio, user=self.user, fund_type=self.fund_type)
    #         index = list(d).index(self)
    #         d[index+1].save()
    #     except Exception as e:
    #         print(e)
    #         return
