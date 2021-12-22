$(document).ready(function () {
    $('.pay').click(function (e) {
        $('#spinner').removeAttr("hidden");
        // Przetwarzanie platnosci stripe przez python
        setTimeout(function () {
            $('#spinner').attr("hidden", 'true');
            setTimeout(function () {
                $('.redirect').click();
            }, 500);
        }, 2000);
    })
});