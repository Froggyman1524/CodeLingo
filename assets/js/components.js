function loadComponent(selector, file) {
    fetch(file)
      .then(response => response.text())
      .then(data => {
        document.querySelector(selector).innerHTML = data;
      });
  }
  
  document.addEventListener("DOMContentLoaded", () => {
    loadComponent("#navbar", "../../components/Navbar.html");
  });