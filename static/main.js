console.log("JavaScript is linked correctly!");

//Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

//Toggle for mobile menu
const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('nav ul');

menuToggle.addEventListener('click', () => {
  nav.classList.toggle('active');
});

//Form validation
document.querySelector('form').addEventListener('submit', function(e) {
  const name = document.querySelector('#name').value;
  if (name.trim() === '') {
    alert('Please enter your name.');
    e.preventDefault();
  }
});

