// Wait for the page to load
document.addEventListener("DOMContentLoaded", function() {
    
    const loginForm = document.getElementById("loginForm");
    const signupForm = document.getElementById("signupForm");

    // ----- LOGIN VALIDATION -----
    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {
            event.preventDefault(); 
            
            const uname = document.getElementById("uname").value.trim();
            const pword = document.getElementById("pword").value.trim();
            const msgBox = document.getElementById("login-msg");

            if (uname === "" || pword === "") {
                msgBox.textContent = "Error: Please fill in all fields.";
                msgBox.style.color = "red";
            } else {
                localStorage.setItem("userName", uname);
                let role = uname.toLowerCase().includes("admin") ? "admin" : "user";
                localStorage.setItem("userRole", role);
                msgBox.textContent = "Success! Redirecting...";
                msgBox.style.color = "green";
                
                // For now, assume login goes to normal jobs page. 
                setTimeout(() => { window.location.href = "index.html";}, 1000);
            }
        });
    }

    // ----- SIGNUP VALIDATION -----
    if (signupForm) {
        signupForm.addEventListener("submit", function(event) {
            event.preventDefault(); 
            
            const fname = document.getElementById("fname").value.trim();
            const lname = document.getElementById("lname").value.trim();
            const uname = document.getElementById("Username").value.trim();
            const email = document.getElementById("email").value.trim();
            const pword1 = document.getElementById("CPword").value.trim();
            const pword2 = document.getElementById("CPword2").value.trim();
            const isAdmin = document.getElementById("admin_checkbox").checked;
            const msgBox = document.getElementById("signup-msg");

            if (fname === "" || lname === "" || uname === "" || email === "" || pword1 === "" || pword2 === "") {
                msgBox.textContent = "Error: Please fill in all required fields.";
                msgBox.style.color = "red";
                return;
            }

            if (pword1.length < 8) {
                msgBox.textContent = "Error: Password must be at least 8 characters.";
                msgBox.style.color = "red";
                return;
            }

            if (pword1 !== pword2) {
                msgBox.textContent = "Error: Passwords do not match.";
                msgBox.style.color = "red";
                return;
            }

            // --- CONNECTING MY WORK TO HAMZA, USE GET ITEM FOR ADMIN  ---
            if (isAdmin) {
                // Save "admin" to browser memory for Hamza to use later
                localStorage.setItem("userRole", "admin");
                localStorage.setItem("userName", fname);
                msgBox.textContent = "Success! Admin Account created. Redirecting to Admin Dashboard...";
                msgBox.style.color = "green";
                
                // Redirects to admin.html (Yasmine/Hamza will build this page)
                setTimeout(() => { window.location.href = "index.html"; }, 1500);
            } else {
                // Save "user" to browser memory
                localStorage.setItem("userRole", "user");
                localStorage.setItem("userName", fname);
                msgBox.textContent = "Success! User Account created. Redirecting to Jobs...";
                msgBox.style.color = "green";
                
                // Redirects to normal jobs page
                setTimeout(() => { window.location.href = "index.html"; }, 1500);
            }
        });
    }
});
