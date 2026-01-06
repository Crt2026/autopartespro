from django.shortcuts import redirect

class RestrictAdminMiddleware:
    """
    Middleware to restrict access to the Admin panel.
    Redirects authenticated non-staff users to the home page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the requested path is for the admin panel
        if request.path.startswith('/admin/'):
            # If user is logged in but NOT a staff member
            if request.user.is_authenticated and not request.user.is_staff:
                return redirect('/')
        
        response = self.get_response(request)
        return response
