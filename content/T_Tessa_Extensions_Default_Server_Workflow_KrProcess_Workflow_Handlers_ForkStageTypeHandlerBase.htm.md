# ForkStageTypeHandlerBase - класс
Абстрактный базовый класс для обработчиков действий взаимодействующих с
вложенными процессами.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ForkStageTypeHandlerBase : StageTypeHandlerBase
VB __Копировать
     Public MustInherit Class ForkStageTypeHandlerBase
    	Inherits StageTypeHandlerBase
C++ __Копировать
     public ref class ForkStageTypeHandlerBase abstract : public StageTypeHandlerBase
F# __Копировать
     [<AbstractClassAttribute>]
    type ForkStageTypeHandlerBase = 
        class
            inherit StageTypeHandlerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm) __ ForkStageTypeHandlerBase
Derived
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.ForkManagementStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkManagementStageTypeHandler.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.Handlers.ForkStageTypeHandler](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandler.htm)
##  __Конструкторы
[ForkStageTypeHandlerBase](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase__ctor.htm)|
Инициализирует новый экземпляр класса ForkStageTypeHandlerBase  
---|---  
##  __Методы
[AfterPostprocessingAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_AfterPostprocessingAsync.htm)|
Метод, вызываемый после вызова скрипта постобработки этапа.  
(Переопределяет
[StageTypeHandlerBase.AfterPostprocessingAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_AfterPostprocessingAsync.htm))  
---|---  
[BeforeInitializationAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_BeforeInitializationAsync.htm)|
Метод, вызываемый перед вызовом скрипта инициализации этапа.  
(Переопределяет
[StageTypeHandlerBase.BeforeInitializationAsync(IStageTypeHandlerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_BeforeInitializationAsync.htm))  
[EnumerateSecondaryProcessRows](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_EnumerateSecondaryProcessRows.htm)|
Возвращает перечисление коллекций ключ-значение содержащих значения элементов
из
[Synthetic](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrForkSecondaryProcessesSettingsVirtual_Synthetic.htm).  
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
[GetProcessInfo](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_GetProcessInfo.htm)|
Возвращает коллекцию ключ-значение содержащую информацию по вложенному
запускаемому процессу.  
[GetProcessInfos](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_GetProcessInfos.htm)|
Возвращает коллекцию ключ-значение: ключ - идентификатор строки в коллекции
[Synthetic](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrForkSecondaryProcessesSettingsVirtual_Synthetic.htm)
представленный в строковом представлении по формату
[ForkSecondaryProcessesRowIDFormat](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_ForkSecondaryProcessesRowIDFormat.htm);
значение - коллекцию ключ-значение содержащая информацию по вложенному
запускаемому процессу, тип значения [IDictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2),
где TKey - [String](https://learn.microsoft.com/dotnet/api/system.string),
TValue - [Object](https://learn.microsoft.com/dotnet/api/system.object).  
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
[HandleStageInterruptAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageInterruptAsync.htm)|
Обработка отмены этапа. Данный метод должен утилизировать все используемые
этапом ресурсы.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
[HandleStageStartAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase_HandleStageStartAsync.htm)|
Обработка старта этапа.  
(Унаследован от
[StageTypeHandlerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageTypeHandlerBase.htm))  
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
[SetProcessInfo](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_SetProcessInfo.htm)|
Устанавливает информацию по вложенному запускаемому процессу.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[BranchAdditionInfoFactory](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_BranchAdditionInfoFactory.htm)|
Фабрика объектов
[BranchAdditionInfo](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_BranchAdditionInfo.htm).  
---|---  
[BranchRemovalInfoFactory](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_BranchRemovalInfoFactory.htm)|
Фабрика объектов
[BranchRemovalInfo](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_BranchRemovalInfo.htm).  
[ForkSecondaryProcessesRowIDFormat](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_ForkStageTypeHandlerBase_ForkSecondaryProcessesRowIDFormat.htm)|
Формат представления идентификатора строки в коллекции
[Synthetic](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrForkSecondaryProcessesSettingsVirtual_Synthetic.htm).  
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
