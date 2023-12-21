# WorkflowQueueProcessor - класс
Базовый класс для объекта, выполняющего обработку действий в очереди с
номерами.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class WorkflowQueueProcessor : IWorkflowQueueProcessor
VB __Копировать
     Public MustInherit Class WorkflowQueueProcessor
    	Implements IWorkflowQueueProcessor
C++ __Копировать
     public ref class WorkflowQueueProcessor abstract : IWorkflowQueueProcessor
F# __Копировать
     [<AbstractClassAttribute>]
    type WorkflowQueueProcessor = 
        class
            interface IWorkflowQueueProcessor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowQueueProcessor
Derived
[Tessa.Cards.Workflow.DefaultWorkflowQueueProcessor](T_Tessa_Cards_Workflow_DefaultWorkflowQueueProcessor.htm)
Implements
    [IWorkflowQueueProcessor](T_Tessa_Cards_Workflow_IWorkflowQueueProcessor.htm)
##  __Конструкторы
[WorkflowQueueProcessor](M_Tessa_Cards_Workflow_WorkflowQueueProcessor__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowQueueProcessor  
---|---  
##  __Методы
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
[ProcessAsync](M_Tessa_Cards_Workflow_WorkflowQueueProcessor_ProcessAsync.htm)|
Выполняет действия из заданной очереди [Tessa.Cards.Workflow.WorkflowQueue].
Возвращает признак того, что во всех выполненных действиях отсутствуют ошибки.
Действия, которые были успешно выполнены, удаляются из очереди.  
[ProcessCoreAsync](M_Tessa_Cards_Workflow_WorkflowQueueProcessor_ProcessCoreAsync.htm)|
Выполняет действия из заданной очереди [Tessa.Cards.Workflow.WorkflowQueue].
Возвращает признак того, что во всех выполненных действиях отсутствуют ошибки.
Действия, которые были успешно выполнены, удаляются из очереди.  
[ProcessItemAsync](M_Tessa_Cards_Workflow_WorkflowQueueProcessor_ProcessItemAsync.htm)|
Выполняет обработку действия в очереди Workflow API и возвращает признак того,
что обработка выполнена удачно.  
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
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
