$('.button1').on({
  'click': function () {
    $("#change-image")
      .fadeOut(500, function () {
        $('#change-image').attr('src', '/img/pluto_2048.webp');
      })
      .fadeIn(500);

  }
});

$('.button2').on({
  'click': function () {
    $("#change-image")
      .fadeOut(500, function () {
        $('#change-image').attr('src', '/img/jupiter_2048.webp');
      })
      .fadeIn(500);

  }
});