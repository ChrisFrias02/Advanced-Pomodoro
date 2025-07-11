//displaying logged in user's profile info
document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('access_token');
    const authButtonSection = document.querySelector(".authButton");
    const profileSection = document.getElementById('profilesection');

    if (token) {
        authButtonSection.style.display = "none";
        profileSection.style.display = "block";

    } else {
        authButtonSection.style.display = "block";
        profileSection.style.display = "none";
    }


    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            localStorage.removeItem('access_token');
            location.reload();
        });
    }
});