document.addEventListener('DOMContentLoaded', function() {
    fetch('/get_docentes')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.querySelector('#docentes-table tbody');
        data.forEach(docente => {
            const row = document.createElement('tr');
            const fechaNacimiento = new Date(docente.fecha_nacimiento);
            const formattedFechaNacimiento = `${fechaNacimiento.getDate()}-${fechaNacimiento.getMonth() + 1}-${fechaNacimiento.getFullYear()}`;
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
            tableBody.appendChild(row);
        });

        const modal = document.getElementById('modal');
        const span = document.getElementsByClassName('close')[0];
        const updateForm = document.getElementById('update-form');

        span.onclick = function() {
            modal.style.display = "none";
        }

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }

        document.querySelectorAll('.update-button').forEach(button => {
            button.addEventListener('click', function() {
                const id = this.getAttribute('data-id');
                fetch(`/get_docente/${id}`)
                    .then(response => response.json())
                    .then(docente => {
                        Object.keys(docente).forEach(key => {
                            const input = document.getElementById(key);
                            if (input) {
                                if (key === 'fecha_nacimiento') {
                                    // Asumiendo que la fecha viene en formato 'YYYY-MM-DD'
                                    input.value = docente[key].split('T')[0];
                                } else {
                                    input.value = docente[key];
                                }
                            }
                        });
                        modal.style.display = "block";
                    })
                    .catch(error => {
                        console.error('Error al cargar los datos del docente:', error);
                        alert('Error al cargar los datos del docente');
                    });
            });
        });

        updateForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const id = formData.get('id_docente');
            fetch(`/update_docente/${id}`, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Docente actualizado correctamente');
                    modal.style.display = "none";
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

        document.querySelectorAll('.delete-button').forEach(button => {
            button.addEventListener('click', function() {
                const id = this.getAttribute('data-id');
                if (confirm(`¿Estás seguro de que quieres eliminar al docente con ID ${id}?`)) {
                    fetch(`/delete_docente/${id}`, { method: 'DELETE' })
                        .then(response => response.json())
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