// ==========================================================
// File: Example.ll
// Description: main logic file that defines multiple circuits
// ==========================================================

this Example has many; // or only  // تعريف الملف وكونه يحتوي على عدة دوائر

// ----------------------------------------------------------
// 1. الاستيراد (Imports)
// ----------------------------------------------------------
import adder;
import comparator.*;  // استيراد كل الدوائر من ملف comparator.ll

// ----------------------------------------------------------
// 2. تعريف دائرة نصف جامع (Half Adder)
// ----------------------------------------------------------
logic half_adder(n_inp=2, n_out=2) {
  // out[0] = ناتج الجمع
  // out[1] = ناتج الحمل

  out[0] = adder(inp[0], inp[1]); // استخدام دائرة adder
  out[1] = inp[0] AND inp[1];
}

// ----------------------------------------------------------
// 3. دائرة مقارنة بت بت واحد (1-bit Comparator)
// ----------------------------------------------------------
logic comparator_1bit(n_inp=2, n_out=1) {
  if (inp[0] == inp[1]) {
    out[0] = 1;
  } else {
    out[0] = 0;
  }
}

// ----------------------------------------------------------
// 4. دائرة رئيسية (Main Circuit)
// ----------------------------------------------------------
logic main_circuit(n_inp=4, n_out=2) {
  int i = 0;
  bool active = true;

  if (active) {
    print("Main circuit active...");
  }

  while (i < 2) {
    print("Processing pair " + i);

    // ناتج الجمع لكل زوج من المدخلات
    out[i] = adder(in[i*2], in[i*2 + 1]);
    i = i + 1;
  }

  // تحقق من التساوي بين المدخلين 0 و1
  bool equal = comparator_1bit(inp[0], inp[1]);
  if (equal) {
    print("Inputs 0 and 1 are equal.");
  } else {
    print("Inputs 0 and 1 are different.");
  }
}

// ----------------------------------------------------------
// 5. وحدة حسابية (Arithmetic Unit)
// ----------------------------------------------------------
logic arithmetic_unit(n_inp=3, n_out=2) {
  int sum = inp[0] + inp[1];
  int remainder = sum mod inp[2];

  if (remainder == 0) {
    out[0] = 1; // success flag
  } else {
    out[0] = 0;
  }

  out[1] = (sum > inp[2]) ? 1 : 0; // مقارنة
}
