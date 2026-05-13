// Shared: mobile menu toggle. Navigation is rendered by Django templates.

document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.getElementById("menu-btn");
    const navMenu = document.getElementById("nav-menu");

    if (menuBtn && navMenu) {
        menuBtn.onclick = function () {
            navMenu.classList.toggle("active");
        };
    }
});
