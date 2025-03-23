<script lang="ts">
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	import { apiUrl } from "$lib/index";
	import axios from "axios";
	let objects: any[];
	objects = [];
	async function fetchObjects() {
		try {
			const response = await fetch(`${apiUrl}/list`, {
				credentials: "same-origin",
				method: "GET",
				headers: { "Content-Type": "application/json" }
			});
			objects = await response.json();
		} catch (error) {
			console.error("Ошибка загрузки", error);
			throw error;
		}
	}
	let activeButton: string = "events_main";
	function setActiveButton(button: string) {
		activeButton = button;
	}

	onMount(async () => {
		await fetchObjects();
	});

	function goToAddPage() {
		goto("/create_event");
	}

	function goToObjectPage(id: number) {
		goto(`/${id}`);
	}
	function goToObjectPageMore(id: number) {
		goto(`/${id}/more`);
	}

	async function deleteEvent(id: number) {
		try {
			const response = await fetch(`${apiUrl}/list/${id}`, {
				method: "DELETE",
				headers: { "Content-Type": "application/json" }
			});
			if (response.ok) {
				objects = objects.filter(obj => obj.id !== id);
			} else {
				const error = await response.json();
				alert("Error: " + error.message);
			}
		} catch (error) {
			console.error("Error: ", error);
		}
	}
</script>

<header>
	<div class="header">
		<div class="logo"><img src="logo.svg" alt="ITAM" /></div>
		<nav>
			<button
				class="nav-btn {activeButton === 'events_main' ? 'active' : ''}"
				on:click={() => setActiveButton("events_main")}>Мероприятия</button
			>
			<button
				class="nav-btn {activeButton === 'admin' ? 'active' : ''}"
				on:click={() => setActiveButton("admin")}>Админ-панель</button
			>
			<div class="avatar"><img src="avatar.svg" alt="avatar" /></div>
		</nav>
	</div>
</header>

<main>
	{#if activeButton === "admin"}
		<h1>Админ-панель</h1>
		<div class="container">
			<div class="controls">
				<div class="dropdown">
					<select>
						<option>Выбрать категорию</option>
					</select>
				</div>
				<div class="dropdown">
					<select>
						<option>Формат проведения</option>
					</select>
				</div>
				<img src="search.svg" alt="Поиск" />
				<input type="text" placeholder="Поиск" style="border: none;" />
			</div>
			<button on:click={goToAddPage} class="goAdd">+ Добавить событие</button>
		</div>
		<table>
			<thead class="super_title">
				<tr>
					<th style="border-radius: 50px 0 0 50px;">Название</th>
					<th>Дата события</th>
					<th>Статус</th>
					<th style="border-radius: 0px 50px 50px 0px;">Изменить</th>
				</tr>
			</thead>
			<tbody>
				{#each objects as obj (obj.id)}
					<tr>
						<td class="event-tag">{obj.name}</td>
						<td>{obj.start_datetime}</td>
						<td>
							<select>
								<option>Опубликовано</option>
							</select>
						</td>
						<td>
							<button on:click={() => goToObjectPage(obj.id)}>
								<img src="edit.svg" style="margin-right: 38px;" class="edit" alt="edit" />
							</button>
							<button on:click={() => deleteEvent(obj.id)}>
								<img src="trash.svg" class="trash" alt="trash" /></button
							>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	{:else if activeButton === "events_main"}
		<h1>Мероприятия</h1>
		<div class="container">
			<div class="controls">
				<div class="dropdown">
					<select>
						<option>Выбрать категорию</option>
					</select>
				</div>
				<div class="dropdown">
					<select>
						<option>Формат проведения</option>
					</select>
				</div>
				<img src="search.svg" alt="Поиск" />
				<input type="text" placeholder="Поиск" style="border: none;" />
			</div>
		</div>
		<table>
			<tbody>
				{#each objects as obj (obj.id)}
					<tr>
						<td style="weight=114px; font-sizt: 20px;">{obj.start_datetime}</td>
						<td
							class="event-tag"
							style="text-align: center; weight=400px; font-sizt: 34px; color: rgba(0, 0, 0, 1)"
							>{obj.name}</td
						>
						<td>
							<button on:click={() => goToObjectPageMore(obj.id)} class="GOto">Перейти →</button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	{/if}
</main>

<style>
	.controls {
		display: flex;
		gap: 10px;
		align-items: center;
		margin-bottom: 20px;
	}

	.controls input {
		flex-grow: 1;
		padding: 5px 10px;
		border: 1px solid #ccc;
		border-radius: 4px;
	}

	.controls .dropdown select {
		padding: 8px;
		border: none;
		border-radius: 4px;
		background-color: white;
		cursor: pointer;
	}

	main {
		margin-left: 60px;
		margin-right: 60px;
		font-family: "ttnormspro-regular", sans-serif;
		color: rgba(102, 102, 102, 1);
	}
	header {
		margin-top: 25px;
		margin-left: 23px;
		margin-right: 23px;
		padding: 18px 37px;
		background: linear-gradient(to right, rgba(252, 205, 205, 1), rgba(200, 170, 231, 1));
		border-radius: 60px;
	}
	.header {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.container {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	option {
		border: none;
		appearance: none;
	}
	.logo {
		margin-top: 7.5px;
		margin-bottom: 7.5px;
		margin-left: 19px;
	}
	.nav-btn {
		background: none;
		border: none;
		border-radius: 40px;
		padding: 10px 20px;
		cursor: pointer;
		font-weight: 500px;
		font-family: "ttnormspro-regular", sans-serif;
		font-size: 18px;
	}
	.nav-btn.active {
		background: white;
		border: none;
		border-radius: 40px;
		padding: 10px 20px;
		cursor: pointer;
	}
	nav {
		display: flex;
	}
	.avatar {
		margin-left: 16px;
	}
	h1 {
		color: rgba(60, 51, 64, 1);
		font-family: "cygre-medium", sans-serif;
		margin-bottom: 28px;
	}
	.goAdd {
		background: linear-gradient(135deg, rgba(250, 202, 206, 0.5), rgba(200, 170, 231, 0.5));
		border: none;
		padding: 13px;
		color: rgba(60, 51, 64, 1);
		border-radius: 20px;
		font-size: 18px;
		cursor: pointer;
		transition:
			transform 0.3s,
			box-shadow 0.3s;
	}

	table {
		width: 100%;
		border-collapse: collapse;
		margin-top: 3px;
	}
	.super_title {
		background: linear-gradient(135deg, rgba(250, 202, 206, 0.5), rgba(200, 170, 231, 0.5));
		margin-top: 22px;
		height: 73px;
		padding: 80.5px;
		text-align: center;
	}
	table tr {
		padding: 17px 90px;
		text-align: center;
		font-size: 22px;
		margin-right: 80px;
	}
	table td {
		padding: 17px 29px;
		text-align: center;
		border-bottom: 2px solid #787878;
		font-size: 22px;
	}
	td select {
		border: 2px solid rgba(120, 120, 120, 0.8);
		border-radius: 10px;
		padding: 9px 19px;
	}

	button {
		background: none;
		border: none;
	}

	.GOto {
		border: 2px solid rgba(250, 202, 206, 0.5);
		padding: 9px 47.75px;
		border-radius: 20px;
	}
</style>
