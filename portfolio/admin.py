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
    change_form_template = 'admin/fund_change_form.html'

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

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        response = super(FundAdmin, self).changeform_view(request, object_id=object_id,
                         form_url=form_url, extra_context=extra_context)
        try:
            fund_obj = Fund.objects.get(id=object_id)
            funds = Fund.objects.filter(portfolio=fund_obj.portfolio, user=fund_obj.user, fund_type=fund_obj.fund_type,
                                        date__lte=fund_obj.date.date())
            funds = funds[::-1]
            response.context_data.update({'data': funds[0]})
        except Exception as e:
            print(e)
            return response
        return response





admin.site.register(Fund, FundAdmin)