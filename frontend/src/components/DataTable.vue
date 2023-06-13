<template>
  <label class="searchLabel">Search:</label>

  <div v-for="(searchField, index) in searchFields" :key="index">
    <select v-model="searchField.column" class="searchColumn">
      <option value="">Select column...</option>
      <option value="plate">Plate</option>
      <option value="brand">Brand</option>
      <option value="regis_center">Registration Center</option>
      <option value="regis_date">Registration Date</option>
      <option value="exp_date">Expiration Date</option>
      <option value="city">City</option>
    </select>
    <select v-model="searchField.datePart" class="searchColumn" v-if="searchField.column === 'regis_date' || searchField.column === 'exp_date'">
      <option value="">Select date part...</option>
      <option value="year">Year</option>
      <option value="quarter">Quarter</option>
      <option value="month">Month</option>
      <option value="date">Date</option>
    </select>
    <input type="text" v-model="searchField.query" class="searchField">
    <button @click="addSearchField" class="addField">+</button>
    <button @click="removeSearchField" class="removeField" v-if="index > 0">-</button>
  </div>

  <div>
    <label class="filterLabel">Filter by expired time: </label>
    <select class="timeRemaining" v-model="timeRemain">
      <option value="">Select time remaining...</option>
      <option value="0">Expired</option>
      <option value="1">Less than 1 month</option>
      <option value="3">Less than 3 months</option>
      <option value="6">Less than 6 months</option>
      <option value="12">Less than 1 year</option>
    </select>
  </div>

  <div>
    <!-- <button @click="addRecord">Add record</button> -->
    <button @click="open" style="text-align: center;" v-if="username!=='admin'">Add record</button>
    <div class="modall" :class="{ 'show': show }">
      <div class="modall-content">
        <span class="close" @click="close">&times;</span>
        <h1>Add Record</h1>
        <form @submit="submitForm">
          <div class="formm-group">
            <label for="license_plate">License Plate:</label>
          <input type="text" id="license_plate" v-model="license_plate" required>
          </div>
          
          <div class="formm-group">
            <label for="code">Code:</label>
          <input type="text" id="code" v-model="code" required>
          </div>
          
          <div class="formm-group">
            <label for="regis_date">Registration Date:</label>
            <input type="text" id="regis_date" v-model="regis_date" required>
          </div>
          
          <div class="formm-group">
            <label for="exp_date">Expiration Date:</label>
            <input type="text" id="exp_date" v-model="exp_date" required>
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>


    <table class="table">
        <thead>
            <tr>
                <th><input type="checkbox" v-model="selectAll" @change="toggleSelectAll"></th>
                <th @click="sortBy('id')" :class="{ active: currentSortColumn === 'id', asc: currentSortDirection === 'asc', desc: currentSortDirection === 'desc'}">ID<span v-if="currentSortColumn === 'id'">{{ currentSortDirection === 'asc' ? '▲' : '▼' }}</span></th>
                <th>License Plate</th>
                <th>Brand</th>
                <th>Registration Date</th>
                <th>Expiration Date</th>
                <th>Registration Center</th>
                <th>Details</th>
                <!-- <th>Actions</th> -->
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in displayedTableData" :key="item.inc">
              <td><input type="checkbox" v-model="item.selected"></td>
              <td>{{ item.inc }}</td>
              <td>{{ item.Vehicle.plate }}</td>
              <td>{{ item.Vehicle.brand }}</td>
              <td>{{ item.Regis.regis_date }}</td>
              <td>{{ item.Regis.expiration_date }}</td>
              <td>{{ item.Regis.regis_center }}</td>
              <td><button @click="showModal(item)" class="detail">Show Details</button></td>
              <!-- <td>
                <button @click="editItem(item)">Edit</button>
                <button @click="deleteItem(item)">Delete</button>
              </td> -->
            </tr>
        </tbody>
        <tfoot>
          <tr>
            <td>Total cars: {{ totalCars }}</td>
          </tr>
        </tfoot>
    </table>
  </div>

  <div>
    <label>Rows per Page:</label>
    <select v-model="perPage">
      <option value="10">10</option>
      <option value="20">20</option>
      <option value="50">50</option>
      <option value="100">100</option>
      <option value="all">All</option>
    </select>
  </div>
  <div>
    <button @click="goToPreviousPage" :disabled="currentPage === 1">Previous</button>
    <button @click="goToNextPage" :disabled="currentPage === totalPages">Next</button>
    <div>Page {{ currentPage }} of {{ totalPages }}</div>
  </div>

  <div v-if="currentItem" class="modal" @click="closeModal">
    <div class="modal-content" @click.stop>
      <span @click="closeModal" class="close">&times;</span>
      <h2>Details about Vehicle Registration</h2>
      <p><b>1. Owner</b></p>
      <p><b>ID:</b> {{ currentItem.Owner.idd }}</p>
      <p><b>Name:</b> {{ currentItem.Owner.last_name }} {{ currentItem.Owner.first_name }}</p>
      <p><b>Address:</b> {{ currentItem.Owner.address }}</p>
      <p><b>Email:</b> {{ currentItem.Owner.email }}</p>
      <p><b>Phone:</b> {{ currentItem.Owner.phone }}</p>
      <p><b>Date of birth:</b> {{ currentItem.Owner.dob }}</p>
      <p><b>2. Vehicle</b></p>
      <p><b>Plate:</b> {{ currentItem.Vehicle.plate }}</p>
      <p><b>Register Date:</b> {{ currentItem.Vehicle.regis_date }}</p>
      <p><b>Register Province:</b> {{ currentItem.Vehicle.province }}</p>
      <p><b>Type:</b> {{ currentItem.Vehicle.type }}</p>
      <p><b>Brand:</b> {{ currentItem.Vehicle.brand }}</p>
      <p><b>Model:</b> {{ currentItem.Vehicle.model_code }}</p>
      <p><b>Manufacturer Year:</b> {{ currentItem.Vehicle.man_year }}</p>
      <p><b>Manufacturer Country:</b> {{ currentItem.Vehicle.man_country }}</p>
      <p><b>Engine No:</b> {{ currentItem.Vehicle.engine_no }}</p>
      <p><b>Chassis No:</b> {{ currentItem.Vehicle.chassis_no }}</p>
      <p><b>Color:</b> {{ currentItem.Vehicle.color }}</p>
      <p><b>Weight:</b> <i>Sit:</i> {{ currentItem.Vehicle.sit }} <i>Load:</i> {{ currentItem.Vehicle.load }}</p>
      <p><b>Modification:</b> {{ currentItem.Vehicle.modification != null ? "Yes" : "No" }} </p>
      <p><b>Lifetime Limit:</b> {{ currentItem.Vehicle.lifetime_limit }}</p>
      <p><b>Purpose:</b> {{ currentItem.Vehicle.purpose }}</p>
      <p><b>3. Vehicle Registration</b></p>
      <p><b>Registration Code:</b> {{ currentItem.Regis.codee }}</p>
      <p><b>Registration Date:</b> {{ currentItem.Regis.regis_date }}</p>
      <p><b>Expiration Date:</b> {{ currentItem.Regis.expiration_date }}</p>
      <p><b>Registration Center:</b> {{ currentItem.Regis.regis_center }}</p>
      <p><b>Registration Province:</b> {{ cityNames[currentItem.Regis.regis_center.substring(0, 2)] }} </p>
      <button @click="exportToPDF">Export to PDF</button>
    </div>
  </div>

  <form v-if="username === 'admin'">
    <input type="file" @change="handleFileUpload" ref="fileInput" enctype="multipart/form-data">
    <button @click="uploadFile">Upload</button>
  </form>
  <button @click="exportToCSV">Export to CSV</button>
