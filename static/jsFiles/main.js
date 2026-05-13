// shared items like navbar

document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.getElementById('menu-btn');
    const navMenu = document.getElementById('nav-menu');
    
    if (menuBtn && navMenu) {
        menuBtn.onclick = function() {
            navMenu.classList.toggle('active');
        };
    }

    const userName = localStorage.getItem("userName");  
    const userRole = localStorage.getItem("userRole"); 
    const navMenuUl = document.querySelector("#nav-menu ul");

    if (userName && userRole && navMenuUl) {
        let links = `<li><a href="index.html">Home</a></li>`;

        if (userRole === "admin") {
            links += `
                <li><a href="admin-dashboard.html">Dashboard</a></li>
                <li><a href="jobs.html">Company Jobs</a></li>
                <li><a href="add-job.html">Add New Job</a></li>
            `;
        } 
        else {
            links += `
                <li><a href="jobs.html">Find Jobs</a></li>
                <li><a href="applied-jobs.html">Applied Jobs</a></li>
            `;
        }
        
        links += `
           
            <li><a href="#" id="logout-btn">Logout</a></li>
        `;

        navMenuUl.innerHTML = links;

        document.getElementById("logout-btn").addEventListener("click", function(e) {
            e.preventDefault();
            localStorage.removeItem("userName");
            localStorage.removeItem("userRole");
            window.location.href = "index.html"; 
        });
    }
});