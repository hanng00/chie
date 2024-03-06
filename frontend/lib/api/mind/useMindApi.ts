import { useAxios } from "@/lib/hooks/useAxios"
import { askMind, listKnowlets } from "./mind"

export const useMindApi = () => {
  const { axiosInstance } = useAxios()

  return {
    askMind: async (question: string) => askMind(question, axiosInstance),
    listKnowlets: async () => listKnowlets(axiosInstance),
  }
}