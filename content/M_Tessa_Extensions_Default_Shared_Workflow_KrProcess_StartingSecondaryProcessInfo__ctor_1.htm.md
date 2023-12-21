# StartingSecondaryProcessInfo(Nullable<Guid>, IDictionary<String, Object>,
Nullable<Guid>, String, Nullable<Guid>, Nullable<Guid>, Nullable<Int32>) -
конструктор
Инициализирует новый экземпляр объекта
[StartingSecondaryProcessInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StartingSecondaryProcessInfo.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public StartingSecondaryProcessInfo(
    	Guid? secondaryProcess,
    	IDictionary<string, Object> processInfo,
    	Guid? parentStageRowID,
    	string parentProcessTypeName,
    	Guid? parentProcessID,
    	Guid? processHolderID,
    	int? nestedOrder
    )
VB __Копировать
     Public Sub New ( 
    	secondaryProcess As Guid?,
    	processInfo As IDictionary(Of String, Object),
    	parentStageRowID As Guid?,
    	parentProcessTypeName As String,
    	parentProcessID As Guid?,
    	processHolderID As Guid?,
    	nestedOrder As Integer?
    )
C++ __Копировать
     public:
    StartingSecondaryProcessInfo(
    	Nullable<Guid> secondaryProcess, 
    	IDictionary<String^, Object^>^ processInfo, 
    	Nullable<Guid> parentStageRowID, 
    	String^ parentProcessTypeName, 
    	Nullable<Guid> parentProcessID, 
    	Nullable<Guid> processHolderID, 
    	Nullable<int> nestedOrder
    )
F# __Копировать
     new : 
            secondaryProcess : Nullable<Guid> * 
            processInfo : IDictionary<string, Object> * 
            parentStageRowID : Nullable<Guid> * 
            parentProcessTypeName : string * 
            parentProcessID : Nullable<Guid> * 
            processHolderID : Nullable<Guid> * 
            nestedOrder : Nullable<int> -> StartingSecondaryProcessInfo
#### Параметры
secondaryProcess
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор вторичного процесса.
processInfo
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительная информация по процессу.
parentStageRowID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор строки этапа создавшего этот вложенный процесс.
parentProcessTypeName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа родитеского процесса.
parentProcessID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор родительского процесса.
processHolderID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор карточки держателя процесса.
nestedOrder
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
    Порядковый номер вложенного опроцесса.
##  __См. также
#### Ссылки
[StartingSecondaryProcessInfo -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StartingSecondaryProcessInfo.htm)
[StartingSecondaryProcessInfo -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StartingSecondaryProcessInfo__ctor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
