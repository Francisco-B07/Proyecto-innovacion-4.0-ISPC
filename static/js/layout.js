const botonesEliminar = document.querySelectorAll(".boton-eliminar");

if (botonesEliminar) {
  const botonesArray = Array.from(botonesEliminar);
  botonesArray.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (!confirm("¿Estas seguro de eliminar este álbum?")) {
        e.preventDefault();
      }
    });
  });
}
