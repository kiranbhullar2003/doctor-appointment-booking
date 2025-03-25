const loginForm = document.querySelector(".login-form")
const registerForm = document.querySelector(".register-form")
const wrapper = document.querySelector(".wrapper")
const loginTitle = document.querySelector(".title-login")
const registerTitle = document.querySelector(".title-register")
const signUpBtn = document.querySelector("#SignUpBtn")
const signInBtn = document.querySelector("#SignInBtn")

function loginFunction(){
    loginForm.style.left = "50%";
    loginForm.style. opacity = 1;
    registerForm.style.left = "150%";
    registerForm.style. opacity = 0;
    wrapper.style. height ="500px";
    loginTitle.style. top ="50%";
    loginTitle.style. opacity = 1;
    registerTitle.style. top ="50px";
    registerTitle.style. opacity = 0;

}
function registerFunction(){
    loginForm.style.left = "-50%";
    loginForm.style. opacity = 0;
    registerForm.style.left = "50%";
    registerForm.style. opacity = 1;
    wrapper.style. height ="580px";
    loginTitle.style. top ="-60px";
    loginTitle.style. opacity = 0;
    registerTitle.style. top ="50%";
    registerTitle.style. opacity = 1;
    
}




document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.querySelector('.register-form');
    const loginForm = document.querySelector('.login-form');

    // Handle registration
    registerForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(registerForm);
        console.log(formData)
        data = {
            register_username: document.getElementById('register_username').value,
            register_email: document.getElementById('register_email').value,
            register_password: document.getElementById('register_password').value,
            
        }

        console.log(JSON.stringify(formData))

        fetch('http://127.0.0.1:8000/api/register', {
            method: 'POST',
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Registration successful! You can now log in.');
                window.location.replace('/register');
                // Optionally redirect to login page or clear the form
            } else {
                alert('Registration failed: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });

        console.log("akldjflksajdf")
    });

    // Handle login
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(loginForm);
        data = {
            login_username: document.getElementById('login_username').value,
            
            login_password: document.getElementById('login_password').value,
            
        }

        fetch('http://127.0.0.1:8000/api/login', {
            method: 'POST',
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Login successful!');
                window.location.replace('/dashboard');
                // Optionally redirect to another page
            } else {
                alert('Login failed: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

