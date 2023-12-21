# CardRequestExtensions.ResetAllTaskAccessCheckIgnores - метод
Удаляет всю информацию по заданиям, для которых не выполняется проверка прав.
Возвращает признак того, что информация присутствовала перед удалением.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ResetAllTaskAccessCheckIgnores(
    	this ICardStoreExtensionContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ResetAllTaskAccessCheckIgnores ( 
    	context As ICardStoreExtensionContext
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool ResetAllTaskAccessCheckIgnores(
    	ICardStoreExtensionContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ResetAllTaskAccessCheckIgnores : 
            context : ICardStoreExtensionContext -> bool 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст сохранения карточки, в процессе которого сохраняются/завершаются задания.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если информация присутствовала перед удалением; false в противном
случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
