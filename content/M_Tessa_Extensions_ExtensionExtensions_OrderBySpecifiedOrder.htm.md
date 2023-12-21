# ExtensionExtensions.OrderBySpecifiedOrder - метод
Упорядочивает типы
[RegistratorImportingItem](T_Tessa_Extensions_RegistratorImportingItem.htm) по
их явно заданному порядку.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IOrderedEnumerable<RegistratorImportingItem> OrderBySpecifiedOrder(
    	this IEnumerable<RegistratorImportingItem> items
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function OrderBySpecifiedOrder ( 
    	items As IEnumerable(Of RegistratorImportingItem)
    ) As IOrderedEnumerable(Of RegistratorImportingItem)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IOrderedEnumerable<RegistratorImportingItem^>^ OrderBySpecifiedOrder(
    	IEnumerable<RegistratorImportingItem^>^ items
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member OrderBySpecifiedOrder : 
            items : IEnumerable<RegistratorImportingItem> -> IOrderedEnumerable<RegistratorImportingItem> 
#### Параметры
items
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RegistratorImportingItem](T_Tessa_Extensions_RegistratorImportingItem.htm)>
    Список объектов с информацией по типам объектов [IRegistrator](T_Tessa_Extensions_IRegistrator.htm).
#### Возвращаемое значение
[IOrderedEnumerable](https://learn.microsoft.com/dotnet/api/system.linq.iorderedenumerable-1)<[RegistratorImportingItem](T_Tessa_Extensions_RegistratorImportingItem.htm)>  
Упорядоченный список типов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[RegistratorImportingItem](T_Tessa_Extensions_RegistratorImportingItem.htm)>.
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[ExtensionExtensions - ](T_Tessa_Extensions_ExtensionExtensions.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
