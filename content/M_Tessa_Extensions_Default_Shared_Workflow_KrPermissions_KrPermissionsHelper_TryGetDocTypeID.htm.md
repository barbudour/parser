# KrPermissionsHelper.TryGetDocTypeID - метод
Возвращает идентификатор типа документа из токена безопасности.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetDocTypeID(
    	this KrToken krToken,
    	out Guid? docTypeID
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetDocTypeID ( 
    	krToken As KrToken,
    	<OutAttribute> ByRef docTypeID As Guid?
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool TryGetDocTypeID(
    	KrToken^ krToken, 
    	[OutAttribute] Nullable<Guid>% docTypeID
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetDocTypeID : 
            krToken : KrToken * 
            docTypeID : Nullable<Guid> byref -> bool 
#### Параметры
krToken
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
    Токен безопасности.
docTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор типа документа или значение null, если для карточки не используется тип документа или токен его не содержит.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если токен безопасности содержит идентификатор типа документа,
иначе - false.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметр krToken имеет значение null.  
---|---  
##  __См. также
#### Ссылки
[KrPermissionsHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
