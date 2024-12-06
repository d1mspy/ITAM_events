export const apiUrl = "http://89.169.172.143:8000/"
export let token: string | null = null;
export async function login(username: string, password:string){
  let promise =  fetch(`${apiUrl}/login`,{
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({login: `${username}`, password:`${password}`})
  });
  let response = await promise;
  let obj = await response.json();
  console.log(obj.token);
  token = obj.token
}