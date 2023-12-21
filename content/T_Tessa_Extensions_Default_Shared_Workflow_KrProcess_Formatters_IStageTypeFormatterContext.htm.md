# IStageTypeFormatterContext - интерфейс
Описывает контекст форматтера этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IStageTypeFormatterContext : IExtensionContext
VB __Копировать
     Public Interface IStageTypeFormatterContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IStageTypeFormatterContext : IExtensionContext
F# __Копировать
     type IStageTypeFormatterContext = 
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
[Card](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext_Card.htm)|
Возвращает карточку содержащую этап.  
[DisplayParticipants](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext_DisplayParticipants.htm)|
Возвращает или задаёт отображаемый список участников.  
[DisplaySettings](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext_DisplaySettings.htm)|
Возвращает или задаёт отображаемые настройки.  
[DisplayTimeLimit](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext_DisplayTimeLimit.htm)|
Возвращает или задаёт отображаемый срок исполнения.  
[Info](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext_Info.htm)|
Возвращает дополнительную информацию.  
[Session](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext_Session.htm)|
Возвращает сессию пользователя.  
[Settings](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext_Settings.htm)|
Возвращает словарь содержащий настройки этапа.  
[StageRow](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_IStageTypeFormatterContext_StageRow.htm)|
Возвращает строку содержащую этап.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)
