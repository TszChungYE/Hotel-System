<template>
  <div>
    <!--页面区域-->
    <div class="page-view">
      <div class="table-operations">
        <a-space>
          <a-button @click="handleBatchDelete">批量删除</a-button>
        </a-space>
      </div>
      <a-table
        size="middle"
        rowKey="id"
        :loading="data.loading"
        :columns="columns"
        :data-source="data.tagList"
        :scroll="{ x: 'max-content' }"
        :row-selection="rowSelection"
        :pagination="{
          size: 'default',
          current: data.page,
          pageSize: data.pageSize,
          onChange: (current) => (data.page = current),
          showSizeChanger: false,
          showTotal: (total) => `共${total}条数据`,
        }"
      >
        <template #bodyCell="{ text, record, index, column }">
          <!-- {{ text }} -->
          <!-- {{ record }} -->
          <template v-if="column.key === 'status'">
          
            <a-tag v-if="text==0" style="background-color: #87d068;color: white;">已完成</a-tag>
            <a-tag v-if="text==1" style="background-color: #d0686d;color: white;">待支付</a-tag>
            <a-tag v-if="text==7" style="background-color: #8468d0;color: white;">已取消</a-tag>
            <a-tag v-if="text==2" style="background-color: #68d0c2;color: white;">已支付</a-tag>


          </template>
          <template v-if="column.key === 'operation'">
            <span>
              <a-popconfirm v-if="record.status == 2" title="确定订单已完成?" ok-text="是" cancel-text="否" @confirm="confirmOk(record)">
                <a>完成</a>
              </a-popconfirm>
              <a-divider type="vertical" v-if="record.status != 0" />
              <a-popconfirm v-if="record.status != 0"  title="确定取消?" ok-text="是" cancel-text="否" @confirm="confirmCancel(record)">
                <a>取消</a>
              </a-popconfirm>
              <a-divider type="vertical" />
              <a-popconfirm title="确定删除?" ok-text="是" cancel-text="否" @confirm="confirmDelete(record)">
                <a>删除</a>
              </a-popconfirm>
            </span>
          </template>
        </template>
      </a-table>
    </div>

  </div>
</template>

<script setup lang="ts">
  import { FormInstance, message } from 'ant-design-vue';
  import { createApi, listApi, updateApi, deleteApi, cancelApi, okApi } from '/@/api/admin/order';
  import {getFormatTime} from "/@/utils";


  const columns = reactive([
    {
      title: '序号',
      dataIndex: 'index',
      key: 'index',
      align: 'center'
    },
    {
      title: '用户',
      dataIndex: 'username',
      key: 'username',
      align: 'center'
    },
    {
      title: '手机号',
      dataIndex: 'receiver_phone',
      key: 'receiver_phone',
      align: 'center'
    },
    {
      title: '房间名称',
      dataIndex: 'title',
      key: 'title',
      align: 'center',
      customRender: ({text}) => text ? text.substring(0, 10) + '...' : '--'
    },
    {
      title: '订单状态',
      dataIndex: 'status',
      key: 'status',
      align: 'center',
      scopedSlots: {customRender: 'status'}
    },
    {
      title: '订单时间',
      dataIndex: 'order_time',
      key: 'order_time',
      align: 'center',
    },
    {
      title: '操作',
      dataIndex: 'action',
      key: 'operation',
      align: 'center',
      fixed: 'right',
      width: 150,
    },
  ]);

  // 页面数据
  const data = reactive({
    tagList: [],
    loading: false,
    keyword: '',
    selectedRowKeys: [] as any[],
    pageSize: 10,
    page: 1,
  });


  onMounted(() => {
    getDataList();
  });

  // 获取订单数据
  const getDataList = () => {
    data.loading = true;
    listApi({
      keyword: data.keyword,
    })
      .then((res) => {
        data.loading = false;
        console.log(res);
        res.data.forEach((item: any, index: any) => {
          item.index = index + 1;
        });
        data.tagList = res.data;
      })
      .catch((err) => {
        data.loading = false;
        console.log(err);
      });
  };


  const rowSelection = ref({
    onChange: (selectedRowKeys: (string | number)[], selectedRows: DataItem[]) => {
      console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
      data.selectedRowKeys = selectedRowKeys;
    },
  });

  // 完成订单
  const confirmOk = (record: any) => {
    okApi({ id: record.id })
        .then((res) => {
          getDataList();
          message.success('订单完成')
        })
        .catch((err) => {
          message.error(err.msg || '操作失败');
        });
  };

  // 取消订单
  const confirmCancel = (record: any) => {
    cancelApi({ id: record.id })
        .then((res) => {
          getDataList();
          message.success('取消成功')
        })
        .catch((err) => {
          message.error(err.msg || '操作失败');
        });
  };

  // 删除订单
  const confirmDelete = (record: any) => {
    console.log('delete', record);
    deleteApi({ ids: record.id })
      .then((res) => {
        getDataList();
      })
      .catch((err) => {
        message.error(err.msg || '操作失败');
      });
  };

  const handleAdd = () => {
    // createApi({
    //   thingId: 1,
    //   userId: 2,
    //   count: 1
    // }).then(res => {
    //   getDataList()
    // }).catch(err => {
    //
    // })
  }

  const handleBatchDelete = () => {
    console.log(data.selectedRowKeys);
    if (data.selectedRowKeys.length <= 0) {
      console.log('hello');
      message.warn('请勾选删除项');
      return;
    }
    deleteApi({ ids: data.selectedRowKeys.join(',') })
      .then((res) => {
        message.success('删除成功');
        data.selectedRowKeys = [];
        getDataList();
      })
      .catch((err) => {
        message.error(err.msg || '操作失败');
      });
  };

</script>

<style scoped lang="less">
  .page-view {
    min-height: 100%;
    background: #fff;
    padding: 24px;
    display: flex;
    flex-direction: column;
  }

  .table-operations {
    margin-bottom: 16px;
    text-align: right;
  }

  .table-operations > button {
    margin-right: 8px;
  }
</style>
