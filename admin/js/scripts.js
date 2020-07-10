const buttonMovie = document.getElementById('movies')
const formMovie = document.getElementById('content-form')
const close = document.getElementById('close')
buttonMovie.addEventListener('click', () => {
	formMovie.classList.remove('hide')
})

close.addEventListener('click', () => {
	formMovie.classList.add('hide')
})