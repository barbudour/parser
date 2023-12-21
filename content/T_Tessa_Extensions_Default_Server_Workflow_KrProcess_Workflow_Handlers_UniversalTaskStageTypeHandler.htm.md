# UniversalTaskStageTypeHandler - класс
Обработчик этапа
[UniversalTaskDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptors_UniversalTaskDescriptor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class UniversalTaskStageTypeHandler : StageTypeHandlerBase
VB __Копировать
     Public Class UniversalTaskStageTypeHandler
    	Inherits StageTypeHandlerBase
C++ __Копировать
     public ref class UniversalTaskStageTypeHandler : public StageTypeHandlerBase
F# __Копировать
     type UniversalTaskStageTypeHandler = 
        class
            inherit StageTypeHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __ UniversalTaskStageTypeHandler
##  __Конструкторы
[UniversalTaskStageTypeHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler__ctor.htm)|
Инициализирует новый экземпляр класса UniversalTaskStageTypeHandler.  
---|---  
## __Свойства
[CalendarService](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_CalendarService.htm)|
Возвращает объект предоставляющий методы для работы с бизнес календарём.  
---|---  
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_CardCache.htm)|
Возвращает потокобезопасный кэш с карточками и дополнительными настройками.  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_CardMetadata.htm)|
Возвращает метаинформацию, необходимую для использования типов карточек
совместно с пакетом карточек.  
[KrScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_KrScope.htm)|
Возвращает объект предоставляющий методы для работы с текущим контекстом
расширений типового расширения и использования разделяемых объектов карточек.  
[NotificationManager](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_NotificationManager.htm)|
Возвращает объект для отправки уведомлений, построенных по карточке
уведомления.  
[RoleRepository](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_RoleRepository.htm)|
Возвращает репозиторий для управления ролевой моделью.  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_Session.htm)|
Возвращает сессию пользователя.  
[TasksRevoker](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_TasksRevoker.htm)|
Возвращает объект выполняющий отзыв заданий этапа.  
## __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_BeforeInitializationAsync.htm)|
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
[HandleStageInterruptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
(Переопределяет
[StageTypeHandlerBase.HandleStageInterruptAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageInterruptAsync.htm))  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_HandleStageStartAsync.htm)|
Обработка старта этапа.  
(Переопределяет
[StageTypeHandlerBase.HandleStageStartAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm))  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_HandleTaskCompletionAsync.htm)|
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
[SendUniversalTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_SendUniversalTaskAsync.htm)|
Асинхронно отправляет настраиваемое задание.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[CompletedTasksCountKey](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_CompletedTasksCountKey.htm)|
Ключ по которому в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
содержится число завершённых заданий. Тип значения:
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
---|---  
[TasksKey](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_TasksKey.htm)|
Ключ по которому в InfoStorage хранится список завершённых заданий. Тип
значения:
[IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist), где
тип элемента -
System.Collections.Generic.IDictionary<[String](https://learn.microsoft.com/dotnet/api/system.string),[Object](https://learn.microsoft.com/dotnet/api/system.object)>
\- хранилище объекта [CardTask](T_Tessa_Cards_CardTask.htm).  
[TotalTasksCountKey](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler_TotalTasksCountKey.htm)|
Ключ по которому в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
содержится общее число заданий. Тип значения:
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
