var jopPositioInput = document.getElementById("jobName");
var jobCampanyInput = document.getElementById("campany");
var jobSalaryInput = document.getElementById("salary");
var jobExperienceInput = document.getElementById("experience");
var jobStatusInput = document.getElementById("options");
var jobTypeInput = document.getElementById("type");

var addBtn = document.querySelector(".btn.w-100");

var jobContainer = [];
var currentIndex = 0;

if (localStorage.getItem("jobs") != null) {
    jobContainer = JSON.parse(localStorage.getItem("jobs"));
    display();
}

function addJOB() {

    var job = {
        name: jopPositioInput.value,
        campany: jobCampanyInput.value,
        salary: jobSalaryInput.value,
        experiance: jobExperienceInput.value,
        status: jobStatusInput.value,
        type: jobTypeInput.value
    };

    if (addBtn.innerHTML == "Update Job") {
        jobContainer[currentIndex] = job;
        addBtn.innerHTML = "Add Job";
    } else {
        jobContainer.push(job);
    }

    localStorage.setItem("jobs", JSON.stringify(jobContainer));

    clearForm();
    display();
}

function display() {
    let cartona = "";

    for (let i = 0; i < jobContainer.length; i++) {

        let statusClass = jobContainer[i].status.toLowerCase();

        cartona += `
        <article class="job-card"
            data-title="${jobContainer[i].name}"
            data-experience="${jobContainer[i].experiance}"
            data-status="${statusClass}">

            <h3>${jobContainer[i].name}</h3>

            <p class="posted-date">
            <strong>Posted:</strong> 22 Feb 2026
            </p>

            <p><strong>Company:</strong> ${jobContainer[i].campany}</p>

            <p><strong>Salary:</strong> ${jobContainer[i].salary} EGP</p>

            <p><strong>Experience Required:</strong> ${jobContainer[i].experiance} Years</p>

            <p><strong>Job Type:</strong> ${jobContainer[i].type}</p>

            <p><strong>Status:</strong>
            <span class="status ${statusClass}">
                ${jobContainer[i].status}
            </span>
            </p>

            <div class="btn-group">
                <a href="job1-details.html">
                    <button class="btn-secondary me-5">View Details</button>
                </a>

                <button onclick="setEdit(${i})" class="btn-edit me-5 bg-warning">Edit</button>

                <button onclick="deleteJob(${i})" class="btn-delete bg-danger">Delete</button>
            </div>

        </article>
        `;
    }

    document.getElementById("jobs-container").innerHTML = cartona;
}
function deleteJob(index) {
    jobContainer.splice(index, 1);
    localStorage.setItem("jobs", JSON.stringify(jobContainer));
    display();
}

function setEdit(index) {
    currentIndex = index;

    jopPositioInput.value = jobContainer[index].name;
    jobCampanyInput.value = jobContainer[index].campany;
    jobSalaryInput.value = jobContainer[index].salary;
    jobExperienceInput.value = jobContainer[index].experiance;
    jobStatusInput.value = jobContainer[index].status;
    jobTypeInput.value = jobContainer[index].type;

    addBtn.innerHTML = "Update Job";
}

function clearForm() {
    jopPositioInput.value = "";
    jobCampanyInput.value = "";
    jobSalaryInput.value = "";
    jobExperienceInput.value = "";
    jobStatusInput.value = "Open";
    jobTypeInput.value = "Full-Time";
}