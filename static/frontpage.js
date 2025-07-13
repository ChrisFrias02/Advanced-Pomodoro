const settingsBtn = document.getElementById('settingsBtn');
const closeBtn = document.getElementById('close');
const modalContainer = document.getElementById('modal_container');

settingsBtn.addEventListener('click', () => {
    modalContainer.style.display = 'flex';
});

closeBtn.addEventListener('click', () => {
    modalContainer.style.display = 'none';
});

//** 
//document.getElementById("background").addEventListener("click", function() {
// const selector = document.getElementById("backgroundSelector");
// selector.style.display = selector.style.display === "block" ? "none" : "block";
//});


// Set the background when an option is clicked
document.querySelectorAll(".bg-option").forEach(button => {
    button.addEventListener("click", function() {
        const bgFile = this.getAttribute("data-bg");
        document.body.style.backgroundImage = `url('/static/backgrounds/${bgFile}')`;
        document.body.style.backgroundSize = 'cover';
        document.body.style.backgroundPosition = 'center center';
        document.body.style.backgroundRepeat = 'no-repeat';
    });
});