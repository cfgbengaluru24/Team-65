function rememberUsername() {
    var username = document.getElementById("email").value;
    var rememberCheckbox = document.getElementById("remember");

    if (rememberCheckbox.checked) {
        localStorage.setItem("rememberedUsername", username);
    } else {
        localStorage.removeItem("rememberedUsername");
    }
}

function fillInUsername() {
    var rememberedUsername = localStorage.getItem("rememberedUsername");
    if (rememberedUsername) {
        document.getElementById("email").value = rememberedUsername;
        document.getElementById("remember").checked = true;
    }
}

fillInUsername();

document.getElementById("remember").addEventListener("change", rememberUsername);
document.getElementById("submit").addEventListener("click", rememberUsername);