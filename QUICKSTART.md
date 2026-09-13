# Business Ledger - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Prepare Database Credentials
Create a `.env` file in the project root with:
```
DB_NAME=business_ledger
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_POST=3306
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Migrations
```bash
python manage.py migrate
```

### Step 4: Create Admin Account
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 5: Start Server
```bash
python manage.py runserver
```

### Step 6: Access the Application
- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## 📱 Main Features

### 1. **Dashboard**
   - Overview of all metrics
   - Recent transactions
   - Quick stats

### 2. **Customers**
   - Add/Edit/Delete customers
   - View customer details
   - Search by name, phone, or city while typing
   - See customer balance

### 3. **Transactions**
   - Add credit/debit transactions
   - View transaction history
   - Filter by type
   - Search descriptions

### 4. **Ledger History**
   - Complete transaction ledger
   - Filter by transaction type
   - Search functionality
   - Sortable columns

### 5. **Reports**
   - Financial summary
   - Balance overview
   - Transaction statistics
   - Export capabilities

---

## 🎨 What's New

✨ **Professional Design**
- Modern Bootstrap 5 interface
- Smooth animations and transitions
- Color-coded status indicators
- Responsive mobile design

💡 **Smart Features**
- Auto-dismissing notifications
- Form validation
- Modal confirmations
- Keyboard shortcuts (Ctrl+S to search)

🔒 **Security**
- User authentication
- CSRF protection
- Secure session handling
- Permission-based access

---

## 🔑 Default URLs

| Page | URL |
|------|-----|
| Register | `/register/` |
| Login | `/login/` |
| Dashboard | `/` |
| Customers | `/customers/` |
| Add Customer | `/customers/add/` |
| Ledger | `/ledger/` |
| Reports | `/reports/` |
| Admin | `/admin/` |
| Logout | `/logout/` |

---

## 💾 Database Models

### Customer
- Name
- Phone
- Email (optional)
- City (optional)
- Address (optional)
- Created Date

### Transaction
- Customer (Foreign Key)
- Type (Credit/Debit)
- Amount
- Description
- Date
- Created Date

---

## 🛠️ Troubleshooting

**Port 8000 already in use?**
```bash
python manage.py runserver 8001
```

**Database connection error?**
- Check MySQL is running
- Verify .env credentials
- Check database exists

**Static files not showing?**
```bash
python manage.py collectstatic --noinput
```

---

## 📚 Documentation

See [README.md](README.md) for complete documentation including:
- Detailed installation steps
- API endpoints
- Project structure
- Security notes
- Browser compatibility
- Performance tips

---

## 🎓 Example Usage

### Adding a Customer
1. Navigate to "Customers" → "Add Customer"
2. Fill in customer details
3. Enter the required initial transaction details
4. Click "Save"

### Recording a Transaction
1. Go to Customers → Select Customer
2. Click "Add Transaction"
3. Choose type (Credit/Debit)
4. Enter amount and date
5. Add description (optional)
6. Click "Save Transaction"

### Viewing Reports
1. Click "Reports" in navigation
2. See financial summary
3. Click "View Ledger History" for detailed transactions

---

## ⌨️ Keyboard Shortcuts

- `Ctrl/Cmd + S` - Focus search field
- `Esc` - Close modals

---

## 🌐 Browser Support

- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

---

## 📞 Support

For issues or questions, refer to the README.md file for comprehensive documentation.

---

**Version**: 1.0  
**Created**: 2024  
**Status**: Ready for Production
