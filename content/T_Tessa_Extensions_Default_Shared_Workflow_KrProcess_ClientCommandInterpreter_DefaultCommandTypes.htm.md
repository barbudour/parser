# DefaultCommandTypes - класс
Предоставляет типы команд.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class DefaultCommandTypes
VB __Копировать
     Public NotInheritable Class DefaultCommandTypes
C++ __Копировать
     public ref class DefaultCommandTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type DefaultCommandTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultCommandTypes
##  __Поля
[CreateCardViaDocType](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes_CreateCardViaDocType.htm)|
Cоздаёт новую карточку заданного типа.  
---|---  
[CreateCardViaTemplate](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes_CreateCardViaTemplate.htm)|
Cоздаёт новую карточку по шаблону на клиенте (карточка не будет сохранена, у
пользователя должны быть права на сохранение карточки).  
[OpenCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes_OpenCard.htm)|
Открывает существующую карточку.  
[RefreshAndNotify](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes_RefreshAndNotify.htm)|
Обновляет список активных заданий пользователя и показывает уведомление при
необходимости.  
[ShowAdvancedDialog](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes_ShowAdvancedDialog.htm)|
Открывает карточку в диалоге. Используется при обработке запроса из подсистемы
маршрутов.  
[ShowConfirmationDialog](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes_ShowConfirmationDialog.htm)|
Отображает заданное сообщение как результат валидации типа
[Info](T_Tessa_Platform_Validation_ValidationResultType.htm).  
[WeShowAdvancedDialog](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes_WeShowAdvancedDialog.htm)|
Открывает карточку в диалоге. Используется при обработке запроса из Workflow
Engine.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
