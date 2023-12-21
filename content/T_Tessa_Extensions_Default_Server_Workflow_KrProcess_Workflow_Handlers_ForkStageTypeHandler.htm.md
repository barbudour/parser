# ForkStageTypeHandler - класс
Обработчик этапа
[ForkDescriptor](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_StageTypeDescriptors_ForkDescriptor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class ForkStageTypeHandler : ForkStageTypeHandlerBase
VB __Копировать
     Public Class ForkStageTypeHandler
    	Inherits ForkStageTypeHandlerBase
C++ __Копировать
     public ref class ForkStageTypeHandler : public ForkStageTypeHandlerBase
F# __Копировать
     type ForkStageTypeHandler = 
        class
            inherit ForkStageTypeHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __[ForkStageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase.htm) __ ForkStageTypeHandler
##  __Конструкторы
[ForkStageTypeHandler](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler__ctor.htm)|
Инициализирует новый экземпляр класса ForkStageTypeHandler.  
---|---  
## __Свойства
[CompilationCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_CompilationCache.htm)|
Возвращает кэш содержащий результаты компиляции.  
---|---  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_DbScope.htm)|
Возвращает объект для взаимодействия с базой данных.  
[ProcessCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_ProcessCache.htm)|
Возвращает кэш с данными из карточек шаблонов этапов.  
[ProcessLauncher](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_ProcessLauncher.htm)|
Возвращает загрузчик процессов.  
[UnityContainer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_UnityContainer.htm)|
Возвращает Unity-контейнер.  
## __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Унаследован от
[ForkStageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase.htm))  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
(Унаследован от
[ForkStageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase.htm))  
[CheckSecondaryProcessAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_CheckSecondaryProcessAsync.htm)|
Проверяет, что вторичный процесс, имеющий указанный идентификатор, существует
и имеет правильный тип, т.е. не является асинхронным, если текущий основной
процесс является синхронным.  
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
[GetProcessIDsOfNestedsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_GetProcessIDsOfNestedsAsync.htm)|
Возвращает коллекцию идентификаторов завершаемых вложенных процессов.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HandleBranchAdditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_HandleBranchAdditionAsync.htm)|
Обрабатывает создание ветки.  
[HandleBranchCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_HandleBranchCompletionAsync.htm)|
Обрабатывает завершение ветки.  
[HandleBranchRemovalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_HandleBranchRemovalAsync.htm)|
Обрабатывает удаление ветки.  
[HandleResurrectionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleResurrectionAsync.htm)|
Обработка восстановления процесса.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleSignalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_HandleSignalAsync.htm)|
Обработка сигнала.  
(Переопределяет
[StageTypeHandlerBase.HandleSignalAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleSignalAsync.htm))  
[HandleStageInterruptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
(Переопределяет
[StageTypeHandlerBase.HandleStageInterruptAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageInterruptAsync.htm))  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_HandleStageStartAsync.htm)|
Обработка старта этапа.  
(Переопределяет
[StageTypeHandlerBase.HandleStageStartAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm))  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskCompletionAsync.htm)|
Обработка завершения задания.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleTaskReinstateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskReinstateAsync.htm)|
Обработка возврата задания на роль.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ProcessKeepBranchesAliveAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_ProcessKeepBranchesAliveAsync.htm)|
Обрабатывает завершение веток этапа при завершении одной из них.  
[RunScriptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_RunScriptAsync.htm)|
Выполняет сценарий после завершения ветки.  
[SetCompleted](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_SetCompleted.htm)|
Устанавливает признак показывающий, что вложенный процесс завершён.  
[StartNestedProcessesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_StartNestedProcessesAsync.htm)|
Запускает новый вложенный процесс.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[AfterNestedMethodDescriptor](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_AfterNestedMethodDescriptor.htm)|
Дескриптор метода "После завершения ветки".  
---|---  
[BranchInfoFactory](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_BranchInfoFactory.htm)|
Фабрика объектов
[ForkStageTypeHandler.BranchInfo](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_BranchInfo.htm).  
[PendingProcesses](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler_PendingProcesses.htm)|
Ключ, по которому в
[InfoStorage](P_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_Stage_InfoStorage.htm)
содержится коллекция объектов содержазих информацию по веткам этапа
"Ветвление".  
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
