# WfHelper.GetResolutionState - метод
Возвращает состояние резолюции, полученное по её параметрам.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetResolutionState(
    	KrSettings settings,
    	string performerRoleName,
    	string userName,
    	Guid? completionOptionID,
    	bool limitLength = true
    )
VB __Копировать
     Public Shared Function GetResolutionState ( 
    	settings As KrSettings,
    	performerRoleName As String,
    	userName As String,
    	completionOptionID As Guid?,
    	Optional limitLength As Boolean = true
    ) As String
C++ __Копировать
     public:
    static String^ GetResolutionState(
    	KrSettings^ settings, 
    	String^ performerRoleName, 
    	String^ userName, 
    	Nullable<Guid> completionOptionID, 
    	bool limitLength = true
    )
F# __Копировать
     static member GetResolutionState : 
            settings : KrSettings * 
            performerRoleName : string * 
            userName : string * 
            completionOptionID : Nullable<Guid> * 
            ?limitLength : bool 
    (* Defaults:
            let _limitLength = defaultArg limitLength true
    *)
    -> string 
#### Параметры
settings
[KrSettings](T_Tessa_Extensions_Default_Shared_Settings_KrSettings.htm)
    Настройки решения для Wf.
performerRoleName
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Роль исполнителя.
userName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя пользователя, взявшего задание в работу или завершившего его, или null, если задание назначено на роль и ещё не взято в работу. 
completionOptionID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор варианта завершения задания или null, если задание ещё не было завершено. 
limitLength [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что следует ограничить максимальный размер строки для удобства вывода. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Состояние резолюции, полученное по её параметрам.
##  __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
