//커서 가져다 대면 나머지 반투명해지는거

// 승연관
function over(leo_1) {
    leo_1.style.opacity = "0.3"
}
function out(leo_1) {
    leo_1.style.opacity = "1"
}

// 일만관
function over(leo_2) {
    leo_2.style.opacity = "0.3"
}
function out(leo_2) {
    leo_2.style.opacity = "1"
}

// 월당관
function over(leo_3) {
    leo_3.style.opacity = "0.3"
}
function out(leo_3) {
    leo_3.style.opacity = "1"
}

// 나눔관
function over(leo_5) {
    leo_5.style.opacity = "0.3"
}
function out(leo_5) {
    leo_5.style.opacity = "1"
}

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

// 중앙도서관
function over(leo_8) {
    leo_8.style.opacity = "0.3"
}
function out(leo_8) {
    leo_8.style.opacity = "1"
}


// 성미가엘성당 / 피츠버그홀
function over(leo_9) {
    leo_9.style.opacity = "0.3"
}
function out(leo_9) {
    leo_9.style.opacity = "1"
}

// 미가엘관
function over(leo_11) {
	leo_11.style.opacity = "0.3"
}
function out(leo_11) {
    leo_11.style.opacity = "1"
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



// PC 모달

function change() {
	document.getElementById('modal').style.display = "flex";
	document.getElementsByClassName('modal-window')[0].style.display = "flex";
}
function change1() {
	document.getElementById('modal').style.display = "none";
	document.getElementsByClassName('modal-window')[0].style.display = "none";
}
