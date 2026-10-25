const form = document.getElementById("comment-form");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const params = new URLSearchParams(window.location.search);
    const imdbID = params.get("imdbID");

    const name = document.getElementById("comment-name").value;
    const comment = document.getElementById("comment-text").value;

    const response = await fetch(
        `http://127.0.0.1:8000/comment`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                id_pelicula: imdbID,
                persona: name,
                comentario: comment,
                fecha: new Date().toISOString()
            })
        }
    ).catch(error => {
            Swal.fire({
                title: `"Error:", ${error}`,
                icon: "error"
            });
    });

    if (!response.ok) {
            Swal.fire({
                title: "No se pudo guardar el comentario",
                icon: "error"
            });
            return;
        }
    
    Swal.fire({
        title: "Comentario enviado correctamente!",
        icon: "success"
    });

    window.location.href =`movie.html?imdbID=${encodeURIComponent(imdbID)}`;
});

const movieLink = document.getElementById("movie-link");
const params = new URLSearchParams(window.location.search);
const imdbID = params.get("imdbID");
movieLink.href = `movie.html?imdbID=${encodeURIComponent(imdbID)}`;