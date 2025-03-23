<script lang="ts">
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	import { page } from "$app/stores";
	import { apiUrl } from "$lib/index";
	let object: any;
	object = null;
	let id = $page.params.id;
	const apiUrl1 = `${apiUrl}/list/${id}`;
	async function fetchObject() {
		try {
			const response = await fetch(apiUrl1, {
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
		const response = await fetch(apiUrl1, {
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

	function goToBack() {
		goto("/");
	}
</script>

<header>
	<div class="header">
		<div class="logo"><img src="logo.svg" alt="ITAM" /></div>
		<nav>
			<button class="nav-btn">Мероприятия</button>
			<button class="nav-btn" style="background: white;">Админ-панель</button>
			<div class="avatar"><img src="avatar.svg" alt="avatar" /></div>
		</nav>
	</div>
</header>

<main>
	<button class="back-btn" on:click={() => goToBack()}>
		<img src="Back.svg" alt="Назад" />
	</button>
	{#if object}
		<form on:submit|preventDefault={saveChanges}>
			<label for="title">Название:</label>
			<input id="title" type="text" bind:value={object.name} required />
			<div class="split_new">
				<div class="element">
					<label for="sart_day">День начала:</label>
					<input
						id="sart_day"
						type="number"
						bind:value={object.start_day}
						min="1"
						max="31"
						required
					/>
				</div>
				<div class="element">
					<label for="sart_month">Месяц начала:</label>
					<input
						id="sart_month"
						type="number"
						bind:value={object.start_month}
						min="1"
						max="12"
						required
					/>
				</div>
				<div class="element">
					<label for="sart_year">Год начала:</label>
					<input id="sart_year" type="number" bind:value={object.start_year} min="2024" required />
				</div>

				<div class="element">
					<label for="sart_hour">Время начала:</label>
					<input
						id="sart_hour"
						type="number"
						bind:value={object.start_hour}
						min="0"
						max="23"
						required
					/>
				</div>
				<div class="element">
					<br />
					<input
						id="start_minute"
						type="number"
						bind:value={object.start_minute}
						min="0"
						max="59"
						required
					/>
				</div>
			</div>
			<div class="split_new">
				<div class="element">
					<label for="end_day">День завершения:</label>
					<input id="end_day" type="number" bind:value={object.end_day} min="1" max="31" required />
				</div>
				<div class="element">
					<label for="end_month">Месяц завершения:</label>
					<input
						id="end_month"
						type="number"
						bind:value={object.end_month}
						min="1"
						max="12"
						required
					/>
				</div>
				<div class="element">
					<label for="end_year">Год завершения:</label>
					<input id="end_year" type="number" bind:value={object.end_year} min="2024" required />
				</div>

				<div class="element">
					<label for="end_hour">Время конца:</label>
					<input
						id="end_hour"
						type="number"
						bind:value={object.end_hour}
						min="0"
						max="23"
						required
					/>
				</div>
				<div class="element">
					<br />
					<input
						id="end_minute"
						type="number"
						bind:value={object.end_minute}
						min="0"
						max="59"
						required
					/>
				</div>
			</div>
			<div class="split">
				<div class="element">
					<label for="tag">Тег:</label>
					<select name="select1" id="tag" bind:value={object.tags}>
						<option value="хакатон">хакатон</option>
						<option value="митап">митап</option>
						<option value="воркшоп">воркшоп</option>
					</select>
				</div>
				<div class="element">
					<label for="format">Формат проведение:</label>
					<select name="select" id="format" bind:value={object.category}>
						<option value="онлайн">онлайн</option>
						<option value="офлайн">офлайн</option>
						<option value="онлайн&офлайн">онлайн&офлайн</option>
					</select>
				</div>
				<div class="element">
					<label for="place">Место проведения</label>
					<input id="place" type="text" bind:value={object.place} required />
				</div>
			</div>
			<label for="content">Описание</label>
			<textarea bind:value={object.content} id="content"></textarea>
			<div style="text-align: right;">
				<button type="submit" class="but">Сохранить изменения</button>
			</div>
		</form>
	{/if}
</main>

<style>
	header {
		margin-top: 25px;
		margin-left: 23px;
		margin-right: 23px;
		padding: 18px 37px;
		background: linear-gradient(to right, rgba(252, 205, 205, 1), rgba(200, 170, 231, 1));
		border-radius: 60px;
		font-weight: 500px;
	}
	.header {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.logo {
		margin-top: 7.5px;
		margin-bottom: 7.5px;
		margin-left: 19px;
	}
	.avatar {
		margin-left: 16px;
	}
	.nav-btn {
		border: none;
		border-radius: 40px;
		padding: 10px 20px;
		cursor: pointer;
		font-weight: 500px;
		font-family: "ttnormspro-regular", sans-serif;
		font-size: 18px;
	}
	nav {
		display: flex;
	}
	main {
		margin-left: 60px;
		margin-right: 60px;
		font-size: 27px;
		font-family: "ttnormspro-regular", sans-serif;
		color: rgba(102, 102, 102, 1);
	}
	label {
		margin-bottom: 3px;
	}
	button {
		background: none;
		border: none;
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.back-btn {
		margin-top: 29px;
	}
	.split_new {
		display: grid;
		grid-template-columns: 5fr 5fr 5fr 3fr 3fr;
		gap: 15px;
	}
	.element select {
		border-radius: 20px;
		height: 78px;
		padding: 10px 18px;
		font-size: 27px;
		color: #787878;
		border: 2px solid #808080;
	}
	.but {
		background: linear-gradient(135deg, rgba(250, 202, 206, 0.5), rgba(200, 170, 231, 0.5));
		border: none;
		padding: 9.5px 14px;
		color: rgba(60, 51, 64, 1);
		border-radius: 20px;
		font-size: 18px;
		cursor: pointer;
		transition:
			transform 0.3s,
			box-shadow 0.3s;
		margin-top: 12px;
		font-size: 25px;
		font-weight: 400px;
		color: rgba(60, 51, 64, 1);
	}
	.element {
		display: flex;
		flex-direction: column;
	}
	input {
		border-radius: 20px;
		height: 52px;
		padding: 10px 18px;
		font-size: 27px;
		color: #787878;
		border: 2px solid #808080;
	}
	textarea {
		border-radius: 20px;
		height: 104px;
		padding: 10px 18px;
		font-size: 27px;
		color: #787878;
		border: 2px solid #808080;
	}
	.split {
		display: grid;
		grid-template-columns: 5fr 5fr 5fr;
		gap: 15px;
	}
</style>
