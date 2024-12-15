# API Authentication Setup - JWT Token-Based Authentication

```markdown
# API Authentication Setup - JWT Token-Based Authentication

This API is secured using JSON Web Tokens (JWT) for authentication. Follow the steps below to set up and test JWT-based authentication.

## Prerequisites

Install the required packages:

```bash
pip install djangorestframework
pip install djangorestframework-simplejwt

```

## Configuration

### 1. Add Installed Apps

Add the necessary apps to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
]

```

### 2. Set Authentication Classes

Configure JWT authentication in `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

```

### 3. Create Token View

Include token views in `urls.py`:

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

```

### 4. Protect API Endpoints

Add `IsAuthenticated` to views to protect them:

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view!'})

```

## How to Obtain a JWT Token

1.  **Request a Token:**
    
    Send a POST request to `/api/token/` with username and password:
    
    ```bash
    curl -X POST -d "username=<username>&password=<password>" http://127.0.0.1:8000/api/token/
    
    ```
    
    Example response:
    
    ```json
    {
        "access": "<access-token>",
        "refresh": "<refresh-token>"
    }
    
    ```
    
2.  **Use the Token for Authentication:**
    
    Include the `access` token in the `Authorization` header as `Bearer <your-access-token>`:
    
    ```bash
    curl -H "Authorization: Bearer <your-access-token>" http://127.0.0.1:8000/protected-endpoint/
    
    ```
    

## Token Expiration and Refresh

When the access token expires, use the `refresh` token to get a new `access` token:

```bash
curl -X POST -d "refresh=<refresh-token>" http://127.0.0.1:8000/api/token/refresh/

```

Example response:

```json
{
    "access": "<new-access-token>"
}

```



```