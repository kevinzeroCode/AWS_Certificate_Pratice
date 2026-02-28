CLF_BATCH6 = [
  {
    "id": 146, "exam": "CLF",
    "question": "Why is AWS more economical than traditional data centers for applications with varying compute workloads?",
    "question_zh": "對於運算工作負載不固定的應用程式，AWS 為何比傳統資料中心更經濟實惠？",
    "options": {
      "A": {"en": "Customers retain full administrative access to their Amazon EC2 instances.", "zh": "客戶保留對其 Amazon EC2 執行個體的完整管理員存取權限"},
      "B": {"en": "Customers can permanently run enough instances to handle peak workloads.", "zh": "客戶可以永久運行足夠的執行個體來處理峰值工作負載"},
      "C": {"en": "Amazon EC2 costs are billed on a monthly basis.", "zh": "Amazon EC2 費用按月計費"},
      "D": {"en": "Amazon EC2 instances can be launched on-demand when needed.", "zh": "Amazon EC2 執行個體可以在需要時隨需啟動"}
    },
    "correct": ["D"], "multi": False,
    "explanations": {
      "A": "✗ 管理員存取權限與成本經濟性無關，本地資料中心也有完整管理員存取權限。",
      "B": "✗ 這正是傳統資料中心的做法（為峰值預購），也是造成浪費的原因。AWS 的優勢在於不需要這樣做。",
      "C": "✗ 按月計費並非 AWS 的獨有特性，也不是 AWS 比傳統資料中心更經濟的主因。",
      "D": "✓ 正確 — 工作負載變動時，可隨需啟動/關閉 EC2 執行個體，只為實際使用量付費，不必為閒置容量付費，這就是雲端彈性帶來的經濟優勢。"
    }
  },
  {
    "id": 147, "exam": "CLF",
    "question": "What is included in an Amazon Machine Image (AMI)? (Select the best answer)",
    "question_zh": "Amazon Machine Image（AMI）包含哪些內容？",
    "options": {
      "A": {"en": "A template for the root volume for the instance", "zh": "執行個體根磁碟區的模板"},
      "B": {"en": "Launch permissions that control which AWS accounts can use the AMI to launch instances", "zh": "控制哪些 AWS 帳戶可使用 AMI 啟動執行個體的啟動許可"},
      "C": {"en": "A block device mapping that specifies the volumes to attach to the instance when it's launched", "zh": "指定執行個體啟動時要附加的磁碟區的區塊設備映射"},
      "D": {"en": "All of the above", "zh": "以上皆是"}
    },
    "correct": ["D"], "multi": False,
    "explanations": {
      "A": "✓ AMI 包含根磁碟區模板（作業系統、應用程式、設定等），但這只是 AMI 的一部分。",
      "B": "✓ AMI 包含啟動許可，控制哪些 AWS 帳戶可以使用該 AMI，但這只是 AMI 的一部分。",
      "C": "✓ AMI 包含區塊設備映射，指定啟動時要附加哪些 EBS 磁碟區，但這只是 AMI 的一部分。",
      "D": "✓ 正確 — AMI 包含三個主要組成：(1) 根磁碟區模板、(2) 啟動許可、(3) 區塊設備映射，三者都是 AMI 的組成部分。"
    }
  },
  {
    "id": 148, "exam": "CLF",
    "question": "Which Amazon EC2 feature ensures your instances will not share a physical host with instances from any other AWS customer?",
    "question_zh": "哪個 Amazon EC2 功能可確保您的執行個體不與任何其他 AWS 客戶的執行個體共用實體主機？",
    "options": {
      "A": {"en": "Amazon VPC", "zh": "Amazon VPC"},
      "B": {"en": "Reserved Instances", "zh": "預留執行個體"},
      "C": {"en": "Dedicated Instances", "zh": "專用執行個體"},
      "D": {"en": "Placement groups", "zh": "置放群組"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ Amazon VPC 是虛擬私有雲端網路隔離服務，不控制實體主機隔離。",
      "B": "✗ Reserved Instances 是定價模型（承諾使用換折扣），不保證實體主機隔離。",
      "C": "✓ 正確 — Dedicated Instances（專用執行個體）在專屬於單一 AWS 帳戶的硬體上執行，不與其他 AWS 客戶共用實體主機，滿足合規隔離需求。",
      "D": "✗ Placement groups 控制執行個體的實體分佈（如低延遲叢集），但不防止與其他客戶共用主機。"
    }
  },
  {
    "id": 149, "exam": "CLF",
    "question": "Your web application needs four instances to support steady traffic all of the time. On the last day of the month, the traffic triples. What is the most cost-effective way to handle this pattern?",
    "question_zh": "您的 Web 應用程式始終需要四個執行個體來支援穩定流量。在月底最後一天，流量增加三倍。處理這種模式最具成本效益的方式是什麼？",
    "options": {
      "A": {"en": "Run 12 Reserved Instances all of the time.", "zh": "全程運行 12 個預留執行個體"},
      "B": {"en": "Run four On-Demand Instances constantly, then add eight more On-Demand Instances on the last day of each month.", "zh": "持續運行四個按需執行個體，在每月最後一天再增加八個按需執行個體"},
      "C": {"en": "Run four Reserved Instances constantly, then add eight On-Demand Instances on the last day of each month.", "zh": "持續運行四個預留執行個體，在每月最後一天增加八個按需執行個體"},
      "D": {"en": "Run four On-Demand Instances constantly, then add eight Reserved Instances on the last day of each month.", "zh": "持續運行四個按需執行個體，在每月最後一天增加八個預留執行個體"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ 全程運行 12 個預留執行個體，在非峰值時段有 8 個執行個體閒置，成本浪費。",
      "B": "✗ 四個常駐按需執行個體比預留執行個體貴；且偶爾峰值使用按需是合理的，但基準負載應用預留。",
      "C": "✓ 正確 — 四個常駐執行個體使用預留執行個體（最低成本處理穩定基準負載），峰值時的額外八個使用按需執行個體（只在需要時付費），是最佳成本組合。",
      "D": "✗ 預留執行個體要求長期承諾（1 或 3 年），不適合只在月底一天使用的峰值容量。"
    }
  },
  {
    "id": 150, "exam": "CLF",
    "question": "Containers contain an entire operating system. (True or False?)",
    "question_zh": "容器包含完整的作業系統。（對或錯？）",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["B"], "multi": False,
    "explanations": {
      "A": "✗ 虛擬機器（VM）才包含完整的作業系統；容器不包含完整 OS。",
      "B": "✓ 正確（False）— 容器只包含應用程式及其依賴項（函式庫、工具等），共享宿主機的作業系統核心，而非包含完整 OS。這使容器比虛擬機器更輕量、啟動更快。"
    }
  },
  {
    "id": 151, "exam": "CLF",
    "question": "Which Amazon EC2 option is best for long-term workloads with predictable usage patterns?",
    "question_zh": "哪個 Amazon EC2 選項最適合使用模式可預測的長期工作負載？",
    "options": {
      "A": {"en": "Reserved Instances", "zh": "預留執行個體"},
      "B": {"en": "Spot Instances", "zh": "競價執行個體"},
      "C": {"en": "On-Demand Instances", "zh": "按需執行個體"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確 — Reserved Instances（預留執行個體）適合長期（1 或 3 年）、使用模式穩定可預測的工作負載，相比按需定價可節省高達 75%。",
      "B": "✗ Spot Instances 適合容錯性高、可中斷的工作負載（如批次處理），不適合需要持續運行的長期工作負載。",
      "C": "✗ On-Demand 適合短期、不規則或難以預測的工作負載，對長期穩定負載而言成本較高。"
    }
  },
  {
    "id": 152, "exam": "CLF",
    "question": "Which of the following must be specified when launching a new Amazon EC2 Windows instance? (Choose two)",
    "question_zh": "啟動新的 Amazon EC2 Windows 執行個體時，必須指定下列哪些項目？（選擇兩個）",
    "options": {
      "A": {"en": "Amazon EC2 instance type", "zh": "Amazon EC2 執行個體類型"},
      "B": {"en": "Password for the administrator account", "zh": "管理員帳戶的密碼"},
      "C": {"en": "Amazon Machine Image (AMI)", "zh": "Amazon Machine Image（AMI）"},
      "D": {"en": "The Amazon EC2 instance ID", "zh": "Amazon EC2 執行個體 ID"}
    },
    "correct": ["A", "C"], "multi": True,
    "explanations": {
      "A": "✓ 正確 — 必須指定執行個體類型（如 t3.micro、m5.large），決定 CPU、記憶體和網路效能。",
      "B": "✗ AWS 不允許使用者在啟動時設定管理員密碼；Windows 的初始管理員密碼是自動生成並加密的，透過金鑰對解密取得。",
      "C": "✓ 正確 — 必須指定 AMI，它定義了執行個體的作業系統、軟體和初始配置。",
      "D": "✗ 執行個體 ID 是 AWS 在執行個體啟動後自動指派的，不是啟動時需要指定的。"
    }
  },
  {
    "id": 153, "exam": "CLF",
    "question": "True or False? Amazon Simple Storage Service (Amazon S3) is an object storage suitable for the storage of flat files like Microsoft Word documents, photos, etc.",
    "question_zh": "對或錯？Amazon Simple Storage Service（Amazon S3）是物件儲存，適合儲存 Microsoft Word 文件、照片等平面文件。",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確（True）— Amazon S3 是物件儲存服務，非常適合儲存非結構化的平面文件，如文件、圖片、影片、備份等。每個物件可以透過 URL 存取，且具備高耐久性（11 個 9）。",
      "B": "✗ 此陳述是正確的，S3 確實適合儲存平面文件，所以答案是「真」。"
    }
  },
  {
    "id": 154, "exam": "CLF",
    "question": "Amazon S3 replicates all objects ___. (Select the best answer)",
    "question_zh": "Amazon S3 將所有物件複製到___。",
    "options": {
      "A": {"en": "on multiple volumes within an Availability Zone", "zh": "可用區域內的多個磁碟區上"},
      "B": {"en": "in multiple Availability Zones within the same Region", "zh": "同一區域內的多個可用區域"},
      "C": {"en": "across multiple Regions for higher durability", "zh": "跨多個區域以提高耐久性"},
      "D": {"en": "on multiple S3 buckets", "zh": "多個 S3 儲存貯體上"}
    },
    "correct": ["B"], "multi": False,
    "explanations": {
      "A": "✗ S3 的複製不限於單一可用區域內，覆蓋範圍更廣。",
      "B": "✓ 正確 — Amazon S3 預設將物件複製到同一 AWS 區域內的多個可用區域，這提供了 99.999999999%（11 個 9）的物件耐久性。",
      "C": "✗ 跨區域複製是可選功能（S3 Cross-Region Replication），不是預設行為。",
      "D": "✗ S3 在可用區層級複製，不是在儲存貯體層級。"
    }
  },
  {
    "id": 155, "exam": "CLF",
    "question": "The name of an S3 bucket must be unique ___. (Select the best answer)",
    "question_zh": "S3 儲存貯體的名稱必須在___中是唯一的。",
    "options": {
      "A": {"en": "worldwide across all AWS accounts", "zh": "全球所有 AWS 帳戶中"},
      "B": {"en": "within a Region", "zh": "在一個區域內"},
      "C": {"en": "across all your AWS accounts", "zh": "在您所有 AWS 帳戶中"},
      "D": {"en": "within your AWS account", "zh": "在您的 AWS 帳戶內"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確 — S3 儲存貯體名稱必須在全球所有 AWS 帳戶中唯一，因為它形成 URL 的一部分（如 https://bucket-name.s3.amazonaws.com），全球 URL 不能重複。",
      "B": "✗ 唯一性要求比單一區域更廣；即使在不同區域，也不能有同名的 S3 儲存貯體（全球唯一）。",
      "C": "✗ 不僅僅是您的帳戶，是所有 AWS 帳戶的所有儲存貯體名稱都不能重複。",
      "D": "✗ 帳戶級別的唯一性不夠；S3 要求全球唯一。"
    }
  },
  {
    "id": 156, "exam": "CLF",
    "question": "True or False? By default, all data stored in Amazon S3 is viewable by the public.",
    "question_zh": "對或錯？預設情況下，儲存在 Amazon S3 中的所有資料都可以被公眾查看。",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["B"], "multi": False,
    "explanations": {
      "A": "✗ 此陳述不正確；S3 的預設設定是私有的，不是公開的。",
      "B": "✓ 正確（False）— 預設情況下，Amazon S3 中的所有物件和儲存貯體都是私有的，只有物件擁有者或明確授權的使用者才能存取。公開存取需要明確設定（儲存貯體策略或 ACL），且 AWS 現在預設啟用「封鎖所有公開存取」設定。"
    }
  },
  {
    "id": 157, "exam": "CLF",
    "question": "True or False? When you create a bucket in Amazon S3, it is associated with a specific AWS Region.",
    "question_zh": "對或錯？當您在 Amazon S3 中建立儲存貯體時，它與特定 AWS 區域相關聯。",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確（True）— 建立 S3 儲存貯體時必須選擇 AWS 區域，物件儲存在該區域的資料中心。這有助於滿足資料駐留合規要求和降低延遲。跨區域複製需要額外配置。",
      "B": "✗ 此陳述是正確的；S3 儲存貯體確實與特定區域綁定。"
    }
  },
  {
    "id": 158, "exam": "CLF",
    "question": "You are designing an ecommerce web application that will scale to hundreds of thousands of concurrent users. Which database technology is best suited to hold the session state?",
    "question_zh": "您正在設計一個將擴展到數十萬個並發使用者的電商 Web 應用程式。哪種資料庫技術最適合保存 Session 狀態？",
    "options": {
      "A": {"en": "Amazon Relational Database Service (Amazon RDS)", "zh": "Amazon Relational Database Service（Amazon RDS）"},
      "B": {"en": "Amazon DynamoDB", "zh": "Amazon DynamoDB"},
      "C": {"en": "Amazon Redshift", "zh": "Amazon Redshift"},
      "D": {"en": "Amazon Simple Storage Service (Amazon S3)", "zh": "Amazon Simple Storage Service（Amazon S3）"}
    },
    "correct": ["B"], "multi": False,
    "explanations": {
      "A": "✗ RDS 是關聯式資料庫，對高並發 Session 讀寫的擴展性不如 DynamoDB，且成本較高。",
      "B": "✓ 正確 — Amazon DynamoDB 是完全托管的 NoSQL 資料庫，具有個位數毫秒延遲、幾乎無限擴展能力，非常適合高並發應用的 Session 狀態儲存。",
      "C": "✗ Amazon Redshift 是資料倉儲，用於大規模分析查詢，不適合高並發的 Session 讀寫。",
      "D": "✗ S3 是物件儲存，延遲較高且不支援快速的鍵值查詢，不適合 Session 狀態。"
    }
  },
  {
    "id": 159, "exam": "CLF",
    "question": "In Amazon DynamoDB, what does the query operation enable you to do? (Select the best answer.)",
    "question_zh": "在 Amazon DynamoDB 中，查詢（Query）操作讓您能做什麼？",
    "options": {
      "A": {"en": "Query a table using the partition key and an optional sort key filter", "zh": "使用分區鍵和可選的排序鍵篩選器查詢資料表"},
      "B": {"en": "Query any secondary indexes that exist for a table", "zh": "查詢資料表存在的任何次要索引"},
      "C": {"en": "Efficiently retrieve items from a table or secondary index", "zh": "從資料表或次要索引有效率地擷取項目"},
      "D": {"en": "All of the above", "zh": "以上皆是"}
    },
    "correct": ["D"], "multi": False,
    "explanations": {
      "A": "✓ Query 操作使用分區鍵（必要）和排序鍵（可選）來查詢，但這只是它能做的事之一。",
      "B": "✓ Query 也可以查詢次要索引（Global Secondary Index / Local Secondary Index），但這只是它能做的事之一。",
      "C": "✓ Query 是從資料表或索引有效率地擷取項目的主要操作，但這只是它能做的事之一。",
      "D": "✓ 正確 — DynamoDB Query 操作包含以上所有功能：使用分區鍵和排序鍵查詢、查詢次要索引、有效率地擷取項目。"
    }
  },
  {
    "id": 160, "exam": "CLF",
    "question": "Which AWS Cloud service is best suited for analyzing your data by using standard structured query language (SQL) and your existing business intelligence (BI) tools?",
    "question_zh": "哪個 AWS 雲端服務最適合使用標準結構化查詢語言（SQL）和現有商業智慧（BI）工具分析資料？",
    "options": {
      "A": {"en": "Amazon Relational Database Service (Amazon RDS)", "zh": "Amazon Relational Database Service（Amazon RDS）"},
      "B": {"en": "Amazon Simple Storage Service Glacier", "zh": "Amazon Simple Storage Service Glacier"},
      "C": {"en": "Amazon DynamoDB", "zh": "Amazon DynamoDB"},
      "D": {"en": "Amazon Redshift", "zh": "Amazon Redshift"}
    },
    "correct": ["D"], "multi": False,
    "explanations": {
      "A": "✗ RDS 適合 OLTP（線上交易處理），不是大規模資料分析的最佳選擇。",
      "B": "✗ S3 Glacier 是封存儲存服務，不用於 SQL 查詢或資料分析。",
      "C": "✗ DynamoDB 是 NoSQL 資料庫，雖可查詢，但不是標準 SQL 或 BI 工具整合的主要選擇。",
      "D": "✓ 正確 — Amazon Redshift 是雲端資料倉儲，專為 OLAP（線上分析處理）設計，支援標準 SQL，並可與 Tableau、Power BI 等主流 BI 工具整合，適合 PB 級資料分析。"
    }
  },
  {
    "id": 161, "exam": "CLF",
    "question": "If you are developing an application that requires a database with extremely fast performance, fast scalability, and flexibility in the database schema, which service should you consider?",
    "question_zh": "如果您正在開發需要極快效能、快速擴展性和資料庫綱要靈活性的資料庫應用程式，應考慮哪個服務？",
    "options": {
      "A": {"en": "Amazon Relational Database Service (Amazon RDS)", "zh": "Amazon Relational Database Service（Amazon RDS）"},
      "B": {"en": "Amazon ElastiCache", "zh": "Amazon ElastiCache"},
      "C": {"en": "Amazon DynamoDB", "zh": "Amazon DynamoDB"},
      "D": {"en": "Amazon Redshift", "zh": "Amazon Redshift"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ RDS 是關聯式資料庫，有固定綱要，擴展性和靈活性不如 NoSQL 資料庫。",
      "B": "✗ ElastiCache 是記憶體快取服務（Redis/Memcached），適合快取場景，不是主要資料庫解決方案。",
      "C": "✓ 正確 — Amazon DynamoDB 是 NoSQL 資料庫，提供：(1) 個位數毫秒的極快回應、(2) 幾乎無限的自動擴展、(3) 無固定綱要的靈活資料模型，完全符合需求。",
      "D": "✗ Redshift 是資料倉儲，適合分析查詢，不是 OLTP 或需要極低延遲的應用場景。"
    }
  },
  {
    "id": 162, "exam": "CLF",
    "question": "Which of the following use cases is appropriate for using Amazon Relational Database Service (Amazon RDS)?",
    "question_zh": "下列哪個使用案例適合使用 Amazon Relational Database Service（Amazon RDS）？",
    "options": {
      "A": {"en": "Massive read/write rates", "zh": "大量讀寫速率"},
      "B": {"en": "Simple GET or PUT requests", "zh": "簡單的 GET 或 PUT 請求"},
      "C": {"en": "Complex transactions", "zh": "複雜交易"},
      "D": {"en": "All of the above", "zh": "以上皆是"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ 大量讀寫速率更適合 DynamoDB（NoSQL）或 ElastiCache，RDS 在超高並發讀寫下可能成為瓶頸。",
      "B": "✗ 簡單的 GET/PUT 請求更適合 DynamoDB 或 S3，不需要 RDS 的完整 SQL 功能。",
      "C": "✓ 正確 — Amazon RDS 最適合需要 ACID 合規的複雜交易（如金融交易、訂單處理），支援 JOIN、外鍵、儲存程序等關聯式資料庫功能。",
      "D": "✗ 並非所有選項都適合 RDS；特別是大量讀寫和簡單 GET/PUT 有更適合的 AWS 服務。"
    }
  },
  {
    "id": 163, "exam": "CLF",
    "question": "A company has an application which consists of a .NET layer that connects to a MySQL database. They want to move this application to AWS and use AWS features such as high availability and automated backups. Which would be an ideal database?",
    "question_zh": "一家公司的應用程式由連接到 MySQL 資料庫的 .NET 層組成。他們想將此應用程式移至 AWS，並使用高可用性和自動備份等 AWS 功能。哪個資料庫最理想？",
    "options": {
      "A": {"en": "Amazon RDS (MySQL engine)", "zh": "Amazon RDS（MySQL 引擎）"},
      "B": {"en": "Amazon Redshift", "zh": "Amazon Redshift"},
      "C": {"en": "Amazon DynamoDB", "zh": "Amazon DynamoDB"},
      "D": {"en": "Amazon Aurora", "zh": "Amazon Aurora"}
    },
    "correct": ["D"], "multi": False,
    "explanations": {
      "A": "✗ RDS MySQL 可行，但 Aurora 是 MySQL 相容的，且效能更好（最多 5 倍於標準 MySQL），並有更完善的高可用性功能。",
      "B": "✗ Redshift 是資料倉儲，不適合 OLTP 應用（如 .NET 應用的交易型資料庫）。",
      "C": "✗ DynamoDB 是 NoSQL，現有的 MySQL 應用程式不能直接遷移，需要大幅重寫程式碼。",
      "D": "✓ 正確 — Amazon Aurora 與 MySQL 完全相容（可直接遷移），同時提供：自動多 AZ 複製、自動備份、故障轉移、比標準 MySQL 更高的效能，是此使用案例的最佳選擇。"
    }
  },
  {
    "id": 164, "exam": "CLF",
    "question": "True or false? Amazon RDS automatically patches the database software and backs up your database, storing the backups for a user-defined retention period and enabling point-in-time recovery.",
    "question_zh": "對或錯？Amazon RDS 自動修補資料庫軟體並備份您的資料庫，按使用者定義的保留期間儲存備份，並啟用時間點恢復。",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確（True）— Amazon RDS 提供完整的托管功能，包括：自動軟體修補（在維護視窗期間）、自動每日備份、可設定的備份保留期間（1-35 天），以及時間點恢復功能，讓您可以將資料庫還原到保留期間內的任何時間點。",
      "B": "✗ 此陳述是正確的，所以答案是「真」。"
    }
  },
  {
    "id": 165, "exam": "CLF",
    "question": "What should you consider when choosing a database type? (Select the best answer.)",
    "question_zh": "選擇資料庫類型時應考慮什麼？",
    "options": {
      "A": {"en": "Data size", "zh": "資料大小"},
      "B": {"en": "Data access period", "zh": "資料存取頻率"},
      "C": {"en": "Query frequency", "zh": "查詢頻率"},
      "D": {"en": "High availability requirements", "zh": "高可用性需求"},
      "E": {"en": "All of the above", "zh": "以上皆是"}
    },
    "correct": ["E"], "multi": False,
    "explanations": {
      "A": "✓ 資料大小影響資料庫選擇（如小型使用 RDS，PB 級分析使用 Redshift），但不是唯一因素。",
      "B": "✓ 資料存取頻率影響選擇（熱資料用 DynamoDB，冷資料用 Glacier），但不是唯一因素。",
      "C": "✓ 查詢頻率和複雜度影響選擇（複雜 SQL 用 RDS，簡單 K-V 用 DynamoDB），但不是唯一因素。",
      "D": "✓ 高可用性需求影響資料庫選擇和配置（Multi-AZ 部署等），但不是唯一因素。",
      "E": "✓ 正確 — 選擇資料庫類型時，必須綜合考慮所有因素：資料大小、存取模式、查詢複雜度、可用性需求等，才能做出最合適的選擇。"
    }
  },
  {
    "id": 166, "exam": "CLF",
    "question": "Which of the following is NOT one of the four areas of the Performance Efficiency pillar of the AWS Well-Architected Framework?",
    "question_zh": "下列哪項不是 AWS Well-Architected Framework 效能效率支柱的四個領域之一？",
    "options": {
      "A": {"en": "Tradeoffs", "zh": "權衡取捨"},
      "B": {"en": "Selection", "zh": "選擇"},
      "C": {"en": "Traceability", "zh": "可追蹤性"},
      "D": {"en": "Monitoring", "zh": "監控"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ Tradeoffs（權衡取捨）是效能效率支柱的四個領域之一，涉及在效能與成本/一致性之間做出取捨。",
      "B": "✗ Selection（選擇）是效能效率支柱的四個領域之一，涉及選擇正確的資源類型和大小。",
      "C": "✓ 正確（非效能效率領域）— Traceability（可追蹤性）屬於「安全性」支柱，而非效能效率支柱。效能效率的四個領域是：Selection（選擇）、Review（檢視）、Monitoring（監控）、Tradeoffs（權衡）。",
      "D": "✗ Monitoring（監控）是效能效率支柱的四個領域之一，涉及監控效能以識別降級情況。"
    }
  },
  {
    "id": 167, "exam": "CLF",
    "question": "Which of the following is a principle when designing cloud-based systems?",
    "question_zh": "下列哪項是設計雲端系統時的原則？",
    "options": {
      "A": {"en": "Build tightly-coupled components", "zh": "建立緊密耦合的元件"},
      "B": {"en": "Make infrequent, large batch changes", "zh": "進行不頻繁的大批次更改"},
      "C": {"en": "Assume everything will fail", "zh": "假設所有事物都會失敗"},
      "D": {"en": "Use as many services as possible", "zh": "盡可能使用最多的服務"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ 雲端設計原則提倡「鬆散耦合」（loose coupling），不是緊密耦合；鬆散耦合讓各元件可獨立擴展和失敗。",
      "B": "✗ AWS 建議頻繁、小批次地部署更改（CI/CD 方法），降低每次變更的風險，而非大批次不頻繁更改。",
      "C": "✓ 正確 — 「假設一切都會失敗」是 AWS Well-Architected 的核心設計原則。設計系統時應假設任何元件（伺服器、網路、資料庫）都可能失敗，並設計相應的容錯機制。",
      "D": "✗ 使用「最少必要」的服務（而非最多），避免不必要的複雜性，是更好的設計原則。"
    }
  },
  {
    "id": 168, "exam": "CLF",
    "question": "Which of the following are pillars of the AWS Well-Architected Framework? (Choose three.)",
    "question_zh": "下列哪些是 AWS Well-Architected Framework 的支柱？（選擇三個）",
    "options": {
      "A": {"en": "Security", "zh": "安全性"},
      "B": {"en": "Persistence", "zh": "持久性"},
      "C": {"en": "Operational Excellence", "zh": "卓越操作"},
      "D": {"en": "Cost Optimization", "zh": "成本優化"}
    },
    "correct": ["A", "C", "D"], "multi": True,
    "explanations": {
      "A": "✓ 正確 — 安全性（Security）是 AWS Well-Architected Framework 的六個支柱之一，涵蓋身份驗證、授權、資料保護等。",
      "B": "✗ 「持久性（Persistence）」不是 Well-Architected Framework 的支柱名稱。六個支柱是：卓越操作、安全性、可靠性、效能效率、成本優化、永續性。",
      "C": "✓ 正確 — 卓越操作（Operational Excellence）是六個支柱之一，涵蓋運作、監控和持續改進。",
      "D": "✓ 正確 — 成本優化（Cost Optimization）是六個支柱之一，涵蓋避免不必要支出、了解支出等。"
    }
  },
  {
    "id": 169, "exam": "CLF",
    "question": "The AWS Well-Architected Framework is organized into how many pillars?",
    "question_zh": "AWS Well-Architected Framework 組織成幾個支柱？",
    "options": {
      "A": {"en": "3", "zh": "3"},
      "B": {"en": "4", "zh": "4"},
      "C": {"en": "6", "zh": "6"},
      "D": {"en": "None of the above", "zh": "以上皆非"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ AWS Well-Architected Framework 不是 3 個支柱。",
      "B": "✗ AWS Well-Architected Framework 不是 4 個支柱。",
      "C": "✓ 正確 — AWS Well-Architected Framework 有 6 個支柱：(1) 卓越操作、(2) 安全性、(3) 可靠性、(4) 效能效率、(5) 成本優化、(6) 永續性（2021 年新增）。",
      "D": "✗ 以上確實有正確答案（6 個支柱）。"
    }
  },
  {
    "id": 170, "exam": "CLF",
    "question": "After you move to the AWS Cloud, you want to ensure that the right security settings are put in place. Which online tool can assist in security compliance?",
    "question_zh": "遷移到 AWS 雲端後，您希望確保正確的安全設定到位。哪個線上工具可以協助安全合規？",
    "options": {
      "A": {"en": "Amazon Kinesis", "zh": "Amazon Kinesis"},
      "B": {"en": "AWS Support", "zh": "AWS Support"},
      "C": {"en": "AWS Trusted Advisor", "zh": "AWS Trusted Advisor"},
      "D": {"en": "Amazon CloudWatch", "zh": "Amazon CloudWatch"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ Amazon Kinesis 是資料串流服務，用於即時處理大量資料，不是安全合規工具。",
      "B": "✗ AWS Support 是客戶支援服務，提供技術協助，不是主動安全掃描工具。",
      "C": "✓ 正確 — AWS Trusted Advisor 提供安全類別的最佳實踐建議，包括：開放的 S3 儲存貯體、過於寬鬆的安全群組、未啟用 MFA 等安全問題的即時警告，協助確保安全合規。",
      "D": "✗ Amazon CloudWatch 是監控和可觀察性服務，主要用於指標和日誌，不是安全合規評估工具。"
    }
  },
  {
    "id": 171, "exam": "CLF",
    "question": "Which of the following is a measure of your system's ability to provide functionality when desired by the user?",
    "question_zh": "下列哪項是衡量系統在使用者需要時提供功能的能力的指標？",
    "options": {
      "A": {"en": "Availability", "zh": "可用性"},
      "B": {"en": "Fault Tolerance", "zh": "容錯能力"},
      "C": {"en": "Reliability", "zh": "可靠性"},
      "D": {"en": "Performance efficiency", "zh": "效能效率"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ 可用性（Availability）通常指系統在正常運行時間內可存取的百分比（如 99.99%），與可靠性相近但不完全相同。",
      "B": "✗ 容錯能力（Fault Tolerance）指系統在元件故障時仍能繼續運作的能力，是可靠性的一個子集。",
      "C": "✓ 正確 — 可靠性（Reliability）是衡量系統在所需時間內正確執行預期功能的能力，即使用者需要時系統能正常提供功能。",
      "D": "✗ 效能效率是 Well-Architected Framework 的支柱，關注資源有效使用，不是衡量功能提供能力的指標。"
    }
  },
  {
    "id": 172, "exam": "CLF",
    "question": "What is defined as the ability for a system to remain operational even if some of the components of that system fail?",
    "question_zh": "什麼定義為系統即使某些元件發生故障仍能保持運行的能力？",
    "options": {
      "A": {"en": "High durability", "zh": "高耐久性"},
      "B": {"en": "Fault tolerance", "zh": "容錯能力"},
      "C": {"en": "High availability", "zh": "高可用性"},
      "D": {"en": "Scalability", "zh": "可擴展性"}
    },
    "correct": ["B"], "multi": False,
    "explanations": {
      "A": "✗ 高耐久性（High durability）指資料長期儲存不遺失的能力（如 S3 的 11 個 9 耐久性），不是系統在元件故障時繼續運作的能力。",
      "B": "✓ 正確 — 容錯能力（Fault tolerance）定義為：即使系統的某些元件故障，系統仍能繼續正確運作。這通常通過冗餘設計實現（如多個 AZ 部署）。",
      "C": "✗ 高可用性（High availability）是指系統在一段時間內可存取和運作的百分比，雖然相關，但容錯能力更強調在故障時的持續運作。",
      "D": "✗ 可擴展性（Scalability）指系統處理增加工作負載的能力，不是在故障時繼續運作的能力。"
    }
  },
  {
    "id": 173, "exam": "CLF",
    "question": "Which of the following best describes a system that can withstand some measures of degradation, experiences minimal downtime, and requires minimal human intervention?",
    "question_zh": "下列哪項最能描述一個能夠承受一定程度的降級、停機時間最短、需要最少人工干預的系統？",
    "options": {
      "A": {"en": "Scalable", "zh": "可擴展的"},
      "B": {"en": "Fault-tolerant", "zh": "容錯的"},
      "C": {"en": "Elastic", "zh": "彈性的"},
      "D": {"en": "Highly available", "zh": "高可用性的"}
    },
    "correct": ["D"], "multi": False,
    "explanations": {
      "A": "✗ 可擴展性描述系統處理增加工作負載的能力，不是最小化停機時間的特性。",
      "B": "✗ 容錯系統在元件故障時繼續完全運作，不描述「可承受一定降級」的情況。",
      "C": "✗ 彈性描述系統自動擴縮資源的能力，不直接描述最小停機時間或降級容忍。",
      "D": "✓ 正確 — 高可用性（Highly available）系統的特徵：(1) 可以承受一定程度的降級（graceful degradation）、(2) 停機時間最短（有快速故障轉移）、(3) 自動恢復需要最少人工干預。"
    }
  },
  {
    "id": 174, "exam": "CLF",
    "question": "Which of the following AWS tools help your application scale up or down based on demand? (Choose two.)",
    "question_zh": "下列哪些 AWS 工具可幫助您的應用程式根據需求向上或向下擴展？（選擇兩個）",
    "options": {
      "A": {"en": "Availability Zones", "zh": "可用區域"},
      "B": {"en": "Amazon EC2 Auto Scaling", "zh": "Amazon EC2 Auto Scaling"},
      "C": {"en": "AWS CloudFormation", "zh": "AWS CloudFormation"},
      "D": {"en": "Elastic Load Balancing", "zh": "Elastic Load Balancing"},
      "E": {"en": "AWS Config", "zh": "AWS Config"}
    },
    "correct": ["B", "D"], "multi": True,
    "explanations": {
      "A": "✗ 可用區域是 AWS 基礎設施的物理分隔，提供高可用性，但本身不根據需求自動擴展應用程式。",
      "B": "✓ 正確 — Amazon EC2 Auto Scaling 根據定義的條件（CPU 使用率、請求數等）自動增加或減少 EC2 執行個體數量，實現需求驅動的擴展。",
      "C": "✗ AWS CloudFormation 是基礎設施即代碼（IaC）服務，用於佈建 AWS 資源，不是自動擴展工具。",
      "D": "✓ 正確 — Elastic Load Balancing 將流量分配到多個執行個體，與 Auto Scaling 配合使用，確保新增的執行個體能接收流量，實現有效的水平擴展。",
      "E": "✗ AWS Config 追蹤 AWS 資源配置變更，是合規和審計工具，不是擴展工具。"
    }
  },
  {
    "id": 175, "exam": "CLF",
    "question": "Which service would you use to send alerts based on Amazon CloudWatch alarms?",
    "question_zh": "您會使用哪個服務根據 Amazon CloudWatch 警報發送提醒？",
    "options": {
      "A": {"en": "Amazon Simple Notification Service (Amazon SNS)", "zh": "Amazon Simple Notification Service（Amazon SNS）"},
      "B": {"en": "AWS CloudTrail", "zh": "AWS CloudTrail"},
      "C": {"en": "AWS Trusted Advisor", "zh": "AWS Trusted Advisor"},
      "D": {"en": "Amazon Route 53", "zh": "Amazon Route 53"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確 — Amazon SNS（簡單通知服務）與 CloudWatch 警報整合，當警報觸發時可通過 Email、SMS、HTTP、SQS 等方式發送通知。CloudWatch 警報直接使用 SNS 主題來傳遞警報。",
      "B": "✗ AWS CloudTrail 記錄 API 呼叫日誌，是審計工具，不用於根據 CloudWatch 警報發送警示。",
      "C": "✗ AWS Trusted Advisor 提供最佳實踐建議，不是警報通知服務。",
      "D": "✗ Amazon Route 53 是 DNS 和流量路由服務，不用於發送 CloudWatch 警報通知。"
    }
  },
  {
    "id": 176, "exam": "CLF",
    "question": "Which of the following are characteristics of Amazon EC2 Auto Scaling? (Choose three.)",
    "question_zh": "下列哪些是 Amazon EC2 Auto Scaling 的特性？（選擇三個）",
    "options": {
      "A": {"en": "Only supports dynamic scaling", "zh": "僅支援動態擴展"},
      "B": {"en": "Responds to changing conditions by adding or terminating instances", "zh": "通過新增或終止執行個體來響應變化的條件"},
      "C": {"en": "Delivers push notifications", "zh": "傳遞推播通知"},
      "D": {"en": "Launches instances from a specified Amazon Machine Image (AMI)", "zh": "從指定的 Amazon Machine Image（AMI）啟動執行個體"},
      "E": {"en": "Enforces a minimum number of running Amazon EC2 instances", "zh": "強制執行最少數量的運行中 Amazon EC2 執行個體"}
    },
    "correct": ["B", "D", "E"], "multi": True,
    "explanations": {
      "A": "✗ Auto Scaling 支援多種擴展類型：動態擴展（基於指標）、預定擴展（Scheduled）和預測擴展（Predictive），不僅僅是動態擴展。",
      "B": "✓ 正確 — Auto Scaling 的核心功能：監控條件（如 CPU 使用率），在需要時自動新增執行個體（scale out）或終止多餘執行個體（scale in）。",
      "C": "✗ 推播通知是 Amazon SNS 的功能，不是 Auto Scaling 的特性。",
      "D": "✓ 正確 — Auto Scaling 使用啟動配置（Launch Configuration）或啟動範本（Launch Template）指定 AMI 來啟動新執行個體。",
      "E": "✓ 正確 — Auto Scaling 群組有最小容量設定，確保始終有指定數量的執行個體在運行，即使需求極低。"
    }
  },
  {
    "id": 177, "exam": "CLF",
    "question": "Which of the following must be configured on an Elastic Load Balancing load balancer to expect incoming traffic?",
    "question_zh": "必須在 Elastic Load Balancing 負載平衡器上配置什麼才能接收傳入流量？",
    "options": {
      "A": {"en": "A port", "zh": "連接埠"},
      "B": {"en": "A network interface", "zh": "網路介面"},
      "C": {"en": "A listener", "zh": "監聽器"},
      "D": {"en": "An instance", "zh": "執行個體"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ 連接埠是監聽器配置的一部分，但僅設定連接埠不夠；監聽器包含連接埠加上協定和路由規則。",
      "B": "✗ 網路介面是底層網路配置，不是 ELB 接收流量的主要配置項目。",
      "C": "✓ 正確 — 監聽器（Listener）是 ELB 的核心配置元件，定義負載平衡器接受傳入連接的協定和連接埠（如 HTTP:80、HTTPS:443），並包含將流量路由到目標群組的規則。",
      "D": "✗ 執行個體是目標群組的成員（接收流量的後端），不是負載平衡器本身接收流量所需的配置。"
    }
  },
  {
    "id": 178, "exam": "CLF",
    "question": "Which of the following elements are used to create an Amazon EC2 Auto Scaling launch configuration? (Choose three.)",
    "question_zh": "下列哪些元素用於建立 Amazon EC2 Auto Scaling 啟動配置？（選擇三個）",
    "options": {
      "A": {"en": "Amazon Machine Image (AMI)", "zh": "Amazon Machine Image（AMI）"},
      "B": {"en": "Load balancer", "zh": "負載平衡器"},
      "C": {"en": "Instance type", "zh": "執行個體類型"},
      "D": {"en": "Virtual private cloud (VPC) and subnets", "zh": "虛擬私有雲（VPC）和子網路"},
      "E": {"en": "Amazon Elastic Block Store (Amazon EBS) volumes", "zh": "Amazon Elastic Block Store（Amazon EBS）磁碟區"}
    },
    "correct": ["A", "C", "E"], "multi": True,
    "explanations": {
      "A": "✓ 正確 — AMI 是啟動配置的必要元素，指定新執行個體的作業系統和初始軟體。",
      "B": "✗ 負載平衡器在 Auto Scaling 群組層級配置（附加到群組），不是啟動配置（Launch Configuration）的元素。",
      "C": "✓ 正確 — 執行個體類型（如 t3.medium、m5.large）是啟動配置的必要元素，決定 CPU、記憶體規格。",
      "D": "✗ VPC 和子網路在 Auto Scaling 群組層級配置（指定在哪裡啟動執行個體），不是啟動配置的元素。",
      "E": "✓ 正確 — EBS 磁碟區配置（包括根磁碟區大小、類型，以及額外的 EBS 磁碟區）是啟動配置的一部分。"
    }
  },
  {
    "id": 179, "exam": "CLF",
    "question": "Which of the following services can help you collect important metrics from Amazon RDS and Amazon EC2 instances?",
    "question_zh": "下列哪個服務可以幫助您從 Amazon RDS 和 Amazon EC2 執行個體收集重要指標？",
    "options": {
      "A": {"en": "Amazon CloudFront", "zh": "Amazon CloudFront"},
      "B": {"en": "Amazon CloudSearch", "zh": "Amazon CloudSearch"},
      "C": {"en": "Amazon CloudWatch", "zh": "Amazon CloudWatch"},
      "D": {"en": "AWS CloudTrail", "zh": "AWS CloudTrail"},
      "E": {"en": "Amazon EC2 Auto Scaling", "zh": "Amazon EC2 Auto Scaling"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ Amazon CloudFront 是內容傳遞網路（CDN），用於加速內容分發，不是指標收集服務。",
      "B": "✗ Amazon CloudSearch 是搜尋服務，用於網站和應用程式搜尋功能，不是監控服務。",
      "C": "✓ 正確 — Amazon CloudWatch 是 AWS 的監控服務，自動收集 EC2（CPU、網路、磁碟）和 RDS（資料庫連接、讀寫延遲、儲存空間）等服務的指標，並支援自定義指標、警報和儀表板。",
      "D": "✗ AWS CloudTrail 記錄 API 呼叫（誰做了什麼操作），是審計和合規工具，不是效能指標收集工具。",
      "E": "✗ EC2 Auto Scaling 根據條件自動調整執行個體數量，不是指標收集服務（雖然它使用 CloudWatch 指標）。"
    }
  },
  {
    "id": 180, "exam": "CLF",
    "question": "Which of the following are elements of an Auto Scaling group? (Choose three.)",
    "question_zh": "下列哪些是 Auto Scaling 群組的元素？（選擇三個）",
    "options": {
      "A": {"en": "Minimum size", "zh": "最小容量"},
      "B": {"en": "Health checks", "zh": "健康檢查"},
      "C": {"en": "Desired capacity", "zh": "所需容量"},
      "D": {"en": "Maximum size", "zh": "最大容量"}
    },
    "correct": ["A", "C", "D"], "multi": True,
    "explanations": {
      "A": "✓ 正確 — 最小容量（Minimum size）定義 Auto Scaling 群組中始終保持運行的最少執行個體數，確保基本可用性。",
      "B": "✗ 健康檢查是 Auto Scaling 的功能（用於偵測並替換不健康的執行個體），但不是群組的三個「容量」定義元素之一。",
      "C": "✓ 正確 — 所需容量（Desired capacity）定義 Auto Scaling 群組在正常情況下應維持的執行個體數，Auto Scaling 會嘗試保持此數量。",
      "D": "✓ 正確 — 最大容量（Maximum size）定義 Auto Scaling 群組可以擴展到的執行個體上限，防止無限制擴展造成成本失控。"
    }
  },
  {
    "id": 181, "exam": "CLF",
    "question": "In Elastic Load Balancing, when the load balancer detects an unhealthy target, which of the following are true? (Choose three.)",
    "question_zh": "在 Elastic Load Balancing 中，當負載平衡器偵測到不健康的目標時，下列哪些是正確的？（選擇三個）",
    "options": {
      "A": {"en": "Stops routing traffic to that target", "zh": "停止將流量路由到該目標"},
      "B": {"en": "Triggers an alarm", "zh": "觸發警報"},
      "C": {"en": "Resumes routing traffic when it detects that the target is healthy again", "zh": "當偵測到目標再次健康時恢復路由流量"},
      "D": {"en": "Resumes routing traffic when manually restarted", "zh": "手動重啟後恢復路由流量"},
      "E": {"en": "Routes traffic to a healthy target", "zh": "將流量路由到健康的目標"}
    },
    "correct": ["A", "C", "E"], "multi": True,
    "explanations": {
      "A": "✓ 正確 — 當 ELB 的健康檢查確認目標不健康時，立即停止將新請求路由到該目標。",
      "B": "✗ ELB 本身不直接觸發 CloudWatch 警報；警報需要另外配置（透過 CloudWatch）。",
      "C": "✓ 正確 — ELB 持續對所有目標執行健康檢查；當不健康的目標通過健康檢查後，ELB 自動恢復向其路由流量，無需人工干預。",
      "D": "✗ ELB 不需要手動重啟就能恢復路由；它自動通過健康檢查來決定是否恢復（選項 C）。",
      "E": "✓ 正確 — 當某個目標不健康時，ELB 將所有流量路由到剩餘的健康目標，確保應用程式持續可用。"
    }
  },
  {
    "id": 182, "exam": "CLF",
    "question": "What are the three types of load balancers that Elastic Load Balancing offers? (Choose three.)",
    "question_zh": "Elastic Load Balancing 提供哪三種類型的負載平衡器？（選擇三個）",
    "options": {
      "A": {"en": "Internet Load Balancer", "zh": "網際網路負載平衡器"},
      "B": {"en": "Application Load Balancer", "zh": "應用程式負載平衡器"},
      "C": {"en": "Network Load Balancer", "zh": "網路負載平衡器"},
      "D": {"en": "Compute Load Balancer", "zh": "運算負載平衡器"},
      "E": {"en": "Classic Load Balancer", "zh": "傳統負載平衡器"},
      "F": {"en": "Auto Scaling Load Balancer", "zh": "Auto Scaling 負載平衡器"}
    },
    "correct": ["B", "C", "E"], "multi": True,
    "explanations": {
      "A": "✗ 「Internet Load Balancer」不是 AWS ELB 的類型名稱。",
      "B": "✓ 正確 — Application Load Balancer（ALB）：Layer 7 負載平衡器，支援 HTTP/HTTPS，可基於 URL、主機名稱等路由規則分配流量，適合 Web 應用和微服務。",
      "C": "✓ 正確 — Network Load Balancer（NLB）：Layer 4 負載平衡器，支援 TCP/UDP，提供極低延遲和高吞吐量，適合需要靜態 IP 或超低延遲的應用。",
      "D": "✗ 「Compute Load Balancer」不是 AWS ELB 的類型名稱。",
      "E": "✓ 正確 — Classic Load Balancer（CLB）：舊世代負載平衡器，同時運作在 Layer 4 和 Layer 7，適合 EC2-Classic 網路中的應用（現代應用建議使用 ALB 或 NLB）。",
      "F": "✗ 「Auto Scaling Load Balancer」不是 AWS ELB 的類型名稱；Auto Scaling 和 ELB 是不同的服務。"
    }
  },
]
