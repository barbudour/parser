# StorageHelper.Merge(IEnumerable, IList) - метод
Выполняет слияние данных из хранилища source в коллекцию объектов target.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void Merge(
    	IEnumerable source,
    	IList target
    )
VB __Копировать
     Public Shared Sub Merge ( 
    	source As IEnumerable,
    	target As IList
    )
C++ __Копировать
     public:
    static void Merge(
    	IEnumerable^ source, 
    	IList^ target
    )
F# __Копировать
     static member Merge : 
            source : IEnumerable * 
            target : IList -> unit 
#### Параметры
source
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
    Хранилище, из которого выбираются данные.
target
[IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist)
     Коллекция объектов, для которой выполняется слияние данных с данными из заданного хранилища. 
## __Заметки
Не производится удаление имеющихся в target данных перед копированием.
При слиянии вложенных коллекций в target данные этих коллекций сливаются с
данными из соответствующих коллекций source, причём данные из source всегда
перезаписывают данные из target.
Если сливается коллекция объектов
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
из source с коллекцией
[IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist) или
IList<object> (а не две коллекции ключ / значение IDictionary<string,
object>), то всегда выполняется копирование объектов из source в target без
проверки существования таких объектов.
##  __См. также
#### Ссылки
[StorageHelper - ](T_Chronos_Platform_StorageHelper.htm)
[Merge - перегрузка](Overload_Chronos_Platform_StorageHelper_Merge.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
