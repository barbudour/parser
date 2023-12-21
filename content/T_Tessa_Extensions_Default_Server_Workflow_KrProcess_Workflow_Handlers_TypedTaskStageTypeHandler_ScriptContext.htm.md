# TypedTaskStageTypeHandler.ScriptContext - класс
Тип параметра метода сценария "После завершения задания".
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class ScriptContext
VB __Копировать
     Public Class ScriptContext
C++ __Копировать
     public ref class ScriptContext
F# __Копировать
     type ScriptContext = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TypedTaskStageTypeHandler.ScriptContext
##  __Конструкторы
[TypedTaskStageTypeHandler.ScriptContext](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_ScriptContext__ctor.htm)|
Инициализирует новый экземпляр класса TypedTaskStageTypeHandler.ScriptContext.  
---|---  
## __Свойства
[CompleteStage](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_ScriptContext_CompleteStage.htm)|
Возвращает или задаёт значение, показывающее, что этап должен быть немедленно
завершён, активные задания, при этом, будут отозваны.  
---|---  
[Task](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_ScriptContext_Task.htm)|
Возвращает завершаемое задание.  
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
[RevokeTaskAsync(Guid,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_ScriptContext_RevokeTaskAsync_1.htm)|
Отзывает задание с указанным идентификатором.  
[RevokeTaskAsync(IEnumerable<Guid>,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_ScriptContext_RevokeTaskAsync.htm)|
Отзывает все задания с указанными идентификаторами.  
[SendTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_ScriptContext_SendTaskAsync.htm)|
Отправляет новое задание.  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
