function applyJob(jobName){

let appliedJobs =
JSON.parse(localStorage.getItem("appliedJobs")) || [];

if(!appliedJobs.includes(jobName)){

appliedJobs.push(jobName);

}

localStorage.setItem(
"appliedJobs",
JSON.stringify(appliedJobs)
);

alert("Application submitted successfully!");

window.location.href = "/applied-jobs/";

}