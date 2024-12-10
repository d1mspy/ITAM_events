<script lang="ts">
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	import { apiUrl } from "$lib/index";
	import axios from "axios";
	let objects = [];
	$: tag = [...new Set(objects.map(obj => obj.tags))];
	$: catigory = [...new Set(objects.map(obj => obj.catigory))];
	let selectedTag = "";
	let selectedCatigory = "";
	$: FilterEvents = selectedTag ? objects.filter(obj => obj.tags === selectedTag) : objects;

	async function fetchObjects() {
		try {
			const response = await axios.get(`${apiUrl}`, {
				withCredentials: true,
				headers: { "Content-Type": "application/json" }
			});
			objects = await response.data();
		} catch (error) {
			console.error("Ошибка загрузки", error);
			throw error;
		}
	}

	onMount(async () => {
		await fetchObjects();
	});

	function goToAddPage() {
		goto("/create_event");
	}

	function goToObjectPage(id) {
		goto(`/${id}`);
	}

	async function deleteEvent(id) {
		try {
			const response = await fetch(`${apiUrl}${id}`, {
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
	<div class="container">
		<div class="filter-bar">
			<select bind:value={selectedTag}>
				<option selected value="">Выбрать категорию</option>
				{#each tag as tags}
					<option value={tags}>{tags}</option>
				{/each}
			</select>
			<select>
				<option selected>Формат проведения</option>
				<option>Онлайн</option>
				<option>Офлайн</option>
			</select>
			<img src="search.svg" />
			<input type="text" placeholder="Поиск..." />
		</div>
		<button on:click={goToAddPage} class="goAdd">+ Добавить событие</button>
	</div>
	<table class="super_title">
		<thead>
			<tr>
				<th>Название</th>
				<th>Дата события</th>
				<th>Статус</th>
				<th>Изменить</th>
			</tr>
		</thead>
	</table>

	<!-- <table>
	<tbody>
        <tr>
          <td>Основы эффективной разработки</td>
          <td>01.12.24</td>
          <td>
            <select>
              <option>Опубликовано</option>
            </select>
          </td>
          <td>
            <img src="edit.svg" style="margin-right: 38px;" class="edit" on:click={() => goToObjectPage(obj.id)}>
			<img src="trash.svg" class="trash" on:click={()=>deleteEvent(obj.id)}>
          </td>
        </tr>
      </tbody>
</table> -->

	<table>
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
						<img
							src="edit.svg"
							style="margin-right: 38px;"
							class="edit"
							on:click={() => goToObjectPage(obj.id)}
						/>
						<img src="trash.svg" class="trash" on:click={() => deleteEvent(obj.id)} />
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
</main>

<style>
	main {
		margin-left: 60px;
		margin-right: 60px;
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
	.event-tag {
		position: absolute;
		top: 23;
		left: 23;
		background: #d9d9d9;
		color: #666666;
		padding: 7px 23px;
		font-size: 12px;
		border-radius: 20;
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

	@font-face {
		font-family: "cygre-medium";
		src: url("/fonts/cygre-medium.ttf");
	}

	@font-face {
		font-family: "ttnormspro-regular";
		src: url("/fonts/ttnormspro-regular.ttf");
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
		border-radius: 50px;
	}
	table tr {
		padding: 17px 90px;
		text-align: left;
		font-size: 22px;
		margin-right: 80px;
	}
	table td {
		padding: 17px 29px;
		text-align: left;
		border-bottom: 2px solid #787878;
		font-size: 22px;
	}
	.filter-bar input {
		height: 24px;
	}
	.filter-bar option {
		height: 24px;
	}
</style>
