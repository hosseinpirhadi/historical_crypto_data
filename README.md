
## Stacks

- **Python**: The main programming language used for data collection and manipulation.
- **Binance API**: Used for fetching cryptocurrency candlestick data.
- **PostgreSQL**: The database used for storing the candlestick data.
- **Docker**: Containerization of the application.
- **Docker Compose**: Managing multi-container Docker applications.

## How to Run the Project

1. **Clone the repository**:

    ```sh
    git clone <repository_url>
    cd project_root
    ```

2. **Build and Run the Docker Containers**:

    ```sh
    docker-compose up --build
    ```

3. **Running the Application**:

    The main script `main.py` will be executed, which will fetch historical candlestick data for predefined cryptocurrency pairs and store it in the PostgreSQL database.

# Binding an IP to localhost in Linux and Windows

## Linux

1. **Open the Terminal:**
   - Press `Ctrl + Alt + T` to open the terminal.

2. **Edit the `/etc/hosts` file:**
   - Use a text editor such as `nano` or `vim`. You might need superuser privileges to edit this file.

   ```bash
   sudo nano /etc/hosts
   ```

3. **Add the IP Address:**
   - At the end of the file, add a new line with the IP address you want to bind to `localhost`. For example, to bind `postgres_crypto` to `localhost`, you would add:

   ```plaintext
   127.0.0.1   postgres_crypto
   ```

4. **Save and Exit:**
   - If you are using `nano`, press `Ctrl + X` to save and exit, then press `Y` and `Enter`.

5. **Verify the Changes:**
   - You can verify the changes by pinging `localhost` and the bound IP address.

   ```bash
   ping localhost
   ping 192.168.1.100
   ```

## Windows

1. **Open Notepad as Administrator:**
   - Click on the Start menu, type `Notepad`, right-click on the Notepad application, and select `Run as administrator`.

2. **Open the `hosts` file:**
   - In Notepad, go to `File` -> `Open`.
   - Navigate to `C:\Windows\System32\drivers\etc\hosts`. Ensure you select `All Files` in the file type dropdown to see the `hosts` file.

3. **Add the IP Address:**
   - At the end of the file, add a new line with the IP address you want to bind to `localhost`. For example, to bind `postgres_crypto` to `localhost`, you would add:

   ```plaintext
   127.0.0.1   postgres_crypto
   ```

4. **Save and Exit:**
   - Save the file (`File` -> `Save`) and close Notepad.

5. **Verify the Changes:**
   - Open Command Prompt (you might need to run it as an administrator) and ping `localhost` and the bound IP address.

   ```cmd
   ping localhost
   ping 192.168.1.100
   ```

## Notes

- **Local Binding Context:** Binding an IP address to `localhost` is typically used for testing purposes and should be done with caution to avoid network conflicts.
- **DNS Cache:** After making these changes, you might need to clear your DNS cache for the changes to take effect immediately. This can be done with the following commands:
  - **Linux:** `sudo systemctl restart network.service` or `sudo /etc/init.d/networking restart`.
  - **Windows:** `ipconfig /flushdns`.

By following these steps, you can bind an IP address to `localhost` on both Linux and Windows systems.


## Using Power BI for Data Visualization

### Export Data to Power BI

1. Ensure your PostgreSQL database is accessible and properly configured to allow remote connections.
2. Open Power BI Desktop.
3. Select "Get Data" from the Home ribbon.
4. Choose "PostgreSQL database" from the list of data sources.
5. Enter your database connection details and load the data you want to visualize.
6. Create your reports and dashboards using the loaded data.

### Importing the Exported Power BI Dashboard

1. Locate the exported Power BI dashboard file (`.pbix`) in the `dashboards` directory of the project.
2. Open Power BI Desktop.
3. Click on "File" -> "Open" and navigate to the location of the exported Power BI dashboard file.
4. Select the `.pbix` file and click "Open".
5. The dashboard will open in Power BI Desktop, allowing you to view and interact with the pre-built reports.

### Publishing Reports

1. Once your report is ready, click on the "Publish" button in Power BI Desktop.
2. Choose your workspace in the Power BI service.
3. After publishing, you can view and share your reports and dashboards online.

## Images

Here are some images showing the project in action:

![Image 1](src/images/candlestick.png)
![Image 2](src/images/mean_price.png)
![Image 3](src/images/volume.png)
