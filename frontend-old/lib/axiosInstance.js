import axios from 'axios'
import getCookie from './getCookie'

export const axiosInstance = axios.create({
  headers: { Authorization: `Bearer ${getCookie('jwt')}` }
})
