# WorkflowWorker<TManager> \- класс
Базовый класс для объекта, реализующего логику подпроцессов и переходов в
бизнес-процессе.
## __Definition
 **Пространство имён:** [Tessa.Cards.Workflow](N_Tessa_Cards_Workflow.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class WorkflowWorker<TManager> : IWorkflowWorker
    where TManager : class, IWorkflowManager
VB __Копировать
     Public MustInherit Class WorkflowWorker(Of TManager As {Class, IWorkflowManager})
    	Implements IWorkflowWorker
C++ __Копировать
    generic<typename TManager>
    where TManager : ref class, IWorkflowManager
    public ref class WorkflowWorker abstract : IWorkflowWorker
F# __Копировать
     [<AbstractClassAttribute>]
    type WorkflowWorker<'TManager when 'TManager : not struct and IWorkflowManager> = 
        class
            interface IWorkflowWorker
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WorkflowWorker<TManager>
Derived
[Tessa.Cards.Workflow.WorkflowTaskWorker<TManager>](T_Tessa_Cards_Workflow_WorkflowTaskWorker_1.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.KrProcessWorkflowWorker](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessWorkflowWorker.htm)
Implements
    [IWorkflowWorker](T_Tessa_Cards_Workflow_IWorkflowWorker.htm)
#### Параметры типа
TManager
     Ссылочный тип для объекта, предоставляющего возможности для управления бизнес-процессом. Тип должен реализовывать интерфейс [IWorkflowManager](T_Tessa_Cards_Workflow_IWorkflowManager.htm). 
## __Конструкторы
[WorkflowWorker<TManager>](M_Tessa_Cards_Workflow_WorkflowWorker_1__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
##  __Свойства
[Manager](P_Tessa_Cards_Workflow_WorkflowWorker_1_Manager.htm)| Объект,
предоставляющий возможности для управления бизнес-процессом.  
---|---  
##  __Методы
[AddTaskToProcessInfo(IWorkflowProcessInfo,
IEnumerable<Guid>)](M_Tessa_Cards_Workflow_WorkflowWorker_1_AddTaskToProcessInfo.htm)|
Добавляет идентификаторы заданий к списку заданий в подпроцессе.  
---|---  
[AddTaskToProcessInfo(IWorkflowProcessInfo,
Guid)](M_Tessa_Cards_Workflow_WorkflowWorker_1_AddTaskToProcessInfo_1.htm)|
Добавляет идентификатор задания к списку заданий в подпроцессе.  
[CompleteTaskAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_CompleteTaskAsync.htm)|
Выполняет действие при завершении заданного задания. Не удаляет запись с
информацией по заданию, т.к. задание может завершаться без удаления записи.  
[CompleteTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_CompleteTaskCoreAsync.htm)|
Выполняет действие при завершении заданного задания.  
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
[GetTaskCount](M_Tessa_Cards_Workflow_WorkflowWorker_1_GetTaskCount.htm)|
Возвращает количество заданий, о которых известно в подпроцессе.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasTasks](M_Tessa_Cards_Workflow_WorkflowWorker_1_HasTasks.htm)|  Возвращает
признак того, что в подпроцессе присутствует хотя бы одно известное задание.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ProcessSignalAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ProcessSignalAsync.htm)|
Выполняет действие по обработке сигнала. Возвращает признак того, что сигнал
был ожидаем и обработан (необязательно успешно). Необработанный сигнал по
умолчанию не приводит к ошибке сохранения карточки и не приводит к откату
транзакции, но не помечается как обработанный в очереди. По умолчанию все
сигналы считаются необработанными. Необработанное исключение, возникшее в
обработчике, также отмечает сигнал как необработанный. Если для ожидаемого
сигнала требуется прервать транзакцию, то добавьте ошибку в
Manager.ValidationResult, но верните в методе true. Если параметры подпроцесса
отмечены как изменённые, то по завершении метода они сохраняются независимо от
возвращённого значения.  
[ProcessSignalCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ProcessSignalCoreAsync.htm)|
Выполняет действие по обработке сигнала. Возвращает признак того, что сигнал
был ожидаем и обработан (необязательно успешно). Необработанный сигнал по
умолчанию не приводит к ошибке сохранения карточки и не приводит к откату
транзакции, но не помечается как обработанный в очереди. По умолчанию все
сигналы считаются необработанными. Необработанное исключение, возникшее в
обработчике, также отмечает сигнал как необработанный. Если для ожидаемого
сигнала требуется прервать транзакцию, то добавьте ошибку в
Manager.ValidationResult, но верните в методе true.  
[ReinstateTaskAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ReinstateTaskAsync.htm)|
Выполняет действие при возврате на роль заданного задания. Не удаляет запись с
информацией по заданию.  
[ReinstateTaskCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_ReinstateTaskCoreAsync.htm)|
Выполняет действие при возврате задания на роль.  
[RemoveTaskFromProcessInfo(IWorkflowProcessInfo,
IEnumerable<Guid>)](M_Tessa_Cards_Workflow_WorkflowWorker_1_RemoveTaskFromProcessInfo.htm)|
Удаляет идентификаторы заданий из списка заданий в подпроцессе. Возвращает
количество идентификаторов, которые присутствовали в списке заданий и были
удалены.  
[RemoveTaskFromProcessInfo(IWorkflowProcessInfo,
Guid)](M_Tessa_Cards_Workflow_WorkflowWorker_1_RemoveTaskFromProcessInfo_1.htm)|
Удаляет идентификатор задания из списка заданий в подпроцессе. Возвращает
признак того, что идентификатор там был, после чего был удалён.  
[RenderStepAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_RenderStepAsync.htm)|
Выполняет переход к состоянию с заданным номером.  
[RenderStepCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_RenderStepCoreAsync.htm)|
Выполняет переход к состоянию с заданным номером.  
[StartProcessAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartProcessAsync.htm)|
Выполняет действие при старте подпроцесса с уникальным именем типа и
параметрами. Создаёт запись с информацией по подпроцессу.  
[StartProcessCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartProcessCoreAsync.htm)|
Выполняет действие при старте подпроцесса с уникальным именем типа и
параметрами.  
[StartSubProcessWithCompletionAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartSubProcessWithCompletionAsync.htm)|
Запускает подпроцесс, который выполняет указанный переход при завершении.  
[StopProcessAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StopProcessAsync.htm)|
Выполняет действие при завершении заданного подпроцесса. Удаляет запись с
информацией по подпроцессу.  
[StopProcessCoreAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StopProcessCoreAsync.htm)|
Выполняет действие при завершении заданного подпроцесса.  
[StopSubProcessWithCompletionAsync](M_Tessa_Cards_Workflow_WorkflowWorker_1_StopSubProcessWithCompletionAsync.htm)|
Завершает подпроцесс, выполняя переход, указанный при запуске подпроцесса
методом [StartSubProcessWithCompletionAsync(String, Int32,
IWorkflowProcessInfo, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Cards_Workflow_WorkflowWorker_1_StartSubProcessWithCompletionAsync.htm).  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetTasksFromProcessInfo](M_Tessa_Cards_Workflow_WorkflowWorker_1_TryGetTasksFromProcessInfo.htm)|
Возвращает массив идентификаторов заданий, о которых известно в подпроцессе,
или null, если таких заданий не существует.  
## __Поля
[CompletionProcessIDKey](F_Tessa_Cards_Workflow_WorkflowWorker_1_CompletionProcessIDKey.htm)|
Ключ в настройках подпроцесса, содержащий идентификатор подпроцесса, переход
которого выполняется по завершении настраиваемого подпроцесса.  
---|---  
[CompletionTransitionKey](F_Tessa_Cards_Workflow_WorkflowWorker_1_CompletionTransitionKey.htm)|
Ключ в настройках задания или подпроцесса, содержащий номер перехода,
выполняемого по завершении запускаемого задания или подпроцесса.  
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
[Tessa.Cards.Workflow - пространство имён](N_Tessa_Cards_Workflow.htm)
