from django.conf.urls import url

from goods.views import index, category, detail

urlpatterns = [
    url(r'^index/',index,name="index"),
    url(r'^detail/(?P<id>\d+)', detail, name="detail"),
    url(r'^category/(?P<cate_id>\d*)_{1}(?P<order>\d?)\.html$', category, name="商品类别"),
]