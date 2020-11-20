//Существует много способов выбрать DOM узел; здесь мы получаем форму и электронную почту
//поле ввода, а также элемент span, в который мы поместим сообщение об ошибке.
var form  = document.getElementById('registration');
var login = document.getElementById('login');
var error = document.querySelector('.error');
var pass1 = document.getElementById('password');
var pass2 = document.getElementById('password2');


pass1.addEventListener("input", (event)=>{
    if (pass1.value.length > 6){
        error.innerHTML = ""; // Сбросить содержимое сообщения
        error.className = "error"; // Сбросить визуальное состояние сообщения
    }  
}, false);

pass2.addEventListener("input", (event)=>{

    if (pass2.value==pass1.value){
        error.innerHTML = ""; // Сбросить содержимое сообщения
        error.className = "error"; // Сбросить визуальное состояние сообщения
    }   
},false);

login.addEventListener("input", function (event) {
    if (login.value.length > 3){
        error.innerHTML = ""; // Сбросить содержимое сообщения
        error.className = "error"; // Сбросить визуальное состояние сообщения
    }

 // Каждый раз, когда пользователь вводит что-либо, мы проверяем,
  // является ли корректным поле электронной почты.
  
}, false);

form.addEventListener("submit", function (event) {
  if (login.value.length <= 3) {    
    error.innerHTML = "Sorry, login must be at least 4 char long";
    error.className = "error active";
    // И мы предотвращаем отправку формы путем отмены события
    event.preventDefault();
  } else if (pass1.value.length <= 6){
        error.innerHTML = "Sorry, password is too short";
        error.className = "error active";
        // И мы предотвращаем отправку формы путем отмены события
        event.preventDefault();
    } else if (pass1.value != pass2.value){
        error.innerHTML = "Sorry, passwords don't match";
        error.className = "error active";
        // И мы предотвращаем отправку формы путем отмены события
        event.preventDefault();
      }  
      
  

}, false);