</template>
  
<script>
  import axios from 'axios'
  import jsPDF from 'jspdf'
  import { normal_font } from "../assets/times-normal.js";
  import { bold_font } from "../assets/timesbd-bold.js";
  import { italic_font } from "../assets/timesi-italic.js";
  import { bi_font } from "../assets/timesbi-bolditalic.js";


  import index from '../store/index.js'
  
  export default {
    data() {
      return {
        tableData: [],
        displayedTableData: [],
        currentSortColumn: null,
        currentSortDirection: 'asc',
        currentItem: null,
        selectAll: false,
        file: null,
        timeRemain: '',
        perPage: 10,
        currentPage: 1,
        totalPages: 1,
        searchFields: [{column: '', datePart: '', query:''}],
        cityNames: {
          '29': 'Hà Nội',
          '50': 'TP. Hồ Chí Minh',
        },
        show: false,
        license_plate:'', code:'', regis_date:'', exp_date:'', regis_center:''
      }
    },

    methods: {
      open() {
      this.show = true
    },
    close() {
      this.show = false
    },
      addRecord() {
        let link = '';
        if (this.username !== 'admin') {link = '/api/record/'}
        const record = {
          license_plate: this.license_plate,
          code: this.code,
          regis_date: this.regis_date,
          exp_date: this.exp_date,
          regis_center: this.username
        }
        axios.post(link, record)
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error.data)
        })
      },
      fetchData() {
        let link = '';
        if (this.username === 'admin') {link = '/api/vehicles/';}
        else {link = `/api/vehicles/${this.username}/`}
        axios.get(link)
        .then(response => {
          // this.tableData = response.data.map(item => ({ ...item, selected: false }));
          this.tableData = response.data;
          this.calculateDisplayedData();
          this.calculateTotalPages();
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
      },

      sortBy(column) {
        if (column === this.currentSortColumn) {
          this.currentSortDirection = this.currentSortDirection === 'asc' ? 'desc' : 'asc';
        } else {
          this.currentSortColumn = column;
          this.currentSortDirection = 'asc';
        }
        this.tableData.sort((a, b) => {
          let modifier = 1;
          if (this.currentSortDirection === 'desc') modifier = -1;
          if (a[this.currentSortColumn] < b[this.currentSortColumn]) return -1 * modifier;
          if (a[this.currentSortColumn] > b[this.currentSortColumn]) return 1 * modifier;
          return 0;
        });
      },

      showModal(item) {
        this.currentItem = item;
      },

      closeModal() {
        this.currentItem = null;
      },

      exportToCSV() {
        const selectedRows = this.tableData.filter(row => row.selected);
        let csvContent = "data:text/csv;charset=utf-8,";
        let headers = ["ID", "License Plate", "Brand", "Registration Date", "Expiration Date", "Registration Center"];
        csvContent += headers.map(header => `"${header}"`).join(",") + "\r\n";
        selectedRows.forEach(function(row) {
          let rowData = [row.id, row.license_plate, row.regis_date, row.expiration_date, row.regis_center];
          let rowString = rowData.map(value => `"${value}"`).join(",");
          csvContent += rowString + "\r\n";
        });
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "selected_rows.csv");
        document.body.appendChild(link);
        link.click();
      },

      exportToPDF() {
        const doc = new jsPDF({
          unit: 'mm',
          orientation: 'p',
          format: 'a4',
        });
        doc.addFileToVFS('../assets/times.ttf', normal_font);
        doc.addFont('../assets/times.ttf', 'Times New Roman', 'normal');
        doc.addFileToVFS('../assets/timesbd.ttf', bold_font);
        doc.addFont('../assets/timesbd.ttf', 'Times New Roman', 'bold');
        doc.addFileToVFS('../assets/timesi.ttf', italic_font);
        doc.addFont('../assets/timesi.ttf', 'Times New Roman', 'italic');
        doc.addFileToVFS('../assets/timesbi.ttf', bi_font);
        doc.addFont('../assets/timesbi.ttf', 'Times New Roman', 'bolditalic');
        doc.setFont('Times New Roman', 'normal');
        doc.setFontSize(12);
        
        doc.setFont('Times New Roman', 'bold');
        doc.setFontSize(24);
        doc.text('Thông tin đăng kiểm', 10, 10);

        doc.setFont('Times New Roman', 'bolditalic');
        doc.setFontSize(14);
        doc.text('1. Thông tin về chủ xe', 10, 20);

        doc.setFont('Times New Roman', 'normal');
        doc.setFontSize(12);
        doc.text(`Số CCCD: ${this.currentItem.Owner.idd}`, 10, 30);
        doc.text(`Họ tên: ${this.currentItem.Owner.last_name} ${this.currentItem.Owner.first_name}`, 10, 40);
        doc.text(`Email: ${this.currentItem.Owner.email}`, 10, 50);
        doc.text(`Số điện thoại: ${this.currentItem.Owner.phone}`, 10, 60);
        doc.text(`Địa chỉ: ${this.currentItem.Owner.address}`, 10, 70);
        doc.text(`Ngày sinh: ${this.currentItem.Owner.dob}`, 10, 80);

        doc.setFont('Times New Roman', 'bolditalic');
        doc.setFontSize(14);
        doc.text('2. Thông tin về phương tiện', 10, 90);

        doc.setFont('Times New Roman', 'normal');
        doc.setFontSize(12);
        doc.text(`Biển số xe: ${this.currentItem.Vehicle.plate}`, 10, 100);
        doc.text(`Ngày đăng ký: ${this.currentItem.Vehicle.regis_date}`, 10, 110);
        doc.text(`Tỉnh đăng ký: ${this.currentItem.Vehicle.province}`, doc.getStringUnitWidth(`Ngày đăng ký: ${this.currentItem.Vehicle.regis_date}`) + 50, 110);
        doc.text(`Loại xe: ${this.currentItem.Vehicle.type}`, 10, 120);
        doc.text(`Hãng xe: ${this.currentItem.Vehicle.brand}`, doc.getStringUnitWidth(`Loại xe: ${this.currentItem.Vehicle.type}`) + 50, 120);
        doc.text(`Mẫu xe: ${this.currentItem.Vehicle.model_code}`, doc.getStringUnitWidth(`Ngày đăng ký: ${this.currentItem.Vehicle.regis_date}`) + doc.getStringUnitWidth(`Loại xe: ${this.currentItem.Vehicle.type}`) + 100, 120);
        doc.text(`Nước, năm sản xuất: ${this.currentItem.Vehicle.man_country}, ${this.currentItem.Vehicle.man_year}`, 10, 130);
        doc.text(`Mã động cơ: ${this.currentItem.Vehicle.engine_no}`, 10, 140);
        doc.text(`Mã khung xe: ${this.currentItem.Vehicle.chassis_no}`, doc.getStringUnitWidth(`Mã động cơ: ${this.currentItem.Vehicle.engine_no}`) + 50, 140);
        doc.text(`Màu xe: ${this.currentItem.Vehicle.color}`, 10, 150);
        doc.text(`Trọng tải: Số ghế ngồi: ${this.currentItem.Vehicle.sit}, Khối lượng chuyên chở: ${this.currentItem.Vehicle.load != null ? this.currentItem.Vehicle.load : ''}`, doc.getStringUnitWidth(`Màu xe: ${this.currentItem.Vehicle.color}`) + 50, 150);
        doc.text(`Mục đích sử dụng: ${this.currentItem.Vehicle.purpose}`, 10, 160);

        doc.setFont('Times New Roman', 'bolditalic');
        doc.setFontSize(14);
        doc.text('3. Thông tin đăng kiểm', 10, 170);

        doc.setFont('Times New Roman', 'normal');
        doc.setFontSize(12);
        doc.text(`Mã đăng kiểm: ${this.currentItem.Regis.codee}`, 10, 180);
        doc.text(`Ngày đăng kiểm: ${this.currentItem.Regis.regis_date}`, 10, 190);
        doc.text(`Ngày hết hạn: ${this.currentItem.Regis.expiration_date}`, 10, 200);
        doc.text(`Trung tâm đăng kiểm: ${this.currentItem.Regis.regis_center}`, 10, 210);
        doc.text(`Tỉnh đăng kiểm: ${this.cityNames[this.currentItem.Regis.regis_center.substring(0, 2)]}`, doc.getStringUnitWidth(`Trung tâm đăng kiểm: ${this.currentItem.Regis.regis_center}`) + 100, 210);

        doc.save('item_details.pdf');
      },

      toggleSelectAll() {
        this.tableData.forEach(item => item.selected = this.selectAll);
      },

      handleFileUpload(event) {
        event.preventDefault();
        this.file = event.target.files[0];
      },

      async uploadFile() {
        const formData = new FormData();
        formData.append('excel_file', this.file);
        await axios
          .post('/api/import/', formData)
          .then(response => {
            console.log(response.data);
            // Handle success message or redirect
          })
          .catch(error => {
            console.error(error);
            // Handle error
          });
      },

      computeDaysRemaining(expiration_date) {
        const [day, month, year] = expiration_date.split('/');
        const dueDateTime = new Date(year, month - 1, day).getTime();
        const currentTime = new Date().getTime();
        const timeDiff = dueDateTime - currentTime;
        return Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
      },

      goToPreviousPage() {
        if (this.currentPage > 1) {
          this.currentPage--;
        }
      },

      goToNextPage() {
        if (this.currentPage < this.totalPages) {
          this.currentPage++;
        }
      },

      calculateDisplayedData() {
        const startIndex = (this.currentPage - 1) * this.perPage;
        let endIndex = startIndex + this.perPage;
        if (this.perPage === 'all' || endIndex > this.filteredTableData.length) {
          endIndex = this.filteredTableData.length;
        }
        this.displayedTableData = this.filteredTableData.slice(startIndex, endIndex);
      },

      calculateTotalPages() {
        if (this.perPage === 'all') {
          this.totalPages = 1;
        } else {
          this.totalPages = Math.ceil(this.filteredTableData.length / this.perPage);
        }
        if (this.currentPage > this.totalPages) {
          this.currentPage = this.totalPages;
        }
        if (this.currentPage === 0 && this.totalPages > 0) {
          this.currentPage = 1; // Reset to page 1 if currentPage is 0
        }
      },

      addSearchField() {
        this.searchFields.push({column: '', datePart: '', query:''});
      },

      removeSearchField() {
        this.searchFields.pop();
      },

    },

    watch: {
      perPage() {
        this.calculateDisplayedData();
        this.calculateTotalPages();
      },
      currentPage() {
        this.calculateDisplayedData();
      },
      filteredTableData() {
        this.calculateDisplayedData();
        this.calculateTotalPages();
      },
    },

    mounted() {
      this.fetchData();
    },

    computed: {
      filteredTableData() {
        let filteredData = this.tableData;
        if (this.searchFields.length > 0) {
          filteredData = filteredData.filter(item => {
            return this.searchFields.every(searchField => {
              if (!searchField.column || !searchField.query) return true;
              // extract day, month, and year from registration date
              const [regisDay, regisMonth, regisYear] = item.Regis.regis_date.split('/');
              const regisQuarter = Math.ceil(regisMonth / 3);
              // extract day, month, and year from expiration date
              const [expDay, expMonth, expYear] = item.Regis.expiration_date.split('/');
              const expQuarter = Math.ceil(expMonth / 3);
              switch (searchField.column) {
                case 'plate':
                  return item.Vehicle.plate.toLowerCase().startsWith(searchField.query.toLowerCase());
                case 'brand':
                  return item.Vehicle.brand.toLowerCase().startsWith(searchField.query.toLowerCase());
                case 'regis_center':
                  return item.Regis.regis_center.toLowerCase().startsWith(searchField.query.toLowerCase());
                case 'regis_date':
                  switch (searchField.datePart) {
                    case 'year':
                      return regisYear === searchField.query;
                    case 'quarter':
                      return regisQuarter === parseInt(searchField.query);
                    case 'month':
                      { // add leading zero to search query if it is a single digit
                        let regisMonthQuery = searchField.query.length === 1 ? '0' + searchField.query : searchField.query;
                        return regisMonth === regisMonthQuery;
                      }
                    case 'date':
                      { // add leading zero to search query if it is a single digit
                        let regisDayQuery = searchField.query.length === 1 ? '0' + searchField.query : searchField.query;
                        return regisDay === regisDayQuery;
                      }
                    default:
                      return false;
                  }
                case 'exp_date':
                  switch (searchField.datePart) {
                    case 'year':
                      return expYear === searchField.query;
                    case 'quarter':
                      return expQuarter === parseInt(searchField.query);
                    case 'month':
                      { // add leading zero to search query if it is a single digit
                        let expMonthQuery = searchField.query.length === 1 ? '0' + searchField.query : searchField.query;
                        return expMonth === expMonthQuery;
                      }
                    case 'date':
                      { // add leading zero to search query if it is a single digit
                        let expDayQuery = searchField.query.length === 1 ? '0' + searchField.query : searchField.query;
                        return expDay === expDayQuery;
                      }
                    default:
                      return false;
                  }
                case 'city':
                  { // extract city code from registration center
                    const cityCode = item.Regis.regis_center.substring(0, 2);
                    // look up city name from city code
                    const cityName = this.cityNames[cityCode];
                    return cityName && cityName.toLowerCase().startsWith(searchField.query.toLowerCase());
                  }
                default:
                  return false;
              }
            });
          });
        }

        if (this.timeRemain) {
          if (this.timeRemain === '0') {
          filteredData = filteredData.filter(
            item => this.computeDaysRemaining(item.Regis.expiration_date) < 0
          );
          } else {
            const days = parseInt(this.timeRemain) * 30;
            filteredData = filteredData.filter(
              item => this.computeDaysRemaining(item.Regis.expiration_date) < days && this.computeDaysRemaining(item.Regis.expiration_date) > 0
            );
          }
        } 
        return filteredData;
      },

      totalCars() {
        return this.filteredTableData.length;
      },

      username: function() {
        return index.getters.getUsername;
      },
    },
  }
