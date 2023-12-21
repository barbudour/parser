# ValidationStorageResultBuilder - класс
Объект, выполняющий построение результата валидации в хранилище
Dictionary<string, object>.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class ValidationStorageResultBuilder : ValidationStorageObject, 
    	IValidationResultBuilder, IReadOnlyList<IValidationResultItem>, IEnumerable<IValidationResultItem>, 
    	IEnumerable, IReadOnlyCollection<IValidationResultItem>, IFormattable, IStorageCleanable, 
    	ICloneable
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class ValidationStorageResultBuilder
    	Inherits ValidationStorageObject
    	Implements IValidationResultBuilder, IReadOnlyList(Of IValidationResultItem), 
    	IEnumerable(Of IValidationResultItem), IEnumerable, IReadOnlyCollection(Of IValidationResultItem), 
    	IFormattable, IStorageCleanable, ICloneable
C++ __Копировать
    [SerializableAttribute]
    public ref class ValidationStorageResultBuilder sealed : public ValidationStorageObject, 
    	IValidationResultBuilder, IReadOnlyList<IValidationResultItem^>, IEnumerable<IValidationResultItem^>, 
    	IEnumerable, IReadOnlyCollection<IValidationResultItem^>, IFormattable, IStorageCleanable, 
    	ICloneable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type ValidationStorageResultBuilder = 
        class
            inherit ValidationStorageObject
            interface IValidationResultBuilder
            interface IReadOnlyList<IValidationResultItem>
            interface IEnumerable<IValidationResultItem>
            interface IEnumerable
            interface IReadOnlyCollection<IValidationResultItem>
            interface IFormattable
            interface IStorageCleanable
            interface ICloneable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm) __[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm) __ ValidationStorageResultBuilder
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>, [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IFormattable](https://learn.microsoft.com/dotnet/api/system.iformattable), [IStorageCleanable](T_Tessa_Platform_Storage_IStorageCleanable.htm), [IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
##  __Конструкторы
[ValidationStorageResultBuilder()](M_Tessa_Platform_Validation_ValidationStorageResultBuilder__ctor.htm)|
Создаёт экземпляр класса и пустое хранилище Dictionary<string, object>,
декоратором для которого является создаваемый объект.  
---|---  
[ValidationStorageResultBuilder(Dictionary<String,
Object>)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder__ctor_1.htm)|
Создаёт экземпляр класса с указанием хранилища, декоратором для которого
является создаваемый объект.  
##  __Свойства
[Count](P_Tessa_Platform_Validation_ValidationStorageResultBuilder_Count.htm)|
Количество элементов в коллекции.  
---|---  
[Item](P_Tessa_Platform_Validation_ValidationStorageResultBuilder_Item.htm)|
Возвращает элемент по заданному индексу.  
[Items](P_Tessa_Platform_Validation_ValidationStorageResultBuilder_Items.htm)|
Список сообщений валидации.  
## __Методы
[Add(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Add.htm)|
Добавляет сообщения валидации, которые были добавлены в заданный объект,
выполняющий построение результата валидации.  
---|---  
[Add(IValidationResultItem)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Add_1.htm)|
Добавляет копию указанного сообщения валидации.  
[Add(ValidationResult)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Add_3.htm)|
Добавляет сообщения о валидации, заданные в указанном результате валидации.  
[Add(ValidationKey, ValidationResultType, String, String, String, String,
String)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Add_2.htm)|
Добавляет информационное сообщение с указанным текстом.  
[Build](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Build.htm)|
Выполняет построение объекта, содержащего результат валидации.  
[Clean](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Clean.htm)|
Выполняет очистку хранилища от избыточных данных.  
[CleanCollectionAndSetNullIfEmpty](M_Tessa_Platform_Storage_StorageObject_CleanCollectionAndSetNullIfEmpty.htm)|
Очищает коллекцию, найденную по ключу key, после чего устанавливает null на
место коллекции, если она стала пустой.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Clear](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Clear.htm)|
Удаляет всю информацию по сообщениям валидации, которая содержится в объекте.  
[ClearCache](M_Tessa_Platform_Storage_StorageObject_ClearCache.htm)|  Очищает
внутренний кэш декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Clone](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Clone.htm)|
Выполняет глубокое клонирование хранилища объекта и возвращает созданный
строго типизированный декоратор для хранилища.  
[ContainsKey](M_Tessa_Platform_Storage_StorageObject_ContainsKey.htm)|
Возвращает признак того, что элемент с заданным ключом содержится в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[EnsureCacheResolved](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_EnsureCacheResolved.htm)|
Инициализирует объект-обёртку для всех значений, в т.ч. для вложенных
объектов. Рекомендуется выполнять при создании заполненного объекта перед
асинхронным обращением к его вложенным объектам.  
(Переопределяет
[StorageObject.EnsureCacheResolved()](M_Tessa_Platform_Storage_StorageObject_EnsureCacheResolved.htm))  
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
[FromJson](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_FromJson.htm)|
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON. Возвращает текущий объект для цепочки вызовов. Рассмотрите
использование метода [Tessa.Platform.Storage.StorageObject.ToTypedJson] для
сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе [Tessa.Platform.Storage.StorageObject.FromTypedJson].  
[FromJsonCore](M_Tessa_Platform_Storage_StorageObject_FromJsonCore.htm)|
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON. Возвращает текущий объект для цепочки вызовов. Рассмотрите
использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе FromTypedJson.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[FromTypedJson](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_FromTypedJson.htm)|
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON с сохранением типов. Используйте метод
[Tessa.Platform.Storage.StorageObject.ToTypedJson] для сериализации с
сохранением типов. Для десериализации других объектов, у которых нет метода
FromTypedJson (например, request/response), используйте метод
[Tessa.Platform.Storage.StorageHelper.DeserializeFromTypedJson], записав
полученную структуру в объект obj.SetStorage(storage).  
[FromTypedJsonCore](M_Tessa_Platform_Storage_StorageObject_FromTypedJsonCore.htm)|
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON с сохранением типов. Используйте метод
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением типов. Для десериализации других объектов, у
которых нет метода FromTypedJson (например, request/response), используйте
метод
[DeserializeFromTypedJson(String)](M_Tessa_Platform_Storage_StorageHelper_DeserializeFromTypedJson.htm),
записав полученную структуру в объект obj.SetStorage(storage).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Get<T>(String)](M_Tessa_Platform_Storage_StorageObject_Get__1.htm)|
Возвращает строго типизированное значение объекта из хранилища по заданному
ключу.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Get<T>(String,
Func<Object>)](M_Tessa_Platform_Storage_StorageObject_Get__1_1.htm)|
Возвращает строго типизированное значение объекта из хранилища по заданнному
ключу с указанием фабрики defaultValueFunc, создающей значение по умолчанию и
добавляющей его в хранилище, если оно было равно null.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetDictionary<T>](M_Tessa_Platform_Storage_StorageObject_GetDictionary__1.htm)|
Возвращает декоратор для коллекции пар ключ / значение, полученный из
хранилища по заданному ключу или созданный посредством заданной фабрики
defaultDictionaryFunc, и добавленный в хранилище, если он там отсутствует.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetEnumerator](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_GetEnumerator.htm)|
Возвращает итератор по элементам коллекции.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetList<T>](M_Tessa_Platform_Storage_StorageObject_GetList__1.htm)|
Возвращает декоратор для коллекции объектов, полученный из хранилища по
заданному ключу или созданный посредством заданной фабрики defaultListFunc, и
добавленный в хранилище, если он там отсутствует.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetObjectData](M_Tessa_Platform_Storage_StorageObject_GetObjectData.htm)|
Записывает сериализованные данные текущего объекта в указанный объект
[System.Runtime.Serialization.SerializationInfo].  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetStorage](M_Tessa_Platform_Storage_StorageObject_GetStorage.htm)|
Возвращает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasData](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_HasData.htm)|
Возвращает признак того, что объект содержит сообщения валидации.  
[Init](M_Tessa_Platform_Storage_StorageObject_Init.htm)|  Инициализирует
значение объекта с заданным ключом, если он отсутствовал в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[InitNotNull](M_Tessa_Platform_Storage_StorageObject_InitNotNull.htm)|
Инициализирует значение объекта с заданным ключом, если он отсутствовал в
хранилище или был равен null, посредством фабрики объектов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Insert](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Insert.htm)|
Вставляет сообщения валидации в позицию index из заданного объекта builder.  
[IsSuccessful](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_IsSuccessful.htm)|
Возвращает признак того, что результат валидации при его построении будет
успешным.  
[IsValid](M_Tessa_Platform_Validation_ValidationStorageObject_IsValid.htm)|
Выполняет проверку объекта на валидность и возвращает признак того, что объект
является валидным.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ObjectCanExistInStorageByKey<T>](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectCanExistInStorageByKey__1.htm)|
Возвращает признак того, что значение, доступное по ключу key, может
содержаться в хранилище и в таком случае должно проходить проверку на
валидность посредством функции valueIsValid, причём значение для проверки
доступно из хранилища по ключу key.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ObjectCanExistInStorageByValue<T>](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectCanExistInStorageByValue__1.htm)|
Возвращает признак того, что значение, доступное по ключу key, может
содержаться в хранилище и в таком случае должно проходить проверку на
валидность посредством функции valueIsValid, причём значение для проверки
определяется по функции, передаваемой первым параметром метода Validate.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ObjectExistsInStorageByKey(String)](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectExistsInStorageByKey.htm)|
Возвращает признак того, что значение, доступное по ключу key, содержится в
хранилище.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ObjectExistsInStorageByKey<T>(String, Func<T,
Boolean>)](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectExistsInStorageByKey__1.htm)|
Возвращает признак того, что значение, доступное по ключу key, содержится в
хранилище и проходит проверку на валидность посредством функции valueIsValid,
причём значение для проверки доступно из хранилища по ключу key.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ObjectExistsInStorageByValue<T>](M_Tessa_Platform_Validation_ValidationStorageObject_ObjectExistsInStorageByValue__1.htm)|
Возвращает признак того, что значение, доступное по ключу key, содержится в
хранилище и проходит проверку на валидность посредством функции valueIsValid,
причём значение для проверки определяется по функции, передаваемой первым
параметром метода Validate.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[Remove(IValidationResultItem)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_Remove.htm)|
Удаляет заданное сообщение валидации. Возвращает признак того, что сообщение
было найдено и удалено.  
[Remove(String)](M_Tessa_Platform_Storage_StorageObject_Remove.htm)|  Удаляет
объект с заданным ключом из хранилища.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[RemoveAll(String)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_RemoveAll.htm)|
Удаляет все сообщения валидации, которые добавлены с заданным сообщением.
Возвращает количество удалённых сообщений.  
[RemoveAll(ValidationKey)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_RemoveAll_1.htm)|
Удаляет все сообщения валидации, которые добавлены с заданным ключом.
Возвращает количество удалённых сообщений.  
[RemoveAt](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_RemoveAt.htm)|
Удаляет сообщение валидации с заданным индексом.  
[RepairStorage](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_RepairStorage.htm)|
Исправляет хранилище объекта, типы в котором установлены некорректно, после
десериализации из JSON. Возвращает признак того, что при исправлении в объекте
были изменения.  
[Set<T>](M_Tessa_Platform_Storage_StorageObject_Set__1.htm)|  Устанавливает
значение в хранилище по заданному ключу. При этом не изменяется внутренний кэш
декораторов, поэтому метод следует использовать только для примитивных типов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetNull](M_Tessa_Platform_Storage_StorageObject_SetNull.htm)|  Устанавливает
значение null для элемента по заданному ключу и удаляет предыдущий элемент из
внутреннего кэша декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetNullIfEmptyEnumerable](M_Tessa_Platform_Storage_StorageObject_SetNullIfEmptyEnumerable.htm)|
Устанавливает равным null элемент с ключом key, если он является пустым
перечислением
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetStorage(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageObject_SetStorage.htm)|
Устанавливает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект, посредством копирования значений из заданного
хранилища. Если текущий объект реализует
[IStorageNotificationReceiver](T_Tessa_Platform_Storage_IStorageNotificationReceiver.htm),
то для него вызывается метод
[NotifyStorageUpdated()](M_Tessa_Platform_Storage_IStorageNotificationReceiver_NotifyStorageUpdated.htm).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetStorage(IStorageObjectProvider)](M_Tessa_Platform_Storage_StorageObject_SetStorage_1.htm)|
Устанавливает хранилище Dictionary<string, object>, декоратором для которого
является текущий объект, посредством копирования значений из хранилища
заданного объекта. Если текущий объект реализует
[IStorageNotificationReceiver](T_Tessa_Platform_Storage_IStorageNotificationReceiver.htm),
то для него вызывается метод
[NotifyStorageUpdated()](M_Tessa_Platform_Storage_IStorageNotificationReceiver_NotifyStorageUpdated.htm).  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[SetStorageValue](M_Tessa_Platform_Storage_StorageObject_SetStorageValue.htm)|
Устанавливает значение объекта, реализующего
[IStorageProvider](T_Tessa_Platform_Storage_IStorageProvider.htm), в хранилище
по заданному ключу. При этом также изменяется внутренний кэш декораторов,
поэтому метод следует использовать для декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ToDynamic](M_Tessa_Platform_Storage_StorageObject_ToDynamic.htm)|  Возвращает
объект, осуществляющий доступ к хранилищу, декоратором для которого является
текущий объект, через позднее связывание.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ToJson](M_Tessa_Platform_Storage_StorageObject_ToJson.htm)|  Сериализует
объект в текстовый JSON. Рассмотрите использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе FromTypedJson.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ToString()](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_ToString.htm)|
Возвращает строковое представление объекта, включающее подробную информацию о
событиях валидации.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
[ToString(String)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_ToString_1.htm)|
Возвращает строковое представление объекта с использованием информации о
форматировании для текущей культуры.  
[ToString(ValidationLevel)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_ToString_3.htm)|
Возвращает текстовое представление для сообщений валидации с указанным режимом
вывода.  
[ToString(String,
IFormatProvider)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_ToString_2.htm)|
Возвращает строковое представление объекта с использованием информации о
форматировании.  
[ToTypedJson](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)|
Сериализует объект в текстовый JSON с сохранением информации по типам для всех
подобъектов, в т.ч. для Info. Используйте метод FromTypedJson для
десериализации. Для сериализации других объектов, у которых нет метода
ToTypedJson (например, request/response), используйте метод
[!:StorageHelper.SerializeToTypedJson(Dictionary<string,object>,bool)],
передав в него структуру объекта obj.GetStorage().  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGet<T>](M_Tessa_Platform_Storage_StorageObject_TryGet__1.htm)|  Возвращает
строго типизированное значение объекта из хранилища по заданному ключу или
default(T), если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetDictionary<T>](M_Tessa_Platform_Storage_StorageObject_TryGetDictionary__1.htm)|
Возвращает строго типизированное значение объекта Dictionary<string, object>
из хранилища по заданному ключу или default(T), если объект по заданному ключу
не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetItems](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_TryGetItems.htm)|
Возвращает список сообщений о валидации или null, если список ещё не был
задан.  
[TryGetList<T>](M_Tessa_Platform_Storage_StorageObject_TryGetList__1.htm)|
Возвращает строго типизированное значение объекта List<object> из хранилища по
заданному ключу или default(T), если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetString](M_Tessa_Platform_Storage_StorageObject_TryGetString.htm)|
Возвращает строковое представление для значения объекта из хранилища по
заданному ключу или null, если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Validate()](M_Tessa_Platform_Validation_ValidationStorageObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationStorageObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm))  
[ValidateInternal](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[ValidationStorageObject.ValidateInternal(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationStorageObject_ValidateInternal.htm))  
##  __Операторы
[ Explicit(ValidationStorageResultBuilder to
ValidationResult)](M_Tessa_Platform_Validation_ValidationStorageResultBuilder_op_Explicit.htm)|
Преобразует заданный объект к типу
[Tessa.Platform.Validation.ValidationResult].  
---|---  
## __Поля
[ItemsKey](F_Tessa_Platform_Validation_ValidationStorageResultBuilder_ItemsKey.htm)|  
---|---  
## __Методы расширения
[AddError](M_Tessa_Platform_Validation_ValidationExtensions_AddError_2.htm)|
Добавляет сообщение об ошибке с заданным текстом. При этом не указывается имя
объекта.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
---|---  
[AddError](M_Tessa_Platform_Validation_ValidationExtensions_AddError.htm)|
Добавляет сообщение об ошибке с заданным текстом.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddError](M_Tessa_Platform_Validation_ValidationExtensions_AddError_1.htm)|
Добавляет сообщение об ошибке с текстом, форматирование которого выполняется.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddException](M_Tessa_Platform_Validation_ValidationExtensions_AddException.htm)|
Добавляет информацию по исключению.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddInfo](M_Tessa_Platform_Validation_ValidationExtensions_AddInfo_2.htm)|
Добавляет информационное сообщение с заданным текстом. При этом не указывается
имя объекта.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddInfo](M_Tessa_Platform_Validation_ValidationExtensions_AddInfo.htm)|
Добавляет информационное сообщение с заданным текстом.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddInfo](M_Tessa_Platform_Validation_ValidationExtensions_AddInfo_1.htm)|
Добавляет информационное сообщение с текстом, форматирование которого
выполняется.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddInstanceNotFoundError](M_Tessa_Cards_CardExtensions_AddInstanceNotFoundError.htm)|
Добавляет ошибку валидации
[InstanceNotFound](F_Tessa_Cards_CardValidationKeys_InstanceNotFound.htm) с
информацией по стеку вызовов, если это разрешено флагами flags.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[AddRange](M_Tessa_Platform_Validation_ValidationExtensions_AddRange.htm)|
Добавляет сообщения валидации items в список сообщений объекта builder.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddRange](M_Tessa_Platform_Validation_ValidationExtensions_AddRange_1.htm)|
Добавляет сообщения валидации items в список сообщений объекта builder.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddWarning](M_Tessa_Platform_Validation_ValidationExtensions_AddWarning_2.htm)|
Добавляет предупреждение с заданным текстом. При этом не указывается имя
объекта.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddWarning](M_Tessa_Platform_Validation_ValidationExtensions_AddWarning.htm)|
Добавляет предупреждение с заданным текстом.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AddWarning](M_Tessa_Platform_Validation_ValidationExtensions_AddWarning_1.htm)|
Добавляет предупреждение с текстом, форматирование которого выполняется.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[AsArray<IValidationResultItem>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[BeginSequence](M_Tessa_Platform_Validation_ValidationExtensions_BeginSequence.htm)|
Создаёт последовательность валидации и возвращает объект, позволяющий
добавлять сообщения валидации. Метод удобен для использования в блоках
using(var validator = validationResult.BeginSequence()) { ... }. Вызов метода
аналогичен вызову
[Begin(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationSequence_Begin.htm).  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
[ConvertToListDictionaries<IValidationResultItem>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<IValidationResultItem>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<IValidationResultItem>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<IValidationResultItem, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[LastIndexOf<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[LastIndexOf<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1_1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IValidationResultItem,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IValidationResultItem,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<IValidationResultItem>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<IValidationResultItem>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<IValidationResultItem>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<IValidationResultItem, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<IValidationResultItem>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<IValidationResultItem>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)
