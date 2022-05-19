# College app :rocket:

## College app es un API-RESTFUL creado con python y su framework por exelencia para desarrollo web, Django; este proyecto también usa una de las bases de datos relacionales más populares en la actualidad, PostgreSQL (La cual ya está en línea y disponible para su uso, sea precavido). College app es una aplicación creada a manera de ser escalable mediante la implementación de servicios a la espera de ser restringidos con JWT y ser validados con middlewares; además, usa JSON y previemente ha sido configurada para la implementación de CORS.

## Servicios y peticiones ✏️
### Para las peticiones de tipo CRUD, se usa el formato JSON. También puede importar el archivo 'college_project.postman_collection.json' dentro de postman para probar las peticiones, ahí va a encontar de manera segmentada la información y con respectivos ejemplos. 

### 1). COURSE:

  
  #### -GET 'api/course/<int:course_id>/', retorna la información de un determinado curso.
  
  #### -GET 'api/course/homework/<int:course_id>/', retorna la información de todas las tareas asignadas a un de un determinado curso.
  
  #### -POST 'api/course/homework/', crea una nueva tarea y la asigna a un curso.
  

### 2). STUDENT


  #### -GET 'api/student/<int:course_id>/', retorna la información de todos los estudiantes de un determinado curso.
  
  #### -GET 'api/student/submission/<int:course_id>/', retorna la información de todos los entregas de un trabajo de un determinado curso.
  
  #### -PUT 'api/student/submission/<int:id_submission>/', edita en valor de grade (calificación) de una determinada entrega.
  
  #### -POST 'api/student/submission/', crea una nueva entrega.  


### 3). TEACHER
  
  
  #### -GET 'api/teacher/<int:teacher_id>/', retorna la información de un determinado profesor.
  
## Por último, espero est proyecto halla sido de su agrado y no presentase dificultades.

## Contact Me

[![Gmail Badge](https://img.shields.io/badge/-juan.gamez1001@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:juan.gamez1001@gmail.com)](mailto:juan.gamez1001@gmail.com)
[![Linkedin Badge](https://img.shields.io/badge/-Sebastian-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/sebastian-gamez-ariza-0963b7228/)](https://www.linkedin.com/in/sebastian-gamez-ariza-0963b7228/)
[![Twitter Badge](https://img.shields.io/badge/-@culturaDmacondo-00acee?style=flat&logo=Twitter&logoColor=white)](https://twitter.com/CulturaDmacondo "Follow on Twitter")
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white&link=https://github.com/SebastianGamez)](https://github.com/SebastianGamez)
  
  
