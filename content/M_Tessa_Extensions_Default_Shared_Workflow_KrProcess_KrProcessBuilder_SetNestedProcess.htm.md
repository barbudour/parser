# KrProcessBuilder.SetNestedProcess - метод
Устанавливает информацию по вложенному процессу.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrProcessBuilder SetNestedProcess(
    	Guid processHolder,
    	string parentProcessTypeName,
    	Guid? parentProcessID,
    	Guid parentStageRow,
    	int nestedOrder
    )
VB __Копировать
     Public Function SetNestedProcess ( 
    	processHolder As Guid,
    	parentProcessTypeName As String,
    	parentProcessID As Guid?,
    	parentStageRow As Guid,
    	nestedOrder As Integer
    ) As KrProcessBuilder
C++ __Копировать
     public:
    KrProcessBuilder^ SetNestedProcess(
    	Guid processHolder, 
    	String^ parentProcessTypeName, 
    	Nullable<Guid> parentProcessID, 
    	Guid parentStageRow, 
    	int nestedOrder
    )
F# __Копировать
     member SetNestedProcess : 
            processHolder : Guid * 
            parentProcessTypeName : string * 
            parentProcessID : Nullable<Guid> * 
            parentStageRow : Guid * 
            nestedOrder : int -> KrProcessBuilder 
#### Параметры
processHolder [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки держателя процесса.
parentProcessTypeName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя типа родитеского процесса.
parentProcessID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор родительского процесса.
parentStageRow [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор строки этапа создавшего этот вложенный процесс.
nestedOrder [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Порядковый номер вложенного опроцесса.
#### Возвращаемое значение
[KrProcessBuilder](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessBuilder.htm)  
Объект
[KrProcessBuilder](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessBuilder.htm)
для создания цепочки.
##  __См. также
#### Ссылки
[KrProcessBuilder -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessBuilder.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
