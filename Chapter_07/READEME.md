# 🌟 Chapter 7: File Handling in Python 🌟

Hello, Python enthusiasts! 👋 In **Chapter 7**, I explored the fundamentals of **file handling** in Python. File I/O operations allow us to interact with files, enabling data persistence and manipulation. Here's a breakdown of what this chapter covers:

---

## 📝 Key Concepts

### 📂 **Types of Files**
- **Text Files**: Human-readable files (e.g., `.txt`).
- **Binary Files**: Files stored in binary format (e.g., `.bin`).

### 🔑 **File Operations**
1. **Opening, Reading, and Closing Files**:
   - Open files using `open()` in various modes (`r`, `w`, `a`, `r+`, etc.).
   - Always close files using `close()` or automatically using the `with` syntax.
2. **File Modes**:
   - `r`: Read (default).
   - `w`: Write (overwrites existing content).
   - `a`: Append (adds content to the end of the file).
   - `r+`: Read and write.
3. **Writing and Appending**:
   - Write to a file using `write()`.
   - Append content using `a` mode.
4. **Using `with` Syntax**:
   - Simplifies file handling by automatically closing files after the block.
5. **Deleting Files with `os` Module**:
   - Remove files using `os.remove(filepath)`.
   - Ensure the file exists and you have the necessary permissions before deleting.
   - Be cautious, as this action is irreversible.

---

## 🛠️ Practice Activities

### 🏆 Practice 01: Replace Text
- **Task**: I created a file `practice.txt` with some content, and my goal was to replace all occurrences of `"java"` with `"python"`.

### 🔍 Practice 02: Search for a Word
- **Task**: I checked if the word `"learning"` exists in `practice.txt`. I wrote a function to perform the search and return whether the word was found or not.

### 📄 Practice 03: Find Line Number of a Word
- **Task**: I determined which line in `practice.txt` contains the word `"learning"`. If the word wasn’t found, I printed `-1`.

---

## 💡 Pro Tip
Practice file handling with both small and large datasets to solidify your understanding. Experiment with different modes and edge cases to handle errors gracefully. 📂✨

Happy Coding! 😊
