# CardRequestExtensions.TryGetContextData<T> \- метод
Возвращает данные, записанные методом [SetContextData(ICardExtensionContext,
Object, Object)](M_Tessa_Cards_CardRequestExtensions_SetContextData.htm) в
контекст цепочки расширений для заданного объекта-отправителя sender. Данные
существует в пределах цепочки расширений. Возвращает null, если данные не
найдены или были установлены как null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static T TryGetContextData<T>(
    	this ICardExtensionContext context,
    	Object sender
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetContextData(Of T) ( 
    	context As ICardExtensionContext,
    	sender As Object
    ) As T
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    static T TryGetContextData(
    	ICardExtensionContext^ context, 
    	Object^ sender
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetContextData : 
            context : ICardExtensionContext * 
            sender : Object -> 'T 
#### Параметры
context
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)
    Контекст цепочки расширений. Не должен быть равен null.
sender [Object](https://learn.microsoft.com/dotnet/api/system.object)
     Объект-отправитель, например, объект текущего расширения this, его тип typeof(MyExtension) или любая строка-ключ "Unique string". Не может быть равен null. 
#### Параметры типа
T
    Тип возвращаемых данных. Должен быть nullable-типом.
#### Возвращаемое значение
T  
Полученные данные, преобразованные к типу T, или null, если данные не найдены
или были установлены как null.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm).
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
