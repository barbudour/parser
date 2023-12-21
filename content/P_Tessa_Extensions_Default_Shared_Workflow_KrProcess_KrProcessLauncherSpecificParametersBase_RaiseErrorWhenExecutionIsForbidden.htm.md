# KrProcessLauncherSpecificParametersBase.RaiseErrorWhenExecutionIsForbidden -
свойство
Возвращает или задаёт значение флага, показывающего, следует ли создавать
ошибку, если процесс не может быть выполнен из-за ограничений (параметр
вторичного процесса "Сообщение при невозможности выполнения процесса").
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public bool RaiseErrorWhenExecutionIsForbidden { get; set; }
VB __Копировать
     Public Property RaiseErrorWhenExecutionIsForbidden As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool RaiseErrorWhenExecutionIsForbidden {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract RaiseErrorWhenExecutionIsForbidden : bool with get, set
    override RaiseErrorWhenExecutionIsForbidden : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[IKrProcessLauncherSpecificParameters.RaiseErrorWhenExecutionIsForbidden](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLauncherSpecificParameters_RaiseErrorWhenExecutionIsForbidden.htm)  
##  __См. также
#### Ссылки
[KrProcessLauncherSpecificParametersBase -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessLauncherSpecificParametersBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
