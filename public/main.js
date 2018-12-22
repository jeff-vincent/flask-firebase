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

function sendPost() {
    const email = document.getElementById('emailInput').value
    const userName = document.getElementById('userName').value
    const signUpData = {'email': email, 'userName': userName}
    postData(`http://0.0.0.0:5000/sign-up`, signUpData)
    .then(data => console.log(JSON.stringify(data)))
    .catch(error => console.error(error));
}
