




function saAnnadir(form) {
  var a ;
  a = form
  console.log(a[6].value)
  var cantidad = a[6].value
  if (cantidad <= 0) {
    Swal.fire({
      icon: 'error',
      title: 'No se puede añadir el producto'
    })
  }
  else{
  Swal.fire({
    icon: 'success',
    title: 'Producto añadido',
    showConfirmButton: true
        }).then ((result) =>{

          if(result.isConfirmed){
            form.submit()
          }else {
            form.submit()
          }
        })
      }
  
    
}

var a ;

function confirmSuscripcion(form) {
  
  a = form
  console.log(a)
  alert('hola')
  Swal.fire({
    icon: 'success',
    title: 'Suscripcion añadida',
    showConfirmButton: true
        }).then ((result) =>{

          if(result.isConfirmed){
            form.submit()
          }else {
            form.submit()
          }
        })
      }
  
    



function confirmacionProd(codigo) {
  console.log(codigo)
    Swal.fire({
        icon: 'warning',
        title: '¿Estas seguro?',
        showConfirmButton: true,
        showCancelButton: true,
        }) .then ((result) => {
          console.log(result)
          if (result.isConfirmed) {
            Swal.fire ({
              icon: 'success',
              title: 'Eliminado con exito!',
            }) .then (() => {
              window.location.href =window.location.origin+"/eliminar_prod/"+codigo
            }) 
          }console.log('jknefkjn')

        })
        
}


function confirmacionUser(run) {

  Swal.fire({
      icon: 'warning',
      title: '¿Estas seguro?',
      showConfirmButton: true,
      showCancelButton: true,
      }) .then ((result) => {
        if (result.isConfirmed) {
          Swal.fire ({
            icon: 'success',
            title: 'Eliminado con exito!',
          }) .then (() => {
            window.location.href =window.location.origin+"/eliminar_user/"+run
          }) 
        }console.log('jknefkjn')

      })
      
}


function confirmacionSeg(cod_seguimiento) {

  Swal.fire({
      icon: 'warning',
      title: '¿Estas seguro?',
      showConfirmButton: true,
      showCancelButton: true,
      }) .then ((result) => {
        if (result.isConfirmed) {
          Swal.fire ({
            icon: 'success',
            title: 'Eliminado con exito!',
          }) .then (() => {
            window.location.href =window.location.origin+"/eliminar_user/"+run
          }) 
        }console.log('jknefkjn')

      })
      
}


function prohibido() {

    Swal.fire({ 
        icon: 'error',
        title: 'Para ingresar aquí debes iniciar sesión',
        showConfirmButton: false,
        timer: 1400
      })
  }

  function login() {
    Swal.fire({
        title: 'Login Form',
        html: `<input type="text" id="login" class="swal2-input" placeholder="Username">
        <input type="password" id="password" class="swal2-input" placeholder="Password">`,
        showCancelButton: true, 
        confirmButtonText: 'Enviar',
        cancelButtonText: 'Cerrar',
        footer: `<a href="`+window.location.origin+'/registro'+`">¿Todavía no tienes cuenta?</a>`,
        
        focusConfirm: false,
        preConfirm: () => {
          const login = Swal.getPopup().querySelector('#login').value
          const password = Swal.getPopup().querySelector('#password').value
          if (!login || !password) {
            Swal.showValidationMessage(`Por favor ingresa el usuario y la contraseña`)
          }
          return { login: login, password: password }
        }
      }).then((result) => {
        console.log(result)
        if (result.isConfirmed) {
          Swal.fire({ 
            icon: 'success',
            title: 'Has ingresado con exito!',
            showConfirmButton: false,
            timer: 1700
            
          }) .then(() => {
            window.location = window.location.origin+"/index";
          })
        } 
        
        
        
      })
  }


  function desuscribir(){

    Swal.fire({
      title: '¿Estas seguro de querer cancelar la suscripción?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Listo',
          'Ya no te encuentras suscrito',
          'success'
        )
      }
    })
  

  }


  