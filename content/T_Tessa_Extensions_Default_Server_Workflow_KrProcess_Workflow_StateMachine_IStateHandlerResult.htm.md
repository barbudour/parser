# IStateHandlerResult - интерфейс
Описывает результат обработки состояния.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.StateMachine](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IStateHandlerResult
VB __Копировать
     Public Interface IStateHandlerResult
C++ __Копировать
     public interface class IStateHandlerResult
F# __Копировать
     type IStateHandlerResult = interface end
##  __Свойства
[ContinueCurrentRun](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_IStateHandlerResult_ContinueCurrentRun.htm)|
Возвращает значение, показывающее, необходимо ли после обработки сотсояния
продолжать текущее выполнение runner-a. Значение false, если текущее
выполнение должно быть прервано. Если запланировано еще одно сохранение
карточки, приводящее к запуску runner-a, то runner будет запущен с текущим
KrScope.  
---|---  
[ForceStartGroup](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_IStateHandlerResult_ForceStartGroup.htm)|
Возвращает значение, показывающее, необходимо ли начать выполнение этапов из
следующей группы этапов, несмотря на то, что в текущей группе этапов остались
не обработанные этапы.  
[Handled](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_IStateHandlerResult_Handled.htm)|
Возвращает значение, показывающее, что состояние было обработано.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.StateMachine -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine.htm)
