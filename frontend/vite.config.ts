import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		host: "0.0.0.0",
		port: 4173
	  },
	optimizeDeps: {
		entries: ["src/routes/+layout.svelte", "src/routes/+page.svelte", "src/app.html"],
		include: ["svelte", "@sveltejs/kit"]
	},
	publicDir: "static",
	preview: {
		allowedHosts: ["frontend"]
	}
});
