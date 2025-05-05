import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {

    public static void main(String[] args) {
        // Sensitive information: Database credentials
        String username = "admin";  // Username
        String password = "secretpassword123";  // Hardcoded password
        String dbUrl = "jdbc:mysql://localhost:3306/mydatabase";

        try {
            Connection conn = DriverManager.getConnection(dbUrl, username, password);
            System.out.println("Connected to the database!");
        } catch (SQLException e) {
            System.out.println("Connection failed: " + e.getMessage());
        }
    }
}
