# CardTypePriorityComparer - класс
Объект, выполняющий упорядочивание карточек в соответствии с их типом.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow](N_Tessa_Extensions_Default_Shared_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardTypePriorityComparer : Comparer<Card>, 
    	ICardTypePriorityComparer, IComparer<Card>
VB __Копировать
     Public NotInheritable Class CardTypePriorityComparer
    	Inherits Comparer(Of Card)
    	Implements ICardTypePriorityComparer, IComparer(Of Card)
C++ __Копировать
     public ref class CardTypePriorityComparer sealed : public Comparer<Card^>, 
    	ICardTypePriorityComparer, IComparer<Card^>
F# __Копировать
     [<SealedAttribute>]
    type CardTypePriorityComparer = 
        class
            inherit Comparer<Card>
            interface ICardTypePriorityComparer
            interface IComparer<Card>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Comparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.comparer-1)<[Card](T_Tessa_Cards_Card.htm)> __ CardTypePriorityComparer
Implements
    [IComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.icomparer-1)<[Card](T_Tessa_Cards_Card.htm)>, [ICardTypePriorityComparer](T_Tessa_Extensions_Default_Shared_Workflow_ICardTypePriorityComparer.htm)
##  __Заметки
Реализует сортировку по убыванию.
##  __Конструкторы
[CardTypePriorityComparer](M_Tessa_Extensions_Default_Shared_Workflow_CardTypePriorityComparer__ctor.htm)|
Инициализирует новый экземпляр класса CardTypePriorityComparer.  
---|---  
## __Свойства
[Order](P_Tessa_Extensions_Default_Shared_Workflow_CardTypePriorityComparer_Order.htm)|
Словарь, содержащий порядок сортировки типов карточек. Ключ - тип карточки.
Значение - порядок сортировки.  
---|---  
## __Методы
[Compare](M_Tessa_Extensions_Default_Shared_Workflow_CardTypePriorityComparer_Compare.htm)|
When overridden in a derived class, performs a comparison of two objects of
the same type and returns a value indicating whether one object is less than,
equal to, or greater than the other.  
(Переопределяет [Comparer<T>.Compare(T,
T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.comparer-1.compare#system-
collections-generic-comparer-1-compare\(-0-0\)))  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Extensions.Default.Shared.Workflow - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow.htm)
