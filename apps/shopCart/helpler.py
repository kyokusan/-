from django_redis import get_redis_connection
def json_msg(code,msg=None,data=None):
    return {"code":code,"errmsg":msg,"data":data}


def get_cart_count(request):
    """获取购物车的数量"""
    user_id=request.session.get("id")
    if user_id is None:
        return 0
    else:
        #连接REDIS
        r = get_redis_connection()
        #获取键
        cart_key = f"cart_{user_id}"
        values = r.hvals(cart_key)

        total_count = 0
        for v in values:
            total_count += int(v)
        return total_count

# def get_cart_one_count(request):
#     """获取购物车的数量"""
#     user_id=request.session.get("id")
#     if user_id is None:
#         return 0
#     else:
#         #连接REDIS
#         r = get_redis_connection()
#         #获取键
#         cart_key = f"cart_{user_id}"
#         values = r.hvals(cart_key)
#
#         # total_count = 0
#         y=1
#         x={}
#         for v in values:
#             x[y]=int(v)
#             y+=1
#         print(x)
#         return x

def get_cart_key(user_id):
    """生成购物车KEY"""
    return f"cart_{user_id}"