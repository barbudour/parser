# LdapEntryExtension.GetString - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetString(
    	this LdapEntry entry,
    	string attributeName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetString ( 
    	entry As LdapEntry,
    	attributeName As String
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ GetString(
    	LdapEntry^ entry, 
    	String^ attributeName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetString : 
            entry : LdapEntry * 
            attributeName : string -> string 
#### Параметры
entry LdapEntry
attributeName [String](https://learn.microsoft.com/dotnet/api/system.string)
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа LdapEntry. При вызове метода для экземпляра следует опускать
первый параметр. Дополнительные сведения см. в разделе [Методы расширения
(Visual Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[LdapEntryExtension -
](T_Tessa_Extensions_Platform_Server_AdSync_LdapEntryExtension.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
