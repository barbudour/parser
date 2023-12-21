# IConditionContext - интерфейс
Контекст проверки условия в
[ICondition](T_Tessa_Platform_Conditions_ICondition.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConditionContext : IExtensionContext
VB __Копировать
     Public Interface IConditionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IConditionContext : IExtensionContext
F# __Копировать
     type IConditionContext = 
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
[CardID](P_Tessa_Platform_Conditions_IConditionContext_CardID.htm)|
Идентификатор карточки, по которой проверяется условие  
[Container](P_Tessa_Platform_Conditions_IConditionContext_Container.htm)|
Контейнер с зависимостями  
[DbScope](P_Tessa_Platform_Conditions_IConditionContext_DbScope.htm)|  Объект
для доступа к базе данных  
[Info](P_Tessa_Platform_Conditions_IConditionContext_Info.htm)|
Дополнительная информация, которая передается между проверками всех условий  
[Session](P_Tessa_Platform_Conditions_IConditionContext_Session.htm)|  Текущая
сессия сотрудника. При отправке уведомлений это сессия получателя  
[Settings](P_Tessa_Platform_Conditions_IConditionContext_Settings.htm)|
Настройки условия  
[ValidationResult](P_Tessa_Platform_Conditions_IConditionContext_ValidationResult.htm)|
Билдер результата валидации  
## __Методы
[GetCardAsync](M_Tessa_Platform_Conditions_IConditionContext_GetCardAsync.htm)|
Метод для получения карточки  
---|---  
## __Методы расширения
[GetWorkflowContext](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetWorkflowContext.htm)|
Метод для получения контекста обработки процессов
[IWorkflowEngineContext](T_Tessa_Workflow_IWorkflowEngineContext.htm) из
контекста проверки условий IConditionContext  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
---|---  
[SetWorkflowContext](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetWorkflowContext.htm)|
Метод для установки контекста обработки процессов
[IWorkflowEngineContext](T_Tessa_Workflow_IWorkflowEngineContext.htm) в
контекст проверки условий IConditionContext  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Conditions - пространство
имён](N_Tessa_Platform_Conditions.htm)
