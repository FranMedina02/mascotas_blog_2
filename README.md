# mascotas_blog_2
 > Hecho por Francisco Medina.
  
## Descripcion del Projecto
Esta red social te permite compartir fotos y publicaciones exclusivamente de tus mascotas.<br><br> Intenta recrear lo que sería el ambiente de Pinterest.

## [Video](https://drive.google.com/file/d/13fZkdxaXEJnBBCzJvcLecNWOXg1gob8j/view?usp=sharing)



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
- [Register](http://127.0.0.1:8000/register/) Crear usuario **Formulario**
- [Log Out](http://127.0.0.1:8000/logout) Log Out para el usuario
- [Profile](http://127.0.0.1:8000/profile/) Pagina de la cuenta del usuario
- [Owner](http://127.0.0.1:8000/profile/<user>) Pagina para ver el dueño de un post
- [Delete User](http://127.0.0.1:8000/delete) Confirmacion para borrar cuenta
- [User Settings](http://127.0.0.1:8000/settings) Editar cuenta
- [User Settings](http://127.0.0.1:8000/settings) Editar usuario
- [All Chats](http://127.0.0.1:8000/Chats) Todos los chats
- [Single Chat](http://127.0.0.1:8000/Chats/<conversation>) Leer Chat unico
- [About Us](http://127.0.0.1:8000/AboutUs/) Pagina sobre el creador

## Instalacion

<b>[Se adjunta un zip con todo el proyecto para solucionar el tema de las imagenes de los posteos y de los avatares. Sino tambien se pueden usar las otras opciones mencionadas posteriormente.](https://drive.google.com/file/d/1F0CSSB1r2oE5E5vIC_dhKX-imf6Z5zo5/view?usp=sharing)</b>

El repositorio *NO* tiene todos los archivos necesarios para usar la pagina en cuanto a bootstrap y base de datos.<br>
Lo unico que hay que hacer es instalar requirements.txt

## Uso de la Pagina

La pagina se utiliza exclusivamente desde el navbar y desde la seccion. <br>
Es considerablemente intuitivo de usar, la pagina redirecciona sola todos los links. <br>
Se recomienda realizar alguna publicacion con el usuario para visualizar correctamente las paginas y urls. 

## A Futuro (10/4/2023)

- [x] Delete user
- [x] Delete Post if owner or admin
- [ ] Edit Post if owner
- [x] Chats
- [x] Chat unico
- [ ] Likes
























