from dj_rest_auth.views import LoginView


class LoginViewWithRole(LoginView):
    def get_response(self):
        response = super().get_response()
        data = {'is_airport': self.user.is_airport, 'is_admin':self.user.is_staff}
        response.data.update(data)
        return response

