# AdHelper.AddPaging - метод
Добавление пейджинга для запроса LDAP
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static LdapSearchConstraints AddPaging(
    	this LdapSearchConstraints constraints,
    	byte[] cookie
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function AddPaging ( 
    	constraints As LdapSearchConstraints,
    	cookie As Byte()
    ) As LdapSearchConstraints
C++ __Копировать
     public:
    [ExtensionAttribute]
    static LdapSearchConstraints^ AddPaging(
    	LdapSearchConstraints^ constraints, 
    	array<unsigned char>^ cookie
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member AddPaging : 
            constraints : LdapSearchConstraints * 
            cookie : byte[] -> LdapSearchConstraints 
#### Параметры
constraints LdapSearchConstraints
    Текущий констрейнт соединения
cookie [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Файл-печенька
#### Возвращаемое значение
LdapSearchConstraints  
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа LdapSearchConstraints. При вызове метода для экземпляра следует
опускать первый параметр. Дополнительные сведения см. в разделе [Методы
расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[AdHelper - ](T_Tessa_Extensions_Platform_Server_AdSync_AdHelper.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
