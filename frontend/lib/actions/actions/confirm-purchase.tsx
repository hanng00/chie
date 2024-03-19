import { createStreamableUI } from "ai/rsc";
import { Spinner } from "../components/spinner";
import StockDisplay, { Step } from "../components/stock-display";

const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

const getStockPrice = (symbol: string) => {
  // Random value between 50 and 200
  return Math.floor(Math.random() * 150) + 50;
};

export async function confirmPurchase(symbol: string, amount: number) {
  "use server";
  const spinner = <Spinner />;
  const price = getStockPrice(symbol);

  const uiStream = createStreamableUI(
    <StockDisplay
      step={Step.REQUESTED}
      symbol={symbol}
      amount={amount}
      price={price}
    />
  );

  // This async function is immediately invoked but it will not block the
  // return statement. Because of that, the client will receive the initial
  // UI immediately and then the updates will be streamed later.
  (async () => {
    await sleep(1000);

    uiStream.update(
      <StockDisplay
        step={Step.PENDING}
        symbol={symbol}
        amount={amount}
        price={price}
      />
    );

    await sleep(1000);

    uiStream.done(
      <StockDisplay
        step={Step.SUCCESS}
        symbol={symbol}
        amount={amount}
        price={price}
      />
    );
  })();

  return {
    id: Date.now(),
    display: uiStream.value,
  };
}
