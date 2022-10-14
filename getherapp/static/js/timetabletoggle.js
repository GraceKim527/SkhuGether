// var found = null;
// var index = null;
// var day = document.getElementsByName("button");
// var test = document.getElementsByClassName("test");


// function timetabletoggle() {
//     if (found != null) {
//         test[index].style.display = 'none';
//     }
    
//     for (var i = 0; i < day.length; ++i) {
//         if (day[i].checked == true) {
//             found = day[i];
//             console.log(found);
//             index = i;
//             test[index].style.display = 'block';

//         }
//     }
// }

$('input[type=radio]').on('click', function(){
    var chkValue = $('input[type=radio]:checked').val();

    if (chkValue == '월') {
        $('#mon').css('display', 'block');
        $('#tue').css('display', 'none');
        $('#wed').css('display', 'none');
        $('#thu').css('display', 'none');
        $('#fri').css('display', 'none');
    }
    else if (chkValue == '화') {
        $('#mon').css('display', 'none');
        $('#tue').css('display', 'block');
        $('#wed').css('display', 'none');
        $('#thu').css('display', 'none');
        $('#fri').css('display', 'none');
    }
    else if (chkValue == '수') {
        $('#mon').css('display', 'none');
        $('#tue').css('display', 'none');
        $('#wed').css('display', 'block');
        $('#thu').css('display', 'none');
        $('#fri').css('display', 'none');
    }
    else if (chkValue == '목') {
        $('#mon').css('display', 'none');
        $('#tue').css('display', 'none');
        $('#wed').css('display', 'none');
        $('#thu').css('display', 'block');
        $('#fri').css('display', 'none');
    }
    else if (chkValue == '금') {
        $('#mon').css('display', 'none');
        $('#tue').css('display', 'none');
        $('#wed').css('display', 'none');
        $('#thu').css('display', 'none');
        $('#fri').css('display', 'block');
    }
})