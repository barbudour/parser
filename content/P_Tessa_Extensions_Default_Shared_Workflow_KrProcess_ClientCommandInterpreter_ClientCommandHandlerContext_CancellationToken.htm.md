# ClientCommandHandlerContext.CancellationToken - свойство
Объект, посредством которого можно отменить асинхронную задачу.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public CancellationToken CancellationToken { get; set; }
VB __Копировать
     Public Property CancellationToken As CancellationToken
    	Get
    	Set
C++ __Копировать
     public:
    virtual property CancellationToken CancellationToken {
    	CancellationToken get () sealed;
    	void set (CancellationToken value) sealed;
    }
F# __Копировать
     abstract CancellationToken : CancellationToken with get, set
    override CancellationToken : CancellationToken with get, set
#### Значение свойства
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
#### Реализации
[IExtensionContext.CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)  
##  __Заметки
Не изменяйте значение этого свойства в процессе выполнения расширений.
##  __См. также
#### Ссылки
[ClientCommandHandlerContext -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_ClientCommandHandlerContext.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
