document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.menu-item');

    menuItems.forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('data-target');
            const submenu = document.getElementById(targetId);

            if (submenu.style.display === 'flex') {
                submenu.style.display = 'none';
            } else {
                submenu.style.display = 'flex';
            }
        });
    });

    const submenuItems = document.querySelectorAll('.submenu a');

    submenuItems.forEach(item => {
        item.addEventListener('click', function() {
            const submenus = document.querySelectorAll('.submenu');
            submenus.forEach(submenu => {
                submenu.style.display = 'none';
            });
        });
    });
});