$(document).ready(function () {
    var login_page_move = 0;
    $('#login_button').on('click', function (e) {
        if (login_page_move == 0) {
            login_page_move = 1;
            var elem = document.getElementById("login_progress_bar");
            var width = 1;
            var id = setInterval(frame, 10);
            function frame() {
                if (width >= 100) {
                    clearInterval(id);
                    login_page_move = 0;
                } else {
                    width++;
                    elem.style.width = width + "%";
                    elem.innerHTML = width + "%";
                }
            }
        }
    });
});
