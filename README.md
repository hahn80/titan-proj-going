# iTitan Project On the Go


Các dự án đang cần hoàn thiện của iTitan:

**Prob 1**) Use function calling to get prams and feed them to a function to get the results from designed functions.

Context: With the database of student records that contains student_id, student_name, subject, and scores.

In the interaction with a chatbot, students can ask questions about their scores on certain subjects, they might or might not provide student_id.

Use `students.json` for the records to start with. This acts as a fake database for our prototype.

---

~~**Prob 2**) Name Entity Recognition~~

**Mục tiêu**: Xây dựng các model DL hoặc Spacy để nhận diện các thực thể. Các thực thể ở đây được định nghĩa rất tổng quát, không nhất thiết phải tên và địa chỉ, hay cơ quan.

Ví dụ: Thực thể có thể là "Tên Sách", "Tên Con Sông",...

Cách tiếp cận:

1) Dùng các model có sẳn để chạy và tách thực thể cho cả tiếng Anh và tiếng Việt. Có thể tham khảo các model sau:
* NER with Spacy: https://github.com/kriesbeck/spacy-ner
* NER with DL: https://huggingface.co/models?other=named-entity-recognition

2) Yêu cầu thực hiện:
* Chạy các model trên để benchmark kết quả và so sánh, đánh giá xem nên dùng Spacy hay DL?
* Tìm hiểu và chuẩn bị quá trình tự train các model này, hoặc finetune nó, cần phải có khả năng thêm các định nghĩa Entities cho các model khi finetune.

---

~~**Prob 3**) Relation Extraction~~

**Mục tiêu**: Xây dựng các model DL để trích xuất ra các mối liên hệ giữa các thực thể.

Ví dụ: Tên người "Musk" là "OWNER" của "SpaceX".

Cách tiếp cận:

1) Dùng các model có sẳn để chạy trích xuất cho tiếng Anh. Có thể tham khảo các model sau:
* Relik: https://github.com/SapienzaNLP/relik

2) Yêu cầu thực hiện:
* Chạy các model trên để trích xuất các mối liên hệ.
* Tìm hiểu và tóm tắt các định dạng người ta đang dùng để  tách các mối quan hệ giữa các thực thể.
* Mục tiêu lâu dài là tự train hoặc finetune model DL cho riêng mình.






