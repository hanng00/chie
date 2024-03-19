import { Spinner } from "./spinner";

export enum Step {
  REQUESTED,
  PENDING,
  SUCCESS,
}
type StockDisplayProps = {
  step: Step;
  symbol: string;
  amount: number;
  price: number;
};

const StockDisplay = ({ step, symbol, amount, price }: StockDisplayProps) => {
  return (
    <div className="border border-rounded p-4 inline-flex gap-1">
      {step !== Step.SUCCESS && <Spinner />}
      {step === Step.REQUESTED && (
        <p className="mb-2">
          Purchasing {amount} ${symbol}...
        </p>
      )}
      {step === Step.PENDING && (
        <p className="mb-2">
          Purchasing {amount} ${symbol}... working on it...
        </p>
      )}
      {step === Step.SUCCESS && (
        <p className="mb-2">
          You have successfully purchased {amount} ${symbol}.
          <br />
          <span className="font-bold"> Total cost: ${amount * price} </span>
        </p>
      )}
    </div>
  );
};
export default StockDisplay;
