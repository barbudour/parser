# IClientCommandHandlerContext - интерфейс
Описывает контекст клиентской команды.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IClientCommandHandlerContext : IExtensionContext
VB __Копировать
     Public Interface IClientCommandHandlerContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IClientCommandHandlerContext : IExtensionContext
F# __Копировать
     type IClientCommandHandlerContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[Command](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandHandlerContext_Command.htm)|
Возвращает или задаёт текущую клиентскую команду.  
[Info](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandHandlerContext_Info.htm)|
Возвращает или задаёт дополнительную информацию.  
[OuterContext](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_IClientCommandHandlerContext_OuterContext.htm)|
Возвращает или задаёт внешний контекст, в котором запущено выполнение. Может
быть null.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
