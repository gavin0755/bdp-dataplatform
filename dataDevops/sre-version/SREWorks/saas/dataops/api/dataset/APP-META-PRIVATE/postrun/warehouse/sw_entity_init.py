# coding: utf-8

import requests
from common.constant import host

headers = {}
# host = {
#     "warehouse": "http://prod-dataops-warehouse.sreworks-dataops.svc.cluster.local:80"
# }

url = host["warehouse"] + "/entity/meta/createEntityWithFields"
sw_schemas = [{
    "metaReq": {
        "description": "团队实体",
        "tableAlias": "ods_team",
        "layer": "ods",
        "tableName": "<ods_team_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "TEAM",
        "alias": "团队",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "avatar",
        "nullable": True,
        "alias": "团队头像",
        "description": "团队头像链接",
        "dim": "avatar",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "团队创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "团队创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "团队最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "团队ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "团队最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "name",
        "nullable": False,
        "alias": "团队名称",
        "description": "团队名称",
        "dim": "name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "visible_scope",
        "nullable": True,
        "alias": "可见范围",
        "description": "团队可见属性",
        "dim": "visible_scope",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "团队成员实体",
        "tableAlias": "ods_team_user",
        "layer": "ods",
        "tableName": "<ods_team_user_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "TEAM_USER",
        "alias": "团队成员",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "用户创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "gmt_access",
        "nullable": True,
        "alias": "访问时间",
        "description": "用户访问时间",
        "dim": "gmt_access",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "用户创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "用户信息的最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "用户ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "is_concern",
        "nullable": True,
        "alias": "是否关注",
        "description": "待补充说明",
        "dim": "is_concern",
        "type": "INTEGER"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "用户信息的最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "role",
        "nullable": False,
        "alias": "角色",
        "description": "用户角色(权限)",
        "dim": "role",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "team_id",
        "nullable": False,
        "alias": "归属团队ID",
        "description": "用户所属的团队ID",
        "dim": "team_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "user",
        "nullable": False,
        "alias": "用户名称",
        "description": "用户名称",
        "dim": "user",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "团队云账户实体",
        "tableAlias": "ods_team_account",
        "layer": "ods",
        "tableName": "<ods_team_account_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "TEAM_ACCOUNT",
        "alias": "团队云账户",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "账户创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "detail",
        "nullable": True,
        "alias": "账户详情",
        "description": "账户详情信息",
        "dim": "detail",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "账户创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "账户最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "账户ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "账户最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "name",
        "nullable": False,
        "alias": "账户名称",
        "description": "账户名称",
        "dim": "name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "team_id",
        "nullable": False,
        "alias": "归属团队ID",
        "description": "账户所属的团队ID",
        "dim": "team_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "type",
        "nullable": False,
        "alias": "账户类型",
        "description": "账户类型",
        "dim": "type",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "团队托管仓库实体",
        "tableAlias": "ods_team_repo",
        "layer": "ods",
        "tableName": "<ods_team_repo_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "TEAM_REPO",
        "alias": "团队托管仓库",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "ci_account",
        "nullable": True,
        "alias": "仓库账户",
        "description": "仓库账户",
        "dim": "ci_account",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "ci_token",
        "nullable": True,
        "alias": "仓库令牌",
        "description": "仓库令牌",
        "dim": "ci_token",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "账户创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "账户创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "账户最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "仓库ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "账户最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "name",
        "nullable": False,
        "alias": "仓库名称",
        "description": "仓库名称",
        "dim": "name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "team_id",
        "nullable": False,
        "alias": "归属团队ID",
        "description": "仓库所属的团队ID",
        "dim": "team_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "url",
        "nullable": False,
        "alias": "仓库链接",
        "description": "仓库链接",
        "dim": "url",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "团队注册信息实体",
        "tableAlias": "ods_team_registry",
        "layer": "ods",
        "tableName": "<ods_team_registry_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "TEAM_REGISTRY",
        "alias": "团队注册信息",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "auth",
        "nullable": True,
        "alias": "认证信息",
        "description": "认证信息",
        "dim": "auth",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "注册ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "name",
        "nullable": False,
        "alias": "注册名称",
        "description": "注册名称",
        "dim": "name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "team_id",
        "nullable": False,
        "alias": "归属团队ID",
        "description": "所属的团队ID",
        "dim": "team_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "url",
        "nullable": False,
        "alias": "注册链接",
        "description": "注册链接",
        "dim": "url",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "集群实体",
        "tableAlias": "ods_cluster",
        "layer": "ods",
        "tableName": "<ods_cluster_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "CLUSTER",
        "alias": "集群",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "account_id",
        "nullable": False,
        "alias": "关联账户",
        "description": "集群关联账户",
        "dim": "account_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "cluster_name",
        "nullable": False,
        "alias": "集群code",
        "description": "集群code",
        "dim": "cluster_name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "集群创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "集群创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "集群最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "集群ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "kubeconfig",
        "nullable": True,
        "alias": "kube配置",
        "description": "集群kube配置",
        "dim": "kubeconfig",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "集群最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "name",
        "nullable": False,
        "alias": "集群名称",
        "description": "集群名称",
        "dim": "name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "team_id",
        "nullable": False,
        "alias": "归属团队ID",
        "description": "集群所属的团队ID",
        "dim": "team_id",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "应用实体",
        "tableAlias": "ods_app",
        "layer": "ods",
        "tableName": "<ods_app_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "APP",
        "alias": "应用",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "annotations",
        "nullable": True,
        "alias": "应用注解",
        "description": "应用注解",
        "dim": "annotations",
        "type": "OBJECT"
    }, {
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "集群创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "detail",
        "nullable": True,
        "alias": "应用详情",
        "description": "应用详情",
        "dim": "detail",
        "type": "OBJECT"
    }, {
        "buildIn": True,
        "field": "display",
        "nullable": True,
        "alias": "显示",
        "description": "显示",
        "dim": "display",
        "type": "INTEGER"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "应用创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "应用最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "应用ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "labels",
        "nullable": True,
        "alias": "应用标签",
        "description": "应用标签",
        "dim": "labels",
        "type": "OBJECT"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "应用最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "name",
        "nullable": False,
        "alias": "应用名称",
        "description": "应用名称",
        "dim": "name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "team_id",
        "nullable": False,
        "alias": "归属团队ID",
        "description": "应用所属的团队ID",
        "dim": "team_id",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "应用组件实体",
        "tableAlias": "ods_app_component",
        "layer": "ods",
        "tableName": "<ods_app_component_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "APP_COMPONENT",
        "alias": "应用组件",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "app_id",
        "nullable": False,
        "alias": "归属应用ID",
        "description": "组件所属的应用ID",
        "dim": "app_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "组件创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "detail",
        "nullable": True,
        "alias": "组件详情",
        "description": "组件详情",
        "dim": "detail",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "ex_id",
        "nullable": True,
        "alias": "扩展ID",
        "description": "扩展ID",
        "dim": "ex_id",
        "type": "LONG"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "组件创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "组件最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "组件ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "组件最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "name",
        "nullable": False,
        "alias": "组件名称",
        "description": "组件名称",
        "dim": "name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "type",
        "nullable": False,
        "alias": "组件类型",
        "description": "组件类型",
        "dim": "type",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "type_detail",
        "nullable": True,
        "alias": "组件类型详情",
        "description": "组件类型详情",
        "dim": "type_detail",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "指标定义实体",
        "tableAlias": "ods_metric",
        "layer": "ods",
        "tableName": "<ods_metric_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "METRIC",
        "alias": "指标定义",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "app_id",
        "nullable": False,
        "alias": "归属应用ID",
        "description": "指标所属的应用ID",
        "dim": "app_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "build_in",
        "nullable": True,
        "alias": "内置指标",
        "description": "内置指标",
        "dim": "build_in",
        "type": "BOOLEAN"
    }, {
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "指标创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "entity",
        "nullable": False,
        "alias": "归属实体",
        "description": "指标归属实体",
        "dim": "entity",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "指标创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "指标最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "指标ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "index_path",
        "nullable": False,
        "alias": "指标值索引",
        "description": "指标值索引路径(ES)",
        "dim": "index_path",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "指标最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "name",
        "nullable": False,
        "alias": "指标名称",
        "description": "指标名称",
        "dim": "name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "table",
        "nullable": False,
        "alias": "存储表名",
        "description": "存储索引(ES)",
        "dim": "table",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "tags",
        "nullable": True,
        "alias": "指标标签",
        "description": "指标标签",
        "dim": "tags",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "type",
        "nullable": False,
        "alias": "指标类型",
        "description": "指标类型",
        "dim": "type",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "事件定义实体",
        "tableAlias": "ods_event",
        "layer": "ods",
        "tableName": "<ods_event_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "EVENT",
        "alias": "事件定义",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "app_id",
        "nullable": False,
        "alias": "归属应用ID",
        "description": "事件所属的应用ID",
        "dim": "app_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "category",
        "nullable": False,
        "alias": "类型标识",
        "description": "类型标识",
        "dim": "category",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "creator",
        "nullable": True,
        "alias": "创建人",
        "description": "事件创建人",
        "dim": "creator",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "entity",
        "nullable": False,
        "alias": "归属实体",
        "description": "事件归属实体",
        "dim": "entity",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "ex_config",
        "nullable": True,
        "alias": "扩展配置",
        "description": "扩展配置",
        "dim": "ex_config",
        "type": "OBJECT"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "事件创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "事件最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "事件ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "last_modifier",
        "nullable": True,
        "alias": "最近修改人",
        "description": "事件最近修改人",
        "dim": "last_modifier",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "name",
        "nullable": False,
        "alias": "事件名称",
        "description": "事件名称",
        "dim": "name",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "事件实例实体",
        "tableAlias": "ods_event_instance",
        "layer": "ods",
        "tableName": "<ods_event_instance_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "EVENT_INSTANCE",
        "alias": "事件实例",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "content",
        "nullable": True,
        "alias": "详情",
        "description": "详情",
        "dim": "content",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "def_id",
        "nullable": False,
        "alias": "关联定义ID",
        "description": "事件实例所属的定义ID",
        "dim": "def_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "description",
        "nullable": True,
        "alias": "说明",
        "description": "备注说明信息",
        "dim": "description",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "entity_value",
        "nullable": False,
        "alias": "实体值",
        "description": "实体值",
        "dim": "entity_value",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "gmt_create",
        "nullable": True,
        "alias": "创建时间",
        "description": "事件实例创建时间",
        "dim": "gmt_create",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_modified",
        "nullable": True,
        "alias": "修改时间",
        "description": "事件实例最近修改时间",
        "dim": "gmt_modified",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "gmt_occur",
        "nullable": True,
        "alias": "发生时间",
        "description": "事件实例发生时间",
        "dim": "gmt_occur",
        "type": "DATE"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "事件实例ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "source",
        "nullable": True,
        "alias": "事件来源",
        "description": "事件来源",
        "dim": "source",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "主机/节点/机器实体",
        "tableAlias": "ods_node",
        "layer": "ods",
        "tableName": "<ods_node_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "NODE",
        "alias": "节点",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "节点ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "作业实体",
        "tableAlias": "ods_job",
        "layer": "ods",
        "tableName": "<ods_job_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "JOB",
        "alias": "作业",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "作业ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "队列实体",
        "tableAlias": "ods_queue",
        "layer": "ods",
        "tableName": "<ods_queue_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "QUEUE",
        "alias": "队列",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "队列ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "命名空间实体",
        "tableAlias": "ods_namespace",
        "layer": "ods",
        "tableName": "<ods_namespace_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "NAMESPACE",
        "alias": "命名空间",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "命名空间ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "云服务实体",
        "tableAlias": "ods_cloud_service",
        "layer": "ods",
        "tableName": "<ods_cloud_service_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "CLOUD_SERVICE",
        "alias": "云服务",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "云服务ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "云资源实体",
        "tableAlias": "ods_cloud_resource",
        "layer": "ods",
        "tableName": "<ods_cloud_resource_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "CLOUD_RESOURCE",
        "alias": "云资源",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "云资源ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "厂商实体",
        "tableAlias": "ods_vendor",
        "layer": "ods",
        "tableName": "<ods_vendor_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "VENDOR",
        "alias": "厂商",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "厂商ID",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }]
}, {
    "metaReq": {
        "description": "POD资源实体",
        "tableAlias": "ods_pod",
        "layer": "ods",
        "tableName": "<ods_pod_{now/d}>",
        "buildIn": True,
        "lifecycle": 7,
        "name": "POD",
        "alias": "POD",
        "partitionFormat": "d"
    },
    "fieldsReq": [{
        "buildIn": True,
        "field": "app_id",
        "nullable": False,
        "alias": "所属应用ID",
        "description": "归属应用ID",
        "dim": "app_id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "app_name",
        "nullable": False,
        "alias": "所属应用名称",
        "description": "归属应用名称",
        "dim": "app_name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "id",
        "nullable": False,
        "alias": "唯一标识",
        "description": "主键",
        "dim": "id",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "namespace",
        "nullable": False,
        "alias": "命名空间",
        "description": "命名空间",
        "dim": "namespace",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "pod_name",
        "nullable": False,
        "alias": "POD名称",
        "description": "POD名称",
        "dim": "pod_name",
        "type": "STRING"
    }, {
        "buildIn": True,
        "field": "timestamp",
        "nullable": False,
        "alias": "入库时间戳",
        "description": "入库时间戳",
        "dim": "timestamp",
        "type": "STRING"
    }]
}]


def add_sw_entities():
    for sw_schema in sw_schemas:
        r = requests.post(url, headers=headers, json=sw_schema)
        if r.status_code == 200:
            print(r.json())