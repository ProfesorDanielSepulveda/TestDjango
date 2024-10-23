document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector(".login100-form");
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
  
      var username = document.querySelector("input[name='username']").value;
      var password1 = document.querySelector("input[name='password1']").value;
      var password2 = document.querySelector("input[name='password2']").value;
      var usernameError = document.querySelector(".error-message-username");
      var password1Error = document.querySelector(".error-message-password1");
      var password2Error = document.querySelector(".error-message-password2");
  
      // Validación del campo username
      if (username.trim() === "") {
        usernameError.textContent = "El usuario es obligatorio";
        return;
      }
      if (username.length > 150) {
        usernameError.textContent = "El usuario no puede tener más de 150 caracteres";
        return;
      }
      var usernameRegex = /^[a-zA-Z0-9@.+\-_]+$/;
      if (!usernameRegex.test(username)) {
        usernameError.textContent = "El usuario solo puede contener letras, dígitos y los caracteres @/./+/-/_";
        return;
      }
      usernameError.textContent = ""; // Limpiar mensaje de error
  
      // Validación del campo password1
      if (password1.trim() === "") {
        password1Error.textContent = "La contraseña es obligatoria";
        return;
      }
      if (password1.length < 8) {
        password1Error.textContent = "La contraseña debe tener al menos 8 caracteres";
        return;
      }
      var containsNumeric = /\d/.test(password1); // Verifica si la contraseña contiene algún número
      var containsAlpha = /[a-zA-Z]/.test(password1); // Verifica si la contraseña contiene alguna letra
      var containsSpecial = /[^a-zA-Z0-9]/.test(password1); // Verifica si la contraseña contiene algún carácter especial
      if (!containsNumeric || !containsAlpha || !containsSpecial) {
        password1Error.textContent = "La contraseña no cumple con los requisitos necesarios";
        return;
      }
      password1Error.textContent = ""; // Limpiar mensaje de error
  
      // Validación del campo password2
      if (password2.trim() === "") {
        password2Error.textContent = "Debe confirmar la contraseña";
        return;
      }
      if (password1 !== password2) {
        password2Error.textContent = "Las contraseñas no coinciden";
        return;
      }
      password2Error.textContent = ""; // Limpiar mensaje de error
  
      // Envía el formulario si todas las validaciones son exitosas
      form.submit();
    });
  });
  