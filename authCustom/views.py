from django.contrib.auth.views import LoginView, LogoutView
from django.utils.http import url_has_allowed_host_and_scheme
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth import update_session_auth_hash
from .forms import SignInForm, UserRegistrationForm, CustomPasswordChangeForm


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = SignInForm

    def get_success_url(self):
        next_url = self.request.GET.get('next') or '/'
        if not url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts={self.request.get_host()},
                require_https=self.request.is_secure()
        ):
            next_url = '/'
        return next_url

    def form_valid(self, form):
        super().form_valid(form)

        if not form.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(1209600)

        redirect_url = self.get_success_url()
        return JsonResponse({'success': True, 'redirect_url': redirect_url})

    def form_invalid(self, form):
        errors = {
            str(form.fields[field_name].label if field_name in form.fields and form.fields[
                field_name].label else field_name):
                [str(message) for message in error_messages]
            for field_name, error_messages in form.errors.items()
        }
        return JsonResponse({'success': False, 'errors': errors}, status=400)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)

        redirect_url = self.get_success_url()
        return JsonResponse({'success': True, 'redirect_url': redirect_url})

    def form_invalid(self, form):
        errors = {
            str(form.fields[field_name].label if field_name in form.fields and form.fields[
                field_name].label else field_name):
                [str(message) for message in error_messages]
            for field_name, error_messages in form.errors.items()
        }
        return JsonResponse({'success': False, 'errors': errors}, status=400)


class CustomPasswordChangeView(FormView):
    template_name = 'auth/edit_password.html'
    form_class = CustomPasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def post(self, request, *args, **kwargs):
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return JsonResponse({'success': True, 'username': request.user.username})
        else:
            errors = {
                str(form.fields[field_name].label if field_name in form.fields and form.fields[
                    field_name].label else field_name):
                    [str(message) for message in error_messages]
                for field_name, error_messages in form.errors.items()
            }

            return JsonResponse({'success': False, 'errors': errors})
