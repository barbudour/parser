# KrProcessLaunchResult.ProcessInfo - свойство
Дополнительная информация процесса после его завершения.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public IDictionary<string, Object?>? ProcessInfo { get; set; }
VB __Копировать
     Public Property ProcessInfo As IDictionary(Of String, Object)
    	Get
    	Set
C++ __Копировать
     public:
    virtual property IDictionary<String^, Object^>^ ProcessInfo {
    	IDictionary<String^, Object^>^ get () sealed;
    	void set (IDictionary<String^, Object^>^ value) sealed;
    }
F# __Копировать
     abstract ProcessInfo : IDictionary<string, Object> with get, set
    override ProcessInfo : IDictionary<string, Object> with get, set
#### Значение свойства
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
#### Реализации
[IKrProcessLaunchResult.ProcessInfo](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLaunchResult_ProcessInfo.htm)  
##  __См. также
#### Ссылки
[KrProcessLaunchResult -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessLaunchResult.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
