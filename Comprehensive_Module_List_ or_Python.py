Comprehensive Python System/File Tools Reference
Works on Linux (Kali), macOS, and Windows.
Perfect for cybersecurity labs.
"""
# --- CORE IMPORTS ---
import os          # File and directory operations, environment variables
import stat        # File permissions, metadata, and mode constants
import sys         # System-specific functions, arguments, interpreter info
import platform    # Information about the underlying OS and hardware
import shutil      # High-level file operations (copy, move, remove, disk usage)
import subprocess  # Running external commands and processes
import pathlib     # Object-oriented filesystem paths
import glob        # Pattern-based file search (wildcards)
import fnmatch     # Filename pattern matching
import datetime    # Date and time handling
import time        # Time access, epoch, delays
import hashlib     # Cryptographic hashing (MD5, SHA1, SHA256, etc.)
import secrets     # Cryptographically secure random numbers/tokens
import uuid        # Generate universally unique identifiers (UUIDs)
import json        # Read/write JSON data
import csv         # Read/write CSV files
import configparser # Handle INI-style configuration files
import getpass     # Secure password input from terminal
import socket      # Networking (hostname, IP resolution, sockets)
import tempfile    # Create and manage temporary files and directories
import logging     # Logging system for debugging and monitoring
import traceback   # Exception tracebacks for debugging
import zipfile     # Read/write ZIP archives
import tarfile     # Read/write TAR archives
# --- UNIX-ONLY MODULES ---
HAS_UNIX_TOOLS = False
if platform.system() in ["Linux", "Darwin"]:
    import pwd        # Unix user database (map UID → username)
    import grp        # Unix group database (map GID → group name)
    import fcntl      # File control (locking, I/O operations)
    import resource   # Query/set system resource limits
    import pty        # Pseudo-terminal handling
    HAS_UNIX_TOOLS = True
# --- WINDOWS-ONLY MODULES ---
if platform.system() == "Windows":
    import msvcrt     # Console I/O (keyboard input, file locking)
    import winreg     # Windows registry access
# --- EXTRA MODULES ---
import argparse      # Parse command-line arguments
import re            # Regular expressions (pattern matching/search)
import ctypes        # Interface with C libraries and system calls
try:
    import psutil    # Process, CPU, memory, disk, network usage (3rd party)
except ImportError:
    psutil = None
# --- PATH UTILITIES (os.path) ---
# os.path.exists(path)          -> Does file/folder exist?
# os.path.isfile(path)          -> Is it a regular file?
# os.path.isdir(path)           -> Is it a directory?
# os.path.getsize(path)         -> File size in bytes
# os.path.getmtime(path)        -> Last modification time (epoch)
# os.path.getatime(path)        -> Last access time (epoch)
# os.path.getctime(path)        -> Creation time (Windows) / Metadata change (Unix)
# os.path.abspath(path)         -> Absolute path
# os.path.basename(path)        -> Filename from path
# os.path.dirname(path)         -> Directory portion
# os.path.splitext(path)        -> Split filename and extension
# os.path.relpath(path, start)  -> Relative path from start
# os.path.join(a, b)            -> Join paths safely
# os.path.isabs(path)           -> Is path absolute?
# --- OS MODULE ---
# os.listdir(path)              -> List files/folders
# os.makedirs(path, exist_ok=True) -> Create directories recursively
# os.remove(path)               -> Delete a file
# os.rename(src, dst)           -> Rename file/folder
# os.environ                    -> Environment variables
# os.getcwd() / os.chdir(path)  -> Current / Change working directory
# --- STAT MODULE ---
# stat.filemode(st_mode)        -> Permissions as string (e.g. -rwxr-xr-x)
# stat.S_ISUID/S_ISGID/S_ISVTX  -> SUID/SGID/Sticky bits
# stat.S_IRUSR/IWUSR/IXUSR      -> Owner read/write/execute
# stat.S_IRGRP/IWGRP/IXGRP      -> Group permissions
# stat.S_IROTH/IWOTH/IXOTH      -> Other permissions
# st.st_uid                     -> User ID (Unix)
# st.st_gid                     -> Group ID (Unix)
# st.st_mode                    -> Raw permission bits
# st.st_size                    -> File size in bytes
# --- PWD & GRP MODULES (Unix only) ---
# pwd.getpwuid(uid).pw_name     -> Username
# grp.getgrgid(gid).gr_name     -> Group name
# --- SYS MODULE ---
# sys.argv                      -> Command line args
# sys.exit(code)                -> Exit program
# sys.version                   -> Python version
# sys.platform                  -> Platform identifier (e.g. win32, linux, darwin)
# --- PLATFORM MODULE ---
# platform.system()             -> OS name
# platform.release()            -> OS release
# platform.version()            -> Detailed OS version
# platform.machine()            -> CPU architecture (e.g. x86_64, arm64)
# --- SHUTIL MODULE ---
# shutil.copy(src, dst)         -> Copy a file
# shutil.copytree(src, dst)     -> Copy entire directory tree
# shutil.move(src, dst)         -> Move or rename
# shutil.rmtree(path)           -> Delete directory tree
# shutil.disk_usage(path)       -> Disk usage: total, used, free
# --- SUBPROCESS MODULE ---
# subprocess.run([...])             -> Run command
# subprocess.run([...], check=True) -> Raise exception on failure
# subprocess.check_output([...])    -> Capture command output
# subprocess.Popen([...])           -> Interactive processes
# --- PATHLIB MODULE ---
# pathlib.Path("file").exists() -> Check existence
# pathlib.Path.cwd()            -> Current directory
# pathlib.Path("file").stat()   -> File metadata
# --- GLOB MODULE ---
# glob.glob("*.py")             -> List files with pattern
# glob.iglob("*.txt")           -> Iterator for matching files
# --- FNMATCH MODULE ---
# fnmatch.fnmatch("file.log", "*.log") -> Match pattern
# fnmatch.filter(files, "*.txt")       -> Filter list with pattern
# --- DATETIME MODULE ---
# datetime.datetime.now()       -> Current date/time
# datetime.date.today()         -> Current date
# datetime.timedelta(days=7)    -> Time delta
# datetime.datetime.fromtimestamp(ts) -> Convert epoch -> datetime
# .strftime("%Y-%m-%d %H:%M:%S") -> Format datetime as string
# --- TIME MODULE ---
# time.time()                   -> Seconds since epoch
# time.sleep(5)                 -> Pause execution
# time.ctime()                  -> Human-readable timestamp
# time.localtime()              -> Local time struct
# time.gmtime()                 -> UTC time struct
# time.perf_counter()           -> High-resolution timer
# --- HASHLIB MODULE ---
# hashlib.md5(b"data").hexdigest()     -> MD5
# hashlib.sha256(b"data").hexdigest()  -> SHA256
# hashlib.file_digest(file, "sha1")    -> File hash (Python 3.11+)
# --- SECRETS MODULE ---
# secrets.token_hex(16)         -> Secure random hex string
# secrets.choice(seq)           -> Secure random choice
# --- UUID MODULE ---
# uuid.uuid4()                  -> Generate random UUID
# --- JSON MODULE ---
# json.load(file)               -> Read JSON
# json.dump(obj, file)          -> Write JSON
# --- CSV MODULE ---
# csv.reader(file)              -> Read CSV
# csv.writer(file)              -> Write CSV
# --- CONFIGPARSER MODULE ---
# configparser.ConfigParser()   -> Work with INI configs
# --- GETPASS MODULE ---
# getpass.getpass()             -> Secure password input
# --- SOCKET MODULE ---
# socket.gethostname()          -> Hostname
# socket.gethostbyname(host)    -> Resolve host to IP
# socket.socket()               -> Create network socket
# --- TEMPFILE MODULE ---
# tempfile.NamedTemporaryFile() -> Temp file
# tempfile.gettempdir()         -> Temp directory
# --- LOGGING MODULE ---
# logging.debug("msg")          -> Debug log
# logging.info("msg")           -> Info log
# logging.error("msg")          -> Error log
# --- TRACEBACK MODULE ---
# traceback.print_exc()         -> Print last exception
# --- ZIPFILE MODULE ---
# zipfile.ZipFile("a.zip")      -> Read/write ZIP
# --- TARFILE MODULE ---
# tarfile.open("a.tar.gz")      -> Read/write TAR
# --- FCNTL MODULE (Unix only) ---
# fcntl.flock(file, fcntl.LOCK_EX) -> File locking
# --- RESOURCE MODULE (Unix only) ---
# resource.getrlimit(resource.RLIMIT_NOFILE) -> Process limits
# --- PTY MODULE (Unix only) ---
# pty.openpty()                 -> Create a new pseudo-terminal
# --- MSVCRT MODULE (Windows only) ---
# msvcrt.getch()                -> Read single keypress
# msvcrt.locking(fd, mode, n)   -> File locking
# --- WINREG MODULE (Windows only) ---
# winreg.OpenKey()              -> Access Windows registry
# winreg.QueryValueEx()         -> Query registry value
# --- ARGPARSE MODULE ---
# argparse.ArgumentParser()       -> Handle command-line arguments cleanly
# parser.add_argument("--flag")   -> Define options/flags
# parser.parse_args()             -> Parse CLI arguments into an object
# --- RE MODULE ---
# re.match(r"^pattern", text)     -> Match at start of string
# re.search(r"pattern", text)     -> Search anywhere in string
# re.findall(r"pattern", text)    -> Find all matches
# re.sub(r"pattern", "repl", text) -> Replace text using regex
# --- CTYPES MODULE ---
# ctypes.CDLL("libc.so.6")        -> Load shared library (Linux/macOS)
# ctypes.windll.kernel32          -> Call Windows API
# ctypes.byref(var)               -> Pass references to C functions
# --- PSUTIL MODULE (3rd party, install separately) ---
# psutil.process_iter()           -> List running processes
# psutil.disk_usage("/")          -> Disk usage stats
# psutil.net_connections()        -> Active network connections
# psutil.virtual_memory()         -> RAM usage stats