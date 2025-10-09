# Django Yadak Marketplace

**Yadak Marketplace** — a Django-based web application for selling automotive spare parts ("yadak").
This README provides an overview, setup instructions, development tips, and deployment notes so contributors and maintainers can quickly get started.

---

## Table of contents

1. [Project overview](#project-overview)
2. [Key features](#key-features)
3. [Tech stack](#tech-stack)
4. [Repository structure (recommended)](#repository-structure-recommended)
5. [Requirements](#requirements)
6. [Environment variables example](#environment-variables-example)
7. [Local setup & development](#local-setup--development)
8. [Database & migrations](#database--migrations)
9. [Creating a superuser](#creating-a-superuser)
10. [Running tests](#running-tests)
11. [API & routes](#api--routes)
12. [Admin & management tasks](#admin--management-tasks)
13. [Deployment notes](#deployment-notes)
14. [Contributing](#contributing)
15. [License](#license)
16. [Contact / Support](#contact--support)

---

## Project overview

Yadak Marketplace is an e-commerce platform focused on buying and selling car spare parts. It supports sellers to list parts (with SKU, compatibility metadata and images), and buyers to search, filter, and purchase parts. Features include basic catalog, user accounts, order management, admin dashboard, and optional REST API for integrations.

Use cases:

* Local mechanics selling parts
* Stores listing available stock with location/price
* Buyers searching by car make/model/year or part number

---

## Key features

* User registration, login, profile management
* Seller dashboards: add/edit/delete listings
* Product catalog with images, stock, SKU, compatibility tags
* Search & filters (make, model, year, part type, price range)
* Shopping cart and checkout (basic) — extendable to payments
* Order management and status tracking
* Admin interface to moderate listings and users
* REST API endpoints (optional) for mobile apps or partners
* i18n-ready (support Persian/English) and currency-aware

---

## Tech stack

* Python 3.11+ (or 3.10+)
* Django 4.x (adjust if you prefer other stable versions)
* Django REST Framework (for API)
* PostgreSQL (recommended) or SQLite for quick local dev
* Celery + Redis (optional — for background tasks like image processing or emails)
* Docker & docker-compose (optional, for consistent local/dev environment)

---

## Repository structure (recommended)

```
yadak-marketplace/
├─ README.md
├─ .env.example
├─ docker-compose.yml
├─ Dockerfile
├─ requirements.txt
├─ manage.py
├─ config/                # django project settings (config/settings/*.py)
├─ apps/
│  ├─ accounts/
│  ├─ products/
│  ├─ orders/
│  ├─ payments/
│  └─ api/
└─ static/ media/
```

---

## Requirements

Install system & Python dependencies:

* Python 3.12.3
* pip
* virtualenv or venv
* PostgreSQL (for production)
* Redis (optional)

Python packages are declared in `requirements.txt`:

* Django
* djangorestframework
* psycopg2
* Pillow (image handling)

---

## Environment variables example

Create an `.env` at project root (do **not** commit secrets). Example `.env`:

```
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@db:5432/yadak_db
DJANGO_EMAIL_HOST=smtp.example.com
DJANGO_EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=secret
REDIS_URL=redis://redis:6379/0
STRIPE_SECRET_KEY=sk_test_xxx   # optional for payments
```

---

## Local setup & development

### 1. Clone repository

```bash
git clone <repo-url>
cd yadak-marketplace
```

### 2. Create virtual environment and install deps

```bash
python -m venv .venv
source .venv/bin/activate         # Linux / macOS
# .venv\Scripts\activate          # Windows PowerShell
pip install -r requirements.txt
```

### 3. Set environment variables

Copy `.env.example` to `.env` and fill values:

```bash
cp .env.example .env
# edit .env
```

(If you use `python-decouple` or `django-environ`, they will load `.env` automatically in settings.)

### 4. Run migrations & collect static

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 5. Run development server

```bash
python manage.py runserver
# Open http://127.0.0.1:8000
```

**Docker (optional)**
If a `docker-compose.yml` is provided:

```bash
docker-compose up --build
# this typically starts web, db, redis services
```

---

## Database & migrations

* Use Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

* If using PostgreSQL, configure `DATABASE_URL` or `DATABASES` in settings.
* Keep migrations small and logical — one feature per migration.

---

## Creating a superuser

```bash
python manage.py createsuperuser
```

Then visit `/admin/` to manage products, users, and orders.

---

## Running tests

Prefer pytest or Django's test runner:

```bash
# Django default
python manage.py test

# Or with pytest
pytest
```

Aim for unit tests for models, views, API endpoints, and integration tests for checkout flows.

---

## API & routes (example)

If using DRF, consider these endpoints:

* `POST /api/auth/login/` — user login
* `POST /api/auth/register/` — user signup
* `GET /api/products/` — list/search products (supports query params)
* `GET /api/products/<id>/` — product detail
* `POST /api/products/` — create listing (seller only)
* `PUT /api/products/<id>/` — update listing (seller or admin)
* `POST /api/cart/` — manage cart
* `POST /api/orders/` — place order
* `GET /api/orders/{id}/` — order status

Document API with OpenAPI/Swagger (e.g., using `drf-yasg` or `drf-spectacular`) and include examples.

---

## Admin & management tasks

* Moderation: approve or reject listings
* Inventory: update stock counts for SKUs
* Bulk import/export: use Django management commands (`python manage.py import_parts --file parts.csv`)
* Scheduled tasks: use Celery for nightly inventory sync/email sending

---

## Deployment notes

* Use Gunicorn + Nginx for production.
* Secure `DJANGO_SECRET_KEY`, set `DEBUG=False`, configure `ALLOWED_HOSTS`.
* Use HTTPS (Let's Encrypt).
* Configure persistent storage for `media/` (S3 or equivalent).
* Use PostgreSQL for production; tune connection pool.
* Run `python manage.py collectstatic` on deploy.
* Use environment variable `DATABASE_URL` or provider-specific secrets manager.

Example minimal Gunicorn systemd unit for `yadak`:

```
ExecStart=/path/to/venv/bin/gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

---

## Security considerations

* Validate and sanitize uploaded images/files.
* Rate-limit authentication endpoints.
* Use CSRF protection for template views.
* Do not store payment credentials on your servers (use tokens from payment providers like Stripe).
* Regularly update dependencies and run security scans.

---

## Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/add-search`
3. Write tests for new features
4. Open a Pull Request with a clear description
5. Follow coding standards (PEP8). Optionally include pre-commit hooks (flake8, isort, black)

---

## Useful management commands (examples)

* Create parts from CSV:

  ```bash
  python manage.py import_parts parts.csv
  ```
* Sync product compatibility:

  ```bash
  python manage.py sync_compatibility
  ```

---

## Troubleshooting

* Migration errors: try `python manage.py migrate --fake appname zero` only when you know the state.
* Static files missing: run `collectstatic` and check `STATIC_ROOT`.
* Permissions issues on upload: ensure media directory writable by web process.

---

## License

Specify a license (e.g. MIT). Example:

```
MIT License
See LICENSE file for details.
```

---

## Contact / Support

For questions, bugs or feature requests, open an issue in the repository or contact the maintainers at the email listed in project settings.

---

### Final notes

This README is intended as a living document. Update it whenever you:

* Add or remove major features
* Change deployment or environment requirements
* Introduce breaking API changes

Happy building — and good luck selling yadak! 🚗🔧
