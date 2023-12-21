# KrPermissionExtensions.SetCardAccessAsync(IKrPermissionExtendedCardSettings,
Boolean, ICardMetadata, String, ICollection<String>, CancellationToken) -
метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task SetCardAccessAsync(
    	this IKrPermissionExtendedCardSettings extendedCardSettings,
    	bool isAllowed,
    	ICardMetadata cardMetadata,
    	string section,
    	ICollection<string> fields,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function SetCardAccessAsync ( 
    	extendedCardSettings As IKrPermissionExtendedCardSettings,
    	isAllowed As Boolean,
    	cardMetadata As ICardMetadata,
    	section As String,
    	fields As ICollection(Of String),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task^ SetCardAccessAsync(
    	IKrPermissionExtendedCardSettings^ extendedCardSettings, 
    	bool isAllowed, 
    	ICardMetadata^ cardMetadata, 
    	String^ section, 
    	ICollection<String^>^ fields, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetCardAccessAsync : 
            extendedCardSettings : IKrPermissionExtendedCardSettings * 
            isAllowed : bool * 
            cardMetadata : ICardMetadata * 
            section : string * 
            fields : ICollection<string> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
extendedCardSettings
[IKrPermissionExtendedCardSettings](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionExtendedCardSettings.htm)
isAllowed [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
section [String](https://learn.microsoft.com/dotnet/api/system.string)
fields
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IKrPermissionExtendedCardSettings](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_IKrPermissionExtendedCardSettings.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[KrPermissionExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtensions.htm)
[SetCardAccessAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtensions_SetCardAccessAsync.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
