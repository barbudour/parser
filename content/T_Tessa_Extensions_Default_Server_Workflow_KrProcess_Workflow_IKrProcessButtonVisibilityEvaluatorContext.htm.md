# IKrProcessButtonVisibilityEvaluatorContext - интерфейс
Описывает контекст используемый при определении видимости тайла вторичного
процесса работающего в режиме "Кнопка".
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrProcessButtonVisibilityEvaluatorContext : IExtensionContext
VB __Копировать
     Public Interface IKrProcessButtonVisibilityEvaluatorContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrProcessButtonVisibilityEvaluatorContext : IExtensionContext
F# __Копировать
     type IKrProcessButtonVisibilityEvaluatorContext = 
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
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessButtonVisibilityEvaluatorContext_CardContext.htm)|
Конекст расширения карточки.  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessButtonVisibilityEvaluatorContext_CardID.htm)|
Идентификатор карточки.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessButtonVisibilityEvaluatorContext_CardType.htm)|
Тип карточки.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessButtonVisibilityEvaluatorContext_DocTypeID.htm)|
Идентификатор типа документа.  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessButtonVisibilityEvaluatorContext_KrComponents.htm)|
Включенные компоненты типового решения для текущей карточки.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessButtonVisibilityEvaluatorContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[State](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessButtonVisibilityEvaluatorContext_State.htm)|
Состояние карточки.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessButtonVisibilityEvaluatorContext_ValidationResult.htm)|
Результат валидации.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
