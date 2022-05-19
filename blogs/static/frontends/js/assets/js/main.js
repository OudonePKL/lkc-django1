/*==================== SCROLL REVEAL ANIMATION ====================*/
const sr = ScrollReveal({
    distance: '60px',
    duration: 2800,
    // reset: true,
})


sr.reveal(`.h-t,.text-hd`, {
    origin: 'top',
    interval: 10,
})

sr.reveal(`.pray`, {
    origin: 'left',
    interval: 100,
})

sr.reveal(`.text-left,.box,.box2`, {
    origin: 'right',
    interval: 200,
})


sr.reveal(`.footer-grid`, {
    origin: 'bottom',
    interval: 100,
})

// /////////////////////////////////////////////