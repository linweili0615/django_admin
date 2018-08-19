<template>
  <el-table
    :data="tableData5"
    v-loading="loading"
    max-height="900px"
    style="width: 90%">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="构建 ID：">
            <span>{{ props.row.name }}</span>
          </el-form-item>
          <el-form-item label="服务器地址：">
            <span>{{ props.row.shop }}</span>
          </el-form-item>
          <el-form-item label="服务名称：">
            <span>{{ props.row.shop }}</span>
          </el-form-item>
          <el-form-item label="服务描述：">
            <span>{{ props.row.id }}</span>
          </el-form-item>
          <el-form-item label="GIT 地址：">
            <span>{{ props.row.shopId }}</span>
          </el-form-item>
          <el-form-item label="GIT 分支：">
            <span>{{ props.row.category }}</span>
          </el-form-item>
          <el-form-item label="上次构建时间：">
            <span>{{ props.row.address }}</span>
          </el-form-item>
          <el-form-item label="上次构建结果：">
            <span>{{ props.row.desc }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="构建 ID"
      prop="id">
    </el-table-column>
    <el-table-column
      label="服务名称"
      prop="name"
      :filters="[{text: '2016-05-01', value: '2016-05-01'}, {text: '2016-05-02', value: '2016-05-02'}, {text: '2016-05-03', value: '2016-05-03'}, {text: '2016-05-04', value: '2016-05-04'}]"
    :filter-method="filterHandler"
      >
    </el-table-column>
    <el-table-column
      label="服务器地址"
      prop="name"
      :filters="[{text: '2016-05-01', value: '2016-05-01'}, {text: '2016-05-02', value: '2016-05-02'}, {text: '2016-05-03', value: '2016-05-03'}, {text: '2016-05-04', value: '2016-05-04'}]"
    :filter-method="filterHandler"
      >
    </el-table-column>
    <el-table-column
      label="服务描述"
      prop="name">
    </el-table-column>
    <el-table-column
      label="GIT 地址"
      prop="desc">
    </el-table-column>
    <el-table-column
      label="GIT 分支"
      prop="desc">
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>  
  </el-table>
</template>

<style scoped>
.demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>

<script>
export default {
    data() {
      return {
        loading : true,
        tableData5: [{
          id: '12987122',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987123',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987125',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987126',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }]
      }
    },
    methods : {
        formatter(row, column) {
        return row.address;
      },
      filterTag(value, row) {
        return row.tag === value;
      },
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      }
    },
    beforeCreate(){
      this.$axios.get('http://localhost:8000/test').then(
        (res) => {
            console.log(res);
            this.loading = false;
        })
      
    }
  }
</script>

