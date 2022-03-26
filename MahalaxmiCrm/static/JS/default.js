const addUser = (event) => {
    event.preventDefault();

    let fullname = document.adduser.fullname.value
    let username = document.adduser.username.value
    let password = document.adduser.password.value
    let utype = document.adduser.utype.value
    
    let user = {
        id: Date.now(),
        fullname,
        username,
        password,
        utype
    }

    let users = []

    if(localStorage.getItem("users")){
        users = JSON.parse(localStorage.getItem("users"))
    }

    users.push(user)
    localStorage.setItem("users", JSON.stringify(users))

    document.adduser.reset()

    alert('Operation Successfull')

    console.log(users);
}


const setHistory = () => {
    let history  = JSON.parse(localStorage.getItem('history') || '[]')

    let table = document.getElementById('historyTable')

    history.forEach(item => {
        let tr = document.createElement('tr')
        let id = document.createElement('td')
        id.textContent = item.userid
        let username = document.createElement('td')
        username.textContent = item.username
        let status = document.createElement('td')
        status.textContent = item.status
        if(item.status === 'Logged In')
            status.style.color = 'green'
        else
            status.style.color = 'red'

        let time = document.createElement('td')
        time.textContent = item.time

        tr.appendChild(id)
        tr.appendChild(username)
        tr.appendChild(time)
        tr.appendChild(status)

        table.appendChild(tr)

    });

}


const setUsers = () => {
    let history  = JSON.parse(localStorage.getItem('users') || '[]')

    let table = document.getElementById('historyTable')

    history.forEach(item => {
        let tr = document.createElement('tr')
        let id = document.createElement('td')
        id.textContent = item.id
        let username = document.createElement('td')
        username.textContent = item.username

        let buttonCell = document.createElement('td')

        let button = document.createElement('button')
        button.classList.add('btn')
        button.classList.add('bg-primary')
        button.classList.add('text-white')
        button.textContent = "Change"

        button.addEventListener('click', () => setUserToChange(item))

        buttonCell.appendChild(button)
        
        tr.appendChild(id)
        tr.appendChild(username)
        tr.appendChild(buttonCell)

        table.appendChild(tr)

    });

}

let userToChangeId = ''

const setUserToChange = (user) => {
    document.getElementById('passwordCard').style.display = 'block'
    userToChangeId = user.id
    document.getElementById('user').innerHTML = 'Set Password For : '+ user.fullname
}

const changePassword = () => {
    let users  = JSON.parse(localStorage.getItem('users') || '[]')
    
    users = users.map(item => {
        
        if(item.id === userToChangeId){
            item.password = document.getElementById('newPass').value
        }
        
        return item
    })

    localStorage.setItem('users', JSON.stringify(users))

    document.getElementById('newPass').value = ''

    alert('Password Changed...!')

} 