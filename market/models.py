from django.db import models

#General Market Item model
class MarketItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='market_items/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Market Item'
        verbose_name_plural = 'Market Items'
        db_table = 'MarketItem'

#Model for Order 
class MarketItemOrder(models.Model):
    item = models.ForeignKey(MarketItem, on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item.name} - {self.user.username}'

    class Meta:
        verbose_name = 'Market Item Order'
        verbose_name_plural = 'Market Item Orders'
        db_table = 'MarketItemOrder'
