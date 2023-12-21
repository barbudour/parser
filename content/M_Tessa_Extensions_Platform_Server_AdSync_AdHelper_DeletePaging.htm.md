# AdHelper.DeletePaging - метод
Удаление пейджинга для запроса LDAP
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static LdapSearchConstraints DeletePaging(
    	this LdapSearchConstraints constraints
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function DeletePaging ( 
    	constraints As LdapSearchConstraints
    ) As LdapSearchConstraints
C++ __Копировать
     public:
    [ExtensionAttribute]
    static LdapSearchConstraints^ DeletePaging(
    	LdapSearchConstraints^ constraints
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DeletePaging : 
            constraints : LdapSearchConstraints -> LdapSearchConstraints 
#### Параметры
constraints LdapSearchConstraints
    Текущий констрейнт соединения
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
