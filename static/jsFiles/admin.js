
let storedJobs = JSON.parse(localStorage.getItem("jobs")) || [];
document.addEventListener("DOMContentLoaded", function () {
    
    const STORAGE_KEY = "jobs";

    function getJobs() {
        return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
    }

    
    function updateDashboardStats() {
        const jobs = getJobs();
        
        
        const openJobs = jobs.filter(j => j.status && j.status.toString().toLowerCase() === "open").length;
        const closedJobs = jobs.filter(j => j.status && j.status.toString().toLowerCase() === "closed").length;

        const openEl = document.getElementById("open-jobs-count");
        const closedEl = document.getElementById("closed-jobs-count");

       
        if (openEl) openEl.innerText = openJobs;
        if (closedEl) closedEl.innerText = closedJobs;
    }

    
    function renderAdminTable() {
        const tbody = document.querySelector(".admin-main-jobs table tbody");
        if (!tbody) return; 

        const jobs = getJobs();
        tbody.innerHTML = ""; 

        jobs.forEach((job, index) => {
            const row = document.createElement("tr");
            
            
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${job.name || "No Title"}</td>
                <td>${job.salary || "0"} EGP</td>
                <td><span class="status ${(job.status || 'open').toLowerCase()}">${job.status || 'Open'}</span></td>
                <td class="button"> 
                     <button class="btn-edit" onclick="alert('Edit logic coming soon!')">Edit</button> 
                     <button type="button" class="btn-delete" data-index="${index}">Delete</button> 
                </td>
            `;
            tbody.appendChild(row);
        });

        
        attachDeleteEvents();
    }

    
    function attachDeleteEvents() {
        document.querySelectorAll('.btn-delete').forEach(btn => {
            btn.onclick = function() {
                const index = this.getAttribute('data-index');
                if (confirm("هل أنتِ متأكدة من حذف هذه الوظيفة؟")) {
                    let jobs = getJobs();
                    jobs.splice(index, 1); 
                    localStorage.setItem(STORAGE_KEY, JSON.stringify(jobs)); 
                    
                    
                    renderAdminTable();
                    updateDashboardStats();
                }
            };
        });
    }

    
    updateDashboardStats();
    renderAdminTable();
});