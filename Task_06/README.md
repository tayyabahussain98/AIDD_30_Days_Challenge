 # 🧠 AIDD 30-Day Challenge — Task 6 Submission
    Name: Tayyaba Hussain | Student ID: 00042883
    ⏱ Time: 1 Hour | Marks: 10 | Deadline: 48 Hours
    📅 Class Slot: Friday — 6:00 PM to 9:00 PM
    Instructor: Sir Hamzah Syed

 # 🎯 Task Objective
 Students will connect GitHub MCP Server with the Google Gemini CLI using the Hosted (Remote) MCP Server.
 
 This method does not require Docker or MCP installation - it's the simplest method.
 
 After completing this task, AI will be able to read repositories and interact with GitHub.
 
 # 📌 Steps to Complete Task 6 (Easy Method)
 ## 🔹 Step 1 - Create Your GitHub Personal Access Token (PAT)
 
 ### Open this link:
 https://github.com/settings/tokens

 #### Generate a token with:
  ✔ repo (Read & Write)

 Copy the token and save it safely.

 ![Create Accoun](Create_Account.png)
 
 #### 🗒️ Token Name

 ![Token Name](Token_Name.png)
 
 #### 📝 Some Permissions

 ![Repo Options](Repo_Options1.png)

 ![Repo Options](Repo_Options2.png)
 
 #### ✅Successfully Generate Token

 ![Generate Token](Generate_Token.png)
 
 ## 🔹 Step 2 - Store Your Token Securely
 
 Do NOT put the token directly into JSON.
 
 ### 📂 Create this file:
 
 ![Create Env File](Create_Env.png)


 ### ➕ ADD

 ![Env File](Env_File.png)
 
 ## 🔹 Step 3 - Configure Gemini to Use GitHub MCP Server
 ### 🗃️ Open or create:

 ![Create JSON File](Create_JSON.png)
 
 ### 📄Paste this:

 ![Setting File](Setting_File.png)
 
 ✔ No installation required
 
 ✔ Token auto-loads from .env
 
 ✔ Fast & easiest MCP setup
 
 ## 🔹 Step 4 - Restart Gemini CLI

 ![Gemini](Gemini.png)
 
 ## 🔹 Step 5 - Verify Connection
 
 ![MCP List](MCP_List.png)

 ### 🔧 Tools List

 ![Tools List](Tools_List1.png)

 ![Tools List](Tools_List2.png)
 
 ## 🔹Step 6 - Test the Server

 ![Prompt](Prompt.png)
 
 ### 🚀 Gemini shows your repos → MCP is fully connected ✔

 ![Repo List](Repo_List.png)
 
 ## 📤 Submission Requirements
 
 ### Students must submit:
 
 #### ✔ Screenshot of:
 ✅ .env file (token blurred)
 
 ✅ settings.json
 
 ✅ /mcp list result
 
 ✅ GitHub repo list output