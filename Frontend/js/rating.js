const form = document.getElementById("rating-form");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const params = new URLSearchParams(window.location.search);
    const imdbID = params.get("imdbID");

    const name = document.getElementById("rating-name").value;
    const ratingNumber = Number(document.getElementById("rating-number").value);

    const response = await fetch(
        `http://127.0.0.1:8000/rating`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                id_pelicula: imdbID,
                persona: name,
                calificacion: ratingNumber,
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
            title: "No se pudo guardar la calificacion",
            icon: "error"
        });
        return;
    }

    Swal.fire({
        title: "Calificación enviada correctamente!",
        icon: "success"
    });

    console.log("");
    window.location.href =`movie.html?imdbID=${encodeURIComponent(imdbID)}`;
});

const movieLink = document.getElementById("movie-link");
const params = new URLSearchParams(window.location.search);
const imdbID = params.get("imdbID");
movieLink.href = `movie.html?imdbID=${encodeURIComponent(imdbID)}`;