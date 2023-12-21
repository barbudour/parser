# KrProcessRunnerBase - класс
Абстрактный базовый класс раннера используемого для выполнения процессов
маршрутов документов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class KrProcessRunnerBase : IKrProcessRunner
VB __Копировать
     Public MustInherit Class KrProcessRunnerBase
    	Implements IKrProcessRunner
C++ __Копировать
     public ref class KrProcessRunnerBase abstract : IKrProcessRunner
F# __Копировать
     [<AbstractClassAttribute>]
    type KrProcessRunnerBase = 
        class
            interface IKrProcessRunner
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessRunnerBase
Derived
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.KrAsyncProcessRunner](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrAsyncProcessRunner.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.KrSyncProcessRunner](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrSyncProcessRunner.htm)
Implements
    [IKrProcessRunner](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_IKrProcessRunner.htm)
##  __Конструкторы
[KrProcessRunnerBase](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase__ctor.htm)|
Инициализирует новый экземпляр класса KrProcessRunnerBase  
---|---  
##  __Свойства
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CardCache.htm)|  
---|---  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CardMetadata.htm)|  
[CompilationCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CompilationCache.htm)|  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_DbScope.htm)|  
[Executor](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_Executor.htm)|  
[ObjectModelMapper](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ObjectModelMapper.htm)|  
[ProcessCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessCache.htm)|  
[ProcessContainer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessContainer.htm)|  
[RunnerMode](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunnerMode.htm)|  
[RunnerProvider](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunnerProvider.htm)|  
[Scope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_Scope.htm)|  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_Session.htm)|  
[SqlExecutor](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_SqlExecutor.htm)|  
[StageSerializer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_StageSerializer.htm)|  
[StateMachine](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_StateMachine.htm)|  
[TypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TypesCache.htm)|  
[UnityContainer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_UnityContainer.htm)|  
## __Методы
[AddTrace](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_AddTrace.htm)|
Добавляет новую запись в список истории выполнения процесса.  
---|---  
[AssertRunnerMode](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_AssertRunnerMode.htm)|  
[CreateRuntimeStageInstanceAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CreateRuntimeStageInstanceAsync.htm)|  
[CreateStageGroupInstanceAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CreateStageGroupInstanceAsync.htm)|  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteScriptConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ExecuteScriptConditionAsync.htm)|
Выполняет C#-условие выполнения маршрута для единицы выполнения.  
[ExecuteSQLConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ExecuteSQLConditionAsync.htm)|
Выполняет SQL-условие времени построения маршрута для единицы выполнения.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FinalizeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_FinalizeAsync.htm)|
Выполняет действия после завершения обработки процесса.  
[GetCurrentStage](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_GetCurrentStage.htm)|
Возвращает текущий активный этап процесса.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNextStage](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_GetNextStage.htm)|  
[GetSubsequentStages](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_GetSubsequentStages.htm)|  
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
[PartialGroupRecalcAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_PartialGroupRecalcAsync.htm)|  
[PrepareAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_PrepareAsync.htm)|
Выполняет действия перед выполнением процесса.  
[ProcessCurrentStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessCurrentStageAsync.htm)|  
[ProcessGlobalSignalsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessGlobalSignalsAsync.htm)|  
[ProcessNextStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessNextStageAsync.htm)|  
[ProcessStageHandlerResultAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessStageHandlerResultAsync.htm)|
Обрабатывает результат выполнения обработчика этапа.  
[ProcessStateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessStateAsync.htm)|  
[RecalcRoleAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RecalcRoleAsync.htm)|  
[RecalcSqlRolesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RecalcSqlRolesAsync.htm)|  
[RunAfterAsync(IKrExecutionUnit)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunAfterAsync.htm)|
Выполняет сценарий постобработки для единицы выполнения.  
[RunAfterAsync(Stage,
IKrProcessRunnerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunAfterAsync_1.htm)|  
[RunAfterStageGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunAfterStageGroupAsync.htm)|  
[RunAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunAsync.htm)|
Начинает обработку процесса информация о котором задана в контексте.  
[RunBeforeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunBeforeAsync.htm)|
Выполняет сценарий инициализации для единицы выполнения.  
[RunConditionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunConditionsAsync.htm)|
Выполняет условия времени выполнения маршрута для единицы выполнения.  
[RunInDifferentCardContextAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunInDifferentCardContextAsync.htm)|  
[RunInternalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunInternalAsync.htm)|
Обрабатывает процесс, информация о котором задана в контексте.  
[RunNextStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunNextStageAsync.htm)|  
[SafeRunAsync(IKrProcessRunnerContext, Func<IKrExecutionUnit, Task<Boolean>>,
IKrExecutionUnit)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_SafeRunAsync.htm)|
Выполняет заданное действие для единицы выполнения.  
[SafeRunAsync(IKrProcessRunnerContext, Func<IKrExecutionUnit, Task>,
IKrExecutionUnit)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_SafeRunAsync_1.htm)|
Выполняет заданное действие для единицы выполнения.  
[SetAuthorAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_SetAuthorAsync.htm)|
Задаёт автора (инициатора) текущего процесса.  
[SetStageFinalState](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_SetStageFinalState.htm)|  
[StopEntireProcess](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_StopEntireProcess.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Transit(Stage, Boolean, Func<Stage, Boolean>,
IKrProcessRunnerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_Transit.htm)|
Выполняет переход к этапу удовлетворяющему заданное условие.  
[Transit(Stage, Boolean, Stage,
IKrProcessRunnerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_Transit_1.htm)|
Выполняет переход на заданный этап.  
[TransitByIndex](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TransitByIndex.htm)|
Выполняет переход к этапу с заданным порядковым индексом.  
[TransitToStage](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TransitToStage.htm)|
Выполняет переход к этапу. Идентификатор этапа к которой должен быть выполнен
переход содержится в
[TransitionID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_TransitionID.htm).  
[TransitToStageGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TransitToStageGroupAsync.htm)|
Выполняет переход к группе этапов. Идентификатор группы этапов к которой
должен быть выполнен переход содержится в
[TransitionID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_TransitionID.htm).  
[TryResurrectStage](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TryResurrectStage.htm)|  
[TryStartStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TryStartStageAsync.htm)|  
[TryStartStageGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TryStartStageGroupAsync.htm)|
Возвращает следующий этап.  
[UpdateSingleSqlPerformer](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_UpdateSingleSqlPerformer.htm)|  
[UpdateSqlPerformers](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_UpdateSqlPerformers.htm)|  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
