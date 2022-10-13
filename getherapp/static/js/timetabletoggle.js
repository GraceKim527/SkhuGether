var found = null;
var index = null;
var day = document.getElementsByName("button");
var test = document.getElementsByClassName("test");


function timetabletoggle() {
    if (found != null) {
        test[index].style.display = 'none';
    }
    
    for (var i = 0; i < day.length; ++i) {
        if (day[i].checked == true) {
            found = day[i];
            console.log(found);
            index = i;
            test[index].style.display = 'block';

        }
    }
}