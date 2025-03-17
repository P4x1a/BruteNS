# 🔍 BruteNS - Advanced Subdomain Enumeration  

## 📌 Description  

**BruteNS** is an advanced **subdomain enumeration** tool. It performs **fast and efficient** DNS queries to identify hidden subdomains that may represent potential attack surfaces.  

The tool uses a **brute-force approach**, testing subdomains from predefined or custom wordlists. With **multithreading support**, it maximizes DNS query performance, enabling faster and more effective discoveries.  

### ✅ **Key Features**  
🔹 **Multithreaded Execution**: Uses `ThreadPoolExecutor` to perform simultaneous queries and reduce execution time.  
🔹 **Customizable Wordlists**: Includes several predefined wordlists and supports external lists.  
🔹 **Structured and Colored Output**: Uses `colorama` for better readability.  
🔹 **Interactive Progress Bar**: `tqdm` integration to track enumeration progress.  
🔹 **Automatic Report Generation**: Saves discovered subdomains in a `.txt` file for future reference.  
🔹 **Robust Exception Handling**: Manages common errors such as NXDOMAIN, timeout, and missing DNS responses.  

### 🎯 **Use Cases**  
- **Security testing**: Identify undocumented entry points in web applications.  
- **Reconnaissance**: Map an organization's infrastructure for security audits.  
- **Bug bounty programs**: Discover hidden subdomains that may contain vulnerabilities.  
- **Pentesting and Red Teaming**: Assess security exposure and attack surfaces.  

---  

## ⚡ Installation and Setup  

### 1️⃣ Clone the repository:  
```bash
git clone https://github.com/P4x1a/BruteNS.git
cd BruteNS
```

### 2️⃣ Manually install dependencies:  
```bash
pip install dnspython tqdm colorama
```

### 3️⃣ Choose a Wordlist  
The script relies on **wordlists** to test subdomains. Several options are available in the repository.

📂 **Available Wordlists:**  
- `wordlists/subdomains` → Base subdomain list  
- `wordlists/subdomains-100` → Small, fast list with 100 common subdomains  
- `wordlists/subdomains-500` → Medium, balanced between size and efficiency (500 subdomains)  
- `wordlists/subdomains-1000` → Large, includes 1,000 well-known subdomains  
- `wordlists/subdomains-10000` → Extensive, detailed but slower (10,000 subdomains)  
- `wordlists/subdomainsGPT` → AI-generated list for advanced discoveries  

You can also download a larger wordlist:  
```bash
curl -o wordlists/biglist.txt https://example.com/big-subdomains.txt
```
Or create your own:  
```bash
nano wordlists/custom.txt
```
Add subdomains line by line:  
```
www
mail
vpn
api
admin
```

---  

## 🚀 Usage  

### 1️⃣ Run the script:  
```bash
python BruteNS.py
```

### 2️⃣ Enter the required information:  
```
Enter target domain: bancocn.com
Enter wordlist path: wordlists/subdomains-500
```

### 3️⃣ Wait for enumeration to complete:  
```
[+] www.bancocn.com -> 192.168.1.1
[+] mail.bancocn.com -> 192.168.1.2
[-] Timeout on vpn.bancocn.com
[i] Report saved in 'relatorio_subdominios.txt'
```

The `relatorio_subdominios.txt` file will contain all discovered subdomains.

---  

## 🛠 Technologies Used  
- **Python 3.x**  
- **dnspython** (for DNS resolution)  
- **tqdm** (for progress bar)  
- **colorama** (for terminal output colors)  
- **concurrent.futures** (for multithreaded execution)  

---  

## 📄 License  
This project is open-source and distributed under the **MIT License**.  

---  

📢 **Want to contribute?** Feel free to fork the project and submit a pull request!  

🔗 **GitHub:** [github.com/P4x1a/BruteNS](https://github.com/P4x1a/BruteNS)  

---
