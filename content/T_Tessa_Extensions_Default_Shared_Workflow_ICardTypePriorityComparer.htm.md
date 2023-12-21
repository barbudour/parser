# ICardTypePriorityComparer - интерфейс
Объект, выполняющий упорядочивание карточек в соответствии с их типом.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow](N_Tessa_Extensions_Default_Shared_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTypePriorityComparer : IComparer<Card>
VB __Копировать
     Public Interface ICardTypePriorityComparer
    	Inherits IComparer(Of Card)
C++ __Копировать
     public interface class ICardTypePriorityComparer : IComparer<Card^>
F# __Копировать
     type ICardTypePriorityComparer = 
        interface
            interface IComparer<Card>
        end
Implements
    [IComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.icomparer-1)<[Card](T_Tessa_Cards_Card.htm)>
##  __Свойства
[Order](P_Tessa_Extensions_Default_Shared_Workflow_ICardTypePriorityComparer_Order.htm)|
Словарь, содержащий порядок сортировки типов карточек. Ключ - тип карточки.
Значение - порядок сортировки.  
---|---  
## __Методы
[Compare](https://learn.microsoft.com/dotnet/api/system.collections.generic.icomparer-1.compare#system-
collections-generic-icomparer-1-compare\(-0-0\))| Compares two objects and
returns a value indicating whether one is less than, equal to, or greater than
the other.  
(Унаследован от
[IComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.icomparer-1)<[Card](T_Tessa_Cards_Card.htm)>)  
---|---  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow.htm)
