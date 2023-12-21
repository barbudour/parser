# DefaultCommandTypes.WeShowAdvancedDialog - поле
Открывает карточку в диалоге. Используется при обработке запроса из Workflow
Engine.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public const string WeShowAdvancedDialog = "WeShowAdvancedDialog"
VB __Копировать
     Public Const WeShowAdvancedDialog As String = "WeShowAdvancedDialog"
C++ __Копировать
     public:
    literal String^ WeShowAdvancedDialog = "WeShowAdvancedDialog"
F# __Копировать
     static val mutable WeShowAdvancedDialog: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Параметры:
Параметр| Тип значения| Описание  
---|---|---  
[CompletionOptionSettings](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_CompletionOptionSettings.htm)|
Запрос на обработку процесса WorkflowEngine и его подпись. Для получения
следует использовать метод [SetProcessInfo(Dictionary<String, Object>, Guid,
String,
Nullable<Guid>)](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_SetProcessInfo.htm).
Для получения [GetProcessRequest(IDictionary<String,
Object>)](M_Tessa_Workflow_Helpful_WorkflowEngineExtensions_GetProcessRequest.htm).|
Info запроса на обработку процесса WorkflowEngine с его подписью.  
[CompletionOptionSettings](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_CompletionOptionSettings.htm)|
Хранилище объекта типа
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)
сохранённое по ключу [!:WorkflowDialogAction.DialogSettingsKey] в коллекции
ключ-значение получаемое для данного параметра| Параметры диалога.  
##  __См. также
#### Ссылки
[DefaultCommandTypes -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
