import type { Metadata, Viewport } from "next";
import "@/styles/globals.css";
import { ThemeProvider } from "@/components/providers/theme-provider";
import { cn } from "@/lib/utils";
import { Poppins as FontSans } from "next/font/google";
import App from "./App";
import { SupabaseProvider } from "@/lib/context/SupabaseProvider/supabase-provider";
import getServerSupabaseClient from "@/lib/helpers/getServerSupabaseClient";

export const metadata: Metadata = {
  title: "Chie",
  description: "Bring life to learning",
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  interactiveWidget: "resizes-content",
};

const fontSans = FontSans({
  subsets: ["latin"],
  weight: ["400", "700"],
  variable: "--font-sans",
});

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const supabase = getServerSupabaseClient();

  const {
    data: { session },
  } = await supabase.auth.getSession();

  return (
    <html lang="en">
      <body
        className={cn("h-dvh bg-background antialiased", fontSans.variable)}
      >
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <SupabaseProvider session={session}>
            <App>{children}</App>
          </SupabaseProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
