from django.contrib.auth.views import LoginView, LogoutView
from django.utils.http import url_has_allowed_host_and_scheme
from django.http import JsonResponse
from .forms import SignInForm
from django.urls import reverse_lazy

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
        errors = {field: list(errors) for field, errors in form.errors.items()}
        return JsonResponse({'success': False, 'errors': errors}, status=400)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')