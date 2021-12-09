var typingTimer;
const doneTypingInterval = 1000;
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
		data: { currentWord: currentWord },
		success: function (response) {
			console.log(response["items"]);
		},
		error: function (response) {
			console.log(response);
		},
	});
}
