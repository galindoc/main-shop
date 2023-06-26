from django.contrib.auth import get_user_model

UserAccount = get_user_model()

def create_username(name):
        username = name.lower().replace(' ', '') 
        similars = UserAccount.objects.filter(username=username) 
        similars_count = similars.count() 
        while True:
            if not UserAccount.objects.filter(username=f'{username}{similars_count}').exists():
                break
            similars_count += 1
        username = f'{username}{similars_count}'
        return username
