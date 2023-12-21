# CardExtensions.OrderManuallyForDeletion<T> \- метод
Упорядочивает строки таким образом, чтобы их можно было удалить из базы
данных, с учётом порядка строк по убыванию, определяемого пользователем в
свойстве [Order](P_Tessa_Cards_ICardOrderable_Order.htm) каждой строки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static T[] OrderManuallyForDeletion<T>(
    	this IEnumerable<T> rows
    )
    where T : ICardOrderable
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function OrderManuallyForDeletion(Of T As ICardOrderable) ( 
    	rows As IEnumerable(Of T)
    ) As T()
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    where T : ICardOrderable
    static array<T>^ OrderManuallyForDeletion(
    	IEnumerable<T>^ rows
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member OrderManuallyForDeletion : 
            rows : IEnumerable<'T> -> 'T[]  when 'T : ICardOrderable
#### Параметры
rows
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<T>
    Строки, которые требуется удалить из базы данных.
#### Параметры типа
T
    Тип строк, которые требуется упорядочить.
#### Возвращаемое значение
T[]  
Строки, упорядоченные в порядке удаления.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<T>.
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
