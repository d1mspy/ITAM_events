<script lang="ts">
    
    import { goto } from '$app/navigation';
    import {apiUrl} from '$lib/index';
  
    let username = '';
    let password = '';
    let error = '';
    
  
    async function handleLogin() {
      try {
        await login(username, password);
        goto('/'); 
      } catch (e) {
        error = 'Ошибка входа: ' + e.message;
      }
    }
  </script>
<div class="container">
  <main>
    <div class="content">
    <h1>Авторизация</h1>
    <form on:submit|preventDefault={handleLogin}>
      <div>      <input bind:value={username} placeholder="Логин" required /></div>
      <div><input bind:value={password} type="password" id="pass" name="password" minlength="8" placeholder="Пароль" required /></div>
      <button type="submit">Войти</button>
      {#if error}<p>{error}</p>{/if}
    </form>
  </div>
  </main></div>

  <style>
    main{
      width: 465px;
      height: 358px;
      background-color: aliceblue;
      border-radius: 20px;
      align-items: center;
      justify-content: center;
      position: absolute;
      top:  50vh;

    }
    .content{
      align-items: center;
    }
    .container {
      align-items: center;
		max-width: 1440px;
		margin: 0 auto;
    display: flex;
		justify-content: center;
    
	}
  </style>