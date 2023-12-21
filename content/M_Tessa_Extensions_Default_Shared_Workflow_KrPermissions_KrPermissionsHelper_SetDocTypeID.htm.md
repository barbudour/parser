# KrPermissionsHelper.SetDocTypeID - метод
Задаёт информацию по идентификатору типа документа в токене безопасности.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetDocTypeID(
    	this KrToken krToken,
    	Guid? docTypeID
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetDocTypeID ( 
    	krToken As KrToken,
    	docTypeID As Guid?
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetDocTypeID(
    	KrToken^ krToken, 
    	Nullable<Guid> docTypeID
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetDocTypeID : 
            krToken : KrToken * 
            docTypeID : Nullable<Guid> -> unit 
#### Параметры
krToken
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
    Токен безопасности.
docTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор типа документа.
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
