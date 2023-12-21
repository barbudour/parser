# AdHelper.GetCookies - метод
Получение cookie из контролов
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static byte[] GetCookies(
    	this LdapControl[] controls
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetCookies ( 
    	controls As LdapControl()
    ) As Byte()
C++ __Копировать
     public:
    [ExtensionAttribute]
    static array<unsigned char>^ GetCookies(
    	array<LdapControl^>^ controls
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetCookies : 
            controls : LdapControl[] -> byte[] 
#### Параметры
controls LdapControl[]
    Список контролов, которые вернул сервер
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Cookie
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа LdapControl[]. При вызове метода для экземпляра следует опускать
первый параметр. Дополнительные сведения см. в разделе [Методы расширения
(Visual Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[AdHelper - ](T_Tessa_Extensions_Platform_Server_AdSync_AdHelper.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
