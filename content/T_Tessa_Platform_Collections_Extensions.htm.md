# Extensions - класс
Методы-расширения для пространства имён Tessa.Platform.Collections.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class Extensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class Extensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class Extensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type Extensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Extensions
##  __Методы
[AddRange<T>(ICollection<T>,
T[])](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|  Добавляет
значения items в коллекцию collection.  
---|---  
[AddRange<T>(ICollection<T>,
IEnumerable<T>)](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
[AddRangeForList](M_Tessa_Platform_Collections_Extensions_AddRangeForList.htm)|
Добавляет значения items в коллекцию collection.  
[AsReadOnly<TKey,
TValue>](M_Tessa_Platform_Collections_Extensions_AsReadOnly__2.htm)|
Оборачивает коллекцию ключ-значение dictionary в коллекцию только для чтения  
[FullOuterJoin<TOuter, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
[IndexOf<T>(IEnumerable<T>, Func<T,
Boolean>)](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
[IndexOf<T>(IEnumerable<T>, T,
IEqualityComparer<T>)](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
[IndexOf<T>(IList<T>, Int32, Func<T,
Boolean>)](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
[IndexOf<T>(IList<T>, Int32, Int32, Func<T,
Boolean>)](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
[InsertRange<T>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
[InsertRangeForList](M_Tessa_Platform_Collections_Extensions_InsertRangeForList.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
[LastIndexOf<T>(IReadOnlyList<T>, Func<T,
Boolean>)](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
[LastIndexOf<T>(IReadOnlyList<T>, T,
IEqualityComparer<T>)](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1_1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
[OrderByDependencies<TSource>(IEnumerable<TSource>, Func<TSource,
IEnumerable<TSource>>)](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
[OrderByDependencies<TSource>(IEnumerable<TSource>, Func<TSource,
IEnumerable<TSource>>, Func<TSource, IEnumerable<TSource>,
TSource>)](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
[OrderByDependencies<TSource, TKey>(IEnumerable<TSource>, Func<TSource, TKey>,
Func<TSource,
IEnumerable<TKey>>)](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
[OrderByDependencies<TSource, TKey>(IEnumerable<TSource>, Func<TSource, TKey>,
Func<TSource, IEnumerable<TKey>>, IEqualityComparer<TKey>, Func<TSource,
IEnumerable<TKey>,
TSource>)](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
[RemoveAll<T>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
[RemoveAllForList](M_Tessa_Platform_Collections_Extensions_RemoveAllForList.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
[RemoveRange<T>(ICollection<T>,
T[])](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|  Удаляет
значения items из коллекции collection.  
[RemoveRange<T>(ICollection<T>,
IEnumerable<T>)](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
[Reorder<TOrderKey,
TValue>](M_Tessa_Platform_Collections_Extensions_Reorder__2.htm)|  Выполняет
упорядочивание элементов коллекции по заданной функции getOrderFunc,
определяющей ключ, по которому производится упорядочивание. Если при
сортировке коллекция была изменена, то она очищается, а затем в неё
добавляются упорядоченные элементы. Рекомендуется использовать метод в случае,
если получение ключа сортировки в функции getOrderFunc может занять
значительное время. Метод возвращает исходную коллекцию values для цепочки
вызовов.  
[ToObservableCollection<T>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
[ToSealableList<T>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
[ToSealableObjectList<T>](M_Tessa_Platform_Collections_Extensions_ToSealableObjectList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm) и защищается от изменений при
активации защиты в списке.  
[TryPeek<T>(Stack<T>)](M_Tessa_Platform_Collections_Extensions_TryPeek__1.htm)|
Возвращает верхний элемент коллекции collection если коллекция содержит
элементы или значение по умолчанию для T  
[TryPeek<T>(Stack<T>,
T)](M_Tessa_Platform_Collections_Extensions_TryPeek__1_1.htm)|  Возвращает
верхний элемент коллекции collection если коллекция содержит элементы или
значение по умолчанию заданное в defaultValue  
##  __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
