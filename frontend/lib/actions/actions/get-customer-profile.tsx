import { createStreamableValue } from "ai/rsc";

const getProfile = async (id: string) => {
  return {
    id,
    name: "John Doe",
    customerId: "123",
  };
};

const getSubscriptions = async (customerId: string) => {
  return [
    {
      id: "1",
      customerId,
      name: "Subscription 1",
    },
    {
      id: "2",
      customerId,
      name: "Subscription 2",
    },
  ];
};

export async function getCustomerProfile(id: string) {
  "use server";

  const valueStream = createStreamableValue({
    profile: null as any,
    subscriptions: null as any[] | null,
  });

  (async () => {
    const profile = await getProfile(id);

    valueStream.update({
      profile,
      subscriptions: null,
    });

    const subscriptions = await getSubscriptions(profile.customerId);

    valueStream.done({
      profile,
      subscriptions,
    });
  })();

  return {
    id: Date.now(),
    profile: valueStream.value,
  };
}
