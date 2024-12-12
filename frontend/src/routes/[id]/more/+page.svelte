<script lang="ts">
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	import { page } from "$app/stores";
	import { apiUrl } from "$lib/index";
	const Months = [
		"января",
		"февраля",
		"марта",
		"апреля",
		"мая",
		"июня",
		"июля",
		"августа",
		"сентября",
		"октября",
		"ноября",
		"декабря"
	] as const;
	let object: any;
	object = null;
	let id = $page.params.id;
	const apiUrl1 = `${apiUrl}/${id}`;
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
				delete object["start_datetime"];
			} else {
				console.error("Ошибка загрузки объекта");
			}
		} catch (error) {
			console.error("Ошибка подключения по id");
		}
	}
	onMount(fetchObject);
	function goToBack() {
		goto("/");
	}
</script>

<header>
	<div class="header">
		<div class="logo"><img src="../logo.svg" alt="ITAM" /></div>
		<nav>
			<button class="nav-btn" style="background: white;">Мероприятия</button>
			<button class="nav-btn">Админ-панель</button>
			<div class="avatar"><img src="../avatar.svg" alt="avatar" /></div>
		</nav>
	</div>
</header>

<main>
	<button class="back-btn" on:click={() => goToBack()}>
		<img src="../Back.svg" alt="Назад" />
	</button>
	{#if object}
		<div class="content">
			<div class="left-panel">
				<img src="../pic.png" alt="Картинка" class="pic" />
			</div>
			<div class="right-panel">
				<h1 style="margin-top: 187px;">{object.name}</h1>
				<p style="margin-top: 175px;">
					{object.start_day}
					{Months[object.start_month - 1]} | {object.start_hour}:{object.start_minute} | {object.place}
				</p>
			</div>
		</div>
		<div class="tags" style="margin-top: 31px;">
			<span class="tag blue">#{object.tags}</span>
			<span class="tag pink">#{object.category}</span>
		</div>
		<div style="margin-top: 37px;" class="info">{object.content}</div>
		<button class="register-btn">Зарегистрироваться</button>
        
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
		font-family: "ttnormspro-regular", sans-serif;
		color: rgba(102, 102, 102, 1);
	}
	button {
		background: none;
		border: none;
	}
	.content {
		display: flex;
	}

	.left-panel {
		height: 564px;
		justify-content: center;
		align-items: center;
		position: relative;
		margin-top: 21px;
	}

	.pic {
		border-radius: 20px;
		height: 564px;
		width: 760px;
	}
	.right-panel {
		height: 498px;
		margin-top: 21px;
		flex: 1;
		border-radius: 20px;
		padding: 30px;
		text-align: center;
		border: 2px solid rgba(252, 205, 205, 1);
	}
	.tags {
		display: flex;
		gap: 20px;
	}
	.tag {
		padding: 3px 13px;
		border-radius: 20px;
		font-size: 18px;
	}
	.tag.blue {
		background-color: rgba(204, 211, 243, 1);
	}

	.tag.pink {
		background-color: rgba(255, 230, 236, 1);
	}
	h1 {
		color: rgba(60, 51, 64, 1);
		font-family: "cygre-medium", sans-serif;
		margin-bottom: 28px;
		font-weight: 500px;
	}
	.back-btn {
		margin-top: 29px;
	}
	.register-btn {
		margin-top: 12px;
		padding: 11px 258px;
		background: linear-gradient(135deg, rgba(250, 202, 206, 0.5), rgba(200, 170, 231, 0.5));
		border-radius: 20px;
		font-size: 25px;
		color: rgba(60, 51, 64, 1);
		width: 760px;
		height: 52px;
	}
</style>
