let isLoggedIn = false
let loggedIn = {}

const isAuthenticated = () => {

    if(localStorage.getItem('loggedIn')){
        isLoggedIn = true
        loggedIn = JSON.parse(localStorage.getItem('loggedIn'))
        document.getElementById('loggedInUser').innerHTML = loggedIn.fullname
        document.getElementById('time').innerHTML = Date(localStorage.getItem('time'))

        document.getElementById('loginForm').style.display = 'none'
        document.getElementById('loginStatus').style.display = 'block'

    }else{
        document.getElementById('loginForm').style.display = 'block'
        document.getElementById('loginStatus').style.display = 'none'
    }

    return isLoggedIn
}

const loginuser = (event) => {
    event.preventDefault()

    let users = JSON.parse(localStorage.getItem('users')) || []

    let requestedUser  = users.filter(item => item.username === document.login.username.value)

    if(requestedUser.length === 0){
        alert('Invalid User')
        console.log(users.filter(item => item.username === document.login.username.value));
    }else{
        if(document.login.password.value === requestedUser[0].password){
            
            let date = new Date().toLocaleString()

            localStorage.setItem('loggedIn', JSON.stringify(requestedUser[0]))
            localStorage.setItem('time', date)

            let obj = {
                username: requestedUser[0].username,
                userid: requestedUser[0].id,
                status: 'Logged In',
                time: date
            }

            let history = []
            if(localStorage.getItem('history')){
                history = JSON.parse(localStorage.getItem('history')) || []
            }

            history.push(obj)
            localStorage.setItem('history', JSON.stringify(history))

            window.location.reload()
        }
    }

}

const logout = () => {
    localStorage.removeItem('loggedIn')
    localStorage.removeItem('time')

    let obj = {
        username: loggedIn.username,
        userid: loggedIn.id,
        status: 'Logged Out',
        time: new Date().toLocaleString()
    }

    let history = []
    if(localStorage.getItem('history')){
        history = JSON.parse(localStorage.getItem('history')) || []
    }
    
    history.push(obj)
    localStorage.setItem('history', JSON.stringify(history))

    window.location.reload()
}