import axios, { AxiosInstance, InternalAxiosRequestConfig } from "axios";
import { DEFAULT_BACKEND_URL } from "../config/CONSTANTS";


const axiosInstance = axios.create({
  baseURL: `${process.env.NEXT_PUBLIC_BACKEND_URL ?? DEFAULT_BACKEND_URL}`,
})

export const useAxios = (): { axiosInstance: AxiosInstance } => {
  // TODO - Add Session / Auth here

  axiosInstance.interceptors.request.use(
    async (value: InternalAxiosRequestConfig) => {
      const token = "NOT-IMPLEMENTED"
      value.headers["Authorization"] = `Bearer ${token}`

      return value
    }
  )

  return { axiosInstance }

}