$(document).ready(function() {
    $("#submit").click(function() {
        let name = $("#name").val();
        let email = $("#email").val();
        let number = $("#number").val();

        if (name.length == "") {
            $(".error1").text("Это поле обязательно");
            return false;
        } 
        else if (email.length == "") {
            $(".error2").text("Это поле обязательно");
            return false;
        }
        else if (!email.match(/^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/)) {
            $(".error2").text("Неправельный формат почты!");
            return false;
        }
        else if (number.length == "") {
            $(".error3").text("Это поле обязательно");
            return false;
        }
        else if (!number.match(/([0-9])\w+/)) {
            $(".error3").text("Цыфровой ввод");
            return false;
        } else {
            return true;
        }
    }) 
});