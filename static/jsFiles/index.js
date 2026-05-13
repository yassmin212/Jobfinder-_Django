document.addEventListener("DOMContentLoaded", function() {
    const userName = localStorage.getItem("userName");
    const heroSection = document.querySelector(".hero");
    const h1 = document.querySelector(".hero h1");

    if (userName && h1) {
        const welcomeTag = document.createElement("p");
        welcomeTag.innerHTML = `Welcome, <strong>${userName}</strong>`;
        
        welcomeTag.style.color = "#7b4aa1";
        welcomeTag.style.fontSize = "1.5rem";
        welcomeTag.style.marginBottom = "10px";
        welcomeTag.style.fontWeight = "500";

        heroSection.insertBefore(welcomeTag, h1);
    }
});