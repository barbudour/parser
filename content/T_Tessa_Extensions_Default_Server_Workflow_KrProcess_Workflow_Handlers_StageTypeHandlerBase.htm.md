# StageTypeHandlerBase - класс
Представляет абстрактный обработчик этапа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class StageTypeHandlerBase : IStageTypeHandler
VB __Копировать
     Public MustInherit Class StageTypeHandlerBase
    	Implements IStageTypeHandler
C++ __Копировать
     public ref class StageTypeHandlerBase abstract : IStageTypeHandler
F# __Копировать
     [<AbstractClassAttribute>]
    type StageTypeHandlerBase = 
        class
            interface IStageTypeHandler
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StageTypeHandlerBase
Derived
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.AcquaintanceStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_AcquaintanceStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.AddFromTemplateStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_AddFromTemplateStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.ChangeStateStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ChangeStateStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.CreateCardStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_CreateCardStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.DeregistrationStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DeregistrationStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.DialogStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_DialogStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.EditStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_EditStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.ForkStageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.HistoryManagementStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_HistoryManagementStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.NotificationStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_NotificationStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.PartialGroupRecalcStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_PartialGroupRecalcStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.ProcessManagementStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ProcessManagementStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.RegistrationStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_RegistrationStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.ResolutionStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ResolutionStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.ScriptStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ScriptStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.SubtaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_SubtaskStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.TypedTaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_TypedTaskStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.UniversalTaskStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_UniversalTaskStageTypeHandler.htm)
Подробнее __Less __
Implements
    [IStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_IStageTypeHandler.htm)
##  __Конструкторы
[StageTypeHandlerBase](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase__ctor.htm)|
Инициализирует новый экземпляр класса StageTypeHandlerBase  
---|---  
##  __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
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
[HandleSignalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleSignalAsync.htm)|
Обработка сигнала.  
[HandleStageInterruptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm)|
Обработка старта этапа.  
[HandleTaskCompletionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskCompletionAsync.htm)|
Обработка завершения задания.  
[HandleTaskReinstateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleTaskReinstateAsync.htm)|
Обработка возврата задания на роль.  
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
