# StageTaskRevokerContext - класс
Контекст
[IStageTasksRevoker](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevoker.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class StageTaskRevokerContext : IStageTasksRevokerContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class StageTaskRevokerContext
    	Implements IStageTasksRevokerContext, IExtensionContext
C++ __Копировать
     public ref class StageTaskRevokerContext sealed : IStageTasksRevokerContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type StageTaskRevokerContext = 
        class
            interface IStageTasksRevokerContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StageTaskRevokerContext
Implements
    [IStageTasksRevokerContext](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTasksRevokerContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[StageTaskRevokerContext](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTaskRevokerContext__ctor.htm)|
Инициализирует новый экземпляр класса StageTaskRevokerContext.  
---|---  
## __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTaskRevokerContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTaskRevokerContext_CardID.htm)|
Идентификатор карточки.  
[Context](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTaskRevokerContext_Context.htm)|
Контекст обработчика этапа.  
[OptionID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTaskRevokerContext_OptionID.htm)|
Опционально указывается вариант завершения. Если не указан, то все задания
отзываются с вариантом завершения
[Cancel](F_Tessa_Extensions_Default_Shared_DefaultCompletionOptions_Cancel.htm)  
[RemoveFromActive](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTaskRevokerContext_RemoveFromActive.htm)|
Удалить задание из активных.  
[TaskID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTaskRevokerContext_TaskID.htm)|
Идентификатор задания для отзыва, если отзывается только одно задание.  
[TaskIDs](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTaskRevokerContext_TaskIDs.htm)|
Список идентификаторов заданий для отзыва  
[TaskModificationAction](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTaskRevokerContext_TaskModificationAction.htm)|
Действие перед завершением задания.  
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
