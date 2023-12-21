# WfHelper.TryGetController - метод
Возвращает информацию о роли, на которую возвращается задание с контролем
исполнения. Возвращает признак того, что контроль исполнения выполняется.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetController(
    	CardTask task,
    	out Guid? controllerID,
    	out string controllerName
    )
VB __Копировать
     Public Shared Function TryGetController ( 
    	task As CardTask,
    	<OutAttribute> ByRef controllerID As Guid?,
    	<OutAttribute> ByRef controllerName As String
    ) As Boolean
C++ __Копировать
     public:
    static bool TryGetController(
    	CardTask^ task, 
    	[OutAttribute] Nullable<Guid>% controllerID, 
    	[OutAttribute] String^% controllerName
    )
F# __Копировать
     static member TryGetController : 
            task : CardTask * 
            controllerID : Nullable<Guid> byref * 
            controllerName : string byref -> bool 
#### Параметры
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание, при завершении которого будет выслан контроль исполнения.
controllerID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор роли, на которую возвращается задание с контролем исполнения, или null, если контроль исполнения не выполняется. 
controllerName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя роли, на которую возвращается задание с контролем исполнения, или null, если контроль исполнения не выполняется. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
