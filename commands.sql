CREATE OR REPLACE FUNCTION create_tab_clients
() RETURNS void AS $$
create table if not exists "clients"(
id_client integer primary key,
name text not null,
surname text not null,
telephone integer,
total_money integer
);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION create_tab_branches
() RETURNS void AS $$
create table if not exists "branches"(
id_branches integer primary key,
name_br text not null,
address text not null,
telephone integer
);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION create_tab_types_of_services
() RETURNS void AS $$
create table if not exists "type_of_services"(
id_tos integer primary key,
name_tos text not null,
type text not null,
price integer
);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION create_tab_services
() RETURNS void AS $$
create table if not exists "services"(
branch_id INTEGER REFERENCES branches (id_branches),
tos_id INTEGER REFERENCES type_of_services (id_tos),
client_id INTEGER REFERENCES clients (id_client),
date_of_receipt text
);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION get_clients ()
    RETURNS TABLE(id_client integer, name text, surname text, telephone integer, total_money integer)
    AS $$
    select * from clients;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION get_branches ()
    RETURNS TABLE(id_branches integer, name_br text, address text, telephone integer)
    AS $$
    select * from branches;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION get_tos ()
    RETURNS TABLE(id_tos integer, name_tos text, type text, price integer)
    AS $$
    select * from type_of_services;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION get_services ()
    RETURNS TABLE(branch_id integer, tos_id integer, client_id integer, date_of_receipt text)
    AS $$
    select * from services;
$$ LANGUAGE sql;
