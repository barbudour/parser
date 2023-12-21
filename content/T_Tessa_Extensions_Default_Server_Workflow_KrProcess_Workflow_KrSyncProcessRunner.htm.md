# KrSyncProcessRunner - класс
Раннер используемый для выполнения синхронных процессов маршрутов документов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrSyncProcessRunner : KrProcessRunnerBase
VB __Копировать
     Public NotInheritable Class KrSyncProcessRunner
    	Inherits KrProcessRunnerBase
C++ __Копировать
     public ref class KrSyncProcessRunner sealed : public KrProcessRunnerBase
F# __Копировать
     [<SealedAttribute>]
    type KrSyncProcessRunner = 
        class
            inherit KrProcessRunnerBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm) __ KrSyncProcessRunner
##  __Конструкторы
[KrSyncProcessRunner](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrSyncProcessRunner__ctor.htm)|
Инициализирует новый экземпляр класса KrSyncProcessRunner  
---|---  
##  __Свойства
[CardCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CardCache.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
---|---  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CardMetadata.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[CompilationCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CompilationCache.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_DbScope.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[Executor](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_Executor.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[ObjectModelMapper](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ObjectModelMapper.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[ProcessCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessCache.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[ProcessContainer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessContainer.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RunnerMode](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrSyncProcessRunner_RunnerMode.htm)|  
(Переопределяет
[KrProcessRunnerBase.RunnerMode](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunnerMode.htm))  
[RunnerProvider](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunnerProvider.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[Scope](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_Scope.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_Session.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[SqlExecutor](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_SqlExecutor.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[StageSerializer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_StageSerializer.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[StateMachine](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_StateMachine.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[TypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TypesCache.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[UnityContainer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_UnityContainer.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
##  __Методы
[AddTrace](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_AddTrace.htm)|
Добавляет новую запись в список истории выполнения процесса.  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
---|---  
[AssertRunnerMode](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_AssertRunnerMode.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[CreateRuntimeStageInstanceAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CreateRuntimeStageInstanceAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[CreateStageGroupInstanceAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_CreateStageGroupInstanceAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteSQLConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ExecuteSQLConditionAsync.htm)|
Выполняет SQL-условие времени построения маршрута для единицы выполнения.  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FinalizeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrSyncProcessRunner_FinalizeAsync.htm)|
Выполняет действия после завершения обработки процесса.  
(Переопределяет [KrProcessRunnerBase.FinalizeAsync(IKrProcessRunnerContext,
Exception)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_FinalizeAsync.htm))  
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
[PartialGroupRecalcAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_PartialGroupRecalcAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[PrepareAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrSyncProcessRunner_PrepareAsync.htm)|
Выполняет действия перед выполнением процесса.  
(Переопределяет
[KrProcessRunnerBase.PrepareAsync(IKrProcessRunnerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_PrepareAsync.htm))  
[ProcessCurrentStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessCurrentStageAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[ProcessGlobalSignalsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessGlobalSignalsAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[ProcessNextStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessNextStageAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[ProcessStageHandlerResultAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrSyncProcessRunner_ProcessStageHandlerResultAsync.htm)|
Обрабатывает результат выполнения обработчика этапа.  
(Переопределяет [KrProcessRunnerBase.ProcessStageHandlerResultAsync(Stage,
StageHandlerResult,
IKrProcessRunnerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessStageHandlerResultAsync.htm))  
[ProcessStateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_ProcessStateAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RecalcRoleAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RecalcRoleAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RecalcSqlRolesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RecalcSqlRolesAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RunAfterAsync(Stage,
IKrProcessRunnerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunAfterAsync_1.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RunAfterStageGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunAfterStageGroupAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RunAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunAsync.htm)|
Начинает обработку процесса информация о котором задана в контексте.  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RunConditionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunConditionsAsync.htm)|
Выполняет условия времени выполнения маршрута для единицы выполнения.  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RunInDifferentCardContextAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunInDifferentCardContextAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RunInternalAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunInternalAsync.htm)|
Обрабатывает процесс, информация о котором задана в контексте.  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[RunNextStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_RunNextStageAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[SafeRunAsync(IKrProcessRunnerContext, Func<IKrExecutionUnit, Task<Boolean>>,
IKrExecutionUnit)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_SafeRunAsync.htm)|
Выполняет заданное действие для единицы выполнения.  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[SafeRunAsync(IKrProcessRunnerContext, Func<IKrExecutionUnit, Task>,
IKrExecutionUnit)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_SafeRunAsync_1.htm)|
Выполняет заданное действие для единицы выполнения.  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[SetAuthorAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_SetAuthorAsync.htm)|
Задаёт автора (инициатора) текущего процесса.  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[StopEntireProcess](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_StopEntireProcess.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TransitToStageGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TransitToStageGroupAsync.htm)|
Выполняет переход к группе этапов. Идентификатор группы этапов к которой
должен быть выполнен переход содержится в
[TransitionID](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_Handlers_StageHandlerResult_TransitionID.htm).  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[TryStartStageAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TryStartStageAsync.htm)|  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
[TryStartStageGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase_TryStartStageGroupAsync.htm)|
Возвращает следующий этап.  
(Унаследован от
[KrProcessRunnerBase](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessRunnerBase.htm))  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
