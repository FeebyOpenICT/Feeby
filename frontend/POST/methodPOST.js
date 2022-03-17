import axios from 'axios'
import getCookie from './getCookie'

const axiosInstance = axios.create({
  headers: {"Authorization": `Bearer` ${getCookie("jwt")},

  }
});
