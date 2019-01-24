from django.contrib import admin

# Register your models here.
from goods.models import Category, Goods_Spu, Goods_Sku, Unit, Goodsphoto, Advertisement, ActivityZone, Activity

admin.site.register(Category)
admin.site.register(Goods_Spu)
admin.site.register(Goods_Sku)
admin.site.register(Unit)
admin.site.register(Goodsphoto)
admin.site.register(Advertisement)
admin.site.register(Activity)
admin.site.register(ActivityZone)