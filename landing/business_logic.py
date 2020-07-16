import requests
from django.http import HttpRequest

from social_django.models import UserSocialAuth


def get_info_of_account_in_vk(request: HttpRequest):
    user = UserSocialAuth.objects.get(uid=request.user.username[2::])
    access_token = user.access_token
    user_id = user.uid
    url = 'https://api.vk.com/method/execute.testfunc?user_id='
    url += user_id
    url += '&v=5.103&access_token='
    url += access_token
    json = requests.get(url).json()

    def account():
        if json['response'] == 'closed':
            return 'private'
        else:
            return json['response'][0][0]

    def friends():
        if json['response'] == 'closed':
            return 'private'
        else:
            return json['response'][1]['items']

    def photos():
        if json['response'] == 'closed':
            return 'private'
        else:
            return json['response'][2]

    return {'account': account, 'friends': friends, 'photos': photos}
