# DefaultCommandTypes.CreateCardViaTemplate - поле
Cоздаёт новую карточку по шаблону на клиенте (карточка не будет сохранена, у
пользователя должны быть права на сохранение карточки).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public const string CreateCardViaTemplate = "CreateCardViaTemplate"
VB __Копировать
     Public Const CreateCardViaTemplate As String = "CreateCardViaTemplate"
C++ __Копировать
     public:
    literal String^ CreateCardViaTemplate = "CreateCardViaTemplate"
F# __Копировать
     static val mutable CreateCardViaTemplate: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Параметры:
Параметр| Тип значения| Описание  
---|---|---  
[TemplateID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_TemplateID.htm)|
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)| Идентификатор
шаблона, по которому создаётся карточка.  
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm)|
Массив [Byte](https://learn.microsoft.com/dotnet/api/system.byte)|
Дополнительный параметр. Сериализованная заготовка карточки используемая для
заполнения создаваемой по шаблону.  
[NewCardSignature](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCardSignature.htm)|
Массив [Byte](https://learn.microsoft.com/dotnet/api/system.byte)|
Дополнительный параметр. Используется совместно с
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm).
Сериализованная подпись заготовки карточки.  
##  __См. также
#### Ссылки
[DefaultCommandTypes -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
