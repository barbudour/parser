# TypedTaskStageTypeHandler - класс
Обработчик этапа
[TypedTaskDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptors_TypedTaskDescriptor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class TypedTaskStageTypeHandler : StageTypeHandlerBase
VB __Копировать
     Public Class TypedTaskStageTypeHandler
    	Inherits StageTypeHandlerBase
C++ __Копировать
     public ref class TypedTaskStageTypeHandler : public StageTypeHandlerBase
F# __Копировать
     type TypedTaskStageTypeHandler = 
        class
            inherit StageTypeHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __ TypedTaskStageTypeHandler
##  __Конструкторы
[TypedTaskStageTypeHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler__ctor.htm)|
Инициализирует новый экземпляр класса TypedTaskStageTypeHandler.  
---|---  
## __Свойства
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_CardCache.htm)|
Возвращает потокобезопасный кэш с карточками и дополнительными настройками.  
---|---  
[CompilationCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_CompilationCache.htm)|
Возвращает кэш содержащий результаты компиляции.  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_DbScope.htm)|
Возвращает объект для взаимодействия с базой данных.  
[KrScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_KrScope.htm)|
Возвращает объект предоставляющий методы для работы с текущим контекстом
расширений типового расширения и использования разделяемых объектов карточек.  
[NotificationManager](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_NotificationManager.htm)|
Возвращает объект для отправки уведомлений, построенных по карточке
уведомления.  
[RoleRepository](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_RoleRepository.htm)|
Возвращает репозиторий для управления ролевой моделью.  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_Session.htm)|
Возвращает сессию пользователя.  
[TasksRevoker](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_TasksRevoker.htm)|
Возвращает объект выполняющий отзыв заданий этапа.  
[UnityContainer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_UnityContainer.htm)|
Возвращает unity-контейнер.  
## __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
(Переопределяет
[StageTypeHandlerBase.BeforeInitializationAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_BeforeInitializationAsync.htm))  
[CompleteStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_CompleteStageAsync.htm)|
Обрабатывает завершение этапа.  
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
[HandleStageInterruptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
(Переопределяет
[StageTypeHandlerBase.HandleStageInterruptAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageInterruptAsync.htm))  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_HandleStageStartAsync.htm)|
Обработка старта этапа.  
(Переопределяет
[StageTypeHandlerBase.HandleStageStartAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm))  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_HandleTaskCompletionAsync.htm)|
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
[SendTaskAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_SendTaskAsync.htm)|
Отправляет новое задание.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[ActiveTasksCount](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_ActiveTasksCount.htm)|
Ключ по которому в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
содержится общее число заданий. Тип значения:
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
---|---  
[AfterTaskMethodDescriptor](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_AfterTaskMethodDescriptor.htm)|
Дескриптор метода "После завершения задания".  
[CompleteStageCountdown](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler_CompleteStageCountdown.htm)|
Ключ по которому в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
содержится число заданий которое ещё надо отозвать. Тип значения:
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
