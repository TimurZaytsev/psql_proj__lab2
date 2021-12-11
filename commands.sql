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

create function add_to_clients(id integer, name text, surname text, telephone integer)
	returns void language sql as $$
		insert into "clients"(id_client, name, surname, telephone) values (id, name, surname, telephone)
	$$;

create function add_to_branches(id integer, name text, address text, telephone integer)
	returns void language sql as $$
		insert into "branches"(id_branches, name_br, address, telephone) values (id, name, address, telephone)
	$$;

create function add_to_tos(id integer, name text, type text, price integer)
	returns void language sql as $$
		insert into "type_of_services"(id_tos, name_tos, type, price) values (id, name, type, price)
	$$;

create function add_to_services(br_id integer, tos_id integer, cl_id integer, date_ text)
	returns void language sql as $$
		insert into "services"(branch_id, tos_id, client_id, date_of_receipt) values (br_id, tos_id, cl_id, date_)
	$$;
