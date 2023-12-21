# ControllableItemEventArgs<TItem> \- класс
Аргументы события по действию с проверяемым элементом коллекции
[IControllableCollection<TItem>](T_Tessa_Platform_Collections_IControllableCollection_1.htm).
Действие может быть отменено при установке признака
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel) равным true.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ControllableItemEventArgs<TItem> : CancelEventArgs
    where TItem : class
VB __Копировать
     Public NotInheritable Class ControllableItemEventArgs(Of TItem As Class)
    	Inherits CancelEventArgs
C++ __Копировать
    generic<typename TItem>
    where TItem : ref class
    public ref class ControllableItemEventArgs sealed : public CancelEventArgs
F# __Копировать
     [<SealedAttribute>]
    type ControllableItemEventArgs<'TItem when 'TItem : not struct> = 
        class
            inherit CancelEventArgs
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __[CancelEventArgs](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs) __ ControllableItemEventArgs<TItem>
#### Параметры типа
TItem
    Ссылочный тип проверямого элемента.
##  __Конструкторы
[ControllableItemEventArgs<TItem>](M_Tessa_Platform_Collections_ControllableItemEventArgs_1__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Action](P_Tessa_Platform_Collections_ControllableItemEventArgs_1_Action.htm)|
Действие, выполняемое с проверяемым элементом.  
---|---  
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel)| Gets or sets a value indicating
whether the event should be canceled.  
(Унаследован от
[CancelEventArgs](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs))  
[Item](P_Tessa_Platform_Collections_ControllableItemEventArgs_1_Item.htm)|
Проверяемый элемент коллекции.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
