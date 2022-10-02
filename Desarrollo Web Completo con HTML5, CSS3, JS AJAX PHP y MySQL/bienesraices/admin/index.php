<?php
    require '../includes/funciones.php';
    incluirTemplate('header');
?>

    <main class="contenedor seccion">
        <h1>Administrador de bienes Raíces</h1>

        <a href="/admin/propiedades/crear.php" class="boton boton-verde">Nueva propiedad</a>
        <a href="/admin/propiedades/actualizar.php" class="boton boton-verde">Actualizar propiedad</a>
        <a href="/admin/propiedades/borrar.php" class="boton boton-verde">Borrar propiedad</a>
    </main>

<?php 
    incluirTemplate('footer');
?>