
document.addEventListener('DOMContentLoaded', () => {
    const navBtns = document.querySelectorAll('.navBtn');
    const darkModeToggle = document.getElementById('dark-mode-toggle');

    function updateActiveState() {
        const currentPath = window.location.pathname;

        navBtns.forEach(btn => {
            const btnPath = btn.parentElement.getAttribute('href');

            if (currentPath === btnPath) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    }
    function toggleDarkMode() {
        const body = document.body;
        const currentMode = body.classList.contains('dark-mode') ? 'dark' : 'light';

        body.classList.toggle('dark-mode');
        if (currentMode === 'light') {
            body.style.backgroundImage = 'url("./images/darkmode.jpg")';

            localStorage.setItem('darkMode', 'enabled');
        } else {
            body.style.backgroundImage = 'url("./images/lightmode.jpg")';

            localStorage.setItem('darkMode', 'disabled');
        }
    }


    updateActiveState();

    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            setTimeout(updateActiveState, 0);
        });
    });

    darkModeToggle.addEventListener('click', toggleDarkMode);
});

document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const aboutUsPageElements = document.getElementsByClassName('aboutUsPage');

    function toggleDarkMode() {
        document.body.classList.toggle('dark-mode');

       
        for (let i = 0; i < aboutUsPageElements.length; i++) {
            if (document.body.classList.contains('dark-mode')) {
                aboutUsPageElements[i].style.color = 'black'; 
            } else {
                aboutUsPageElements[i].style.color = 'white';
            }
        }

        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
        } else {
            localStorage.setItem('darkMode', 'disabled');
        }
    }

    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');

        
        for (let i = 0; i < aboutUsPageElements.length; i++) {
            aboutUsPageElements[i].style.color = 'black'; 
        }
    }

    darkModeToggle.addEventListener('click', toggleDarkMode);
});

let isRoundMoved = false;

function moveRound() {
    let darkModeToggle = document.getElementById('darkModeToggle');
    let currentLeft = parseFloat(window.getComputedStyle(darkModeToggle).left);
    let newLeft = isRoundMoved ? 5 : currentLeft + 40;

    darkModeToggle.style.left = newLeft + 'px';


    darkModeToggle.classList.toggle('dark-mode-toggle-light');
    darkModeToggle.classList.toggle('dark-mode-toggle-dark');

    isRoundMoved = !isRoundMoved;
}

