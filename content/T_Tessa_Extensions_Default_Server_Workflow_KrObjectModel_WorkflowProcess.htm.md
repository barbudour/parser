# WorkflowProcess - класс
Объектная модель процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel](N_Tessa_Extensions_Default_Server_Workflow_KrObjectModel.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkflowProcess : IEquatable<WorkflowProcess>, 
    	ISealable
VB __Копировать
     Public NotInheritable Class WorkflowProcess
    	Implements IEquatable(Of WorkflowProcess), ISealable
C++ __Копировать
     public ref class WorkflowProcess sealed : IEquatable<WorkflowProcess^>, 
    	ISealable
F# __Копировать
     [<SealedAttribute>]
    type WorkflowProcess = 
        class
            interface IEquatable<WorkflowProcess>
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowProcess
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<WorkflowProcess>, [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[WorkflowProcess](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess__ctor.htm)|
Инициализирует новый экземпляр класса WorkflowProcess.  
---|---  
## __Свойства
[AffectMainCardVersionWhenStateChanged](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AffectMainCardVersionWhenStateChanged.htm)|
Возвращает или задаёт значение, показывающее, что версию основной карточки
должна быть изменена, если состояние документа изменилось.  
---|---  
[AffectMainCardVersionWhenStateChangedTimestamp](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AffectMainCardVersionWhenStateChangedTimestamp.htm)|
Возвращает штамп времени изменения флага версии основной карточки.  
[Author](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_Author.htm)|
Возвращает или задаёт автора (инициатора) основного процесса.  
[AuthorComment](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AuthorComment.htm)|
Возвращает или задаёт комментарий автора (инициатора) основного процесса.  
[AuthorCommentTimestamp](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AuthorCommentTimestamp.htm)|
Возвращает штамп времени изменения комментария автора (инициатора) основного
процесса.  
[AuthorCurrentProcess](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AuthorCurrentProcess.htm)|
Возвращает или задаёт автора (инициатора) текущего процесса. Значение
совпадает с
[Author](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_Author.htm),
если текущий процесс является основным.  
[AuthorCurrentProcessTimestamp](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AuthorCurrentProcessTimestamp.htm)|
Возвращает штамп времени изменения автора (инициатора) текущего процесса.  
[AuthorTimestamp](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AuthorTimestamp.htm)|
Возвращает штамп времени изменения автора (инициатора) основного процесса.  
[CurrentApprovalStageRowID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_CurrentApprovalStageRowID.htm)|
Возвращает идентификатор текущего активного этапа процесса.  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_Info.htm)|
Возвращает дополнительную информацию по процессу.  
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_InfoStorage.htm)|
Возвращает хранилище с дополнительной информацией по процессу.  
[InitialWorkflowProcess](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_InitialWorkflowProcess.htm)|
Возвращает состояние процесса до выполнения обработчиков этапов.  
[IsSealed](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
[MainProcessInfo](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_MainProcessInfo.htm)|
Возвращает дополнительную информация по родительскому процессу. Актуально для
вложенных, для родительского MainProcessInfo = Info.  
[MainProcessInfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_MainProcessInfoStorage.htm)|
Возвращает хранилище с дополнительной информацией по родительскому процессу.
Актуально для вложенных, для родительского MainProcessInfo = Info.  
[NestedProcessID](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_NestedProcessID.htm)|
Возвращает идентификатор вложенного процесса.  
[ProcessOwner](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_ProcessOwner.htm)|
Возвращает или задаёт владельца основного процесса.  
[ProcessOwnerCurrentProcess](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_ProcessOwnerCurrentProcess.htm)|
Возвращает или задаёт владельца текущего процесса. Значение совпадает с
[ProcessOwner](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_ProcessOwner.htm),
если текущий процесс является основным.  
[ProcessOwnerCurrentProcessTimestamp](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_ProcessOwnerCurrentProcessTimestamp.htm)|
Возвращает штамп времени изменения автора (инициатора) текущего процесса.  
[ProcessOwnerTimestamp](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_ProcessOwnerTimestamp.htm)|
Возвращает штамп времени изменения владельца основного процесса.  
[Stages](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_Stages.htm)|
Возвращает или задаёт коллекцию этапов процесса.  
[State](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_State.htm)|
Возвращает или задаёт состояние основного процесса.  
[StateTimestamp](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_StateTimestamp.htm)|
Возвращает штамп времени изменения состояния основного процесса.  
## __Методы
[CloneWithDedicatedStageGroup](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_CloneWithDedicatedStageGroup.htm)|
Создаёт частичную копию текущего объекта. Клонирует этапы входящие в группу с
указанным идентификатором.  
---|---  
[Equals(Object)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_Equals.htm)|
Determines whether the specified object is equal to the current object.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Equals(WorkflowProcess)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_Equals_1.htm)|
Indicates whether the current object is equal to another object of the same
type.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_GetHashCode.htm)|
Serves as the default hash function.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[Seal](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_Seal.htm)|
Защищает объект от изменений.  
[SetAffectMainCardVersionWhenStateChanged](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_SetAffectMainCardVersionWhenStateChanged.htm)|
Устанавливает флаг изменения версии документа при изменении состояния
документа. В общем случае необходимо использовать свойство
[AffectMainCardVersionWhenStateChanged](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AffectMainCardVersionWhenStateChanged.htm).  
[SetAuthor](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_SetAuthor.htm)|
Установить инициатора основного процесса. В общем случае необходимо
использовать свойство
[Author](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_Author.htm).  
[SetAuthorComment](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_SetAuthorComment.htm)|
Установить комментарий инициатора основного процесса. В общем случае
необходимо использовать свойство
[AuthorComment](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AuthorComment.htm).  
[SetAuthorCurrentProcess](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_SetAuthorCurrentProcess.htm)|
Установить инициатора текущего процесса. В общем случае необходимо
использовать свойство
[AuthorCurrentProcess](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_AuthorCurrentProcess.htm).  
[SetProcessOwner](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_SetProcessOwner.htm)|
Устанавливает владельца основного процесса. В общем случае необходимо
использовать свойство
[ProcessOwner](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_ProcessOwner.htm).  
[SetProcessOwnerCurrentProcess](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_SetProcessOwnerCurrentProcess.htm)|
Устанавливает владельца текущего процесса. В общем случае необходимо
использовать свойство
[ProcessOwnerCurrentProcess](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_ProcessOwnerCurrentProcess.htm).  
[SetState](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_SetState.htm)|
Устанавливает состояние основного процесса. В общем случае необходимо
использовать свойство
[State](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_State.htm).  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Операторы
[Equality(WorkflowProcess,
WorkflowProcess)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_op_Equality.htm)|  
---|---  
[Inequality(WorkflowProcess,
WorkflowProcess)](M_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_op_Inequality.htm)|  
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
[Tessa.Extensions.Default.Server.Workflow.KrObjectModel - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrObjectModel.htm)
