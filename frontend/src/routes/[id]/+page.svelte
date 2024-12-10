<script lang="ts">
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	import { page } from "$app/stores";
	import { apiUrl } from "$lib/index";
	let object = null;
	let id = $page.params.id;
	async function fetchObject() {
		try {
			const response = await fetch(`${apiUrl}${id}`, {
				method: "GET",
				headers: { "Content-Type": "application/json;charset=utf-8" }
			});
			if (response.ok) {
				object = await response.json();
				object["start_year"] = Number(object.start_datetime.substr(0, 4));
				object["start_month"] = Number(object.start_datetime.substr(5, 2));
				object["start_day"] = Number(object.start_datetime.substr(8, 2));
				object["start_hour"] = Number(object.start_datetime.substr(11, 2));
				object["start_minute"] = Number(object.start_datetime.substr(14, 2));
				object["end_year"] = Number(object.end_datetime.substr(0, 4));
				object["end_month"] = Number(object.end_datetime.substr(5, 2));
				object["end_day"] = Number(object.end_datetime.substr(8, 2));
				object["end_hour"] = Number(object.end_datetime.substr(11, 2));
				object["end_minute"] = Number(object.end_datetime.substr(14, 2));
				delete object["start_datetime"];
				delete object["end_datetime"];
			} else {
				console.error("Ошибка загрузки объекта");
			}
		} catch (error) {
			console.error("Ошибка подключения по id");
		}
	}

	async function saveChanges() {
		const response = await fetch(`${apiUrl}${id}`, {
			method: "PUT",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(object)
		});
		if (response.ok) {
			goto("/");
		} else {
			console.error("Ошибка сохранения изменений");
		}
	}

	onMount(fetchObject);
</script>

<header>
	<div class="header">
		<div class="logo"><img src="logo.svg" /></div>
		<nav>
			<button class="nav-btn">Мероприятия</button>
			<button class="nav-btn">Админ-панель</button>
			<div class="avatar"><img src="avatar.svg" /></div>
		</nav>
	</div>
</header>
<main>
	{#if object}
		<form on:submit|preventDefault={saveChanges}>
			<input type="text" bind:value={object.name} required />
			<textarea bind:value={object.content}></textarea>
			<input type="number" bind:value={object.start_day} min="1" max="31" required />
			<input type="number" bind:value={object.start_month} min="1" max="12" required />
			<input type="number" bind:value={object.start_year} min="2024" required />
			<input type="number" bind:value={object.start_hour} min="0" max="23" required />
			<input type="number" bind:value={object.start_minute} min="0" max="59" required />
			<input type="number" bind:value={object.end_day} min="1" max="31" required />
			<input type="number" bind:value={object.end_month} min="1" max="12" required />
			<input type="number" bind:value={object.end_year} min="2024" required />
			<input type="number" bind:value={object.end_hour} min="0" max="23" required />
			<input type="number" bind:value={object.end_minute} min="0" max="59" required />
			<input type="text" bind:value={object.place} required />
			<input type="text" bind:value={object.tags} required />
			<input type="text" bind:value={object.category} required />

			<button type="submit">Сохранить изменения</button>
		</form>
	{/if}
</main>

<style>
	main {
		padding: 1rem;
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}
	header {
		margin-top: 25px;
		margin-left: 23px;
		margin-right: 23px;
		padding: 18px 37px;
		background: linear-gradient(to right, #fccdcd, #c8aae7);
		border-radius: 60px;
		height: 91;
	}
	.header {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.logo {
		margin-top: 7.5;
		margin-bottom: 7.5;
		margin-left: 19;
	}
	.nav-btn {
		background: white;
		border: none;
		border-radius: 40px;
		padding: 10px 20px;
		cursor: pointer;
	}
	nav {
		display: flex;
	}

	button {
		background: linear-gradient(135deg, rgba(250, 202, 206, 0.5), rgba(200, 170, 231, 0.5));
		border: none;
		padding: 10.5px;
		color: rgba(60, 51, 64, 1);
		border-radius: 10px;
		font-size: 18px;
		cursor: pointer;
		height: 70px;
		transition:
			transform 0.3s,
			box-shadow 0.3s;
	}

	button:hover {
		transform: translateY(-3px);
		box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
	}
</style>
