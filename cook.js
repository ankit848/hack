const { CookieManager } = require('react-native-cookies'); // Assuming you have a similar module available

class MainActivity {
    async onCreate(savedInstanceState) {
        // Initialize CookieManager
        await CookieManager.createInstance();

        // Get cookies for a specific URL (e.g., "https://example.com")
        const cookies = await CookieManager.getCookie("https://example.com");

        // Print or process the cookies as needed
        console.log("Cookies:", cookies);
    }
}

// Simulating activity creation
const mainActivity = new MainActivity();
mainActivity.onCreate();
