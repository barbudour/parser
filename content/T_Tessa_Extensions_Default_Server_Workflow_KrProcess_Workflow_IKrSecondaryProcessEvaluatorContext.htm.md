# IKrSecondaryProcessEvaluatorContext - интерфейс
Описывает контекст содержащий информацию о запускаемом вторичном процессе.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrSecondaryProcessEvaluatorContext : IExtensionContext
VB __Копировать
     Public Interface IKrSecondaryProcessEvaluatorContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrSecondaryProcessEvaluatorContext : IExtensionContext
F# __Копировать
     type IKrSecondaryProcessEvaluatorContext = 
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
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_CardContext.htm)|
Конекст расширения карточки.  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_CardID.htm)|
Идентификатор карточки.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_CardType.htm)|
Тип карточки.  
[ContextualSatellite](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_ContextualSatellite.htm)|
Контекстуальный сателлит карточки.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_DocTypeID.htm)|
Идентификатор типа документа.  
[KrComponents](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_KrComponents.htm)|
Включенные компоненты типового решения для текущей карточки.  
[MainCardAccessStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_MainCardAccessStrategy.htm)|
Стратегия загрузки основной карточки.  
[SecondaryProcess](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_SecondaryProcess.htm)|
Кнопка, для которой проводится вычисление.  
[State](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_State.htm)|
Состояние карточки.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrSecondaryProcessEvaluatorContext_ValidationResult.htm)|
Результат валидации.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
