
from accounts.models import CbUserProfile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import get_template
from django.template import Context
from django.core.mail import BadHeaderError,EmailMessage
#
# USER_FIELDS = ['username', 'email']
#
# def create_user(strategy, details, backend,response, user=None, *args, **kwargs):
#     print(1,2,134)
#     print(kwargs, response)
#     if user:
#         return {'is_new': False}
#
#     fields = dict((name, kwargs.get(name, details.get(name)))
#                   for name in backend.setting('USER_FIELDS', USER_FIELDS))
#     if not fields:
#         return
#
#     return {
#         'is_new': True,
#         'user': strategy.create_user(**fields)
#     }


def create_profile(backend,user,response,*args,**kwargs):
    print(backend,kwargs,response)
    if kwargs['is_new']:
        attrs = {'user': user}

        if backend.name == "linkedin-oauth2":
             social_data ={
                 "first_name" : kwargs['details']['first_name'],
                 "last_name" : kwargs['details']['last_name'],
                }

        elif backend.name == "google-oauth2":
            social_data ={
                "first_name": kwargs['details']['first_name'],
                "last_name": kwargs['details']['last_name'],
                "avatar": response.get("image").get("url"),
            }
        elif backend.name == "facebook":
            social_data ={
                'first_name': kwargs['details']['first_name'],
                "last_name":  kwargs['details']['last_name'],
            }

        attrs = dict(attrs, **social_data)
        CbUserProfile.objects.create(
                    **attrs
        )

        # except:
        #     pass


def associate_with_user(backend,user,response,*args,**kwargs):

    try:
        CbUserProfile.objects.get(user=user.id)
    except CbUserProfile.DoesNotExist:
        create_profile(backend,user,response,*args,**kwargs)


def send_password_reset_token(user,request,temp):
    context = {
            'site': get_current_site(request),
            'user': user,
            'username': user.profile.first_name,
            'token': temp.token,
            'secure': request.is_secure(),
    }
    body = get_template("accounts/email/recovery_email.html").render(context)
    subject = "Password reset on Cibansa"
    try:
        msg=EmailMessage(subject,body,to=[user.email])
        msg.content_subtype="html"
        msg.send()
    except BadHeaderError:
        pass