# -*- coding: utf-8 -*-
'''
Created on 2015年5月26日

@author: Administrator
'''

class MBase(Base,MModle):
    '''
    基础模型
    '''
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = Column(String(32), primary_key=True, default=ColumnDefault(uuid))
    
    def __init__(self, *args, **kwargs):
        pass
        
    class Meta:
        db_label = 'default' 
         
    def __repr__(self):
        return 'Base(%r)' % (self.id)


class Order(MBase):
    '''
   订单模型
    '''
    __tablename__ = 'orders' 
    COMMON = 0
    GROUP_PURCHASE = 1
    COUPONS = 2
    #订单状态：10(默认):未付款;20:已付款;30:已发货;40:已收货;50:已提交;60已确认;70取消;80过期
    UNPAID=10
    PAID=20
    SHIPPED=30
    GOT=40
    SUBMITTED=50
    CONFIRMED=60
    CANCELED=70
    PAST_DUE=80
    order_sn = Column(String(100))
    seller_id = Column(String(32))
#     store_id = Column(String(32),ForeignKey('store.id'))
#     store_name=Column(String(50))
    buyer_id = Column(String(32),ForeignKey('users.id'))
    buyer_name = Column(String(50))
    buyer_email = Column(String(100))
    buyer_phone = Column(String(11))
    add_time=Column(DateTime,default=ColumnDefault(datetime.now))
    order_type=Column(SmallInteger,default=COMMON)
    payment_id = Column(String(32))
    payment_name = Column(String(50))
    payment_code = Column(String(50))
    payment_direct = Column(String(1))
    out_sn = Column(String(100))
    payment_time = Column(DateTime)
    pay_message = Column(String(100))
    shipping_time = Column(DateTime)
    shipping_code = Column(String(50))
    finnshed_time = Column(DateTime)
    invoice = Column(String(100))
    goods_amount = Column(Float,default=0)
    discount=Column(Float,default=0)
    order_amount=Column(Float,default=0)
    evaluation_status =Column(SmallInteger,default=0)
    evaluation_time =Column(DateTime)
    order_message = Column(String(300))
    order_state = Column(Integer,default=UNPAID)
    is_freeze=Column(SmallInteger,default=0)
    consignee=Column(String(100))
    consignee_area_id=Column(String(32))
    consignee_address=Column(String(200))
    consignee_phone=Column(String(11))
    shipping_company=Column(String(50))
    order_source=Column(String(32))
#     warehouse_id = Column(String(32),ForeignKey('warehouse.id'))
    order_goods = relationship("OrderGoods", backref="orders")
    
    class Meta:
        db_label = 'default'
     
    def __init__(self, *args, **kwargs):
        super(Order, self).__init__()

