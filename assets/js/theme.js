document.addEventListener("DOMContentLoaded", function() {
    var toggleSwitch = document.getElementById('toggle-color-mode');
    if (toggleSwitch) {
        toggleSwitch.addEventListener('change', function() {
            if (this.checked) {
                document.documentElement.setAttribute('data-bs-theme', 'dark');
            } else {
                document.documentElement.setAttribute('data-bs-theme', 'light');
            }
        });
    }
});