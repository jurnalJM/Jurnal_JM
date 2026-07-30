// JayaMotor - Design System & Interactions

document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
    initThemeToggle();
    updateBreadcrumb();
});

// Navigation
function initNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    const currentPath = window.location.pathname;

    navItems.forEach(item => {
        if (item.getAttribute('href') === currentPath ||
            (currentPath === '/' && item.getAttribute('href') === '/')) {
            item.classList.add('active');
        }

        item.addEventListener('click', function() {
            navItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

// Theme toggle
function initThemeToggle() {
    const themeToggle = document.getElementById('themeToggle');
    if (!themeToggle) return; // Exit if theme toggle not found

    const root = document.documentElement;
    const sunIcon = themeToggle.querySelector('.sun-icon');
    const moonIcon = themeToggle.querySelector('.moon-icon');

    const savedTheme = localStorage.getItem('theme') || 'dark';
    applyTheme(savedTheme);

    themeToggle.addEventListener('click', () => {
        const current = localStorage.getItem('theme') || 'dark';
        const next = current === 'dark' ? 'light' : 'dark';
        localStorage.setItem('theme', next);
        applyTheme(next);
    });

    function applyTheme(theme) {
        root.setAttribute('data-theme', theme);

        if (theme === 'dark') {
            sunIcon.style.display = 'block';
            moonIcon.style.display = 'none';
        } else {
            sunIcon.style.display = 'none';
            moonIcon.style.display = 'block';
        }
    }
}

// Update breadcrumb
function updateBreadcrumb() {
    const breadcrumb = document.getElementById('breadcrumb');
    if (!breadcrumb) return; // Exit if breadcrumb not found

    const path = window.location.pathname;
    const pageNames = {
        '/': 'Dasbor',
        '/transaksi': 'Transaksi',
        '/laporan': 'Laporan'
    };

    const pageName = pageNames[path] || 'Halaman';
    breadcrumb.innerHTML = `
        <a href="/">JayaMotor - Honda</a>
        <span style="margin: 0 8px;">→</span>
        <span>${pageName}</span>
    `;
}

// Utility: Format numbers
window.formatNumber = function(value) {
    if (!value && value !== 0) return '-';
    return new Intl.NumberFormat('id-ID').format(value);
};

// Utility: Format currency
window.formatCurrency = function(value) {
    if (!value && value !== 0) return 'Rp 0';
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(value);
};

// Utility: Format date
window.formatDate = function(dateString) {
    if (!dateString) return '-';
    const date = new Date(dateString);
    return date.toLocaleDateString('id-ID', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
    });
};

// Utility: Get status color
window.getStatusColor = function(status) {
    const colors = {
        'Pending': 'warning',
        'Approved': 'success',
        'Paid': 'info',
        'Cancelled': 'danger'
    };
    return colors[status] || 'info';
};

// Utility: Get status label
window.getStatusLabel = function(status) {
    const labels = {
        'Pending': 'Menunggu',
        'Approved': 'Disetujui',
        'Paid': 'Dibayar',
        'Cancelled': 'Dibatalkan'
    };
    return labels[status] || status;
};

// Toast notifications
window.showToast = function(message, type = 'info') {
    const toast = document.createElement('div');

    const colorMap = {
        'success': '10, 185, 129',
        'error': '239, 68, 68',
        'warning': '245, 158, 11',
        'info': '37, 99, 235'
    };

    const color = colorMap[type] || colorMap['info'];

    toast.style.cssText = `
        position: fixed;
        bottom: 24px;
        right: 24px;
        z-index: 10000;
        padding: 14px 20px;
        border-radius: 8px;
        background-color: rgba(${color}, 0.15);
        border-left: 4px solid rgb(${color});
        color: #f1f5f9;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        animation: slideInUp 200ms ease;
        font-size: 14px;
        font-weight: 500;
        max-width: 450px;
        white-space: pre-wrap;
        word-wrap: break-word;
    `;

    toast.textContent = message;
    document.body.appendChild(toast);

    // Adjust timing based on message length
    const displayTime = Math.max(3500, message.length * 50);

    setTimeout(() => {
        toast.style.animation = 'slideOutDown 200ms ease';
        setTimeout(() => toast.remove(), 200);
    }, displayTime);
};

// Animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInUp {
        from {
            transform: translateY(100%);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }

    @keyframes slideOutDown {
        from {
            transform: translateY(0);
            opacity: 1;
        }
        to {
            transform: translateY(100%);
            opacity: 0;
        }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);
