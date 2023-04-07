# mascotas_blog_2
 > Hecho por Francisco Medina.
  
## Descripcion del Projecto
Esta red social te permite compartir fotos y publicaciones exclusivamente de tus mascotas.<br><br> Intenta recrear lo que sería el ambiente de Pinterest.

## Indice
1. [Estructura](#estructura)
	1. [Apps](#apps)
	2. [Modelos](#modelos)
2. [URLS](#urls)
3. [Instalacion](#instalacion)
4. [Uso de la Pagina](#uso-de-la-pagina)


## Estructura 

- Apps <a name="apps"></a>

	| Nombre | Description | Ejemplos |
	| ----------- | ----------- | ----------- |
	| UserApp | Modelos y metodos referentes al usuario | Login, Profile |
	| FeedApp | Todo lo referente al Feed y a las publicaciones | Ver y Crear publicaciones |
	| ChatApp | Todo lo referente al chat entre dos usuarios | En desarrollo... |

- Modelos <a name="modelos"></a>

	| Nombre | Description | App |
	| ----------- | ----------- | ----------- |
	| CustomUser | Todo lo referente a un Usuario | UserApp |
	| Post | Todo lo referente a una publicacion | FeedApp |
	| Chat | Todo lo referente al chat entre dos usuarios | ChatApp |
	| Message | Contenido de cada mensaje individual | ChatApp | 

## URLS 

- [Admin](http://127.0.0.1:8000/admin) Pagina admin 
- [Home](http://127.0.0.1:8000/) Default page
- [Single Post](http://127.0.0.1:8000/posts/<id_post>) Publicacion individual
- [Crear Post](http://127.0.0.1:8000/crearPost) Para subir publicaciones **Formulario**
- [Search](http://127.0.0.1:8000/search) Para buscar usuarios **Formulario Busqueda**
- [Log in](http://127.0.0.1:8000/login) Log In para el usuario **Formulario**
- [Log Out](http://127.0.0.1:8000/logout) Log Out para el usuario
- [Profile](http://127.0.0.1:8000/profile/) Pagina de la cuenta del usuario
- [Owner](http://127.0.0.1:8000/profile/<user>) Pagina para ver el dueño de un post
- [User Settings](http://127.0.0.1:8000/settings) Editar usuario
- ~~[All Chats](http://127.0.0.1:8000/Chats) Todos los chats~~
- ~~[Single Chat](http://127.0.0.1:8000/Chats/<conversation>) Leer Chat unico~~
- [About Us](http://127.0.0.1:8000/AboutUs/) Pagina sobre el creador
> Los tres que estan tachados estan en desarrollo no se pueden usar

## Instalacion

Esta Branch del repositorio tiene todos los archivos necesarios para usar la pagina en cuanto a bootstrap y templates.<br>
Lo unico que hay que hacer es instalar requirements.txt

Se adjunta la base de datos que ya contiene un superuser 'Profesor'<br>
Password 'ProfesorCoder123' por si se quieren ver opciones extra.

A su vez en la pagina para el login se puede usar un usuario con mismos atributos para su navegacion.

## Uso de la Pagina

La pagina se utiliza exclusivamente desde el navbar y desde la seccion. <br>
Es considerablemente intuitivo de usar, la pagina redirecciona sola todos los links. <br>
Se recomienda realizar alguna publicacion con el usuario para visualizar correctamente las paginas y urls. 

## A Futuro (30/3/2023)

- [x] Delete user
- [x] Delete Post if owner or admin
- [ ] Edit Post if owner
- [ ] Chats
- [ ] Chat unico
























