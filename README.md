**easy-skype**

A command-line utility designed to reliably download files shared over Skype chats, especially when Skype's built-in download functionality fails with large files. 

**Features**

* **Robust Downloads:** Handles large files that might cause Skype's default download feature to break.
* **User-Friendly Interface:** Provides a straightforward command-line experience with clear prompts and progress tracking.
* **Contact and File Selection:** Lets you list your Skype contacts and conveniently choose files from specific conversations.

**Installation**

```bash
pip install bhaskar-kernel-easy-skype
```

**Usage**

1. **Run the tool:**
   ```bash
   bhaskar-kernel-easy-skype
   ```

2. **Initial Setup (if needed):**
   * The tool checks for existing Skype credentials.  
   * If not found, you'll be prompted to enter your Skype username, password, and a preferred default download path.  
   * These credentials are stored locally for future use.  

3. **Select Contact (if needed):**
   *  If you haven't specified a contact with the `-c` flag, the tool lists your contacts.
   * Enter the ID of the desired contact.

4. **View and Select Files:**
   * The tool displays a list of files shared within the chosen conversation.

5. **Download Files:**
   * Enter the ID of the file you want to download.
   * The download starts, and you'll see a progress bar using `tqdm`.

**Command Line Options**

* `-u`, `--username`:  Provide your Skype username (needed for the first run).
* `-p`, `--password`:  Provide your Skype password (needed for the first run).
* `--default_path`:  Set the default download location.
* `-c`, `--contact`: Specify the Skype ID of the contact for file download.

**Example**

```bash
bhaskar-kernel-easy-skype -u my_skype_username -p my_skype_password --default_path /home/me/Downloads -c friend_skype_id 
```

**Important Notes**

* This tool uses the Skype API, which may be subject to changes by Microsoft.
* Securely store your Skype credentials. For enhanced security consider using environment variables instead of direct command-line input.

**Dependencies**

* Python 3+
* `pip`
* `requests`
* `skpy`
* `tqdm`
* `rich`

**License**

This project is licensed under MIT.
