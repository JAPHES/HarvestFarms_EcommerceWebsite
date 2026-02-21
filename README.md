# Harvest Farms Ecommerce Website

Django-based ecommerce website for Harvest Farms with product catalog, cart, contact form, authentication, and admin product management.

## Tech Stack
- Python 3.14+
- Django 5.1.3
- SQLite (default for local development)
- PostgreSQL (optional, via environment variables)
- Bootstrap 5 + custom templates

## Project Apps
- `core` - Home page and shared site pages
- `accounts` - Registration, login, logout, custom user model
- `shop` - Product listing, product detail, add product (admin)
- `cart` - Session-based cart (add, update quantity, remove, view)
- `contact` - Contact form and success page

## Key Features
- Responsive farm-themed UI
- Shared navbar and shared footer across site pages
- Floating WhatsApp button on all pages
- Product search (name + description, partial matching)
- Product list pagination
- Product detail page with improved purchase flow
- Cart with:
  - product thumbnails
  - update quantity
  - remove item
  - total amount and item count

## Local Setup
1. Clone/open project folder:
```powershell
cd "C:\Users\User\Desktop\harvest farm\HarvestFarms_EcommerceWebsite"
```

2. Create virtual environment and activate:
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Run migrations:
```powershell
python manage.py migrate
```

5. Start development server:
```powershell
python manage.py runserver
```

6. Open:
- Home: `http://127.0.0.1:8000/`
- Products: `http://127.0.0.1:8000/shop/`
- Cart: `http://127.0.0.1:8000/cart/view/`
- Contact: `http://127.0.0.1:8000/contact/`

## Admin Access
Create superuser:
```powershell
python manage.py createsuperuser
```

Admin panel:
- `http://127.0.0.1:8000/admin/`

Add product page (superuser only):
- `http://127.0.0.1:8000/shop/add/`

## Environment Variables
Current settings support:
- `DEBUG` (`1` for local dev, `0` for production)
- `USE_REMOTE_DB` (`0` for SQLite, `1` for PostgreSQL)
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

Example (PowerShell):
```powershell
$env:DEBUG="1"
$env:USE_REMOTE_DB="0"
```

## Static & Media
- Static URL: `/static/`
- Media URL: `/media/`
- Product images are stored under `media/products_image/`

## Common Commands
Run checks:
```powershell
python manage.py check
```

Create migrations after model changes:
```powershell
python manage.py makemigrations
python manage.py migrate
```

## Notes
- `shop/add/` requires login and superuser permission.
- If UI changes are not visible, hard refresh browser (`Ctrl + F5`).
- For production, move secrets (DB password, secret key) to environment variables.
