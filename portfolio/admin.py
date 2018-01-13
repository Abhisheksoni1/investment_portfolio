from django.contrib import admin

# Register your models here.
from django.forms import model_to_dict
import json
from .models import *

admin.site.register(Profile)
admin.site.register(Portfolio)


def parse_obj(obj):
    obj_dict = {'total_injected': float(obj.total_injected),
                'total_asset': float(obj.total_asset),
                'shares': float(obj.shares),
                'cumul_realized': float(obj.cumul_realized),
                'nav_share': float(obj.nav_share),
                'cumul_variation': float(obj.cumul_variation)
             }
    return obj_dict


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
        return response

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        response = super(FundAdmin, self).changeform_view(request, object_id=object_id,
                                                          form_url=form_url, extra_context=extra_context)
        try:
            if object_id:
                fund_obj = Fund.objects.get(id=object_id)
                funds = Fund.objects.filter(portfolio=fund_obj.portfolio, user=fund_obj.user,
                                            fund_type=fund_obj.fund_type,
                                            date__lte=fund_obj.date.date())
                funds = funds[::-1]
                response.context_data.update({'data': funds[0]})
            else:
                funds = Fund.objects.all()
                portoliio = Portfolio.objects.all()
                crypto, stock = {}, {}
                for i in portoliio:
                    crypto_fund = funds.filter(portfolio=i, fund_type='crypto', user=request.user)
                    stock_fund = funds.filter(portfolio=i, fund_type='stocks', user=request.user)
                    if crypto_fund:
                        crypto_fund = crypto_fund[::-1]
                        crypto.update({i.name: parse_obj(crypto_fund[0])})
                    else:
                        crypto.update({i.name: ''})
                    if stock_fund:
                        stock_fund = stock_fund[::-1]
                        stock.update({i.name: parse_obj(stock_fund[0]).update({'set': float(stock_fund[0].set)})})
                    else:
                        stock.update({i.name: ''})
                # print(json.dumps(crypto))
                # print(json.dumps(stock))

                response.context_data.update({'crypto': crypto,
                                              'stocks': stock})

                # crypto_funds = ''
                # stock_funds = ''
                # crypto, crypto1, stock = None, None, None
                # print(crypto_funds)
                # print(stock_funds)
                # print(btc)
                # if crypto_funds:
                #     crypto = json.dumps({'key1': 'hello', 'key2': 2.0, 'key3': 3})
                #     crypto1 = json.dumps({'fund_type': crypto_funds[0].fund_type,
                #                          'portfolio': crypto_funds[0].portfolio.name,
                #                          'buying': float(crypto_funds[0].buying)})
                # if stock_funds:
                #     stock = json.dumps(model_to_dict(stock_funds[0]))
                # response.context_data.update({'stock': stock or '',
                #                               'crypto': crypto or '',
                #                               'test': crypto1})
                # print(response.context_data['crypto'])
        except Exception as e:
            print(e)
            return response
        return response


admin.site.register(Fund, FundAdmin)
