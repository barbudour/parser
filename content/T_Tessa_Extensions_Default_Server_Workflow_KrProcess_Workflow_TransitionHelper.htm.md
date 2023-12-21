# TransitionHelper - класс
Предоставляет вспомогательные методы для выполнения переходов между этапами.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TransitionHelper
VB __Копировать
     Public NotInheritable Class TransitionHelper
C++ __Копировать
     public ref class TransitionHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TransitionHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TransitionHelper
##  __Методы
[ChangeStatesTransition](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_TransitionHelper_ChangeStatesTransition.htm)|
Обновляет состояния этапов в маршруте в связи с переходом.  
---|---  
[SetInactiveStateToAllStages](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_TransitionHelper_SetInactiveStateToAllStages.htm)|
Устанавливает состояние
[Inactive](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Inactive.htm)
для всех этапов.  
[SetSkipStateToSubsequentStages](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_TransitionHelper_SetSkipStateToSubsequentStages.htm)|
Установить состояние
[Skipped](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Skipped.htm)
для всех этапов расположенных после указанного этапа.  
[TransitByPredicate](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_TransitionHelper_TransitByPredicate.htm)|
Определяет порядковый номер первого этапа удовлетворяющего заданное условие.  
[TransitToNextGroup](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_TransitionHelper_TransitToNextGroup.htm)|
Определяет порядковый номер первого этапа, относящегося к группе следующей за
группой с указанным идентификатором.  
[TransitToPreviousGroup](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_TransitionHelper_TransitToPreviousGroup.htm)|
Определяет порядковый номер первого этапа, относящегося к группе
предшествующей группе с указанным идентификатором.  
[TransitToStage](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_TransitionHelper_TransitToStage.htm)|
Определяет порядковый номер этапа имеющего указанный идентификатор.  
[TransitToStageGroup](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_TransitionHelper_TransitToStageGroup.htm)|
Определяет порядковый номер первого этапа, относящегося к группе с указанным
идентификатором.  
## __Поля
[NotFound](F_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_TransitionHelper_NotFound.htm)|
Порядковый индекс этапа, если его не удалось найти.  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
