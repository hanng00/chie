import { Knowlet } from "@/lib/types/Mind";
import { AxiosInstance } from "axios";

export const askMind = async (
  questions: string,
  axiosInstance: AxiosInstance
): Promise<Knowlet[]> => {
  const response = await axiosInstance.post("/mind/ask", {
    question: questions
  })
  return response.data
}

export const listKnowlets = async (axiosInstance: AxiosInstance): Promise<Knowlet[]> => {
  const response = await axiosInstance.get("/mind/knowlets", { method: "GET" })
  return response.data
}