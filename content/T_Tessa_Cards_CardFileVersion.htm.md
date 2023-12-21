# CardFileVersion - класс
Информация о версии файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardFileVersion : CardStorageObject
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardFileVersion
    	Inherits CardStorageObject
C++ __Копировать
    [SerializableAttribute]
    public ref class CardFileVersion sealed : public CardStorageObject
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardFileVersion = 
        class
            inherit CardStorageObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm) __[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm) __[CardStorageObject](T_Tessa_Cards_CardStorageObject.htm) __ CardFileVersion
##  __Конструкторы
[CardFileVersion()](M_Tessa_Cards_CardFileVersion__ctor.htm)|  Создаёт
экземпляр класса и пустое хранилище Dictionary<string, object>, декоратором
для которого является создаваемый объект.  
---|---  
[CardFileVersion(Dictionary<String,
Object>)](M_Tessa_Cards_CardFileVersion__ctor_1.htm)| Создаёт экземпляр класса
с указанием хранилища, декоратором для которого является создаваемый объект.  
[CardFileVersion(IStorageObjectProvider)](M_Tessa_Cards_CardFileVersion__ctor_2.htm)|
Создаёт экземпляр класса с указанием объекта, предоставляющего доступ к
хранилищу, декоратором для которого является создаваемый объект.  
## __Свойства
[Created](P_Tessa_Cards_CardFileVersion_Created.htm)|  Дата создания версии
(изменения файла).  
---|---  
[CreatedByID](P_Tessa_Cards_CardFileVersion_CreatedByID.htm)|  Идентификатор
пользователя, создавшего версию (изменившего файл).  
[CreatedByName](P_Tessa_Cards_CardFileVersion_CreatedByName.htm)|  Имя
пользователя, создавшего версию (изменившего файл).  
[ErrorDate](P_Tessa_Cards_CardFileVersion_ErrorDate.htm)|  Дата ошибки,
произошедшей для версии файла, или null, если ошибок не было.  
[ErrorMessage](P_Tessa_Cards_CardFileVersion_ErrorMessage.htm)|  Сообщение об
ошибке, произошедшей для версии файла, или null, если ошибок не было.  
[Hash](P_Tessa_Cards_CardFileVersion_Hash.htm)|  Хеш контента для сохранённой
версии файла или null, если версия файла новая или хеш не указан. По умолчанию
значение равно null, при этом для новых версий хеш считается не заданным.
Изменение этого значения позволяет установить другой хеш для использования в
расширениях, но не позволяет изменить хеш у версии. Для установки хеша
создаваемой версии укажите свойство [Hash](P_Tessa_Cards_CardFile_Hash.htm).  
[LinkID](P_Tessa_Cards_CardFileVersion_LinkID.htm)|  Внешний идентификатор
версии файла или null, если такой идентификатор не задан. Может использоваться
в расширениях для связи с содержимым во внешнем местоположении.  
[Name](P_Tessa_Cards_CardFileVersion_Name.htm)|  Имя версии файла.  
[Number](P_Tessa_Cards_CardFileVersion_Number.htm)|  Номер версии файла,
отсчитываемый от единицы.  
[Options](P_Tessa_Cards_CardFileVersion_Options.htm)|  Сериализованные в JSON
настройки файла. Могут быть равны null или пустой строке, если настройки не
заданы.  
[RequestInfo](P_Tessa_Cards_CardFileVersion_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запрос
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm) и в
запрос на загрузку списка подписей
[GetVersionSignatures](F_Tessa_Cards_CardRequestTypes_GetVersionSignatures.htm).  
[RowID](P_Tessa_Cards_CardFileVersion_RowID.htm)|  Идентификатор версии файла.  
[Size](P_Tessa_Cards_CardFileVersion_Size.htm)|  Размер контента в байтах для
версии файла.  
[Source](P_Tessa_Cards_CardFileVersion_Source.htm)|  Местоположение контента
версии файла.  
[State](P_Tessa_Cards_CardFileVersion_State.htm)|  Состояние версии файла.  
[Tags](P_Tessa_Cards_CardFileVersion_Tags.htm)|  Теги версии файла. Могут быть
равны null или пустой строке, если теги не заданы.  
## __Методы
[AddTag](M_Tessa_Cards_CardFileVersion_AddTag.htm)|  Добавляет заданный тег в
список тегов, соответствующих текущей версии файла
[Tags](P_Tessa_Cards_CardFileVersion_Tags.htm). Возвращает признак того, что
тег отсутствовал и был добавлен.  
---|---  
[Clean](M_Tessa_Cards_CardFileVersion_Clean.htm)| Выполняет очистку хранилища
от избыточных данных.  
(Переопределяет
[CardStorageObject.Clean()](M_Tessa_Cards_CardStorageObject_Clean.htm))  
[CleanCollectionAndSetNullIfEmpty](M_Tessa_Platform_Storage_StorageObject_CleanCollectionAndSetNullIfEmpty.htm)|
Очищает коллекцию, найденную по ключу key, после чего устанавливает null на
место коллекции, если она стала пустой.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ClearCache](M_Tessa_Platform_Storage_StorageObject_ClearCache.htm)|  Очищает
внутренний кэш декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ContainsKey](M_Tessa_Platform_Storage_StorageObject_ContainsKey.htm)|
Возвращает признак того, что элемент с заданным ключом содержится в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[DeserializeOptions](M_Tessa_Cards_CardFileVersion_DeserializeOptions.htm)|
Десериализует настройки [Options](P_Tessa_Cards_CardFileVersion_Options.htm).
Возвращаемый объект не равен null. Если настройки не заданы, то возвращается
пустой объект.  
[EnsureCacheResolved](M_Tessa_Cards_CardFileVersion_EnsureCacheResolved.htm)|
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
[FromJsonCore](M_Tessa_Platform_Storage_StorageObject_FromJsonCore.htm)|
Устанавливает содержимое объекта в соответствии с данными, десериализованными
из текстового JSON. Возвращает текущий объект для цепочки вызовов. Рассмотрите
использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе FromTypedJson.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
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
[HasTag](M_Tessa_Cards_CardFileVersion_HasTag.htm)|  Возвращает признак того,
что текущая версия содержит указанный тег в свойстве
[Tags](P_Tessa_Cards_CardFileVersion_Tags.htm).  
[Init](M_Tessa_Platform_Storage_StorageObject_Init.htm)|  Инициализирует
значение объекта с заданным ключом, если он отсутствовал в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[InitNotNull](M_Tessa_Platform_Storage_StorageObject_InitNotNull.htm)|
Инициализирует значение объекта с заданным ключом, если он отсутствовал в
хранилище или был равен null, посредством фабрики объектов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[IsEmpty](M_Tessa_Cards_CardFileVersion_IsEmpty.htm)|  Возвращает признак
того, что объект не содержит значимых данных для метода очистки
[Tessa.Platform.Storage.IStorageCleanable.Clean].  
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
[Remove](M_Tessa_Platform_Storage_StorageObject_Remove.htm)|  Удаляет объект с
заданным ключом из хранилища.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[RemoveTag](M_Tessa_Cards_CardFileVersion_RemoveTag.htm)|  Удаляет заданный
тег из списка тегов, соответствующих текущей версии файла
[Tags](P_Tessa_Cards_CardFileVersion_Tags.htm). Возвращает признак того, что
тег присутствовал и был удалён.  
[RepairStorage](M_Tessa_Cards_CardFileVersion_RepairStorage.htm)|  Исправляет
хранилище объекта, типы в котором установлены некорректно, после
десериализации из JSON. Возвращает признак того, что при исправлении в объекте
были изменения.  
[Set(CardFileVersion)](M_Tessa_Cards_CardFileVersion_Set.htm)|  Устанавливает
свойства текущего объекта в соответствии с заданной версией файла.  
[Set<T>(String, T)](M_Tessa_Platform_Storage_StorageObject_Set__1.htm)|
Устанавливает значение в хранилище по заданному ключу. При этом не изменяется
внутренний кэш декораторов, поэтому метод следует использовать только для
примитивных типов.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[TryGetList<T>](M_Tessa_Platform_Storage_StorageObject_TryGetList__1.htm)|
Возвращает строго типизированное значение объекта List<object> из хранилища по
заданному ключу или default(T), если объект по заданному ключу не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetRequestInfo](M_Tessa_Cards_CardFileVersion_TryGetRequestInfo.htm)|
Возвращает дополнительную пользовательскую информацию по текущему объекту,
передаваемую в запрос
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm) и в
запрос на загрузку списка подписей
[GetVersionSignatures](F_Tessa_Cards_CardRequestTypes_GetVersionSignatures.htm),
или null, если информация ещё не была задана.  
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
[ValidateInternal](M_Tessa_Cards_CardFileVersion_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[ValidationStorageObject.ValidateInternal(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationStorageObject_ValidateInternal.htm))  
##  __Поля
[CreatedByIDKey](F_Tessa_Cards_CardFileVersion_CreatedByIDKey.htm)|  
---|---  
[CreatedByNameKey](F_Tessa_Cards_CardFileVersion_CreatedByNameKey.htm)|  
[CreatedKey](F_Tessa_Cards_CardFileVersion_CreatedKey.htm)|  
[ErrorDateKey](F_Tessa_Cards_CardFileVersion_ErrorDateKey.htm)|  
[ErrorMessageKey](F_Tessa_Cards_CardFileVersion_ErrorMessageKey.htm)|  
[HashKey](F_Tessa_Cards_CardFileVersion_HashKey.htm)|  
[LinkIDKey](F_Tessa_Cards_CardFileVersion_LinkIDKey.htm)|  
[NameKey](F_Tessa_Cards_CardFileVersion_NameKey.htm)|  
[NumberKey](F_Tessa_Cards_CardFileVersion_NumberKey.htm)|  
[OptionsKey](F_Tessa_Cards_CardFileVersion_OptionsKey.htm)|  
[RequestInfoKey](F_Tessa_Cards_CardFileVersion_RequestInfoKey.htm)|  
[RowIDKey](F_Tessa_Cards_CardFileVersion_RowIDKey.htm)|  
[SizeKey](F_Tessa_Cards_CardFileVersion_SizeKey.htm)|  
[SourceKey](F_Tessa_Cards_CardFileVersion_SourceKey.htm)|  
[StateKey](F_Tessa_Cards_CardFileVersion_StateKey.htm)|  
[TagsKey](F_Tessa_Cards_CardFileVersion_TagsKey.htm)|  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
