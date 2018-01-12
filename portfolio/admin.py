from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Profile)
admin.site.register(Portfolio)


class FundAdmin(admin.ModelAdmin):
    list_display = ('fund_type', 'portfolio', 'user', 'cash_balance', 'cost', 'market_value', 'total_asset',
                    'realized', 'gross_nav', 'expenses', 'net_nav', 'shares',)
    list_filter = ('fund_type', 'portfolio', 'user')
    change_list_template = 'admin/fund_change_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super(FundAdmin, self).changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl']
        except (AttributeError, KeyError):
            return response

        return response


admin.site.register(Fund, FundAdmin)