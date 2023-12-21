# AdUserAccountControlExtension.Has - метод
Возвращает признак того, что заданный флаг установлен.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool Has(
    	this AdUserAccountControl flags,
    	AdUserAccountControl flag
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function Has ( 
    	flags As AdUserAccountControl,
    	flag As AdUserAccountControl
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool Has(
    	AdUserAccountControl flags, 
    	AdUserAccountControl flag
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member Has : 
            flags : AdUserAccountControl * 
            flag : AdUserAccountControl -> bool 
#### Параметры
flags
[AdUserAccountControl](T_Tessa_Extensions_Platform_Server_AdSync_AdUserAccountControl.htm)
    Установленные флаги.
flag
[AdUserAccountControl](T_Tessa_Extensions_Platform_Server_AdSync_AdUserAccountControl.htm)
     Флаг, который требуется проверить. Если указано несколько флагов, то проверяется, что все из них установлены. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что заданный флаг установлен.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[AdUserAccountControl](T_Tessa_Extensions_Platform_Server_AdSync_AdUserAccountControl.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[AdUserAccountControlExtension -
](T_Tessa_Extensions_Platform_Server_AdSync_AdUserAccountControlExtension.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