</script>

<style>

.table {
    width: 100%;
    margin-bottom: 1rem;
    color: #212529;
    border-collapse: collapse;
    border-spacing: 0;
    background-color: #fff;
}
.table td, .table th {
    padding: .75rem;
    vertical-align: top;
    border-top: 1px solid #dee2e6;
}
.table thead th {
    vertical-align: bottom;
    border-bottom: 2px solid #dee2e6;
}
.table tbody + tbody {
    border-top: 2px solid #dee2e6;
}
.table :hover {
    background-color: rgba(0, 0, 0, 0.075);
}
th.active {
  background-color: lightblue;
}
.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}
.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 70%;
}
.close {
  color: #aaa;
  float:right;
  font-size:28px;
}
.close:hover, .close:focus {
   color:black;
   text-decoration:none;
   cursor:pointer;
}
.searchLabel {
  margin-right: 10px;
}
.searchColumn {
  margin-right: 10px;
  border: 1px solid #ccc;
}
.searchField {
  margin-right: 10px;
  border: 1px solid #ccc;
}
.addField {
  margin-right: 10px;
  border: 1px solid #ccc;
}
.removeField {
  margin-right: 10px;
  border: 1px solid #ccc;
}
.filterLabel {
  margin-right: 10px;
}
.timeRemaining {
  margin-right: 10px;
  border: 1px solid #ccc;
}

/* Modal */
.modall {
  display: none;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.5);
}

.modall.show {
  display: block;
}

/* Modal Content */
.modall-content {
  background-color: #fefefe;
  margin: 10% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 400px;
  max-width: 90%;
}

/* Close Button */
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
}

/* Form */
.formm-group {
  margin-bottom: 20px;
}
</style>