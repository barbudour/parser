# WorkflowEngineCardsScope - класс
Scope для загрузки карточек в рамках обработки WorkflowEngine.
## __Definition
 **Пространство имён:** [Tessa.Workflow](N_Tessa_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowEngineCardsScope : IWorkflowEngineCardsScope
VB __Копировать
     Public NotInheritable Class WorkflowEngineCardsScope
    	Implements IWorkflowEngineCardsScope
C++ __Копировать
     public ref class WorkflowEngineCardsScope sealed : IWorkflowEngineCardsScope
F# __Копировать
     [<SealedAttribute>]
    type WorkflowEngineCardsScope = 
        class
            interface IWorkflowEngineCardsScope
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowEngineCardsScope
Implements
    [IWorkflowEngineCardsScope](T_Tessa_Workflow_IWorkflowEngineCardsScope.htm)
##  __Конструкторы
[WorkflowEngineCardsScope](M_Tessa_Workflow_WorkflowEngineCardsScope__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowEngineCardsScope  
---|---  
##  __Свойства
[CardStorePriorityComparer](P_Tessa_Workflow_WorkflowEngineCardsScope_CardStorePriorityComparer.htm)|
Возвращает или задаёт компаратор определяющий порядок сохранения карточек.
Может иметь значение по умолчанию для типа, в этом случае упорядочивание
карточек при сохранении не выполняется.  
---|---  
## __Методы
[AddNewCard](M_Tessa_Workflow_WorkflowEngineCardsScope_AddNewCard.htm)|
Добавляет указанную карточку в Scope.  
---|---  
[CardIsLoaded](M_Tessa_Workflow_WorkflowEngineCardsScope_CardIsLoaded.htm)|
Проверяет, загружена ли карточка с заданным идентификатором или нет.  
[Create](M_Tessa_Workflow_WorkflowEngineCardsScope_Create.htm)|  Создаёт
контекст загрузки карточек для WorkflowEngine.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetCardAsync(Guid, IValidationResultBuilder,
CancellationToken)](M_Tessa_Workflow_WorkflowEngineCardsScope_GetCardAsync_1.htm)|
Загружает карточку с заданным идентификатором.  
[GetCardAsync(Guid, Func<Guid, CardGetRequest>, IValidationResultBuilder,
CancellationToken)](M_Tessa_Workflow_WorkflowEngineCardsScope_GetCardAsync.htm)|
Загружает карточку имеющую указанный идентификатор, если карточка не найдена в
кэше карточек, то она загружается из БД.  
[GetCardForSendTasksAsync](M_Tessa_Workflow_WorkflowEngineCardsScope_GetCardForSendTasksAsync.htm)|
Создаёт и возвращает карточку для отправки задания.  
[GetFileContainerAsync](M_Tessa_Workflow_WorkflowEngineCardsScope_GetFileContainerAsync.htm)|
Возвращает файловый контейнер для карточки с заданным идентификатором.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLoadedCards](M_Tessa_Workflow_WorkflowEngineCardsScope_GetLoadedCards.htm)|
Возвращает перечисление загруженных карточек.  
[GetLoadedFileContainers](M_Tessa_Workflow_WorkflowEngineCardsScope_GetLoadedFileContainers.htm)|
Возвращает перечисление загруженных контейнеров файлов.  
[GetSatelliteAsync](M_Tessa_Workflow_WorkflowEngineCardsScope_GetSatelliteAsync.htm)|
Возвращает карточку сателлита.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateAsync](M_Tessa_Workflow_WorkflowEngineCardsScope_InvalidateAsync.htm)|
Сбрасывает все загруженные объекты.  
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
[Tessa.Workflow - пространство имён](N_Tessa_Workflow.htm)
