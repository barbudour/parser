# KrProcessSharedHelper.RepairStorageRowsOrders(IList, String) - метод
Восстанавливает порядок сортировки для списка строк.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void RepairStorageRowsOrders(
    	IList rows,
    	string orderFieldName
    )
VB __Копировать
     Public Shared Sub RepairStorageRowsOrders ( 
    	rows As IList,
    	orderFieldName As String
    )
C++ __Копировать
     public:
    static void RepairStorageRowsOrders(
    	IList^ rows, 
    	String^ orderFieldName
    )
F# __Копировать
     static member RepairStorageRowsOrders : 
            rows : IList * 
            orderFieldName : string -> unit 
#### Параметры
rows [IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist)
    Список сортируемых строк. Тип значений: IDictionary<string, object>.
orderFieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля, содержащего порядок сортировки.
##  __Заметки
Метод выполняет следующие действия:
  1. Упорядочивает строки в соответствии с порядком сортировки. Используется стабильная сортировка.
  2. Восстанавливает порядок сортировки, т.о. что бы он располагался в интервале [0; [Count](https://learn.microsoft.com/dotnet/api/system.collections.icollection.count#system-collections-icollection-count)) и не имел разрывов.
##  __См. также
#### Ссылки
[KrProcessSharedHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper.htm)
[RepairStorageRowsOrders -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper_RepairStorageRowsOrders.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
