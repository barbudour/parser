# StorageHelper.Merge(IDictionary<String, Object>, IDictionary<String,
Object>, Boolean) - метод
Выполняет слияние данных из хранилища source в коллекцию ключ / значение
target.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static void Merge(
    	IDictionary<string, Object> source,
    	IDictionary<string, Object> target,
    	bool allowOverrides = false
    )
VB __Копировать
     Public Shared Sub Merge ( 
    	source As IDictionary(Of String, Object),
    	target As IDictionary(Of String, Object),
    	Optional allowOverrides As Boolean = false
    )
C++ __Копировать
     public:
    static void Merge(
    	IDictionary<String^, Object^>^ source, 
    	IDictionary<String^, Object^>^ target, 
    	bool allowOverrides = false
    )
F# __Копировать
     static member Merge : 
            source : IDictionary<string, Object> * 
            target : IDictionary<string, Object> * 
            ?allowOverrides : bool 
    (* Defaults:
            let _allowOverrides = defaultArg allowOverrides false
    *)
    -> unit 
#### Параметры
source
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, из которого выбираются данные.
target
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
     Коллекция ключ / значение, для которой выполняется слияние данных с данными из заданного хранилища. 
allowOverrides
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что разрешено перезаписывание ключей при объединении посредством суффиксов [OverrideSuffix](F_Chronos_Platform_StorageHelper_OverrideSuffix.htm). 
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
