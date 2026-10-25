const url = 'http://127.0.0.1:8000/movies'


function showMovies() {
    let tbody = document.getElementById('movieTableBody')

    let movieTitle = document.getElementById('movieTitle').value
    let movieYear = document.getElementById('movieYear').value

    let final_url = `${url}/${movieTitle}`

    if (movieYear != undefined && movieYear != '')
        final_url = `${final_url}?year=${movieYear}`
    
    fetch(final_url)
        .then(response => {
            return response.json();
        })
        .then(data => {
            filas = '';
            console.log(data.Search);
            console.log(Array.isArray(data.Search));
            data.Search.forEach(element => {
                filas += `
                <tr data-imdb-id="${element.imdbID}" class="movie-row">
                    <td>${element.Title}</td>
                    <td>${element.Year}</td>
                    <td>${element.imdbID}</td>
                    <td>${element.Type}</td>
                    <td>
                        <img 
                            class="poster" 
                            src="${element.Poster}" 
                            alt="${element.Title}"
                            onerror="this.src='img/no_image.png'"
                        >
                    </td>
                </tr>
                `;
            });
            tbody.innerHTML = filas
        }).catch(error =>{
            Swal.fire({
                title: `"Error al cargar los datos:", ${error}`,
                icon: "error"
            });
        });
}

let searchMovies = document.getElementById('btnSearchMovies')
searchMovies.addEventListener("click", showMovies)

let tbody = document.getElementById('movieTableBody')
tbody.addEventListener("click", function(event) {
    const fila = event.target.closest("tr[data-imdb-id]");

    if (!fila) return;

    const imdbID = fila.dataset.imdbId;

    window.location.href =
        `movie.html?imdbID=${encodeURIComponent(imdbID)}`;
});