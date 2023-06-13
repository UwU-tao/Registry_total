<template>
  <div class="about">
    <h1>Registry Total</h1>
    <p>RegistryTotal là là ứng dụng web được phát triển nhằm hỗ trợ Cục đăng kiểm và các trung tâm đăng điểm trên toàn quốc quản lý đăng kiểm đối với xe ô tô. CSDL về xe ô tô đã đăng ký (cấp biển số) cũng như các lần đăng kiểm, giấy đăng ký, giấy đăng kiểm được sử dụng chung, thống nhất trên toàn quốc. Chủ xe (công dân) có thể tiến hành đăng kiểm ở bất kỳ trung tâm đăng kiểm nào. Hệ thống phục vụ hai đối tượng sử dụng là Cục đăng kiểm và các trung tâm đăng kiểm. Hệ thống cung cấp các chức năng chính như sau:</p>
    <h4>Chức năng cho Cục đăng kiểm</h4>
    <ul>
      <li>Tạo lập CSDL về xe ô tô đã qua đăng ký (cấp biển số). Cho phép upload từ file danh sách các xe ô tô đã qua đăng ký. (Lưu ý về phạm vi dự án: Hệ thống này không quản lý hoạt động đăng ký cấp biển số mà giả định lấy/đồng bộ dữ liệu đăng ký từ hệ thống khác. Hệ thống này cũng chỉ quản lý đăng kiểm đối với xe ô tô).</li>
      <li>Cấp tài khoản sử dụng cho các trung tâm đăng kiểm.</li>
      <li>Theo dõi và thống kê số lượng, danh sách xe đã được đăng kiểm hàng tháng, quý, năm ở từng trung tâm đăng kiểm, khu vực, hay trên toàn quốc.</li>
      <li>Theo dõi và thống kê số lượng, danh sách xe sắp hết hạn đăng kiểm hàng tháng. Dự báo số lượng xe sẽ đăng kiểm mới và đăng kiểm lại hàng tháng ở từng trung tâm đăng kiểm, khu vực, hay trên toàn quốc.</li>
    </ul>
    <h4>Chức năng cho các trung tâm đăng kiểm</h4>
    <ul>
      <li>Ghi nhận kết quả đăng kiểm và cấp giấy chứng nhận đăng kiểm.</li>
      <li>Theo dõi và thống kê số lượng, danh sách xe đã được đăng kiểm hàng tháng, quý, năm.</li>
      <li>Theo dõi và thống kê số lượng, danh sách xe sắp hết hạn đăng kiểm hàng tháng. Dự báo số lượng xe sẽ đăng kiểm mới và đăng kiểm lại hàng tháng ở  trung tâm.</li>
    </ul>
  </div>
</template>

<style scoped>
.about {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.about h1 {
  text-align: center;
  font-size: 36px;
  margin-bottom: 20px;
}

.about p {
  font-size: 18px;
  line-height: 1.5;
}

.about h4 {
  font-size: 24px;
  margin-top: 40px;
}

.about ul {
  list-style: none;
  padding-left: 0;
}

.about li:before {
  content: '✔';
  margin-right: 10px;
}

@media (max-width: 600px) {
  .about h1 {
    text-align: center;
    font-size: 30px;
  }

  .about p {
    font-size: 16px;
  }

  .about h4 {
    font-size: 20px;
    margin-top: 30px;
  }
}
</style>