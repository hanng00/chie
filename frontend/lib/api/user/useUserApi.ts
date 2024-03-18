import { useAxios } from "@/lib/hooks/useAxios"
import { getMe, signIn, signUp, signOut } from "./user"
import { userAuthSchema } from "@/lib/validations/auth"
import { z } from "zod"
import { useSupabase } from "@/lib/context/SupabaseProvider"

export const useUserApi = () => {
  const { axiosInstance } = useAxios()
  const { supabase } = useSupabase();


  return {
    getMe: async () => getMe(axiosInstance),
    signUp: async (data: z.infer<typeof userAuthSchema>) => signUp(data, axiosInstance, supabase),
    signIn: async (data: z.infer<typeof userAuthSchema>) => signIn(data, axiosInstance, supabase),
    signOut: async () => signOut(supabase)
  }
}