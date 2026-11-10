/* FLOATING HEARTS */

function createHeart() {

    const heart = document.createElement("div");

    heart.className = "floating-heart";

    const symbols = ["❤️", "💗", "💕", "💖", "✨"];

    heart.innerHTML =
        symbols[Math.floor(Math.random() * symbols.length)];

    heart.style.left =
        Math.random() * 100 + "vw";

    heart.style.fontSize =
        (12 + Math.random() * 25) + "px";

    const duration =
        4 + Math.random() * 5;

    heart.style.animationDuration =
        duration + "s";

    document.body.appendChild(heart);

    setTimeout(() => {
        heart.remove();
    }, duration * 1000);
}


setInterval(createHeart, 400);


/* TYPING EFFECT */

const text =
    "Life is full of ordinary moments, but sometimes a special person can make those moments unforgettable. This little corner of the internet is just a reminder of how beautiful good memories can be. ❤️";

const typingElement =
    document.getElementById("typing");

let index = 0;


function typeText() {

    if (index < text.length) {

        typingElement.innerHTML +=
            text.charAt(index);

        index++;

        setTimeout(typeText, 35);
    }
}


window.addEventListener("load", typeText);


/* SURPRISE */

const surpriseBtn =
    document.getElementById("surpriseBtn");

const surprise =
    document.getElementById("surprise");

const closeBtn =
    document.getElementById("closeBtn");


surpriseBtn.addEventListener("click", () => {

    surprise.classList.add("show");

    /* Extra hearts */

    for (let i = 0; i < 25; i++) {
        setTimeout(createHeart, i * 80);
    }
});


closeBtn.addEventListener("click", () => {

    surprise.classList.remove("show");
});


/* CLICK OUTSIDE */

surprise.addEventListener("click", (event) => {

    if (event.target === surprise) {

        surprise.classList.remove("show");
    }
});