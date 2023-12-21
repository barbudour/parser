# IGlobalSignalHandlerResult - интерфейс
Описывает результат обработки глобального сигнала.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.GlobalSignals](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IGlobalSignalHandlerResult
VB __Копировать
     Public Interface IGlobalSignalHandlerResult
C++ __Копировать
     public interface class IGlobalSignalHandlerResult
F# __Копировать
     type IGlobalSignalHandlerResult = interface end
##  __Свойства
[ContinueCurrentRun](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_IGlobalSignalHandlerResult_ContinueCurrentRun.htm)|
Возвращает значение, показывающее, необходимо ли после обработки сигнала
продолжать текущее выполнение runner-a. Значение false, если текущее
выполнение должно быть прервано. Если запланировано еще одно сохранение
карточки, приводящее к запуску runner-a, то runner будет запущен с текущим
KrScope.  
---|---  
[ForceStartGroup](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_IGlobalSignalHandlerResult_ForceStartGroup.htm)|
Возвращает значение, показывающее, необходимо ли начать выполнение этапов из
следующей группы этапов, несмотря на то, что в текущей группе этапов остались
не обработанные этапы.  
[Handled](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals_IGlobalSignalHandlerResult_Handled.htm)|
Возвращает значение, показывающее, что сигнал был обработан.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow.GlobalSignals -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_GlobalSignals.htm)
