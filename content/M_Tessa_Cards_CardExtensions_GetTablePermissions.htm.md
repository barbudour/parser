# CardExtensions.GetTablePermissions - метод
Возвращает права доступа к строкам коллекционной секции с именем sectionName.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardPermissionFlags GetTablePermissions(
    	this ICardPermissionResolver resolver,
    	string sectionName
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetTablePermissions ( 
    	resolver As ICardPermissionResolver,
    	sectionName As String
    ) As CardPermissionFlags
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardPermissionFlags GetTablePermissions(
    	ICardPermissionResolver^ resolver, 
    	String^ sectionName
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetTablePermissions : 
            resolver : ICardPermissionResolver * 
            sectionName : string -> CardPermissionFlags 
#### Параметры
resolver [ICardPermissionResolver](T_Tessa_Cards_ICardPermissionResolver.htm)
    Объект, осуществляющий поиск прав доступа для полей и строк.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции.
#### Возвращаемое значение
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)  
Права доступа к строкам секции.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardPermissionResolver](T_Tessa_Cards_ICardPermissionResolver.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
Параметр sectionName равен null.  
---|---  
## __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
