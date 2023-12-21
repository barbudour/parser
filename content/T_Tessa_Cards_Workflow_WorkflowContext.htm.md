# WorkflowContext - класс
Контекст бизнес-процесса, содержащий информацию по сохраняемой карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowContext : IWorkflowContext
VB __Копировать
     Public NotInheritable Class WorkflowContext
    	Implements IWorkflowContext
C++ __Копировать
     public ref class WorkflowContext sealed : IWorkflowContext
F# __Копировать
     [<SealedAttribute>]
    type WorkflowContext = 
        class
            interface IWorkflowContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowContext
Implements
    [IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm)
##  __Конструкторы
[WorkflowContext(ICardStoreExtensionContext, CardStoreRequest,
ICardTaskHistoryManager, ICardGetStrategy, Dictionary<String,
Object>)](M_Tessa_Cards_Workflow_WorkflowContext__ctor_1.htm)|  Создаёт
экземпляр класса с указанием контекста на сохранение карточки, используемого
для заполнение свойств объекта.  
---|---  
[WorkflowContext(CardStoreRequest, CardStoreRequest, CardType, ICardMetadata,
ISession, IDbScope, DateTime, ICardTaskHistoryManager, ICardGetStrategy,
IValidationResultBuilder, Dictionary<String,
Object>)](M_Tessa_Cards_Workflow_WorkflowContext__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
## __Свойства
[CardGetStrategy](P_Tessa_Cards_Workflow_WorkflowContext_CardGetStrategy.htm)|
Стратегия, выполняющая низкоуровневую загрузку секций карточки, или null, если
такая загрузка не поддерживается. Обычно требуется для создания групп в
истории заданий совместно с объектом TaskHistoryManager.  
---|---  
[CardMetadata](P_Tessa_Cards_Workflow_WorkflowContext_CardMetadata.htm)|
Метаинформация по типам карточек, известным в системе.  
[CardType](P_Tessa_Cards_Workflow_WorkflowContext_CardType.htm)| Тип карточки,
в рамках которого выполняется бизнес-процесс.  
[DbScope](P_Tessa_Cards_Workflow_WorkflowContext_DbScope.htm)|  Объект,
посредством которого выполняется взаимодействие с базой данных в пределах
транзакции на сохранение карточки.  
[Info](P_Tessa_Cards_Workflow_WorkflowContext_Info.htm)| Дополнительная
информация, связанная с контекстом бизнес-процесса.  
[NextRequest](P_Tessa_Cards_Workflow_WorkflowContext_NextRequest.htm)|  Запрос
на дополнительное сохранение карточки, в процессе которого могут высылаться
задания бизнес-процесса. После изменения запроса обязательно следует вызвать
метод [IWorkflowContext.NotifyNextRequestPending], чтобы определить
необходимость дополнительного сохранения карточки.  
[NextRequestPending](P_Tessa_Cards_Workflow_WorkflowContext_NextRequestPending.htm)|
Признак того, что хотя бы раз был вызван метод
[IWorkflowContext.NotifyNextRequestPending] для того, чтобы определить
необходимость дополнительного сохранения карточки посредством запроса
[IWorkflowContext.NextRequest].  
[Request](P_Tessa_Cards_Workflow_WorkflowContext_Request.htm)| Запрос на
сохранение карточки, в процессе которого производится управление бизнес-
процессом.  
[Session](P_Tessa_Cards_Workflow_WorkflowContext_Session.htm)| Сессия
пользователя, который совершил действие, вызвавшее изменение в бизнес-
процессе.  
[StoreDateTime](P_Tessa_Cards_Workflow_WorkflowContext_StoreDateTime.htm)|
Текущие дата и время сохранения для использования в транзакции.  
[TaskHistoryManager](P_Tessa_Cards_Workflow_WorkflowContext_TaskHistoryManager.htm)|
Объект, управляющий созданием групп в истории заданий.  
[ValidationResult](P_Tessa_Cards_Workflow_WorkflowContext_ValidationResult.htm)|
Объект, посредством которого добавляются сообщения валидации, связанные с
управлением бизнес-процессом.  
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
[NotifyNextRequestPending](M_Tessa_Cards_Workflow_WorkflowContext_NotifyNextRequestPending.htm)|
Уведомляет о необходимости выполнить повторное сохранение карточки. Если метод
был вызван хотя бы раз, то свойство [IWorkflowContext.NextRequestPending]
вернёт значение true.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[AddTask](M_Tessa_Cards_Workflow_WorkflowExtensions_AddTask.htm)|  Добавляет
задание в состоянии [Inserted](T_Tessa_Cards_CardRowState.htm) к следующей
сохраняемой карточке
[NextRequest](P_Tessa_Cards_Workflow_IWorkflowContext_NextRequest.htm).  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
##  __См. также
#### Ссылки
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
