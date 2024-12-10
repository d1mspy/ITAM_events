<script lang="ts">
	import { goto } from "$app/navigation";
	import { apiUrl } from "$lib/index";
	let name: string = "";
	let content: string = "";
	let start_year: number;
	let start_month: number;
	let start_day: number;
	let start_hour: number;
	let start_minute: number;
	let end_year: number;
	let end_month: number;
	let end_day: number;
	let end_hour: number;
	let end_minute: number;
	let place: string = "";
	let category: string = "";
	let tags: string = "";
	$: newObject = {
		name,
		start_year,
		start_month,
		start_day,
		start_hour,
		start_minute,
		end_year,
		end_month,
		end_day,
		end_hour,
		end_minute,
		place,
		content,
		category,
		tags
	};

	async function saveObject(newObject) {
		// const newObject = { name,  start_year, start_month, start_day,start_hour, start_minute,
		//   end_year, end_month, end_day, end_hour,end_minute,place, content, category,tags };
		try {
			const response = await fetch(`${apiUrl}`, {
				method: "POST",
				headers: { "Content-Type": "application/json;charset=utf-8" },
				body: JSON.stringify(newObject)
			});
			if (response.ok) {
				goto("/");
			} else {
				console.error("Ошибка сохранения объекта");
			}
		} catch (error) {
			console.error("Ошибка подключения");
		}
	}

	function cancel() {
		goto("/");
	}
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
	<h1>Админ-панель</h1>
	<img src="Стрелка.svg" class="back" on:click={cancel} />
	<form on:submit|preventDefault={saveObject(newObject)}>
		<label>Название</label>
		<input type="text" bind:value={name} required />
		<label>День</label>
		<div class="split">
			<input type="number" bind:value={start_day} min="1" max="31" required />

			<input type="number" bind:value={start_month} min="1" max="12" required />

			<input type="number" bind:value={start_year} min="2024" required />

			<input type="number" bind:value={start_hour} min="0" max="23" required />

			<input type="number" bind:value={start_minute} min="0" max="59" required />
		</div>
		<label>День</label>
		<div class="split">
			<input type="number" bind:value={end_day} min="1" max="31" required />
			<input type="number" bind:value={end_month} min="1" max="12" required />
			<input type="number" bind:value={end_year} min="2024" required />
			<input type="number" bind:value={end_hour} min="0" max="23" required />
			<input type="number" bind:value={end_minute} min="0" max="59" required />
		</div>
		<div class="split_new">
			<div class="element">
				<label>Тег</label><br />
				<input type="text" bind:value={tags} required />
			</div>
			<div class="element">
				<label>Формат проведение</label><br />
				<input type="text" bind:value={category} required />
			</div>
			<div class="element">
				<label>Место проведения</label><br />
				<input type="text" bind:value={place} required />
			</div>
		</div>
		<label>Описание</label>
		<textarea bind:value={content}></textarea>
		<button type="submit">Сохранить</button>
	</form>
</main>

<style>
	.split {
		display: grid;
		grid-template-columns: 2fr 3fr 3fr 3fr 3fr;
		gap: 15px;
	}
	.split_new {
		display: grid;
		grid-template-columns: 5fr 5fr 5fr;
		gap: 15px;
	}
	main {
		margin-left: 60px;
		margin-right: 60px;
		font-family: "ttnormspro-regular", sans-serif;
		font-size: 27px;
	}
	label {
		margin-bottom: 3px;
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
	.avatar {
		margin-left: 16px;
	}
	h1 {
		color: rgba(60, 51, 64, 1);
		font-family: "cygre-medium", sans-serif;
		margin-bottom: 16px;
	}
	.back {
		margin-bottom: 21px;
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
	@font-face {
		font-family: "ttnormspro-regular";
		src: url("/fonts/ttnormspro-regular.ttf");
	}
</style>
