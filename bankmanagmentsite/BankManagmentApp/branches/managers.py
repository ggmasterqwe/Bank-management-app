from django.db import models
from common.utils import get_seccond

class AccountManager(models.Manager):
    def get_open_accounts(self):
        queryset = super(AccountManager, self).get_queryset().filter(is_closed=False)
        return queryset
    
    def order_by_params(self,request):
        try:
            order_by = request.query_params['order_by']
        except:
            order_by=''
            
        print(order_by)
        if  order_by == 'date_added':
            return self.all().order_by('date_added')
        
        if  order_by == 'money':
            my_list = []
            query_ids = []
            for acc in self.all():
                my_list.append((acc.id, acc.get_balance()))

            my_list.sort(key=get_seccond, reverse=True)
            
            for acc in my_list:
                query_ids.append(acc[0])
            return sorted(self.filter(id__in=query_ids), key=lambda i: query_ids.index(i.pk))

        return self.all()
            


        

            
