function checkLogin() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    var correctUsername = "test";
    var correctPassword = "123";

    if (username === correctUsername && password === correctPassword) {
	window.location.href = "main_page.html";
    } 
    else {
        alert("Invalid username or password.");
    }
}
