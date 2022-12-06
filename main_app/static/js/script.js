let sighnUpButton = document.querySelector('#signUp');
let sighnInButton = document.querySelector('#signIn');
let container = document.querySelector('#container');


sighnUpButton.addEventListener('click', () => {
 container.classList.add('right-panel-active');
});
sighnInButton.addEventListener('click', () => {
 container.classList.remove('right-panel-active');
});