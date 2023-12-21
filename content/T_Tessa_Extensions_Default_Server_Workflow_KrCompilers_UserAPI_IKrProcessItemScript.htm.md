# IKrProcessItemScript - интерфейс
Описывает объект, поддерживающий выполнение сценариев процесса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrProcessItemScript
VB __Копировать
     Public Interface IKrProcessItemScript
C++ __Копировать
     public interface class IKrProcessItemScript
F# __Копировать
     type IKrProcessItemScript = interface end
##  __Заметки
Объектом может быть: группа этапов, шаблон этапов и этап маршрута.
##  __Методы
[AfterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_AfterAsync.htm)|
Сценарий постобработки.  
---|---  
[BeforeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_BeforeAsync.htm)|
Сценарий инициализации.  
[ConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_ConditionAsync.htm)|
Сценарий C#-условия.  
[RunAfterAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_RunAfterAsync.htm)|
Выполняет сценарий постобработки
[AfterAsync()](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_AfterAsync.htm).  
[RunBeforeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_RunBeforeAsync.htm)|
Выполняет сценарий инициализации
[BeforeAsync()](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_BeforeAsync.htm).  
[RunConditionAsync](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_RunConditionAsync.htm)|
Выполняет C#-условие
[ConditionAsync()](M_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI_IKrProcessItemScript_ConditionAsync.htm).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.UserAPI - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrCompilers_UserAPI.htm)
