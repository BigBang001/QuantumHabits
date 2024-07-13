const flashCards = document.querySelectorAll('.flash-card');

flashCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-8px)';
        this.style.boxShadow = '0px 8px 20px rgba(0, 0, 0, 0.2)';
    });

    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
        this.style.boxShadow = '0px 4px 10px rgba(0, 0, 0, 0.1)';
    });
});
