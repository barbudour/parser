# SubtaskStageTypeHandler - класс
Представляет абстрактный обработчик этапа поддерживающий дочерние задания.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SubtaskStageTypeHandler : StageTypeHandlerBase
VB __Копировать
     Public MustInherit Class SubtaskStageTypeHandler
    	Inherits StageTypeHandlerBase
C++ __Копировать
     public ref class SubtaskStageTypeHandler abstract : public StageTypeHandlerBase
F# __Копировать
     [<AbstractClassAttribute>]
    type SubtaskStageTypeHandler = 
        class
            inherit StageTypeHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __ SubtaskStageTypeHandler
Derived
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.ApprovalStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ApprovalStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.SigningStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler.htm)
##  __Конструкторы
[SubtaskStageTypeHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler__ctor.htm)|
Инициализирует новый экземпляр класса SubtaskStageTypeHandler  
---|---  
##  __Свойства
[CalendarService](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_CalendarService.htm)|  
---|---  
[CardGetStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_CardGetStrategy.htm)|  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_CardMetadata.htm)|  
[CommentNameField](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_CommentNameField.htm)|
Возвращает название поля содержащего комментарий к заданию.  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_DbScope.htm)|  
[KrScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_KrScope.htm)|  
[NotificationManager](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_NotificationManager.htm)|  
[RoleRepository](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RoleRepository.htm)|  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_Session.htm)|  
[TasksRevoker](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_TasksRevoker.htm)|  
## __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
(Переопределяет
[StageTypeHandlerBase.BeforeInitializationAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_BeforeInitializationAsync.htm))  
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
[GetCycle](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_GetCycle.htm)|
Возвращает номер текущего цикла согласования из
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess_InfoStorage.htm).  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSubTaskTypesToRevoke](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_GetSubTaskTypesToRevoke.htm)|
Возвращает массив идентификаторов типов дочерних заданий которые должны быть
завершены.  
[GetTaskDigest](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_GetTaskDigest.htm)|
Возвращает стандартный дайджест задания созданный по информации из контекста
обработчика этапа.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HandleResurrectionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleResurrectionAsync.htm)|
Обработка восстановления процесса.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleSignalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleSignalAsync.htm)|
Обработка сигнала.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleStageInterruptAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
(Переопределяет
[StageTypeHandlerBase.HandleStageInterruptAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageInterruptAsync.htm))  
[HandleStageInterruptAsync(IStageTypeHandlerContext, Guid[],
Action<CardTask>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_HandleStageInterruptAsync_1.htm)|
Обрабатывает отмену этапа.  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm)|
Обработка старта этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_HandleTaskCompletionAsync.htm)|
Обработка завершения задания.  
(Переопределяет
[StageTypeHandlerBase.HandleTaskCompletionAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskCompletionAsync.htm))  
[HandleTaskDelegateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_HandleTaskDelegateAsync.htm)|
Обрабатывает делегирование задания.  
[HandleTaskReinstateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskReinstateAsync.htm)|
Обработка возврата задания на роль.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[IsInterjected](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_IsInterjected.htm)|
Возвращает значение, показывающее,  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RevokeSubTasksAsync(IStageTypeHandlerContext,
CardTask)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RevokeSubTasksAsync.htm)|
Завершает дочерние задания типов возвращаемых
[GetSubTaskTypesToRevoke()](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_GetSubTaskTypesToRevoke.htm).  
[RevokeSubTasksAsync(IStageTypeHandlerContext, CardTask, Guid[],
Action<CardTask>,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RevokeSubTasksAsync_1.htm)|
Завершает дочерние задания указанных типов.  
[RevokeTasksAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RevokeTasksAsync.htm)|
Завершает задания указанных типов.  
[RevokeTasksCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RevokeTasksCoreAsync.htm)|
Завершает задания имеющие идентификаторы из указанного списка.  
[SendSubTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_SendSubTaskAsync.htm)|
Отправляет дочернее к указанному задание.  
[SendTaskAsync(IStageTypeHandlerContext, Guid, String, Performer,
Func<CardTask, CancellationToken, ValueTask>,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_SendTaskAsync_1.htm)|
Отправляет задание указанного типа.  
[SendTaskAsync(IStageTypeHandlerContext, Guid, String, Guid, String,
Func<CardTask, CancellationToken, ValueTask>,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_SendTaskAsync.htm)|
Отправляет задание указанного типа.  
[StageCompleted](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_StageCompleted.htm)|
Обрабатывает завершение этапа.  
[SubTaskCompleted](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_SubTaskCompleted.htm)|
Обрабатывает завершение дочерних заданий.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[Interjected](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_Interjected.htm)|  
---|---  
[ResultAction](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_ResultAction.htm)|  
[ResultKeepStates](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_ResultKeepStates.htm)|  
[ResultTransitTo](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_ResultTransitTo.htm)|  
[SubtaskCount](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_SubtaskCount.htm)|  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)
