// JayaMotor Web App - Main JavaScript

// Global error handler
window.addEventListener('error', function(event) {
    console.error('Global error:', event.error);
});

// Axios default config
axios.defaults.baseURL = window.location.origin;
axios.defaults.headers.common['Content-Type'] = 'application/json';

// Axios interceptors
axios.interceptors.response.use(
    response => response,
    error => {
        if (error.response?.status === 401) {
            // Redirect to login if unauthorized
            window.location.href = '/login';
        }
        return Promise.reject(error);
    }
);

// Utility Functions

/**
 * Format date to Indonesia locale (DD/MM/YYYY)
 */
function formatDate(dateString) {
    if (!dateString) return '-';
    const date = new Date(dateString);
    return date.toLocaleDateString('id-ID', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
    });
}

/**
 * Format date and time
 */
function formatDateTime(dateString) {
    if (!dateString) return '-';
    const date = new Date(dateString);
    return date.toLocaleString('id-ID');
}

/**
 * Format currency to Indonesian Rupiah (IDR)
 */
function formatCurrency(value) {
    if (!value) return 'Rp 0';
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(value);
}

/**
 * Format number with thousand separator
 */
function formatNumber(value) {
    if (!value) return '0';
    return new Intl.NumberFormat('id-ID').format(value);
}

/**
 * Get status badge color
 */
function getStatusColor(status) {
    const colors = {
        'Pending': 'warning',
        'Approved': 'success',
        'Paid': 'info',
        'Cancelled': 'danger',
        'Draft': 'secondary'
    };
    return colors[status] || 'secondary';
}

/**
 * Get status label
 */
function getStatusLabel(status) {
    const labels = {
        'Pending': 'Menunggu',
        'Approved': 'Disetujui',
        'Paid': 'Lunas',
        'Cancelled': 'Dibatalkan',
        'Draft': 'Draf'
    };
    return labels[status] || status;
}

/**
 * Show success toast notification
 */
function showSuccess(message, duration = 3000) {
    const toast = document.createElement('div');
    toast.className = 'alert alert-success alert-dismissible fade show position-fixed';
    toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, duration);
}

/**
 * Show error toast notification
 */
function showError(message, duration = 3000) {
    const toast = document.createElement('div');
    toast.className = 'alert alert-danger alert-dismissible fade show position-fixed';
    toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, duration);
}

/**
 * Show warning toast notification
 */
function showWarning(message, duration = 3000) {
    const toast = document.createElement('div');
    toast.className = 'alert alert-warning alert-dismissible fade show position-fixed';
    toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, duration);
}

/**
 * Show info toast notification
 */
function showInfo(message, duration = 3000) {
    const toast = document.createElement('div');
    toast.className = 'alert alert-info alert-dismissible fade show position-fixed';
    toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, duration);
}

/**
 * Show confirmation dialog
 */
function showConfirm(message) {
    return new Promise((resolve) => {
        if (confirm(message)) {
            resolve(true);
        } else {
            resolve(false);
        }
    });
}

/**
 * Debounce function for search
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Export data to CSV
 */
function exportToCSV(filename, data, columns) {
    let csvContent = "data:text/csv;charset=utf-8,";

    // Add header
    csvContent += columns.join(',') + '\n';

    // Add data
    data.forEach(row => {
        const values = columns.map(col => {
            const value = row[col] || '';
            // Escape quotes and wrap in quotes if contains comma
            return `"${String(value).replace(/"/g, '""')}"`;
        });
        csvContent += values.join(',') + '\n';
    });

    // Download
    const link = document.createElement('a');
    link.setAttribute('href', encodeURI(csvContent));
    link.setAttribute('download', filename);
    link.click();
}

/**
 * Parse error response
 */
function getErrorMessage(error) {
    if (error.response?.data?.error) {
        return error.response.data.error;
    }
    if (error.message) {
        return error.message;
    }
    return 'Terjadi kesalahan yang tidak diketahui';
}

/**
 * Parse form data to JSON
 */
function formToJSON(formElement) {
    const formData = new FormData(formElement);
    const json = {};

    for (let [key, value] of formData.entries()) {
        if (json.hasOwnProperty(key)) {
            if (!Array.isArray(json[key])) {
                json[key] = [json[key]];
            }
            json[key].push(value);
        } else {
            json[key] = value;
        }
    }

    return json;
}

/**
 * Check if string is valid email
 */
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

/**
 * Check if string is valid phone number
 */
function isValidPhone(phone) {
    const regex = /^(\+62|0)[0-9]{9,12}$/;
    return regex.test(phone);
}

/**
 * Copy text to clipboard
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showSuccess('Teks berhasil disalin');
    }).catch(() => {
        showError('Gagal menyalin teks');
    });
}

/**
 * Get current date in YYYY-MM-DD format
 */
function getTodayDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

/**
 * Calculate date difference in days
 */
function dateDiffInDays(date1, date2) {
    const d1 = new Date(date1);
    const d2 = new Date(date2);
    const diffTime = Math.abs(d2 - d1);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays;
}

/**
 * Get date n days ago
 */
function getDateNDaysAgo(n) {
    const date = new Date();
    date.setDate(date.getDate() - n);
    return date.toISOString().split('T')[0];
}

// Console welcome message
console.log('%cJayaMotor Web App', 'font-size: 24px; font-weight: bold; color: #0d6efd;');
console.log('%cModern Motor Sales Management System', 'font-size: 14px; color: #666;');
