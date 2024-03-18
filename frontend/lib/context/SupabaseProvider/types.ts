import { SupabaseClient, Session } from '@supabase/supabase-js';


export type SupabaseContextType = {
  supabase: SupabaseClient;
  session: Session | null;
};