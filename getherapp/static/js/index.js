//커서 가져다 대면 나머지 반투명해지는거

// 정보과학관
function over(leo_6) {
    leo_6.style.opacity = "0.3"
}
function out(leo_6) {
    leo_6.style.opacity = "1"
}

// 새천년관
function over(leo_7) {
    leo_7.style.opacity = "0.3"
}
function out(leo_7) {
    leo_7.style.opacity = "1"
}

// 나머지
function over(leo_1) {
    leo_1.style.opacity = "0.3"
}
function out(leo_1) {
    leo_1.style.opacity = "1"
}

function over(leo_2) {
    leo_2.style.opacity = "0.3"
}
function out(leo_2) {
    leo_2.style.opacity = "1"
}

function over(leo_3) {
    leo_3.style.opacity = "0.3"
}
function out(leo_3) {
    leo_3.style.opacity = "1"
}

function over(leo_5) {
    leo_5.style.opacity = "0.3"
}
function out(leo_5) {
    leo_5.style.opacity = "1"
}

function over(leo_10) {
    leo_10.style.opacity = "0.3"
}
function out(leo_10) {
    leo_10.style.opacity = "1"
}

function over(leo_11) {
    leo_11.style.opacity = "0.3"
}
function out(leo_11) {
    leo_11.style.opacity = "1"
}

function over(leo_12) {
    leo_12.style.opacity = "0.3"
}
function out(leo_12) {
    leo_12.style.opacity = "1"
}

function over(leo_13) {
    leo_13.style.opacity = "0.3"
}
function out(leo_13) {
    leo_13.style.opacity = "1"
}

// 말주머니
function leo_scn_show() {
    const element = document.getElementById("leo_ala");
    element.innerHTML = '<a href="scn_gwan"><img id="leo_scn" src="static/img/scn.png" alt="새천년관 세부사항" style="display:block;"></a>';
}

function leo_jg_show() {
    const element = document.getElementById("leo_molla");
    element.innerHTML = '<a href="jg_gwan"><img id="leo_jg" src="static/img/jg.png" alt="정보과학관 세부사항" style="display:block;"></a>';
}

function leo_scn_hide() {
    const element = document.getElementById("leo_ala");
    element.innerHTML = '<a href="scn_gwan"><img id="leo_scn" src="static/img/scn.png" alt="새천년관 세부사항" style="display:none;"></a>';
}

function leo_jg_hide() {
    const element = document.getElementById("leo_molla");
    element.innerHTML = '<a href="jg_gwan"><img id="leo_jg" src="static/img/jg.png" alt="정보과학관 세부사항" style="display:none;"></a>';
}


// 토글

const toggleBtn = document.querySelector(".toggle1")
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