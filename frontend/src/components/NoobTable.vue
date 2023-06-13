<template>
    <table class="table">
        <thead>
            <tr>
                <th><input type="checkbox" v-model="selectAll" @change="toggleSelectAll"></th>
                <th @click="sortBy('id')" :class="{ active: currentSortColumn === 'id', asc: currentSortDirection === 'asc', desc: currentSortDirection === 'desc'}">ID<span v-if="currentSortColumn === 'id'">{{ currentSortDirection === 'asc' ? '▲' : '▼' }}</span></th>
                <th>License Plate</th>
                <th>Brand</th>
                <th>Registration Date</th>
                <th>Expiration Date</th>
                <th>Details</th>
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
            </tr>
        </tbody>
    </table>
</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {

            }
        },
        methods: {

        }
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