from pdf2image import convert_from_path
import cv2

def pdf_to_high_res_image(pdf_path, output_folder, dpi=900):
    # Chuyển đổi từng trang của PDF thành ảnh độ phân giải cao
    pages = convert_from_path(pdf_path, dpi=dpi)

    # Lưu từng trang ảnh xuống đĩa
    for i, page in enumerate(pages):
        image_path = f"{output_folder}/page_{i+1}.jpg"  # Đường dẫn và tên file ảnh đầu ra
        page.save(image_path, 'JPEG')

# Thực thi hàm chuyển đổi
pdf_file = "Project/demo.pdf"
output_folder = "Project/Img"
pdf_to_high_res_image(pdf_file, output_folder)

import cv2

def rotate_image(image_path, output_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)
    
    # Xoay ảnh 90 độ theo chiều kim đồng hồ
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    
    # Lưu ảnh đã xoay xuống đĩa
    cv2.imwrite(output_path, rotated_image)

# Thực thi hàm xoay ảnh
input_image = "Project/Img/page_1.jpg"
output_image = "Project/Img/page_1.jpg"

rotate_image(input_image, output_image)
