# EditStageTypeHandler - класс
Обработчик этапа
[EditDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptors_EditDescriptor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class EditStageTypeHandler : StageTypeHandlerBase
VB __Копировать
     Public Class EditStageTypeHandler
    	Inherits StageTypeHandlerBase
C++ __Копировать
     public ref class EditStageTypeHandler : public StageTypeHandlerBase
F# __Копировать
     type EditStageTypeHandler = 
        class
            inherit StageTypeHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __ EditStageTypeHandler
##  __Конструкторы
[EditStageTypeHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler__ctor.htm)|
Инициализирует новый экземпляр класса
[DeregistrationStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler.htm).  
---|---  
## __Свойства
[CalendarService](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_CalendarService.htm)|
Возвращает объект предоставляющий методы для взаимодействия с бизнес
календарём.  
---|---  
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_CardCache.htm)|
Возвращает потокобезопасный кэш с карточками и дополнительными настройками.  
[KrScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_KrScope.htm)|
Возвращает объект предоставляющий методы для работы с текущим контекстом
расширений типового расширения и использования разделяемых объектов карточек.  
[NotificationManager](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_NotificationManager.htm)|
Возвращает объект для отправки уведомлений, построенных по карточке
уведомления.  
[RoleRepository](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_RoleRepository.htm)|
Возвращает репозиторий для управления ролевой моделью.  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_Session.htm)|
Возвращает сессию пользователя.  
[TasksRevoker](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_TasksRevoker.htm)|
Возвращает объект выполняющий отзыв заданий этапа.  
## __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_BeforeInitializationAsync.htm)|
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
[HandleResurrectionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleResurrectionAsync.htm)|
Обработка восстановления процесса.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleSignalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleSignalAsync.htm)|
Обработка сигнала.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleStageInterruptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
(Переопределяет
[StageTypeHandlerBase.HandleStageInterruptAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageInterruptAsync.htm))  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_HandleStageStartAsync.htm)|
Обработка старта этапа.  
(Переопределяет
[StageTypeHandlerBase.HandleStageStartAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm))  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_HandleTaskCompletionAsync.htm)|
Обработка завершения задания.  
(Переопределяет
[StageTypeHandlerBase.HandleTaskCompletionAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskCompletionAsync.htm))  
[HandleTaskReinstateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskReinstateAsync.htm)|
Обработка возврата задания на роль.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[StartApproval](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_StartApproval.htm)|
Начинает новый цикл согласования.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TransitFromDifferentGroup](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_TransitFromDifferentGroup.htm)|
Возвращает значение, показывающее, выполнялся ли предыдущий этап из другой
группы этапов или карточки.  
[TryIncrementCycle](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_TryIncrementCycle.htm)|
Увеличивает номер цикла согласования, если это разрешено настроками этапа.  
## __Поля
[ReturnToStage](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler_ReturnToStage.htm)|
Имя ключа, по которому в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
содержится идентификатор этапа на который необходимо выполнить переход после
завершения этапа "Доработка". Используется при возврате на этап согласование
или подписание после доработки автором. Тип значения:
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
---|---  
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
