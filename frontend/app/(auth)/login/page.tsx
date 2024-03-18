"use client";

import { buttonVariants } from "@/components/ui/button";
import UserAuthForm from "@/app/(auth)/components/user-auth-form";
import { cn } from "@/lib/utils";
import { Brain, ChevronLeft } from "lucide-react";
import Link from "next/link";
import { userAuthSchema } from "@/lib/validations/auth";
import { z } from "zod";
import { useUserApi } from "@/lib/api/user/useUserApi";
import { useMutation } from "@tanstack/react-query";
import { toast } from "sonner";
import { useRouter } from "next/navigation";

type FormData = z.infer<typeof userAuthSchema>;

const LoginPage = () => {
  const userApi = useUserApi();
  const router = useRouter();
  const { mutate: signIn } = useMutation({
    mutationFn: userApi.signIn,
    onSuccess: (data) => {
      router.push("/");
    },
    onError: (error) => {
      toast.error(error.message);
    },
  });

  const onFormSubmit = (data: FormData) => {
    signIn(data);
  };

  return (
    <div className="container flex h-screen w-screen flex-col items-center justify-center">
      <Link
        href="/"
        className={cn(
          buttonVariants({ variant: "ghost" }),
          "absolute left-4 top-4 md:left-8 md:top-8"
        )}
      >
        <ChevronLeft /> Back
      </Link>
      <div className="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]">
        <div className="flex flex-col space-y-2 text-center">
          <Brain size={64} className="mx-auto" />
          <h1 className="text-2xl font-semibold tracking-tight">
            Welcome back
          </h1>
          <p className="text-sm text-muted-foreground">
            Enter your email to sign in to your accont
          </p>
        </div>

        <UserAuthForm onFormSubmit={onFormSubmit} />

        <p className="px-8 text-center text-sm text-muted-foreground">
          <Link
            href="/register"
            className="underline underline-offset-4 hover:text-brand"
          >
            Don&apos;t have an account? Sign up
          </Link>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;
