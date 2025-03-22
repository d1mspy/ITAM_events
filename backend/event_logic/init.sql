create table event(
	id uuid primary key,
	created_at timestamp not null,
	updated_at timestamp not null,
	name text not null,
	start_datetime timestamp not null,
	end_datetime timestamp not null,
	place text not null,
	content text not null,
	category text,
	tags text,
	max_people integer
);

create table user_data(
	id uuid primary key,
	created_at timestamp not null,
	updated_at timestamp not null,
	email text not null,
	surname text not null,
	age integer not null,
	user_group text
);

create table registered_users(
	id uuid primary key,
	created_at timestamp not null,
	updated_at timestamp not null,
	user_id text not null,
	event_id text not null
);
