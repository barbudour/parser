# ConditionContext - класс
Контекст проверки условия в
[ICondition](T_Tessa_Platform_Conditions_ICondition.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ConditionContext : IConditionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class ConditionContext
    	Implements IConditionContext, IExtensionContext
C++ __Копировать
     public ref class ConditionContext sealed : IConditionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type ConditionContext = 
        class
            interface IConditionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConditionContext
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [IConditionContext](T_Tessa_Platform_Conditions_IConditionContext.htm)
##  __Конструкторы
[ConditionContext(Card, IDbScope, ISession, IValidationResultBuilder,
IUnityContainer)](M_Tessa_Platform_Conditions_ConditionContext__ctor_1.htm)|
Инициализирует новый экземпляр класса ConditionContext  
---|---  
[ConditionContext(Guid, Func<CancellationToken, ValueTask<Card>>, IDbScope,
ISession, IValidationResultBuilder,
IUnityContainer)](M_Tessa_Platform_Conditions_ConditionContext__ctor.htm)|
Инициализирует новый экземпляр класса ConditionContext  
##  __Свойства
[CancellationToken](P_Tessa_Platform_Conditions_ConditionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardID](P_Tessa_Platform_Conditions_ConditionContext_CardID.htm)|
Идентификатор карточки, по которой проверяется условие  
[Container](P_Tessa_Platform_Conditions_ConditionContext_Container.htm)|
Контейнер с зависимостями  
[DbScope](P_Tessa_Platform_Conditions_ConditionContext_DbScope.htm)|  Объект
для доступа к базе данных  
[Info](P_Tessa_Platform_Conditions_ConditionContext_Info.htm)|  Дополнительная
информация, которая передается между проверками всех условий  
[Session](P_Tessa_Platform_Conditions_ConditionContext_Session.htm)|  Текущая
сессия сотрудника. При отправке уведомлений это сессия получателя  
[Settings](P_Tessa_Platform_Conditions_ConditionContext_Settings.htm)|
Настройки условия  
[ValidationResult](P_Tessa_Platform_Conditions_ConditionContext_ValidationResult.htm)|
Билдер результата валидации  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetCardAsync](M_Tessa_Platform_Conditions_ConditionContext_GetCardAsync.htm)|
Метод для получения карточки  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetWorkflowContext](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetWorkflowContext.htm)|
Метод для получения контекста обработки процессов
[IWorkflowEngineContext](T_Tessa_Workflow_IWorkflowEngineContext.htm) из
контекста проверки условий
[IConditionContext](T_Tessa_Platform_Conditions_IConditionContext.htm)  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SetWorkflowContext](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetWorkflowContext.htm)|
Метод для установки контекста обработки процессов
[IWorkflowEngineContext](T_Tessa_Workflow_IWorkflowEngineContext.htm) в
контекст проверки условий
[IConditionContext](T_Tessa_Platform_Conditions_IConditionContext.htm)  
(Определяется
[WorkflowEngineExtensions](T_Tessa_Workflow_Helpful_WorkflowEngineExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Conditions - пространство
имён](N_Tessa_Platform_Conditions.htm)
