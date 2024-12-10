<script lang="ts">
	import { goto } from "$app/navigation";
	import { apiUrl } from "$lib/index";
	let username = "";
	let password = "";
	let error = "";

	async function handleLogin() {
		try {
			await login(username, password);
			goto("/");
		} catch (e) {
			error = "Ошибка входа: " + e.message;
		}
	}
	let currentTab = "login";
	let step = 1;

	function switchToRegistration() {
		currentTab = "registration";
		step = 1;
	}

	function switchToLogin() {
		currentTab = "login";
	}

	function nextStep() {
		step++;
	}
	function lastStep() {
		step--;
	}
</script>

<main>
	<div class="form-container">
		<div class="tab">
			<button class={currentTab === "login" ? "active-tab" : ""} on:click={switchToLogin}>
				Вход
			</button>
			<button
				class={currentTab === "registration" ? "active-tab" : ""}
				on:click={switchToRegistration}
			>
				Регистрация
			</button>
		</div>

		{#if currentTab === "login"}
			<!-- Форма входа -->
			<div class="login_form">
				<form on:submit|preventDefault={handleLogin}>
					<div class="form-e">
						<input id="email" type="email" placeholder="Email" bind:value={username} required />
						<input
							id="password"
							type="password"
							placeholder="Пароль"
							bind:value={password}
							minlength="8"
							required
						/>
						<button type="submit">Войти</button>
					</div>
					<p><a href="#">Забыли пароль?</a></p>
				</form>
				<img src="el.svg" class="el" />
			</div>
		{/if}

		{#if currentTab === "registration"}
			<!-- Форма регистрации -->
			{#if step === 1}
				<form>
					<div class="form-e">
						<input id="surname" type="text" placeholder="Фамилия" required />
						<input id="name" type="text" placeholder="Имя" required />
						<input
							required
							type="text"
							class="form-control"
							placeholder="Дата рождения"
							onFocus="(this.type='date')"
						/>
						<input id="group" type="text" placeholder="Группа" required />

						<button type="button" on:click={nextStep}>Далее →</button>
					</div>
				</form>
			{/if}
			{#if step === 2}
				<form>
					<img src="Стрелка.svg" class="back" on:click={lastStep} />
					<div class="form-e">
						<input id="reg-email" type="email" placeholder="Email" bind:value={username} required />
						<input
							id="reg-password"
							type="password"
							placeholder="Пароль"
							bind:value={password}
							minlength="8"
							required
						/>
						<button type="submit">Зарегистрироваться</button>
					</div>
				</form>
			{/if}
		{/if}
	</div>
</main>

<style>
	@font-face {
		font-family: "ttnormspro-regular";
		src: url("/fonts/ttnormspro-regular.ttf");
	}
	.back {
		margin-bottom: 18.33px;
	}
	main {
		margin: 0;
		font-family: "ttnormspro-regular", sans-serif;
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100vh;
		background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
	}
	.login_form form {
		text-align: left;
	}
	.login_form {
		text-align: right;
	}
	.el {
		position: absolute;
		margin-top: -26px;
		margin-left: -32px;
	}
	.form-container {
		background: white;
		box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
		border-radius: 20px;
		width: 462px;
		padding: 57px;
	}

	.tab {
		display: flex;
		justify-content: center;
		margin-bottom: 55px;
	}

	.tab button {
		background: none;
		border: none;
		font-size: 22px;
		padding: 18px 50px;
		width: 231px;
		height: 62px;
		cursor: pointer;
		color: #000000;
	}

	.tab button:hover {
		background: linear-gradient(135deg, rgba(250, 202, 206, 0.5), rgba(200, 170, 231, 0.5));
	}

	.active-tab {
		background: linear-gradient(135deg, rgba(250, 202, 206, 0.5), rgba(200, 170, 231, 0.5));
	}

	.form-e {
		display: flex;
		flex-direction: column;
		gap: 15px;
		margin-bottom: 8;
		text-align: center;
	}

	input {
		padding: 10.5px 22px;
		border: 1px solid rgba(128, 128, 128, 1);
		border-radius: 10px;
		font-size: 18px;
		outline: none;
		transition: border 0.3s;
	}

	input:focus {
		border-color: #a6c1ee;
	}

	button {
		background: linear-gradient(135deg, rgba(250, 202, 206, 0.5), rgba(200, 170, 231, 0.5));
		border: none;
		padding: 10.5px;
		color: rgba(60, 51, 64, 1);
		border-radius: 10px;
		font-size: 18px;
		cursor: pointer;
		transition:
			transform 0.3s,
			box-shadow 0.3s;
	}

	button:hover {
		transform: translateY(-3px);
		box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
	}

	p {
		font-size: 18px;
		color: rgba(0, 0, 0, 0.5);
	}

	p a {
		color: rgba(0, 0, 0, 0.5);
		text-decoration: none;
		text-align: left;
		margin-bottom: 49px;
	}

	p a:hover {
		text-decoration: underline;
	}
	::-webkit-calendar-picker-indicator {
		color: transparent;
		opacity: 1;
		background: url(/calendar.svg) no-repeat center;
		background-size: contain;
	}
</style>
