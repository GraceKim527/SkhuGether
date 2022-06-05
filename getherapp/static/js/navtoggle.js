const toggleBtn = document.querySelector(".toggle2")
const ul = document.querySelector(".nav-links")
const li = document.querySelectorAll(".nav-links li")


function toggleHandler() {
    toggleBtn.classList.toggle("toggleAnimation")
    ul.classList.toggle("nav-active")
    
    li.forEach((link, index) => {
        console.log(link, index)
        if (link.style.animation) {
            link.style.animation = "";
        } else {
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 10 + 1}s`;
        }
    })
}

function init() {
    toggleBtn.addEventListener("click", toggleHandler)

}

init()