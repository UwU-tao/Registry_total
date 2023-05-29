<template>
    <table class="table">
        <thead>
            <tr>
                <th><input type="checkbox" v-model="selectAll" @change="toggleSelectAll"></th>
                <th @click="sortBy('id')" :class="{ active: currentSortColumn === 'id', asc: currentSortDirection === 'asc', desc: currentSortDirection === 'desc'}">ID<span v-if="currentSortColumn === 'id'">{{ currentSortDirection === 'asc' ? '▲' : '▼' }}</span></th>
                <th @click="sortBy('name')" :class="{ active: currentSortColumn === 'name', asc: currentSortDirection === 'asc', desc: currentSortDirection === 'desc'}">Name<span v-if="currentSortColumn === 'name'">{{ currentSortDirection === 'asc' ? '▲' : '▼' }}</span></th>
                <th>Email</th>
                <th>Username</th>
                <th>Zipcode</th>
                <th>Phone</th>
                <th>Website</th>
                <th>Company</th>
                <th>Details</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in tableData" :key="item.id">
              <td><input type="checkbox" v-model="item.selected"></td>
              <td>{{ item.id }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.email }}</td>
              <td>{{ item.username }}</td>
              <td>{{ item.address.zipcode }}</td>
              <td>{{ item.phone }}</td>
              <td>{{ item.website }}</td>
              <td>{{ item.company.name }}</td>
              <td><button @click="showModal(item)" class="detail">Show Details</button></td>
              <td>
                <button @click="editItem(item)">Edit</button>
                <button @click="deleteItem(item)">Delete</button>
              </td>
            </tr>
        </tbody>
    </table>
    <div v-if="currentItem" class="modal" @click="closeModal">
      <div class="modal-content" @click.stop>
        <span @click="closeModal" class="close">&times;</span>
        <h2>{{ currentItem.name }}</h2>
        <p><b>Address:</b> {{ currentItem.address.street }}, {{ currentItem.address.suite }}, {{ currentItem.address.city }}</p>
        <p><b>Company:</b> {{ currentItem.company.name }}</p>
        <p><b>Company catchphrase:</b> {{ currentItem.company.catchPhrase }}</p>
        <p><b>Company bs:</b> {{ currentItem.company.bs }}</p>
        <button @click="exportToPDF">Export to PDF</button>
      </div>
    </div>
     <button @click="exportToCSV">Export to CSV</button>
</template>
  
<script>
  import axios from 'axios'
  import jsPDF from 'jspdf'
  
  export default {
    data() {
      return {
        tableData: [],
        currentSortColumn: null,
        currentSortDirection: 'asc',
        dialog: false,
        currentItem: null,
        selectAll: false,
      }
    },
    methods: {
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
        let headers = ["ID", "Name", "Email", "Username"];
        csvContent += headers.map(header => `"${header}"`).join(",") + "\r\n";
        selectedRows.forEach(function(row) {
          let rowData = [row.id, row.name, row.email, row.username];
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
        // Create a new jsPDF instance
        const doc = new jsPDF()
        
        // Add the item details to the PDF
        doc.text(`Name: ${this.currentItem.name}`, 10, 10)
        doc.text(`Address: ${this.currentItem.address.street}, ${this.currentItem.address.suite}, ${this.currentItem.address.city}`, 10, 20)
        doc.text(`Company: ${this.currentItem.company.name}`, 10, 30)
        doc.text(`Company catchphrase: ${this.currentItem.company.catchPhrase}`, 10, 40)
        doc.text(`Company bs: ${this.currentItem.company.bs}`, 10, 50)
        
        // Save the PDF
        doc.save('item_details.pdf')
      },
      toggleSelectAll() {
        this.tableData.forEach(item => item.selected = this.selectAll)
      },
    },
    mounted() {
      axios.get('http://localhost:8080/data.json')
        .then(response => {
          this.tableData = response.data.map(item => ({ ...item, selected: false }));
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
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
</style>