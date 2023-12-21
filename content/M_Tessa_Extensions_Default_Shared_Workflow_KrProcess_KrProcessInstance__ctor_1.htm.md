# KrProcessInstance(Guid, Nullable<Guid>, IDictionary<String, Object>,
Nullable<Guid>, String, Nullable<Guid>, Nullable<Guid>, Nullable<Int32>) -
конструктор
Инициализирует новый экземпляр объекта
[KrProcessInstance](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrProcessInstance(
    	Guid processID,
    	Guid? cardID,
    	IDictionary<string, Object> processInfo,
    	Guid? parentStageRowID,
    	string parentProcessTypeName,
    	Guid? parentProcessID,
    	Guid? processHolderID,
    	int? nestedOrder
    )
VB __Копировать
     Public Sub New ( 
    	processID As Guid,
    	cardID As Guid?,
    	processInfo As IDictionary(Of String, Object),
    	parentStageRowID As Guid?,
    	parentProcessTypeName As String,
    	parentProcessID As Guid?,
    	processHolderID As Guid?,
    	nestedOrder As Integer?
    )
C++ __Копировать
     public:
    KrProcessInstance(
    	Guid processID, 
    	Nullable<Guid> cardID, 
    	IDictionary<String^, Object^>^ processInfo, 
    	Nullable<Guid> parentStageRowID, 
    	String^ parentProcessTypeName, 
    	Nullable<Guid> parentProcessID, 
    	Nullable<Guid> processHolderID, 
    	Nullable<int> nestedOrder
    )
F# __Копировать
     new : 
            processID : Guid * 
            cardID : Nullable<Guid> * 
            processInfo : IDictionary<string, Object> * 
            parentStageRowID : Nullable<Guid> * 
            parentProcessTypeName : string * 
            parentProcessID : Nullable<Guid> * 
            processHolderID : Nullable<Guid> * 
            nestedOrder : Nullable<int> -> KrProcessInstance
#### Параметры
processID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор процесса.
cardID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор карточки в которой запущен процесс.
processInfo
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительная информация по процессу.
parentStageRowID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор строки этапа создавшего этот вложенный процесс.
parentProcessTypeName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа родительского процесса.
parentProcessID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор родительского процесса.
processHolderID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор карточки держателя процесса.
nestedOrder
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
    Порядковый номер вложенного процесса.
##  __См. также
#### Ссылки
[KrProcessInstance -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance.htm)
[KrProcessInstance -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance__ctor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
