# WfHelper.SetController - метод
Устанавливает информацию о роли, на которую возвращается задание с контролем
исполнения. Устанавливать и проверять информацию имеет смысл только для
добавляемого задания task.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetController(
    	CardTask task,
    	Guid? controllerID,
    	string controllerName
    )
VB __Копировать
     Public Shared Sub SetController ( 
    	task As CardTask,
    	controllerID As Guid?,
    	controllerName As String
    )
C++ __Копировать
     public:
    static void SetController(
    	CardTask^ task, 
    	Nullable<Guid> controllerID, 
    	String^ controllerName
    )
F# __Копировать
     static member SetController : 
            task : CardTask * 
            controllerID : Nullable<Guid> * 
            controllerName : string -> unit 
#### Параметры
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание, при завершении которого будет выслан контроль исполнения.
controllerID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор роли, на которую возвращается задание с контролем исполнения, или null, если контроль исполнения не выполняется. 
controllerName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя роли, на которую возвращается задание с контролем исполнения, или null, если контроль исполнения не выполняется. 
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
