class MobileNavbar {
    constructor(mobileMenu, mobileMenuex, navList, navLinks) {
      this.body = document.querySelector("body");
      this.mobileMenu = document.querySelector(mobileMenu);
      this.mobileMenuEx = document.querySelector(mobileMenuex);
      this.navList = document.querySelector(navList);
      this.navLinks = document.querySelectorAll(navLinks);
      this.activeClass = "active";
      this.hiddenClass = "hidden";
  
      this.handleClick = this.handleClick.bind(this);
    }
  
    animateLinks() {
      this.navLinks.forEach((link, index) => {
        link.style.animation
          ? (link.style.animation = "")
          : (link.style.animation = `navLinkFade 0.5s ease forwards ${
              index / 7 + 0.3
            }s`);
      });
    }
  
    handleClick() {
      this.navList.classList.toggle(this.activeClass);
      this.mobileMenu.classList.toggle(this.activeClass);
      this.body.classList.toggle(this.hiddenClass);
      this.mobileMenuEx.classList.toggle(this.activeClass);
      this.animateLinks();
    }
  
    addClickEvent() {
      this.mobileMenu.addEventListener("click", this.handleClick);
      this.mobileMenuEx.addEventListener("click", this.handleClick);
    }
  
    init() {
      if (this.mobileMenu) {
        this.addClickEvent();
      }
      return this;
    }
  }
  
  const mobileNavbar = new MobileNavbar(
    ".mobile-menu",
    ".mobile-menu-ex",
    ".nav-list",
    ".nav-list li",
  );
  
  
  mobileNavbar.init();
  
  
  function closeMenu(){
    const menu = document.querySelector(".mobile-menu");
    const menuEx = document.querySelector(".mobile-menu-ex");
    const navList = document.querySelector(".nav-list");
    const body = document.querySelector("body")
  
    menu.classList.remove("active")
    menuEx.classList.remove("active")
    navList.classList.remove("active")
    body.classList.remove("hidden")
    mobileNavbar.animateLinks()
  }


// Menu fixed
var elemento1 = document.getElementById('nav');

// Obtém as dimensões do elemento 1
var largura = elemento1.offsetWidth;
var altura = elemento1.offsetHeight;

// Aplica as dimensões ao elemento 2
var elemento2 = document.getElementById('fixed');
elemento2.style.width = largura + 'px';
elemento2.style.height = altura + 'px';


// Questions

function captElement(elemento) {

  const visibles = document.querySelectorAll('.visible-box');
  var elemento2 = elemento.nextElementSibling;
  
  // Percorre cada div
  visibles.forEach(div => {
    console.log(elemento2)
    console.log('----------')
    console.log(div)
    console.log('////////////')


    if (div ==! elemento2) {
      div.classList.remove('visible-box');
      div.classList.add('hidden-box');
    }
  
  });

  // Modificar a propriedade CSS
  elemento2.classList.toggle("hidden-box");
  elemento2.classList.toggle("visible-box");

}

// Fechar o menu ao clicar fora dele

function toggleDiv(clickedDiv) {
  var clickedContainer = $(clickedDiv).closest(".grid-container");
  var allContainers = $(".grid-container");

  // Fechar todas as outras divs
  allContainers.not(clickedContainer).find(".item").fadeOut(500);

  // Abrir ou fechar a div clicada
  $(clickedDiv).next(".item").slideToggle(400);
}