# Retrieval Retrieval Augmented Generation Assessment (RAGAS)

Ragas là một framework giúp đánh giá RAG. RAG biểu thị một lớp ứng dụng LLM sử dụng dữ liệu bên ngoài để tăng cường ngữ cảnh của LLM. Hiện có các công cụ và khung giúp bạn xây dựng các quy trình này nhưng việc đánh giá nó và định lượng hiệu suất quy trình có thể khó khăn. Đây là lúc Ragas xuất hiện.

## Evaluation Strategies

**Hệ thống RAG: câu hỏi q, context c(q) và sinh câu trả lời a(q)**

* **Faithfulness** 

Đo lường tính nhất quán thực tế của câu trả lời được tạo ra so với bối cảnh nhất định. Nó được tính toán từ câu trả lời và bối cảnh được truy xuất. Câu trả lời được chia tỷ lệ thành phạm vi (0,1), càng cao càng tốt.

Để đánh giá faithfulness, sử dụng LLM 

* **Answer relevancy**

Mức độ liên quan của Câu trả lời, tập trung vào việc đánh giá mức độ phù hợp của câu trả lời được tạo ra với lời nhắc đưa ra. Điểm thấp hơn được ấn định cho các câu trả lời không đầy đủ hoặc chứa thông tin dư thừa và điểm cao hơn cho thấy mức độ liên quan tốt hơn. Số liệu này được tính bằng cách sử dụng câu hỏi, ngữ cảnh và câu trả lời

* **Context recall**

Đo lường mức độ mà bối cảnh được truy xuất phù hợp với câu trả lời được chú thích, được coi là sự thật cơ bản. Nó được tính toán dựa trên sự thật cơ bản và bối cảnh được truy xuất, đồng thời các giá trị nằm trong khoảng từ 0 đến 1, với giá trị cao hơn cho thấy hiệu suất tốt hơn.

* **Context precision**

Độ chính xác của bối cảnh là thước đo đánh giá xem liệu tất cả các mục có liên quan đến sự thật cơ bản có trong ngữ cảnh có được xếp hạng cao hơn hay không. Lý tưởng nhất là tất cả các phần có liên quan phải xuất hiện ở hàng đầu. Số liệu này được tính toán bằng cách sử dụng câu hỏi, ground_truth và ngữ cảnh, với các giá trị nằm trong khoảng từ 0 đến 1, trong đó điểm cao hơn biểu thị độ chính xác cao hơn.

