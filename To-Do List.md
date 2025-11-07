
## **قائمة المهام – مشروع LogiLang**

### المرحلة 1: التصميم النظري

* تحديد الهدف من اللغة (التركيز على المنطق والدوائر الرقمية).
* كتابة قواعد اللغة (Syntax) بشكل شبه نهائي.
* تحديد أنواع البيانات (int, bool, logic, pcb...).
* وضع أمثلة عملية لبرامج صغيرة.

---

### المرحلة 2: بناء اللبنة الأولى (Lexer)

* إنشاء ملف مصدر بلغة Python أو C#.
* تعريف الرموز (tokens): الكلمات المحجوزة، الأرقام، الأقواس، الفواصل...
* بناء **دالة tokenize()** لتحويل النص إلى قائمة tokens.
* اختبار الـ lexer على أمثلة بسيطة.

---

### المرحلة 3: بناء الـ Parser

* تحديد القواعد النحوية (grammar) بناءً على الـ EBNF.
* كتابة دالة **parse()** لبناء شجرة AST.
* دعم العمليات المنطقية (AND, OR, NOT...).
* دعم التعريف بالـ `logic name(inputs=..., outputs=...)`.
* اختبار parsing لعدة ملفات.

---

### المرحلة 4: بناء الـ Interpreter

* بناء **بيئة تنفيذ (Environment)** للمدخلات والمخرجات.
* تنفيذ العمليات المنطقية.
* تنفيذ المعادلات الرياضية الأساسية (+, -, *, /, mod).
* دعم المتغيرات بأنواع int و bool.
* دعم الشروط (`if`, `else`) والحلقات (`loop`, `for`).

---

### المرحلة 5: تحسين اللغة

* إضافة import logic files (`import custom;`).
* دعم أكثر من ملف (Modules).
* دعم رسائل الخطأ المفصلة (SyntaxError, RuntimeError).
* تحسين الـ Lexer/Parser ليقبل تعليقات (`// comment`).

---

### 📘 المرحلة 6: تحسين التجربة وتوثيق اللغة

* إنشاء **وثيقة Grammar رسمية (EBNF)** كاملة.
* إعداد **أمثلة توضيحية** (Logic Gates, Half Adder, Full Adder...).
* إنشاء **مترجم (Compiler)** بسيط يحوّل الشيفرة إلى كود C أو بايت كود.
* إعداد **اختبارات (unit tests)** للغة.

---

### 💻 المرحلة 7: الواجهة الأمامية (Frontend) للغة

* إنشاء **محرر أكواد بسيط** (مثلاً بلغة Python أو Electron).
* تلوين الكلمات المحجوزة (Syntax Highlighting).
* إمكانية تشغيل الكود وعرض النتائج في الواجهة.

---

## **To-Do List – LogiLang Project**

### Stage 1: Theoretical Design

* Define the language’s goal (focus on logic and digital circuits).
* Write the language syntax (nearly final version).
* Define data types (int, bool, logic, pcb...).
* Provide practical examples of small programs.

---

### Stage 2: Building the First Component (Lexer)

* Create a source file using Python or C#.
* Define tokens: keywords, numbers, parentheses, commas, etc.
* Implement **tokenize()** to convert source code into tokens.
* Test the lexer on simple examples.

---

### Stage 3: Building the Parser

* Define grammar rules based on EBNF.
* Implement **parse()** to build an AST (Abstract Syntax Tree).
* Support logical operations (AND, OR, NOT...).
* Support logic definitions like `logic name(inputs=..., outputs=...)`.
* Test parsing across multiple files.

---

### Stage 4: Building the Interpreter

* Build an **execution environment** for inputs and outputs.
* Implement logical operations.
* Support basic arithmetic operations (+, -, *, /, mod).
* Support variable types int and bool.
* Add conditionals (`if`, `else`) and loops (`loop`, `for`).

---

### Stage 5: Language Enhancements

* Add import logic files (`import custom;`).
* Support multiple modules.
* Implement detailed error messages (SyntaxError, RuntimeError).
* Extend Lexer/Parser to handle comments (`// comment`).

---

### Stage 6: Documentation and Language Experience

* Write the **official Grammar (EBNF)** document.
* Prepare **example programs** (Logic Gates, Half Adder, Full Adder...).
* Create a simple **Compiler** that outputs C code or bytecode.
* Add **unit tests** for the language.

---

### Stage 7: Language Frontend

* Build a simple **code editor** (Python or Electron).
* Add syntax highlighting for reserved keywords.
* Enable code execution and result display within the interface.
