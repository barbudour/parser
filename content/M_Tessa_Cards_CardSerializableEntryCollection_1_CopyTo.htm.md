# CardSerializableEntryCollection<T>.CopyTo - метод
Копирует элементы коллекции в массив, начиная с заданного отсчитываемого от
нуля индекса.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void CopyTo(
    	T[] array,
    	int arrayIndex
    )
VB __Копировать
     Public Sub CopyTo ( 
    	array As T(),
    	arrayIndex As Integer
    )
C++ __Копировать
     public:
    virtual void CopyTo(
    	array<T>^ array, 
    	int arrayIndex
    ) sealed
F# __Копировать
     abstract CopyTo : 
            array : 'T[] * 
            arrayIndex : int -> unit 
    override CopyTo : 
            array : 'T[] * 
            arrayIndex : int -> unit 
#### Параметры
array [T](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)[]
    Массив, в который требуется скопировать элементы коллекции.
arrayIndex [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Отсчитываемый от нуля индекс, начиная с которого требуется скопировать элементы коллекции.
#### Реализации
[ICollection<T>.CopyTo(T[],
Int32)](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.copyto#system-
collections-generic-icollection-1-copyto\(-0\(\)-system-int32\))  
##  __См. также
#### Ссылки
[CardSerializableEntryCollection<T> \-
](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
