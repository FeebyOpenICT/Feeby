import { axiosInstance } from './axiosInstance'
class DataService {
  update (id, data) {
    return axiosInstance.put(`/api/v1/ratings/${id}`, data)
  }
}
export default new DataService()
