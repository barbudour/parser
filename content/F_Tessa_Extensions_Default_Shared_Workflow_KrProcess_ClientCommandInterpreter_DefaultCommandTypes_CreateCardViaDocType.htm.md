# DefaultCommandTypes.CreateCardViaDocType - поле
Cоздаёт новую карточку заданного типа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public const string CreateCardViaDocType = "CreateCardViaDocType"
VB __Копировать
     Public Const CreateCardViaDocType As String = "CreateCardViaDocType"
C++ __Копировать
     public:
    literal String^ CreateCardViaDocType = "CreateCardViaDocType"
F# __Копировать
     static val mutable CreateCardViaDocType: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Параметры:
Параметр| Тип значения| Описание  
---|---|---  
[TypeID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_TypeID.htm)|
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)| Идентификатор типа
создаваемой карточки.  
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm)|
Массив [Byte](https://learn.microsoft.com/dotnet/api/system.byte)|
Дополнительный параметр. Сериализованная заготовка карточки используемая для
заполнения создаваемой по шаблону.  
[NewCardSignature](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCardSignature.htm)|
Массив [Byte](https://learn.microsoft.com/dotnet/api/system.byte)|
Дополнительный параметр. Используется совместно с
[NewCard](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_NewCard.htm).
Сериализованная подпись заготовки карточки.  
[DocTypeID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_DocTypeID.htm)|
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)| Дополнительный
параметр. Идентификатор типа документа создаваемой карточки.  
[DocTypeTitle](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_DocTypeTitle.htm)|
[String](https://learn.microsoft.com/dotnet/api/system.string)| Дополнительный
параметр. Используется совместно с
[DocTypeID](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_Keys_DocTypeID.htm).
Имя типа документа создаваемой карточки.  
##  __См. также
#### Ссылки
[DefaultCommandTypes -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter_DefaultCommandTypes.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.ClientCommandInterpreter -
пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_ClientCommandInterpreter.htm)
