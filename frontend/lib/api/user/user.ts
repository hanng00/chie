import { userAuthSchema } from "@/lib/validations/auth";
import { SupabaseClient } from "@supabase/supabase-js";
import { AxiosInstance } from "axios";
import { z } from "zod";
import { UserProfile } from "./types";

export const getMe = async (
  axiosInstance: AxiosInstance
): Promise<UserProfile> => {
  const response = await axiosInstance
    .get("/user/me")
    .then((res) => res.data)
    .catch((error) => {
      // Check if we received a 401, if so, the user is not authenticated.
      if (error.response.status === 403) {
        return null
      }
      throw error
    })
  return response
}

export const signUpOLD = async (
  data: z.infer<typeof userAuthSchema>,
  axiosInstance: AxiosInstance,
) => {
  const response = await axiosInstance.post("/user/signup", data)
  return response.data
}


export const signUp = async (
  data: z.infer<typeof userAuthSchema>,
  axiosInstance: AxiosInstance,
  supabase: SupabaseClient
) => {

  const { data: responseData, error } = await supabase.auth.signUp({
    email: data.email,
    password: data.password
  })

  if (error) {
    throw error
  }

  return responseData
}

export const signIn = async (
  data: z.infer<typeof userAuthSchema>,
  axiosInstance: AxiosInstance,
  supabase: SupabaseClient
) => {
  const { data: responseData, error } = await supabase.auth.signInWithPassword({
    email: data.email,
    password: data.password,
  })

  if (error) {
    throw error
  }

  return responseData
}

export const signOut = async (
  supabase: SupabaseClient
) => {
  const { error } = await supabase.auth.signOut()
  if (error) {
    throw error
  }
  return
}