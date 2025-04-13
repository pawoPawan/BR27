// Auth Modal Functions
function openAuthModal(tab = 'login') {
    const modal = document.getElementById('auth-modal');
    modal.classList.remove('hidden');
    switchTab(tab);
}

function closeAuthModal() {
    const modal = document.getElementById('auth-modal');
    modal.classList.add('hidden');
}

function switchTab(tab) {
    const loginTab = document.getElementById('login-tab');
    const signupTab = document.getElementById('signup-tab');
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

    if (tab === 'login') {
        loginTab.classList.add('text-blue-600', 'border-b-2', 'border-blue-600');
        loginTab.classList.remove('text-gray-500');
        signupTab.classList.remove('text-blue-600', 'border-b-2', 'border-blue-600');
        signupTab.classList.add('text-gray-500');
        loginForm.classList.remove('hidden');
        signupForm.classList.add('hidden');
    } else {
        signupTab.classList.add('text-blue-600', 'border-b-2', 'border-blue-600');
        signupTab.classList.remove('text-gray-500');
        loginTab.classList.remove('text-blue-600', 'border-b-2', 'border-blue-600');
        loginTab.classList.add('text-gray-500');
        signupForm.classList.remove('hidden');
        loginForm.classList.add('hidden');
    }
}

// Form Submission Handlers
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    const rememberMe = document.getElementById('remember-me').checked;

    try {
        const response = await fetch('/api/auth/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email,
                password,
                remember_me: rememberMe
            })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('token', data.token);
            closeAuthModal();
            window.location.reload();
        } else {
            const error = await response.json();
            alert(error.message || 'Login failed. Please try again.');
        }
    } catch (error) {
        console.error('Login error:', error);
        alert('An error occurred during login. Please try again.');
    }
});

document.getElementById('signup-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = {
        name: document.getElementById('signup-name').value,
        email: document.getElementById('signup-email').value,
        password: document.getElementById('signup-password').value,
        confirm_password: document.getElementById('signup-confirm-password').value,
        industry: document.getElementById('signup-industry').value,
        company: document.getElementById('signup-company').value
    };

    if (formData.password !== formData.confirm_password) {
        alert('Passwords do not match');
        return;
    }

    try {
        const response = await fetch('/api/auth/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('token', data.token);
            closeAuthModal();
            window.location.reload();
        } else {
            const error = await response.json();
            alert(error.message || 'Signup failed. Please try again.');
        }
    } catch (error) {
        console.error('Signup error:', error);
        alert('An error occurred during signup. Please try again.');
    }
});

// Close modal when clicking outside
document.getElementById('auth-modal').addEventListener('click', (e) => {
    if (e.target === e.currentTarget) {
        closeAuthModal();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    // Get all tab buttons and forms
    const tabButtons = document.querySelectorAll('.auth-tab');
    const forms = document.querySelectorAll('.auth-form');
    
    // Add click event listener to each tab button
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons and forms
            tabButtons.forEach(btn => btn.classList.remove('active'));
            forms.forEach(form => form.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Show corresponding form
            const tabName = this.getAttribute('data-tab');
            document.getElementById(`${tabName}-form`).classList.add('active');
        });
    });
}); 