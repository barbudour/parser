# SigningStageTypeHandler - класс
Обработчик этапа
[SigningDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptors_SigningDescriptor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class SigningStageTypeHandler : SubtaskStageTypeHandler
VB __Копировать
     Public Class SigningStageTypeHandler
    	Inherits SubtaskStageTypeHandler
C++ __Копировать
     public ref class SigningStageTypeHandler : public SubtaskStageTypeHandler
F# __Копировать
     type SigningStageTypeHandler = 
        class
            inherit SubtaskStageTypeHandler
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm) __ SigningStageTypeHandler
##  __Конструкторы
[SigningStageTypeHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler__ctor.htm)|
Инициализирует новый экземпляр класса SigningStageTypeHandler.  
---|---  
## __Свойства
[CalendarService](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_CalendarService.htm)|  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
---|---  
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_CardCache.htm)|
Возвращает или задаёт потокобезопасный кэш с карточками и дополнительными
настройками.  
[CardGetStrategy](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_CardGetStrategy.htm)|  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_CardMetadata.htm)|  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[CommentNameField](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_CommentNameField.htm)|
Возвращает название поля содержащего комментарий к заданию.  
(Переопределяет
[SubtaskStageTypeHandler.CommentNameField](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_CommentNameField.htm))  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_DbScope.htm)|  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[KrScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_KrScope.htm)|  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[NotificationManager](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_NotificationManager.htm)|  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[RoleRepository](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RoleRepository.htm)|  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_Session.htm)|  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[TasksRevoker](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_TasksRevoker.htm)|  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
##  __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[CompleteAdditionalApprovalTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_CompleteAdditionalApprovalTaskAsync.htm)|
Обрабатывает завершение задания дополнительного согласования.  
[CompleteSigningTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_CompleteSigningTaskAsync.htm)|
Обрабатывает завершение задания подписания.  
[DeclineAndCompleteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_DeclineAndCompleteAsync.htm)|
Обрабатывает отказ в подписании.  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSubTaskTypesToRevoke](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_GetSubTaskTypesToRevoke.htm)|
Возвращает массив идентификаторов типов дочерних заданий которые должны быть
завершены.  
(Переопределяет
[SubtaskStageTypeHandler.GetSubTaskTypesToRevoke()](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_GetSubTaskTypesToRevoke.htm))  
[GetTaskDigest](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_GetTaskDigest.htm)|
Возвращает стандартный дайджест задания созданный по информации из контекста
обработчика этапа.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
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
[HandleStageInterruptAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
(Переопределяет
[SubtaskStageTypeHandler.HandleStageInterruptAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_HandleStageInterruptAsync.htm))  
[HandleStageInterruptAsync(IStageTypeHandlerContext, Guid[],
Action<CardTask>)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_HandleStageInterruptAsync_1.htm)|
Обрабатывает отмену этапа.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_HandleStageStartAsync.htm)|
Обработка старта этапа.  
(Переопределяет
[StageTypeHandlerBase.HandleStageStartAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm))  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_HandleTaskCompletionAsync.htm)|
Обработка завершения задания.  
(Переопределяет
[SubtaskStageTypeHandler.HandleTaskCompletionAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_HandleTaskCompletionAsync.htm))  
[HandleTaskDelegateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_HandleTaskDelegateAsync.htm)|
Обрабатывает делегирование задания.  
(Переопределяет
[SubtaskStageTypeHandler.HandleTaskDelegateAsync(IStageTypeHandlerContext,
CardTask)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_HandleTaskDelegateAsync.htm))  
[HandleTaskReinstateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskReinstateAsync.htm)|
Обработка возврата задания на роль.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RevokeSubTasksAsync(IStageTypeHandlerContext,
CardTask)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_RevokeSubTasksAsync.htm)|
Завершает дочерние задания типов возвращаемых
[GetSubTaskTypesToRevoke()](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_GetSubTaskTypesToRevoke.htm).  
(Переопределяет
[SubtaskStageTypeHandler.RevokeSubTasksAsync(IStageTypeHandlerContext,
CardTask)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RevokeSubTasksAsync.htm))  
[RevokeSubTasksAsync(IStageTypeHandlerContext, CardTask, Guid[],
Action<CardTask>,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RevokeSubTasksAsync_1.htm)|
Завершает дочерние задания указанных типов.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[RevokeTasksAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RevokeTasksAsync.htm)|
Завершает задания указанных типов.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[RevokeTasksCoreAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_RevokeTasksCoreAsync.htm)|
Завершает задания имеющие идентификаторы из указанного списка.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[SendAdditionalApprovalTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_SendAdditionalApprovalTaskAsync.htm)|
Отправляет задание дополнительного согласования.  
[SendSigningTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_SendSigningTaskAsync.htm)|
Отправляет задание подписания.  
[SendSubTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_SendSubTaskAsync.htm)|
Отправляет дочернее к указанному задание.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[SendTaskAsync(IStageTypeHandlerContext, Guid, String, Performer,
Func<CardTask, CancellationToken, ValueTask>,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_SendTaskAsync_1.htm)|
Отправляет задание указанного типа.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[SendTaskAsync(IStageTypeHandlerContext, Guid, String, Guid, String,
Func<CardTask, CancellationToken, ValueTask>,
Boolean)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_SendTaskAsync.htm)|
Отправляет задание указанного типа.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[SignAndCompleteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_SignAndCompleteAsync.htm)|
Обрабатывает подписание.  
[StageCompleted](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_StageCompleted.htm)|
Обрабатывает завершение этапа.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[StartAdditionalApprovalTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_StartAdditionalApprovalTaskAsync.htm)|
Обрабатывает создание заданий дополнительного согласования.  
[SubTaskCompleted](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler_SubTaskCompleted.htm)|
Обрабатывает завершение дочерних заданий.  
(Унаследован от
[SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[CurrentPerformerCount](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_CurrentPerformerCount.htm)|
Ключ по которому в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
содержится текущий порядковый номер исполнителя. Тип значения:
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
---|---  
[Disapproved](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_Disapproved.htm)|
Ключ по которому в InfoStorage содержится значение, показывающее наличие
несогласовавших - значение true. Тип значения:
[Nullable<T>](https://learn.microsoft.com/dotnet/api/system.nullable-1), где T
- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
[TotalPerformerCount](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SigningStageTypeHandler_TotalPerformerCount.htm)|
Ключ по которому в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
содержится общее число исполнителей. Тип значения:
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
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
