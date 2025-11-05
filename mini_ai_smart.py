import re

class MiniLegalAI:
    def __init__(self, workbook_path=None):
        self.workbook_path = workbook_path
        self.index = {}  # lightweight placeholder
        # In production: load Excel into searchable DB (pandas, whoosh/FAISS, etc.)

    def analyze(self, text):
        if not text or not isinstance(text, str):
            return "❗ يرجى إدخال نص صحيح للتحليل."
        txt = text.strip()
        # Simple rule-based examples
        if "إجاز" in txt or "إجازة" in txt:
            return "يبدو أن الاستفسار عن الإجازات — الموظف قد يستحق إجازة سنوية حسب سنوات الخدمة."
        if "فصل" in txt or "طرد" in txt:
            return "قد يتعلق الأمر بفصل تعسفي — ينصح بجمع المستندات والتواصل مع مفتش العمل."
        return "لا توجد نتيجة قطعية — يُنصح بإرسال نص أو سؤال أكثر تفصيلاً."

    def search_law(self, term):
        return f"بحث وهمي عن '{term}' — في النسخة الكاملة سيتم عرض المواد المطابقة."

    def compare_versions(self, clause_id, v_a=1996, v_b=2024):
        return f"مقارنة افتراضية للمادة {clause_id} بين {v_a} و {v_b}."