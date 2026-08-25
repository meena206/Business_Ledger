// ===================== Initialize on DOM Ready =====================
document.addEventListener("DOMContentLoaded", function () {
    // Auto-dismiss alerts after 4 seconds
    autoCloseAlerts();
    
    // Add Bootstrap validation
    initializeFormValidation();
    
    // Add number formatting to currency fields
    formatCurrencyFields();
    
    // Initialize tooltips
    initializeTooltips();

    // Refresh customer results while typing
    initializeCustomerSearch();
});

function initializeCustomerSearch() {
    const form = document.getElementById("customer-search-form");
    const input = form?.querySelector('input[name="search"]');

    if (!form || !input) return;

    let searchTimeout;
    let activeRequest;

    const refreshResults = async function () {
        activeRequest?.abort();
        activeRequest = new AbortController();

        const url = new URL(form.action || window.location.href);
        url.searchParams.set("search", input.value);

        try {
            const response = await fetch(url, {
                signal: activeRequest.signal,
                headers: { "X-Requested-With": "XMLHttpRequest" }
            });
            if (!response.ok) return;

            const page = new DOMParser().parseFromString(await response.text(), "text/html");
            const results = page.querySelector("#customer-results");
            const currentResults = document.querySelector("#customer-results");
            if (results && currentResults) currentResults.replaceWith(results);
            window.history.replaceState({}, "", url);
        } catch (error) {
            if (error.name !== "AbortError") console.error("Customer search failed", error);
        }
    };

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        refreshResults();
    });

    input.addEventListener("input", function () {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(refreshResults, 300);
    });
}

// ===================== Auto-close Alerts =====================
function autoCloseAlerts() {
    setTimeout(function () {
        document.querySelectorAll(".alert").forEach(function(alert) {
            if (alert) {
                alert.style.transition = "opacity 0.5s ease";
                alert.style.opacity = "0";
                setTimeout(() => {
                    if (alert.parentNode) {
                        alert.parentNode.removeChild(alert);
                    }
                }, 500);
            }
        });
    }, 4000);
}

// ===================== Bootstrap Form Validation =====================
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            // Don't validate forms that are inline (like delete forms)
            if (!form.classList.contains('no-validation')) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }
        }, false);
    });
}

// ===================== Currency Formatting =====================
function formatCurrencyFields() {
    // Format any field with data-currency attribute
    const currencyFields = document.querySelectorAll('[data-currency]');
    
    currencyFields.forEach(field => {
        // Format initial value if exists
        if (field.textContent && !isNaN(field.textContent)) {
            const value = parseFloat(field.textContent);
            field.textContent = value.toFixed(2);
        }
    });
    
    // Format amount input fields
    const amountInputs = document.querySelectorAll('input[name="amount"]');
    
    amountInputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value && !isNaN(this.value)) {
                this.value = parseFloat(this.value).toFixed(2);
            }
        });
    });
}

// ===================== Bootstrap Tooltips =====================
function initializeTooltips() {
    // Enable Bootstrap tooltips if available
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
}

// ===================== Confirmation Dialog =====================
function confirmDelete(customerName) {
    return confirm(`Are you sure you want to delete "${customerName}"? This action cannot be undone.`);
}

// ===================== Search Highlighting =====================
function highlightSearchTerm(searchTerm) {
    if (!searchTerm) return;
    
    const elements = document.querySelectorAll('td, li, .card-title, .customer-name');
    
    elements.forEach(element => {
        const text = element.textContent;
        const regex = new RegExp(`(${searchTerm})`, 'gi');
        
        if (regex.test(text)) {
            element.innerHTML = text.replace(regex, '<mark>$1</mark>');
        }
    });
}

// ===================== Date Formatter =====================
function formatDate(dateString) {
    if (!dateString) return '';
    
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', options);
}

// ===================== Number Formatter =====================
function formatCurrency(value) {
    if (isNaN(value)) return value;
    
    return parseFloat(value).toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

// ===================== Smooth Scrolling =====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===================== Keyboard Navigation =====================
document.addEventListener('keydown', function(e) {
    // ESC to close modals
    if (e.key === 'Escape') {
        const modals = document.querySelectorAll('.modal.show');
        modals.forEach(modal => {
            const bsModal = bootstrap.Modal.getInstance(modal);
            if (bsModal) {
                bsModal.hide();
            }
        });
    }
    
    // Ctrl/Cmd + S to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        const searchInput = document.querySelector('input[name="search"]');
        if (searchInput) {
            searchInput.focus();
        }
    }
});

// ===================== Print Functionality =====================
function printReport() {
    window.print();
}

// ===================== Export to CSV =====================
function exportToCSV(filename = 'report.csv') {
    const table = document.querySelector('table');
    if (!table) {
        alert('No table found to export');
        return;
    }
    
    let csv = [];
    const rows = table.querySelectorAll('tr');
    
    rows.forEach(row => {
        const cols = row.querySelectorAll('td, th');
        const csvRow = [];
        
        cols.forEach(col => {
            csvRow.push('"' + col.textContent.trim().replace(/"/g, '""') + '"');
        });
        
        csv.push(csvRow.join(','));
    });
    
    downloadCSV(csv.join('\n'), filename);
}

function downloadCSV(csv, filename) {
    const link = document.createElement('a');
    link.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
    link.setAttribute('download', filename);
    link.click();
}

// ===================== Responsive Table Handling =====================
function makeTablesResponsive() {
    const tables = document.querySelectorAll('table');
    
    tables.forEach(table => {
        if (!table.closest('.table-responsive')) {
            const wrapper = document.createElement('div');
            wrapper.className = 'table-responsive';
            table.parentNode.insertBefore(wrapper, table);
            wrapper.appendChild(table);
        }
    });
}

// Call after DOM is ready
document.addEventListener('DOMContentLoaded', makeTablesResponsive);

// ===================== Dark Mode Toggle (Optional) =====================
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

// Check for saved dark mode preference
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
}

// ===================== Console Info =====================
console.log('%cBusiness Ledger v1.0', 'color: #0d6efd; font-size: 16px; font-weight: bold;');
console.log('%cManage your business finances with ease', 'color: #6c757d; font-size: 12px;');