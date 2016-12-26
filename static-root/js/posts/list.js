
$(document).ready(function () {
    $.ajax({
        url:"/api/",
        method: "GET",
        success: function (data) {
            $.each(data, function (key, value) {
                console.log(value);
                var k = key;
                var content = value.content;
                var user = value.user;
                $("#list").append(
                    "<li>"+content+"</li>"
                )
            })
        },
        error: function (data) {
            console.log("error");
        }
    })
})
