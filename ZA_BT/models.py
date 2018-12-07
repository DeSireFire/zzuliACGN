from django.db import models

# Create your models here.

# 全部资源分类
class R_type(models.Model):
    R_title = models.CharField(max_length=15,unique=True)
    isdelete = models.BooleanField(default=False)
    def __str__(self):
        return self.R_title

#资源信息
class R_info(models.Model):
    a_i_u_e_o = models.CharField(max_length=50,unique=True)#资源名称
    ka_ki_ku_ke_ko = models.CharField(max_length=30,unique=True)  # 资源发布时间
    sa_shi_su_se_so = models.CharField(max_length=30,default='-')#资源大小
    ta_chi_tsu_te_to = models.CharField(max_length=50,default='-')#资源上传数
    na_ni_nu_ne_no = models.CharField(max_length=50,default='-')#资源下载数
    ha_hi_fu_he_ho = models.TextField(default='暂无')#资源介绍
    ma_mi_mu_me_mo = models.CharField(max_length=50,default='-')#资源完成数
    ya_yu_yo = models.TextField(default='暂无')    #资源下载链接
    ra_ri_ru_le_ro = models.ForeignKey('R_type',on_delete=models.CASCADE)#资源种类
    wa_n_wo = models.BooleanField(default=False)#是否删除
    def __str__(self):
        return self.a_i_u_e_o