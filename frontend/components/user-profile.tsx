import { useUserApi } from "@/lib/api/user/useUserApi";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { Spinner } from "./spinner";
import { Button } from "./ui/button";
import Link from "next/link";
import { useRouter } from "next/navigation";

const UserProfile = () => {
  const router = useRouter();

  const userApi = useUserApi();

  const queryClient = useQueryClient();
  const { data, isLoading } = useQuery({
    queryKey: ["me"],
    queryFn: userApi.getMe,
    
  });

  const { mutate: signOut, isPending } = useMutation({
    mutationFn: userApi.signOut,
    onSuccess: () => {
      router.refresh();
      queryClient.invalidateQueries({ queryKey: ["me"] });
    },
  });

  if (isLoading) {
    return <Spinner />;
  }

  const handleSignOut = () => {
    signOut();
  };

  return (
    <div className="w-md">
      {!data ? (
        <Button asChild variant="outline">
          <Link href="/login">Login</Link>
        </Button>
      ) : (
        <div className="flex flex-row items-center space-x-2">
          <p className="text-sm">{data.email}</p>
          <Button disabled={isPending} variant="link" onClick={handleSignOut}>
            Sign Out
          </Button>
        </div>
      )}
    </div>
  );
};

export default UserProfile;
