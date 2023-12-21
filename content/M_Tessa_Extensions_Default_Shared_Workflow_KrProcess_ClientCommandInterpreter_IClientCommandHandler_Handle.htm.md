# IClientCommandHandler.Handle - метод
Обработать клиентскую команду.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     Task Handle(
    	IClientCommandHandlerContext context
    )
VB __Копировать
     Function Handle ( 
    	context As IClientCommandHandlerContext
    ) As Task
C++ __Копировать
    Task^ Handle(
    	IClientCommandHandlerContext^ context
    )
F# __Копировать
     abstract Handle : 
            context : IClientCommandHandlerContext -> Task 
#### Параметры
context
[IClientCommandHandlerContext](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandHandlerContext.htm)
    Контекст клиентской команды.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IClientCommandHandler -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandHandler.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
