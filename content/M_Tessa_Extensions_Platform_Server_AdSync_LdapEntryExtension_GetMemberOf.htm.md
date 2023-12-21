# LdapEntryExtension.GetMemberOf - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IEnumerable<string> GetMemberOf(
    	this LdapEntry entry
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetMemberOf ( 
    	entry As LdapEntry
    ) As IEnumerable(Of String)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IEnumerable<String^>^ GetMemberOf(
    	LdapEntry^ entry
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetMemberOf : 
            entry : LdapEntry -> IEnumerable<string> 
#### Параметры
entry LdapEntry
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
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
