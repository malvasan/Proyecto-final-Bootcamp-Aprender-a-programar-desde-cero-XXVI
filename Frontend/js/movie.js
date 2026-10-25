const url = 'http://127.0.0.1:8000/movie';

const params = new URLSearchParams(window.location.search);
const imdbID = params.get("imdbID");

console.log(imdbID);

function createCommentRows(commentsList) {
    let filas = '';
    commentsList.forEach(element => {
        filas += `
        <tr>
            <td>${element.comentario}</td>
        </tr>
        `
    });
    return filas;
}

function paintStars(rating) {
    let stars = document.getElementsByClassName("star");
    
    const ratingRound = Math.round(Number(rating))

    let cls = "";

    for (let i = 0; i < ratingRound; i++) {
        if (ratingRound == 1) cls = "one";
        else if (ratingRound == 2) cls = "two";
        else if (ratingRound == 3) cls = "three";
        else if (ratingRound == 4) cls = "four";
        else if (ratingRound == 5) cls = "five";
        stars[i].className = "star " + cls;
    }
}


function get_movie() {
    fetch(`${url}/${imdbID}`)
        .then(response => {
            return response.json()
        })
        .then(data => {
            let movieTitle = document.getElementById('movie-title');
            let movieYear  = document.getElementById('movie-year');

            let moviePoster   = document.getElementById('movie-poster');
            let movieDirector = document.getElementById('movie-director');
            let movieGenre    = document.getElementById('movie-genre');
            let movieRuntime  = document.getElementById('movie-runtime');
            let movieImbd     = document.getElementById('movie-imdb');
            let movieLanguage = document.getElementById('movie-language');
            let movieActors   = document.getElementById('movie-actors');
            let moviePlot     = document.getElementById('movie-plot');

            let movieComments = document.getElementById('movie-comments');

            movieTitle.textContent = data.Title
            movieYear.textContent  = data.Year
            moviePoster.src = data.Poster
            moviePoster.alt = data.Title;
            movieDirector.textContent = data.Director
            movieGenre.textContent = data.Genre
            movieRuntime.textContent = data.Runtime
            movieImbd.textContent = data.imdbID
            movieLanguage.textContent = data.Language
            movieActors.textContent = data.Actors
            moviePlot.textContent = data.Plot

            movieComments.innerHTML = createCommentRows(data.comments)
            paintStars(data.avgRating)
        })
        .catch(error => {
            Swal.fire({
                title: `"Error:", ${error}`,
                icon: "error"
            });
    });
}

get_movie();


const buttonComment = document.getElementById("add-comment-btn");
buttonComment.addEventListener("click", ()=>{
    window.location.href = `comment.html?imdbID=${encodeURIComponent(imdbID)}`;
})

const buttonRating = document.getElementById("add-rating-btn");
buttonRating.addEventListener("click", ()=>{
    window.location.href = `rating.html?imdbID=${encodeURIComponent(imdbID)}`;
})