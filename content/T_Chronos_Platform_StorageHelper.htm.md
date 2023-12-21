# StorageHelper - класс
Хэлперы для взаимодействия с хранилищем.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class StorageHelper
VB __Копировать
     Public NotInheritable Class StorageHelper
C++ __Копировать
     public ref class StorageHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type StorageHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ StorageHelper
##  __Методы
[Merge(IEnumerable, IList)](M_Chronos_Platform_StorageHelper_Merge_1.htm)|
Выполняет слияние данных из хранилища source в коллекцию объектов target.  
---|---  
[Merge(IDictionary<String, Object>, IDictionary<String, Object>,
Boolean)](M_Chronos_Platform_StorageHelper_Merge.htm)|  Выполняет слияние
данных из хранилища source в коллекцию ключ / значение target.  
## __Поля
[OverrideSuffix](F_Chronos_Platform_StorageHelper_OverrideSuffix.htm)|  Если
ключ в хеш-таблице заканчивается на этот суффикс, то при объединении структуры
объектов посредством методов Merge значение по этому ключу перезаписывает
значение в исходном объекте, а не объединяется с ним. При этом суффикс
удаляется из ключа.  
---|---  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
