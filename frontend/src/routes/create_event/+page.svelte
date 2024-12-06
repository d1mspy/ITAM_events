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

<main>
	<h1>Админ-панель</h1>
	<form on:submit|preventDefault={saveObject(newObject)}>
		<label>
			Название
			<input type="text" bind:value={name} required />
		</label>
		<label>
			Описание
			<textarea bind:value={content}></textarea>
		</label>
		<label>
			День
			<input type="number" bind:value={start_day} min="1" max="31" required />
		</label>
		<label>
			Месяц
			<input type="number" bind:value={start_month} min="1" max="12" required />
		</label>
		<label>
			Год
			<input type="number" bind:value={start_year} min="2024" required />
		</label>
		<label>
			Время
			<input type="number" bind:value={start_hour} min="0" max="23" required />
		</label>
		<label>
			<input type="number" bind:value={start_minute} min="0" max="59" required />
		</label>
		<label>
			День
			<input type="number" bind:value={end_day} min="1" max="31" required />
		</label>
		<label>
			Месяц
			<input type="number" bind:value={end_month} min="1" max="12" required />
		</label>
		<label>
			Год
			<input type="number" bind:value={end_year} min="2024" required />
		</label>
		<label>
			Время
			<input type="number" bind:value={end_hour} min="0" max="23" required />
		</label>
		<label>
			<input type="number" bind:value={end_minute} min="0" max="59" required />
		</label>
		<label>
			Тег
			<input type="text" bind:value={tags} required />
		</label>
		<label>
			Формат проведение
			<input type="text" bind:value={category} required />
		</label>
		<label>
			Место проведения
			<input type="text" bind:value={place} required />
		</label>
		<button type="submit">Сохранить</button>
		<button type="button" on:click={cancel}>Отмена</button>
	</form>
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
