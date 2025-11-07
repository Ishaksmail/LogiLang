// ==========================================================
// File: Example.ll
// Description: main logic file that defines multiple circuits
// ==========================================================

Example this has many;  // تعريف الملف وكونه يحتوي على عدة دوائر

// ----------------------------------------------------------
// 1. الاستيراد (Imports)
// ----------------------------------------------------------
import adder;
import comparator.*;  // استيراد كل الدوائر من ملف comparator.ll

// ----------------------------------------------------------
// 2. تعريف دائرة نصف جامع (Half Adder)
// ----------------------------------------------------------
logic half_adder(inputs=2, outputs=2) {
  // out[0] = ناتج الجمع
  // out[1] = ناتج الحمل

  out[0] = adder(in[0], in[1]); // استخدام دائرة adder
  out[1] = in[0] AND in[1];
}

// ----------------------------------------------------------
// 3. دائرة مقارنة بت بت واحد (1-bit Comparator)
// ----------------------------------------------------------
logic comparator_1bit(inputs=2, outputs=1) {
  if (in[0] == in[1]) {
    out[0] = 1;
  } else {
    out[0] = 0;
  }
}

// ----------------------------------------------------------
// 4. دائرة رئيسية (Main Circuit)
// ----------------------------------------------------------
logic main_circuit(inputs=4, outputs=2) {
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
  bool equal = comparator_1bit(in[0], in[1]);
  if (equal) {
    print("Inputs 0 and 1 are equal.");
  } else {
    print("Inputs 0 and 1 are different.");
  }
}

// ----------------------------------------------------------
// 5. وحدة حسابية (Arithmetic Unit)
// ----------------------------------------------------------
logic arithmetic_unit(inputs=3, outputs=2) {
  int sum = in[0] + in[1];
  int remainder = sum mod in[2];

  if (remainder == 0) {
    out[0] = 1; // success flag
  } else {
    out[0] = 0;
  }

  out[1] = (sum > in[2]) ? 1 : 0; // مقارنة
}
