function showCert(certId) {
    // Logic to show certificate details or handle display
    alert("Showing certificate: " + certId);
}

document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('header nav a');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
        });
    });
});
