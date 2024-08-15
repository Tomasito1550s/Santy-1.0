document.getElementById("bookingForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el comportamiento por defecto del formulario
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;
    const name = document.getElementById("name").value;

    // Aquí agregarías el código para enviar los datos a tu servidor o base de datos
    console.log(`Fecha: ${date}, Hora: ${time}, Nombre: ${name}`);
    alert("Turno reservado con éxito!");
});
