# KrProcessLaunchResult.ProcessID - свойство
Идентификатор запущенного асинхронного процесса или значение null, если при
запуске процесса произошла ошибка или запускался синхронный процесс.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? ProcessID { get; set; }
VB __Копировать
     Public Property ProcessID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    virtual property Nullable<Guid> ProcessID {
    	Nullable<Guid> get () sealed;
    	void set (Nullable<Guid> value) sealed;
    }
F# __Копировать
     abstract ProcessID : Nullable<Guid> with get, set
    override ProcessID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
#### Реализации
[IKrProcessLaunchResult.ProcessID](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLaunchResult_ProcessID.htm)  
##  __См. также
#### Ссылки
[KrProcessLaunchResult -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessLaunchResult.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
