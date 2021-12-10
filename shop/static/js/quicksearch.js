var typingTimer;
const doneTypingInterval = 200;
$(document).ready(function () {
    $("#quicksearch").on("input", function (e) {
        clearTimeout(typingTimer);
        if ($("#quicksearch").val()) {
            typingTimer = setTimeout(sendAjax, doneTypingInterval);
        }
    });
});

function sendAjax() {
    var currentWord = $("#quicksearch").val();
    $.ajax({
        type: "GET",
        url: "/quicksearch/",
        data: {currentWord: currentWord},
        success: function (response) {
            addSearches(response["items"]);
        },
        error: function (response) {
            console.log(response);
        },
    });
}

function addSearches(items) {
    $(".generated").html('');
    items.forEach(function (item) {
        console.log(item)
        $('#searches').append(`<li class="generated"><a href="/listings/${item.id}">
							<p class=\'dropdown-item text-truncate\'>
							<img class="img-fluid" width="50px" height="50px" src="${item.image}"></img>
							 ${item.name}</p></a>
							</li>\n`)
    })
}