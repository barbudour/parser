# WorkflowAPIBridge - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowAPIBridge : IWorkflowAPIBridge
VB __Копировать
     Public NotInheritable Class WorkflowAPIBridge
    	Implements IWorkflowAPIBridge
C++ __Копировать
     public ref class WorkflowAPIBridge sealed : IWorkflowAPIBridge
F# __Копировать
     [<SealedAttribute>]
    type WorkflowAPIBridge = 
        class
            interface IWorkflowAPIBridge
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowAPIBridge
Implements
    [IWorkflowAPIBridge](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IWorkflowAPIBridge.htm)
##  __Конструкторы
[WorkflowAPIBridge](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowAPIBridge  
---|---  
##  __Свойства
[NextRequest](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_NextRequest.htm)|
Возвращает запрос на следующее сохранение.  
---|---  
[NextRequestPending](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_NextRequestPending.htm)|
Возвращает флаг, показывающий, необходимо ли выполнить следующее сохранение.  
[ProcessesAwaitingRemoval](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_ProcessesAwaitingRemoval.htm)|
Возвращает список процессов, ожидающих завершения.  
## __Методы
[AddActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_AddActiveTaskAsync.htm)|
Добавляет задание с указанным идентификатором в список активных.  
---|---  
[DecrementCounterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_DecrementCounterAsync.htm)|
Уменьшает текущее значение счётчика на заданное значение decrementValue. Если
текущее значение становится не больше нуля, то счётчик удаляется.  
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
[GetActiveTasksAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_GetActiveTasksAsync.htm)|
Возвращает список идентификаторов активных заданий.  
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
[InitCounterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_InitCounterAsync.htm)|
Инициализирует счётчик с заданным номером с указанием начального значения.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NotifyNextRequestPending](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_NotifyNextRequestPending.htm)|
Уведомляет WorkflowAPI о необходимости выполнения следующего сохранения.  
[RemoveActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_RemoveActiveTaskAsync.htm)|
Удяляет задание с указанным идентификатором из списка активных. В случае
неудачи будет выброшено исключение  
[RemoveCounterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_RemoveCounterAsync.htm)|
Удаляет счётчик с заданным номером, уникальным для подпроцесса.  
[SendTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_SendTaskAsync.htm)|
Отправляет задание.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryRemoveActiveTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_WorkflowAPIBridge_TryRemoveActiveTaskAsync.htm)|
Удаляет задание с указанным идентификатором из списка активных.  
## __Методы расширения
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
