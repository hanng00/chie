import axios, { AxiosError, AxiosInstance, InternalAxiosRequestConfig } from "axios";
import { DEFAULT_BACKEND_URL } from "../config/CONSTANTS";
import { useSupabase } from "../context/SupabaseProvider";


const axiosInstance = axios.create({
  baseURL: `${process.env.NEXT_PUBLIC_BACKEND_URL ?? DEFAULT_BACKEND_URL}`,
})

export const useAxios = (): { axiosInstance: AxiosInstance } => {
  let { session } = useSupabase()
  const { supabase } = useSupabase()

  axiosInstance.interceptors.request.use(
    async (value: InternalAxiosRequestConfig) => {
      const tokenIsNotValid = session?.expires_at && session.expires_at * 1000 < Date.now()

      if (tokenIsNotValid) {
        const { data, error } = await supabase.auth.refreshSession()
        if (error) {
          throw error
        }
        session = data.session
      }
      value.headers["Authorization"] = `Bearer ${session?.access_token ?? ""}`

      return value
    },
    (error: AxiosError) => {
      return Promise.reject(error)
    }
  )

  return { axiosInstance }

}