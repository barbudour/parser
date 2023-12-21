# KrProcessExtensions - класс
Предоставляет вспомогательные методы используемые в подсистеме маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrProcessExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class KrProcessExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class KrProcessExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type KrProcessExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessExtensions
##  __Методы
[AddLaunchedRunner](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_AddLaunchedRunner.htm)|
Добавляет информацию о том, что для указанного процесса запущен обработчик.  
---|---  
[AddToLaunchedLevels](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_AddToLaunchedLevels.htm)|
Добавляет информацию о запуске процесса в рамках запроса.  
[DisableMultirunForRequest](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_DisableMultirunForRequest.htm)|
Запрещает повторное выполнение процесса за запрос.  
[FirstLaunchPerRequest](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_FirstLaunchPerRequest.htm)|
Возвращает значение, показывающее, что процесс с указанным идентификатором
запускается первый раз за запрос.  
[GetCaption](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_GetCaption.htm)|
Возвращает строку локализации соответствующую названию заданного режима.  
[GetKrProcessClientCommands](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_GetKrProcessClientCommands.htm)|
Возвращает список клиентских команд.  
[GetKrProcessRunnerTrace](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_GetKrProcessRunnerTrace.htm)|
Возвращает список, содержащий информацию по истории выполнения.  
[GetTemplateStagesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_GetTemplateStagesAsync.htm)|
Возвращает этапы из шаблона этапов.  
[HasLaunchedRunner](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_HasLaunchedRunner.htm)|
Возвращает значение, показывающее, запущен ли для указанного процесса раннер
или нет.  
[IsMainProcessStarted](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_IsMainProcessStarted.htm)|
Возвращает значение, показывающее, что указанный сателлит содержит информацию
по основному процессу
[KrProcessName](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrProcessName.htm).  
[MultirunEnabled](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_MultirunEnabled.htm)|
Возвращает значение, показывающее разрешено ли запускать процесс повторно за
запрос.  
[RemoveLaunchedRunner](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_RemoveLaunchedRunner.htm)|
Удаляет информацию о том, что для указанного процесса запущен раннер.  
[TryAddClientCommand](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_TryAddClientCommand.htm)|
Добавляет клиентскую команду, если список команд доступен.  
[TryAddToTrace](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_TryAddToTrace.htm)|
Добавляет новую запись в историю выполнения процесса.  
[TryGetKrProcessClientCommands](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_TryGetKrProcessClientCommands.htm)|
Возвращает список клиентских команд.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
