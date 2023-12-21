# WorkflowHelper.AppendApprovalInfoUserCompleteTask - метод
Добавляет информацию о согласовавшем/не согласовавшем пользователе в строковую
секцию
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrApprovalCommonInfo_Name.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void AppendApprovalInfoUserCompleteTask(
    	IDictionary<string, CardSection> sections,
    	IUser user,
    	CardTask task,
    	bool isNegativeResult
    )
VB __Копировать
     Public Shared Sub AppendApprovalInfoUserCompleteTask ( 
    	sections As IDictionary(Of String, CardSection),
    	user As IUser,
    	task As CardTask,
    	isNegativeResult As Boolean
    )
C++ __Копировать
     public:
    static void AppendApprovalInfoUserCompleteTask(
    	IDictionary<String^, CardSection^>^ sections, 
    	IUser^ user, 
    	CardTask^ task, 
    	bool isNegativeResult
    )
F# __Копировать
     static member AppendApprovalInfoUserCompleteTask : 
            sections : IDictionary<string, CardSection> * 
            user : IUser * 
            task : CardTask * 
            isNegativeResult : bool -> unit 
#### Параметры
sections
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CardSection](T_Tessa_Cards_CardSection.htm)>
    Словарь содержащий информацию о секциях карточки.
user [IUser](T_Tessa_Platform_Runtime_IUser.htm)
    Пользователь завершивший задание процесса согласования.
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Завершенное задание.
isNegativeResult
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение true, если результат завершения задания отрицательный, иначе - false.
##  __См. также
#### Ссылки
[WorkflowHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine_WorkflowHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.WorkflowEngine - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_WorkflowEngine.htm)
