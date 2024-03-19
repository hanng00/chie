import { FlightCard } from "./components/flight-card";
import { z } from "zod";
import { Spinner } from "./components/spinner";

/* ------- DEFINING TOOLS -------- */
export const createGetFlightInfoTool = (aiState: any) => {
  return {
    description: "Get the information for a flight",
    parameters: z
      .object({
        flightNumber: z.string().describe("the number of the flight"),
      })
      .required(),
    render: async function* ({ flightNumber }: { flightNumber: string }) {
      // Show a spinner on the client while we wait for the response.
      yield <Spinner />;

      // Fetch the flight information from an external API.
      const flightInfo = await getFlightInfo(flightNumber);

      // Update the final AI state.
      aiState.done([
        ...aiState.get(),
        {
          role: "function",
          name: "get_flight_info",
          // Content can be any string to provide context to the LLM in the rest of the conversation.
          content: JSON.stringify(flightInfo),
        },
      ]);

      // Return the flight card to the client.
      return <FlightCard flightInfo={flightInfo} />;
    },
  };
};

// An example of a function that fetches flight information from an external API.
async function getFlightInfo(flightNumber: string) {
  return {
    flightNumber,
    departure: "New York",
    arrival: "San Francisco",
  };
}
