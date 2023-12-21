# CardExtensions.CopyAndAddRange<T> \- метод
Копирует коллекцию сериализуемых объектов sourceItems и в конец коллекции
сериализуемых объектов targetItems. Устанавливает порядок следования объектов,
если объекты поддерживают
[ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void CopyAndAddRange<T>(
    	this IEnumerable<T> sourceItems,
    	ICollection<T> targetItems,
    	int startFromIndex = 0,
    	int? count = null
    )
    where T : new(), CardSerializableObject
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub CopyAndAddRange(Of T As {New, CardSerializableObject}) ( 
    	sourceItems As IEnumerable(Of T),
    	targetItems As ICollection(Of T),
    	Optional startFromIndex As Integer = 0,
    	Optional count As Integer? = Nothing
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    where T : gcnew(), CardSerializableObject
    static void CopyAndAddRange(
    	IEnumerable<T>^ sourceItems, 
    	ICollection<T>^ targetItems, 
    	int startFromIndex = 0, 
    	Nullable<int> count = nullptr
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member CopyAndAddRange : 
            sourceItems : IEnumerable<'T> * 
            targetItems : ICollection<'T> * 
            ?startFromIndex : int * 
            ?count : Nullable<int> 
    (* Defaults:
            let _startFromIndex = defaultArg startFromIndex 0
            let _count = defaultArg count null
    *)
    -> unit  when 'T : new() and CardSerializableObject
#### Параметры
sourceItems
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<T>
    Коллекция с копируемыми объектами.
targetItems
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>
    Коллекция, в которую добавляются копии объектов sourceItems.
startFromIndex [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
     Индекс с которого необходимо начать копирование из sourceItems. Если не указано, объекты будут скопированы с нулевого индекса. 
count
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
(Optional)
     Количество копируемых элементов. Если не указано или указано как null>, то будут скопированы все элементы коллекции-источника. 
#### Параметры типа
T
     Тип сериализуемых объектов, унаследованный от [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm) и имеющий конструктор по умолчанию, используемый при десериализации. Если тип реализует интерфейс [ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm), то после копирования для всех объектов коллекции targetItems проставляется порядок [Order](P_Tessa_Cards_ICardMetadataOrderable_Order.htm). 
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
