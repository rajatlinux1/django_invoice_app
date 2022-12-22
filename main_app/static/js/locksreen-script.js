const password = '12345';

$('#password').on('focusin', () => {
  $('.arrow').css('display', 'inline-flex');
});

$('.arrow').on('click', () => {
  if($('#password').val().toUpperCase() === password) {
    $('.content').slideUp();
    $('.tbar').css('color', 'black').css('background-color', 'rgb(200,200,200)');
    $('.chrome').css('display', 'block');
  } else {
      $('#password').effect("shake")  }
});