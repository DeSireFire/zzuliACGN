from django.contrib import admin
from .models import *
# Register your models here.
class R_typeAdmin(admin.ModelAdmin):
    list_display = ['id','R_title']
class R_infoAdmin(admin.ModelAdmin):
    '''
    用户查询在admin界面中的显示
    '''
    list_per_page = 30
    list_display = [
    'rdName',
    'rdUpTime',
    'rdSize',
    'rdUpNum',
    'rdDownloadNum',
    'rdInfo',
    'rdOK',
    'rdURLS',
    'rdType',
    'isdelete',
    ]
    # list_display = [
    #     'a_i_u_e_o',
    #     'ka_ki_ku_ke_ko',
    #     'sa_shi_su_se_so',
    #     'ta_chi_tsu_te_to',
    #     'na_ni_nu_ne_no',
    #     'ha_hi_fu_he_ho',
    #     'ma_mi_mu_me_mo',
    #     'ya_yu_yo',
    #     'ra_ri_ru_le_ro',
    #     'wa_n_wo',
    # ]
# # 在admin页面里面注册model中的类和admin.py中对应的类
admin.site.register(R_type,R_typeAdmin)
admin.site.register(R_info,R_infoAdmin)