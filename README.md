# Harvest Farms Ecommerce Website

Django ecommerce project for Harvest Farms with product browsing, account auth, cart management, and a contact form.

## Stack
- Python `3.13` (see `runtime.txt`)
- Django `5.1.3`
- SQLite by default, optional PostgreSQL via environment variables
- Pillow for product image uploads
- WhiteNoise + Gunicorn for deployment

## Apps
- `core`: home page and shared layout pages
- `accounts`: register, login, logout, custom user model
- `shop`: product list/detail, search, pagination, add product (superuser only)
- `cart`: session-based cart (add, view, update quantity, remove)
- `contact`: contact form with success page

## Features
- Product listing with search (`q`) and pagination
- Product detail pages by slug
- Session cart with total price and item count
- Login-protected cart routes
- Superuser-only product creation route
- Shared navbar/footer partials and sitewide static assets

## Project Structure
```text
HarvestFarms_EcommerceWebsite/
  manage.py
  HarvestFarms_EcommerceWebsite/   # settings, urls, wsgi
  accounts/
  shop/
  cart/
  contact/
  core/
  templates/partials/
  media/products_image/
```

## Local Development (Windows PowerShell)
1. Go to project root:
```powershell
cd "C:\Users\User\Desktop\harvest farm\HarvestFarms_EcommerceWebsite"
```
2. Create and activate a virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
3. Install dependencies:
```powershell
pip install -r requirements.txt
```
4. Apply migrations:
```powershell
python manage.py migrate
```
5. (Optional) create admin user:
```powershell
python manage.py createsuperuser
```
6. Start server:
```powershell
python manage.py runserver
```

## Main Routes
- `/` home page
- `/shop/` product list
- `/shop/product/<slug>/` product detail
- `/shop/add/` add product (superuser)
- `/cart/view/` cart page
- `/contact/` contact form
- `/accounts/register/`, `/accounts/login/`, `/accounts/logout/`
- `/admin/` Django admin

## Configuration
Environment variables supported in `settings.py`:
- `DEBUG` (`1` or `0`)
- `USE_REMOTE_DB` (`1` enables PostgreSQL; otherwise SQLite)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `CONSUMER_KEY`
- `CONSUMER_SECRET`
- `BASE_URL`
- `SHORTCODE`
- `PASSKEY`

PowerShell example:
```powershell
$env:DEBUG="1"
$env:USE_REMOTE_DB="0"
```

## Static and Media
- Static URL: `/static/`
- Static root: `staticfiles/`
- Media URL: `/media/`
- Media root: `media/`
- Product uploads: `media/products_image/`

## Useful Commands
```powershell
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
```

## Deployment Notes
- `procfle` contains: `web: gunicorn HarvestFarms_EcommerceWebsite.wsgi:application`
- Set `DEBUG=0` in production.
- Move all secrets and database credentials to environment variables.
