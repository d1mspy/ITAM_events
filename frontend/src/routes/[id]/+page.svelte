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

<main>
	{#if object}
		<form on:submit|preventDefault={saveChanges}>
			<label>
				Название:
				<input type="text" bind:value={object.name} required />
			</label>
			<label>
				Контент:
				<textarea bind:value={object.content}></textarea>
			</label>
			<label>
				День:
				<input type="number" bind:value={object.start_day} min="1" max="31" required />
			</label>
			<label>
				Месяц:
				<input type="number" bind:value={object.start_month} min="1" max="12" required />
			</label>
			<label>
				Год:
				<input type="number" bind:value={object.start_year} min="2024" required />
			</label>
			<label>
				Время:
				<input type="number" bind:value={object.start_hour} min="0" max="23" required />
			</label>
			<label>
				<input type="number" bind:value={object.start_minute} min="0" max="59" required />
			</label>
			<label>
				День:
				<input type="number" bind:value={object.end_day} min="1" max="31" required />
			</label>
			<label>
				Месяц:
				<input type="number" bind:value={object.end_month} min="1" max="12" required />
			</label>
			<label>
				Год:
				<input type="number" bind:value={object.end_year} min="2024" required />
			</label>
			<label>
				Время:
				<input type="number" bind:value={object.end_hour} min="0" max="23" required />
			</label>
			<label>
				<input type="number" bind:value={object.end_minute} min="0" max="59" required />
			</label>
			<label>
				Место:
				<input type="text" bind:value={object.place} required />
			</label>
			<label>
				тег:
				<input type="text" bind:value={object.tags} required />
			</label>
			<label>
				категория:
				<input type="text" bind:value={object.category} required />
			</label>

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
</style>
