$(document).ready(function () {
    $('.addToCart').click(function (e) {
        addToCart($(this).attr("data-id"));
    })
    $('.deleteFromCart').click(function (e) {
        deleteFromCart($(this).attr("data-id"));
    })
    $('.setItemQuantityValue').change(function (e) {
        setItemQuantityValue($(this).attr("data-id"), this.value);
    })
    $('.deleteFavorite').click(function (e) {
        deleteFavorite($(this).attr("data-id"), this.value);
    })
    $('.add_to_favorite').click(function (e) {
        add_to_favorite($(this).attr("data-id"), this.value);
    })

    let device = getCookie('device')
    if (device == null) {
        device = uuidv4()
    }
    document.cookie = 'device=' + device + ";domain=;path=/"
});

function addToCart(id) {
    $.ajax({
        type: "POST",
        url: "/updateCart/",
        data: {
            'item': id,
            'csrfmiddlewaretoken': window.CSRF_TOKEN,
            'action': "add",
        },
        success: function (response) {
            console.log(response);
        },
        error: function (response) {
            console.log(response);
        },
    });
}

function deleteFromCart(id) {
    $.post({
        url: "/updateCart/",
        data: {
            'item': id,
            'csrfmiddlewaretoken': window.CSRF_TOKEN,
            'action': "delete",
        },
        success: function (response) {
            location.reload();
        },
        error: function (response) {
            console.log(response);
        },
    });
}

function setItemQuantityValue(id, value) {
    $.post({
        url: "/updateCart/",
        data: {
            'item': id,
            'csrfmiddlewaretoken': window.CSRF_TOKEN,
            'action': "set",
            'quantity': value,
        },
        success: function (response) {
            location.reload();
        },
        error: function (response) {
            console.log(response);
        },
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function add_to_favorite(id) {
    $.post({
        url: "/accounts/addFavorite/",
        data: {
            'item': id,
            'csrfmiddlewaretoken': window.CSRF_TOKEN,
        },
        success: function (response) {
            location.reload();
        },
        error: function (response) {
            console.log(response);
        },
    });
}

function deleteFavorite(id) {
    $.post({
        url: "/accounts/deleteFavorite/",
        data: {
            'item': id,
            'csrfmiddlewaretoken': window.CSRF_TOKEN,
        },
        success: function (response) {
            location.reload();
        },
        error: function (response) {
            console.log(response);
        },
    });
}

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}
