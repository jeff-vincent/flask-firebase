function postData(url = ``, data = {}) {
    return fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json; charset=utf-8",
        },
        body: JSON.stringify(data),
    })
    .then(response => console.log(response.json()));
}

function signUp() {
    const email = document.getElementById('emailInput').value
    const password = document.getElementById('password').value
    const signUpData = {'email': email, 'password': password}
    postData(`http://0.0.0.0:5000/sign-up`, signUpData)
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error));
}

function logIn() {
    const email = document.getElementById('emailInput').value
    const password = document.getElementById('password').value
    const logInData = {'email': email, 'password': password}
    postData(`http://0.0.0.0:5000/log-in`, logInData)
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error));
}