-- Arme P&B: stato dell'app (dieta e palestra) per utente, protetto da RLS.
create table if not exists public.app_state (
  user_id    uuid not null default auth.uid() references auth.users(id) on delete cascade,
  key        text not null check (key in ('diet', 'gym')),
  value      jsonb not null,
  updated_at timestamptz not null default now(),
  primary key (user_id, key)
);

alter table public.app_state enable row level security;

drop policy if exists "app_state: solo i propri dati" on public.app_state;
create policy "app_state: solo i propri dati" on public.app_state
  for all to authenticated
  using (user_id = (select auth.uid()))
  with check (user_id = (select auth.uid()));

create or replace function public.app_state_touch() returns trigger
language plpgsql set search_path = '' as $$
begin new.updated_at := now(); return new; end $$;

drop trigger if exists app_state_touch on public.app_state;
create trigger app_state_touch before insert or update on public.app_state
  for each row execute function public.app_state_touch();
