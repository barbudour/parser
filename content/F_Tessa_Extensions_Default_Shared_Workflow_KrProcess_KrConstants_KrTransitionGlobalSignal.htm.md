# KrConstants.KrTransitionGlobalSignal - поле
Имя типа сигнала, по которому выполняется переход внутри процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public const string KrTransitionGlobalSignal = "KrTransitionGlobalSignal"
VB __Копировать
     Public Const KrTransitionGlobalSignal As String = "KrTransitionGlobalSignal"
C++ __Копировать
     public:
    literal String^ KrTransitionGlobalSignal = "KrTransitionGlobalSignal"
F# __Копировать
     static val mutable KrTransitionGlobalSignal: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Режим работы| Дополнительные параметры, указываемые в при отправке сигнала в
[AddSignal(String, String, Int32, Dictionary<String, Object>,
WorkflowSignalType, WorkflowQueueEventType,
Nullable<Guid>)](M_Tessa_Cards_Workflow_WorkflowQueue_AddSignal.htm)  
---|---  
Переход на этап|
[StageRowID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_StageRowID.htm)
(Тип значения [Guid](https://learn.microsoft.com/dotnet/api/system.guid).
Значение по умолчанию: null) - идентификатор этапа (ID)  
Переход в начало группы|
[StageGroupID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_StageGroupID.htm)
(Тип значения [Guid](https://learn.microsoft.com/dotnet/api/system.guid).
Значение по умолчанию: null) - идентификатор группы этапов  
Переход в начало текущей группы|
[KrTransitionCurrentGroup](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrTransitionCurrentGroup.htm)
(Тип значения
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Значение по
умолчанию: false) - значение true, если переход должен быть выполнен в начало
текущей группы  
Переход на следующую группу (если следующая группа отсутствует, процесс будет
пропущен)|
[KrTransitionNextGroup](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrTransitionNextGroup.htm)
(Тип значения
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Значение по
умолчанию: false) - значение true, если переход должен быть выполнен на
следующую группу  
Переход на предыдущую группу|
[KrTransitionPrevGroup](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrTransitionPrevGroup.htm)
(Тип значения
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Значение по
умолчанию: false) - значение true, если переход должен быть выполнен на
предыдущую группу  
Сохранить текущее состояние этапов при выполнении перехода. Дополнительный
параметр. Может быть указан при указании других параметров.|
[KrTransitionKeepStates](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrTransitionKeepStates.htm)
(Тип значения
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Значение по
умолчанию: false) - значение true, если должно быть сохранено текущее
состояние этапов несмотря на выполнение перехода  
##  __См. также
#### Ссылки
[KrConstants -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
