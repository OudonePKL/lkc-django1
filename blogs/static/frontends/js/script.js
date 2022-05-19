'use strict';

const navbarNav = document.querySelector('.navbar-nav');
const navbarToggleBtn = document.querySelector('.nav-toggle-btn');

navbarToggleBtn.addEventListener('click', function() {

    navbarNav.classList.toggle('active');
    this.classList.toggle('active');

    if (toggle && nav) {
        toggle.addEventListener('click', () => {
            nav.classList.toggle('show')
        })
    }

    function linkAction() {
        /*Active link*/
        navLink.forEach(n => n.classList.remove('active'));
        this.classList.add('active');

        /*Remove menu mobile*/
        const navMenu = document.getElementById('nav-menu')
        navMenu.classList.remove('show')
    }
    navLink.forEach(n => n.addEventListener('click', linkAction));
});