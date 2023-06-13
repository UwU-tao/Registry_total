<template>
<div>
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Center Code</th>
                <th>Location</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in dataTable" :key="item.id">
              <td>{{ item.id }}</td>
              <td>{{ item.username }}</td>
              <td>{{ cityNames[item.username.substring(0, 2)] }}</td>
            </tr>
        </tbody>
    </table>
</div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
        return {
            dataTable: [],
            cityNames: {
                '29': 'Hà Nội',
                '50': 'TP. Hồ Chí Minh',
            },
        }
    },
    methods: {
        fetchData() {
            axios.get('/api/users/')
            .then(response => {
                console.log(response.data)
                this.dataTable = response.data
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    mounted() {
        this.fetchData()
    },
  }

</script>

<style scoped>
* {
    text-align: center;
}
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
</style>