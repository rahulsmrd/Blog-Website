var like = $('.like');
like.on('click', function () {
    if (like.hasClass('bi-heart')) {
        like.removeClass('bi-heart');
        like.addClass('bi-heart-fill');
        like.css('color', 'red');
    }
    else {
        like.removeClass('bi-heart-fill');
        like.addClass('bi-heart');
        like.css('color', 'black');
    }
});
