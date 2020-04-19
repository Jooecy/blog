import axios from 'axios'
export function request(config) {
    const instance = axios.create({
 
        withCredentials: true,
        // headers: {'Authorization':localStorage.getItem('logintoken')}
    })
    return instance(config)
}
