# App web demo Django
Web de demostración de habilidades en Django

## Instalación
Se recomienda crear un entorno virtual e instalar "requirement.txt" asi como la base de datos incluida en el proyecto "FQBD.sql" con las credenciales User:root Pass:root

## El proyecto
Este proyecto se realizó con Django como framework backend, PostgreSQL como BD y otros elementos como Bootstrap, ajax, tensorflow-keras... dividido en 4 apps:

- **mypage:**     Carpeta de inicio de Django

  - **mainpage:**   Pagina de inicio
  - **store:**      App web de ventas de productos online
  - **mlearn:**     Muestra de clasificador de imágenes con machine learning
  - **users:**      Gestor de usuarios

  
##### Credenciales de administrador
- **User:** root
- **Password:** root

Elementos empaquetados:

- **Static**
- **Templates**
- **Views**

### Store
Se creo una pantalla incial como catalogo de productos dodne es posible seleccionar los productos y agregar a un carro de compras el cual posteriormente puede ser modificado, una vez el usuario este ocnforme con la compra pasara a una pantalla de compra; los usuarios tienen dos modalidades de compra

<img src="https://github.com/fquezadageldres/Fq_Django_Demo/blob/master/Store.PNG" width="300"> <img src="https://github.com/fquezadageldres/Fq_Django_Demo/blob/master/Cart.PNG" width="300"> <img src="https://github.com/fquezadageldres/Fq_Django_Demo/blob/master/Pay.PNG" width="300">

- **Anónimo**:
-Los usuarios pueden ingresar y comprar los productos los cuales se almacenan por medio de cookies en su navegador, luego pueden agregar manualmente sus datos de envío y pago para hacer efectiva la compra
 - **Usuario registrado**:
 -Los usuarios pueden iniciar sesión y los datos de compra se grabaran en la base de datos, pudiendo interrumpir la compra y continuarla en otro momentos, una vez finalizada la compra los datos de envío se completan automáticamente con la información del usuario registrada en la BD

 
 Para efectos prácticos se pueden usar las credenciales de administrador o las siguientes.
  - **User:** visitante
  - **Password:** contraseña
  
  ### Mlearn
Desarrollo de red neuronal convolucional y su deploy web, el cual consiste en un clasificador de imágenes con tres categorías, al agregar una imagen el modelo podrá predecir si en la imagen hay un Gato, un Perro o algo que no es ni gato ni perro

<img src="https://github.com/fquezadageldres/Fq_Django_Demo/blob/master/p003.PNG" width="500">

#### Modelo
El modelo se entreno en 300 ciclos de 100 pasos cada uno, con un total de 30.000.- imagenes
- Accurracy final de validacion : 0.8515
- Costo de perdida : 0.3613

<img src="https://github.com/fquezadageldres/Fq_Django_Demo/blob/master/Model_Accu_p003_3classes.png" width="300"> <img src="https://github.com/fquezadageldres/Fq_Django_Demo/blob/master/Model_Loss_p003_3classes.png" width="300">

## Proximos desarrollos

- [ ] Agregar Paypal como medio de pago en store
- [ ] Agregar pantalla de vista individual de productos
- [ ] implementar formulario de contacto y su envió por e-mail
- [ ] Implemente modelo de machine learning clasificar de nombre con Árbol de decisión

  
  
  


