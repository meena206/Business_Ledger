# Business Ledger

A professional web-based Business Ledger application built with Django for managing customers and financial transactions.

## Features

- **User Authentication**: Secure login and registration system
- **Customer Management**: Add, edit, view, and delete customers
- **Live Customer Search**: Search name, phone, or city while typing without a full-page refresh
- **Transaction Tracking**: Record and manage credit/debit transactions
- **Financial Dashboard**: View real-time balance, total credits, debits, and recent transactions
- **Ledger History**: Complete transaction history with filtering and search
- **Financial Reports**: Comprehensive financial reports and summaries
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Modern UI**: Professional styling with smooth animations and intuitive navigation

## Technology Stack

- **Backend**: Django 6.1
- **Database**: MySQL
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Authentication**: Django's built-in auth system

## Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)
- Virtual Environment (recommended)

## Installation & Setup

### 1. Clone or Extract the Project
```bash
cd Business_Ledger
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
Create a `.env` file in the project root with your database credentials:
```
DB_NAME=business_ledger
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_POST=3306
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### First-Time Setup
1. Go to `http://127.0.0.1:8000/register/` to create a new account
2. Log in with your credentials
3. You'll be directed to the Dashboard

### Dashboard
- View key metrics: customer count, transaction count, total credits/debits, and balance
- See recent transactions
- Quick access to all features

### Customers
- **View All Customers**: Navigate to "Customers" in the navbar
- **Add Customer**: Click "Add Customer" button
- **Initial Transaction**: Enter the first credit/debit transaction while creating a customer; both records are saved together
- **View Details**: Click on any customer to see their account summary and transactions
- **Edit Customer**: Click "Edit" on customer detail page
- **Delete Customer**: Click "Delete" (confirmation required)
- **Search Customers**: Type a name, phone number, or city; results update automatically after a short pause

### Transactions
- **Add Transaction**: From customer detail page, click "Add Transaction"
- **View Transactions**: All transactions are listed on customer detail page
- **Filter by Type**: Use the Ledger History page to filter by Credit/Debit

### Ledger History
- View all transactions across all customers
- Search by customer name or description
- Filter by transaction type (Credit/Debit)
- View complete transaction details

### Reports
- View comprehensive financial summaries
- See total credits, debits, and net balance
- Analyze transaction counts and patterns
- Access detailed ledger history from reports page

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/`

**Features:**
- Manage users and permissions
- View and edit customers
- View and edit transactions
- Apply filters and search

## Project Structure

```
Business_Ledger/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── business_ledger/          # Main project folder
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── ledger/                   # Ledger app
│   ├── models.py             # Database models (Customer, Transaction)
│   ├── views.py              # View functions
│   ├── forms.py              # Django forms
│   ├── urls.py               # App URL configuration
│   ├── admin.py              # Admin configuration
│   ├── templates/ledger/     # HTML templates
│   │   ├── base.html         # Base template
│   │   ├── dashboard.html    # Dashboard page
│   │   ├── customer_list.html
│   │   ├── customer_detail.html
│   │   ├── customer_form.html
│   │   ├── transaction_form.html
│   │   ├── ledger_history.html
│   │   ├── reports.html
│   │   ├── login.html
│   │   └── register.html
│   ├── templates/static/     # Static files configured in settings.py
│   │   └── ledger/
│   │       ├── css/style.css
│   │       └── js/script.js  # Live customer search behavior
│   └── migrations/           # Database migrations
└── README.md                 # This file
```

## API Endpoints

### Authentication
- `GET/POST /register/` - User registration
- `GET/POST /login/` - User login
- `GET /logout/` - User logout

### Dashboard
- `GET /` - Dashboard home page

### Customers
- `GET /customers/` - List all customers
- `GET/POST /customers/add/` - Add customer and required initial transaction
- `GET /customers/<id>/` - View customer details
- `GET/POST /customers/<id>/edit/` - Edit customer
- `POST /customers/<id>/delete/` - Delete customer
- `GET/POST /customers/<id>/transaction/add/` - Add transaction for customer

### Ledger & Reports
- `GET /ledger/` - Ledger history with filtering
- `GET /reports/` - Financial reports

## Features in Detail

### Dashboard Statistics
- **Customer Count**: Total number of customers
- **Transaction Count**: Total number of transactions
- **Total Credit**: Sum of all credit transactions
- **Total Debit**: Sum of all debit transactions
- **Balance**: Net balance (Credit - Debit)
- **Recent Transactions**: Last 8 transactions with customer info

### Customer Account Summary
- Total credits received
- Total debits paid
- Current balance
- Transaction history
- Member since date

### Transaction Filtering
- Filter by transaction type (Credit/Debit)
- Search by customer name or description
- Sort by date
- View detailed transaction information

### Customer Search
- Search is case-insensitive across name, phone, and city
- The browser fetches updated results without a full-page refresh

### Responsive Features
- Mobile-friendly navigation
- Collapsible navbar
- Responsive card layouts
- Touch-friendly buttons
- Optimized table display for small screens

## Keyboard Shortcuts

- `Ctrl/Cmd + S` - Focus search box
- `Esc` - Close modals/dialogs

## Troubleshooting

### Database Connection Error
- Ensure MySQL is running
- Verify `.env` file has correct credentials
- Check database name exists in MySQL

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Port Already in Use
```bash
python manage.py runserver 8001  # Use different port
```

### Permission Denied Errors
- Check database user permissions
- Ensure user can create/modify tables

## Security Notes

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Set `ALLOWED_HOSTS = ['your-domain.com']`
3. Use environment variables for sensitive data
4. Enable `CSRF_COOKIE_SECURE = True`
5. Enable `SESSION_COOKIE_SECURE = True`
6. Use HTTPS
7. Use a production-grade database
8. Set `SECURE_SSL_REDIRECT = True`

## Browser Compatibility

- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome for Android)

## Performance Tips

- Implement pagination for large datasets
- Cache dashboard data for better performance
- Use database connection pooling

## Support & Contribution

For issues or feature requests, please contact the development team.

## License

All rights reserved © 2026 Business Ledger

## Version

**v1.0** - Initial Release

---

**Last Updated**: 2026
**Maintained By**: Business Ledger Team
