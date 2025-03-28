from django.utils.deprecation import MiddlewareMixin

class NoCacheMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Impede cache para as páginas de autenticação
        if request.path.startswith('/login') or request.path.startswith('/accounts/') or request.path.startswith('/logout'):
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
        return response 