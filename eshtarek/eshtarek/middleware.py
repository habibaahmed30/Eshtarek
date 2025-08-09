from django.utils.deprecation import MiddlewareMixin
from tenants.models import Tenant

class TenantMiddleware(MiddlewareMixin):

    def process_request(self, request):

        tenant_key = request.headers.get('X-Tenant') or request.GET.get('tenant')
        request.tenant = None
        if tenant_key:
            try:
                request.tenant = Tenant.objects.get(name=tenant_key)
            except Tenant.DoesNotExist:
                request.tenant = None