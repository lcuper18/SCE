document.addEventListener('DOMContentLoaded', function() {
    // Realiza una solicitud fetch para obtener la lista de docentes desde el servidor
    fetch('/get_docentes')
    .then(response => response.json()) // Convierte la respuesta a formato JSON
    .then(data => {
        const tableBody = document.querySelector('#docentes-table tbody'); // Selecciona el cuerpo de la tabla donde se insertarán los datos
        data.forEach(docente => {
            const row = document.createElement('tr'); // Crea una nueva fila para cada docente
            const fechaNacimiento = new Date(docente.fecha_nacimiento); // Convierte la fecha de nacimiento a un objeto Date
            const formattedFechaNacimiento = `${fechaNacimiento.getDate()+1}-${fechaNacimiento.getMonth()+1}-${fechaNacimiento.getFullYear()}`; // Formatea la fecha de nacimiento
            row.innerHTML = `
                <td>${docente.id_docente}</td>
                <td>${docente.nombre}</td>
                <td>${docente.apellido1}</td>
                <td>${docente.apellido2}</td>
                <td>${docente.telefono}</td>
                <td>${docente.email}</td>
                <td>${formattedFechaNacimiento}</td>
                <td>${docente.edad}</td>
                <td>${docente.direccion}</td>
                <td>
                    <button class="play-button update-button" data-id="${docente.id_docente}">Actualizar</button>
                    <button class="play-button delete-button" data-id="${docente.id_docente}">Eliminar</button>
                </td>
            `;
            tableBody.appendChild(row); // Agrega la fila a la tabla
        });

        const modal = document.getElementById('modal'); // Selecciona el modal
        const span = document.getElementsByClassName('close')[0]; // Selecciona el botón de cierre del modal
        const updateForm = document.getElementById('update-form'); // Selecciona el formulario de actualización

        // Cierra el modal cuando se hace clic en el botón de cierre
        span.onclick = function() {
            modal.style.display = "none";
        }

        // Cierra el modal si se hace clic fuera de él
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }

        // Agrega un evento de clic a todos los botones de actualización
        document.querySelectorAll('.update-button').forEach(button => {
            button.addEventListener('click', function() {
                const id = this.getAttribute('data-id'); // Obtiene el ID del docente desde el atributo data-id
                fetch(`/get_docente/${id}`) // Realiza una solicitud fetch para obtener los datos del docente
                    .then(response => response.json()) // Convierte la respuesta a formato JSON
                    .then(docente => {
                        Object.keys(docente).forEach(key => {
                            const input = document.getElementById(key); // Selecciona el campo de entrada correspondiente
                            if (input) {
                                if (key === 'fecha_nacimiento') {
                                    // Asumiendo que la fecha viene en formato 'YYYY-MM-DD'
                                    input.value = docente[key].split('T')[0]; // Establece el valor del campo de fecha de nacimiento
                                } else {
                                    input.value = docente[key]; // Establece el valor del campo de entrada
                                }
                            }
                        });
                        modal.style.display = "block"; // Muestra el modal
                    })
                    .catch(error => {
                        console.error('Error al cargar los datos del docente:', error);
                        alert('Error al cargar los datos del docente');
                    });
            });
        });

        // Agrega un evento de envío al formulario de actualización
        updateForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Previene el comportamiento predeterminado del formulario
            const formData = new FormData(this); // Crea un objeto FormData con los datos del formulario
            const id = formData.get('id_docente'); // Obtiene el ID del docente
            fetch(`/update_docente/${id}`, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json()) // Convierte la respuesta a formato JSON
            .then(data => {
                if (data.success) {
                    alert('Docente actualizado correctamente');
                    modal.style.display = "none"; // Cierra el modal
                    // Aquí podrías recargar la tabla o actualizar la fila específica
                } else {
                    alert('Error al actualizar el docente');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al actualizar el docente');
            });
        });

        // Agrega un evento de clic a todos los botones de eliminación
        document.querySelectorAll('.delete-button').forEach(button => {
            button.addEventListener('click', function() {
                const id = this.getAttribute('data-id'); // Obtiene el ID del docente desde el atributo data-id
                if (confirm(`¿Estás seguro de que quieres eliminar al docente con ID ${id}?`)) {
                    fetch(`/delete_docente/${id}`, { method: 'DELETE' }) // Realiza una solicitud fetch para eliminar el docente
                        .then(response => response.json()) // Convierte la respuesta a formato JSON
                        .then(data => {
                            if (data.success) {
                                alert('Docente eliminado correctamente');
                                // Aquí podrías eliminar la fila de la tabla
                            } else {
                                alert('Error al eliminar el docente');
                            }
                        })
                        .catch(error => {
                            console.error('Error:', error);
                            alert('Error al eliminar el docente');
                        });
                }
            });
        });
    });
});