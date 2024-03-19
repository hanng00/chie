type FlightInfo = {
  flightNumber: string;
  departure: string;
  arrival: string;
};

export function FlightCard({ flightInfo }: { flightInfo: FlightInfo }) {
  return (
    <div className="p-2 border rounded-md w-xl">
      <h2 className="font-bold">Flight Information</h2>
      <p>Flight Number: {flightInfo.flightNumber}</p>
      <p>Departure: {flightInfo.departure}</p>
      <p>Arrival: {flightInfo.arrival}</p>
    </div>
  );
}
