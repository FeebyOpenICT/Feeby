import { axiosInstance } from './axiosInstance'
class DataService {
  update (id, data) {
    return axiosInstance.patch(`/api/v1/ratings/${id}`, data)
  }
}
export default new DataService()
