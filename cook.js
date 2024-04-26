import android.webkit.CookieManager;
import android.webkit.CookieSyncManager;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize CookieSyncManager
        CookieSyncManager.createInstance(this);

        // Get CookieManager instance
        CookieManager cookieManager = CookieManager.getInstance();

        // Get cookies for a specific URL (e.g., "https://example.com")
        String cookies = cookieManager.getCookie("https://example.com");

        // Print or process the cookies as needed
        Log.d("Cookies", cookies);
    }
}
