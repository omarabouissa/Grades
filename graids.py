def calculate_grade():
    """
    برنامج لحساب تقدير الطالب بناءً على الدرجة المدخلة.
    يدعم الاستمرارية ومعالجة الأخطاء.
    """
    print("--- برنامج نظام التقديرات ---")
    print("أدخل درجة الطالب (0-100) أو اكتب 'خروج' للإغلاق.")

    while True:
        user_input = input("\nأدخل الدرجة: ").strip().lower()

        # شرط الخروج
        if user_input == "خروج" or user_input == "exit":
            print("تم إغلاق البرنامج. وداعاً!")
            break

        try:
            # محاولة تحويل المدخل إلى رقم
            score = float(user_input)

            # التحقق من منطقية الدرجة
            if score < 0 or score > 100:
                print("خطأ: يرجى إدخال درجة ما بين 0 و 100.")
                continue

            # تحديد التقدير
            if score >= 90:
                grade = "ممتاز (Excellent)"
            elif score >= 80:
                grade = "جيد جداً (Very Good)"
            elif score >= 70:
                grade = "جيد (Good)"
            elif score >= 60:
                grade = "مقبول (Pass)"
            else:
                grade = "راسب (Fail)"

            print(f"تقدير الطالب هو: {grade}")

        except ValueError:
            # معالجة حالات الإدخال غير الصحيح (نصوص بدلاً من أرقام)
            print("خطأ: مدخل غير صالح! يرجى إدخال رقم صحيح أو كلمة 'خروج'.")

if __name__ == "__main__":
    calculate_grade()
