from django.contrib import admin
import json
from .models import *
admin.site.index_title = 'Investment Portfolio Admin'
admin.site.site_header = 'Investment Portfolio'
admin.site.index_title = 'Investment Portfolio Site Administrator'

admin.site.register(Portfolio)
admin.site.register(FundTypes)


class ClientAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        # to do changes before the page loads selecting only admin user to use ForeignKey
        context['adminform'].form.fields['user'].queryset = User.objects.filter(is_staff=False)
        context['adminform'].form.fields['investor'].queryset = User.objects.filter(is_staff=True)
        return super(ClientAdmin, self).render_change_form(request, context, *args, **kwargs)

    list_display = ('user', 'shares', 'portfolio')
    list_filter = ('user', 'portfolio')


admin.site.register(Client, ClientAdmin)


def parse_obj(obj):
    obj_dict = {'total_injected': float(obj.total_injected),
                'total_asset': float(obj.total_asset),
                'shares': float(obj.shares),
                'cumul_realized': float(obj.cumul_realized),
                'nav_share': float(obj.nav_share),
                'cumul_variation': float(obj.cumul_variation),
                'set': float(obj.set)
             }
    return obj_dict


class FundAdmin(admin.ModelAdmin):

    def render_change_form(self, request, context, *args, **kwargs):
        # to do changes before the page loads selecting
        # only admin user to use ForeignKey
        context['adminform'].form.fields['user'].queryset = User.objects.filter(username=request.user.username)
        # context['adminform'].form.fields['fund_type'].queryset = FundTypes.objects.all()
        return super(FundAdmin, self).render_change_form(request, context, *args, **kwargs)

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
        portfolio = Portfolio.objects.all()
        # print(portfolio)
        response.context_data.update({'portfolios': portfolio})
        return response

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        response = super(FundAdmin, self).changeform_view(request, object_id=object_id,
                                                          form_url=form_url, extra_context=extra_context)
        return response


admin.site.register(Fund, FundAdmin)
