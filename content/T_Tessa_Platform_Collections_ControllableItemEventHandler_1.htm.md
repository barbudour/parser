# ControllableItemEventHandler<TItem> \- делегат
Обработчик события по действию с проверяемым элементом коллекции
[IControllableCollection<TItem>](T_Tessa_Platform_Collections_IControllableCollection_1.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate void ControllableItemEventHandler<TItem>(
    	Object sender,
    	ControllableItemEventArgs<TItem> e
    )
    where TItem : class
VB __Копировать
     Public Delegate Sub ControllableItemEventHandler(Of TItem As Class) ( 
    	sender As Object,
    	e As ControllableItemEventArgs(Of TItem)
    )
C++ __Копировать
    generic<typename TItem>
    where TItem : ref class
    public delegate void ControllableItemEventHandler(
    	Object^ sender, 
    	ControllableItemEventArgs<TItem>^ e
    )
F# __Копировать
     type ControllableItemEventHandler = 
        delegate of 
            sender : Object * 
            e : ControllableItemEventArgs<'TItem> -> unit
#### Параметры
sender [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Коллекция, для которой выполняется проверка.
e
[ControllableItemEventArgs](T_Tessa_Platform_Collections_ControllableItemEventArgs_1.htm)<TItem>
    Аргументы события.
#### Параметры типа
TItem
    Ссылочный тип проверямого элемента.
##  __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
