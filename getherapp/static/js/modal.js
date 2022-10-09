var modal = document.getElementsByClassName("lec-modal")[0];
var btn = document.getElementsByClassName("test");
var span = document.getElementsByClassName("closebtn")[0];

btn.onclick = function() {
    console.log("dma")
    modal.style.display = "block";
}

function Modal(){
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.addEventListener("click", function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
});
// 백엔드와 합칠 때 모달 기능 더 수정