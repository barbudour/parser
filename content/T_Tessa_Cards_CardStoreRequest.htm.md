# CardStoreRequest - класс
Запрос на сохранение информации по карточке посредством сервиса карточек.
Содержит только изменённую информацию о карточке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class CardStoreRequest : CardInfoStorageObject, 
    	ICloneable
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class CardStoreRequest
    	Inherits CardInfoStorageObject
    	Implements ICloneable
C++ __Копировать
    [SerializableAttribute]
    public ref class CardStoreRequest sealed : public CardInfoStorageObject, 
    	ICloneable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type CardStoreRequest = 
        class
            inherit CardInfoStorageObject
            interface ICloneable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm) __[ValidationStorageObject](T_Tessa_Platform_Validation_ValidationStorageObject.htm) __[CardStorageObject](T_Tessa_Cards_CardStorageObject.htm) __[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm) __ CardStoreRequest
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)
##  __Конструкторы
[CardStoreRequest()](M_Tessa_Cards_CardStoreRequest__ctor.htm)|  Создаёт
экземпляр класса и пустое хранилище Dictionary<string, object>, декоратором
для которого является создаваемый объект.  
---|---  
[CardStoreRequest(Dictionary<String,
Object>)](M_Tessa_Cards_CardStoreRequest__ctor_1.htm)| Создаёт экземпляр
класса с указанием хранилища, декоратором для которого является создаваемый
объект.  
[CardStoreRequest(IStorageObjectProvider)](M_Tessa_Cards_CardStoreRequest__ctor_2.htm)|
Создаёт экземпляр класса с указанием объекта, предоставляющего доступ к
хранилищу, декоратором для которого является создаваемый объект.  
## __Свойства
[AffectVersion](P_Tessa_Cards_CardStoreRequest_AffectVersion.htm)|  Признак
того, что изменение карточки будет принудительно выполняться с проверкой её
версии и приведёт к увеличению номера версии, даже если отсутствуют изменяемые
значения в основной карточке или её файлах. Изменение заданий не приводит к
проверке и увеличению версии, только если этот флаг установлен в false. Этот
флаг менее приоритетный, чем
[DoesNotAffectVersion](P_Tessa_Cards_CardStoreRequest_DoesNotAffectVersion.htm).  
---|---  
[Card](P_Tessa_Cards_CardStoreRequest_Card.htm)|  Карточка.  
[DoesNotAffectVersion](P_Tessa_Cards_CardStoreRequest_DoesNotAffectVersion.htm)|
Признак того, что изменение карточки не приведёт к проверке версии и к
увеличению номера версии, даже если присутствуют изменяемые значения в
основной карточке или её файлах. При первом сохранении карточки версия всё
равно увеличивается до 1. Этот флаг более приоритетный, чем
[AffectVersion](P_Tessa_Cards_CardStoreRequest_AffectVersion.htm).  
[Dynamic](P_Tessa_Cards_CardInfoStorageObject_Dynamic.htm)|  Объект,
осуществляющий доступ к текущему объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[DynamicInfo](P_Tessa_Cards_CardInfoStorageObject_DynamicInfo.htm)|  Объект,
осуществляющий доступ к дополнительной пользовательской информации по текущему
объекту через позднее связывание свойств.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[FileMapping](P_Tessa_Cards_CardStoreRequest_FileMapping.htm)|  Маппинг для
контента сохраняемых файлов. Значение актуально задавать при сохранении
карточки с контентом файлов, которые являются виртуальными, т.е. принадлежат
другой карточке.  
[ForceReleaseLock](P_Tessa_Cards_CardStoreRequest_ForceReleaseLock.htm)|
Признак того, что для карточки будет принудительно закрыта блокировка на
запись даже в том случае, если она не должна быть закрыта. Этот флаг имеет
смысл только в том случае, когда
[Method](P_Tessa_Cards_CardStoreRequest_Method.htm) равен
[Restore](T_Tessa_Cards_CardStoreMethod.htm). Актуально, например, при
восстановлении карточки-сателлита.  
[ForceTransaction](P_Tessa_Cards_CardStoreRequest_ForceTransaction.htm)|
Признак того, что для карточки будет принудительно открыта транзакция даже в
том случае, если изменения карточки отсутствуют. Это позволит гарантировать,
что расширения внутри транзакции будут выполнены. При отсутствии других
изменений в карточке транзакция будет открыта без блокировки.  
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)|  Дополнительная
пользовательская информация.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[Method](P_Tessa_Cards_CardStoreRequest_Method.htm)|  Способ сохранения
карточки.  
[ServiceType](P_Tessa_Cards_CardStoreRequest_ServiceType.htm)|  Тип сервиса,
от которого был получен текущий объект запроса. Позволяет определить
надёжность данных в запросе. При сериализации значение не передаётся с клиента
на сервер. Это свойство используется платформой, не рекомендуется
устанавливать его значение вручную.  
## __Методы
[Clean](M_Tessa_Cards_CardStoreRequest_Clean.htm)| Выполняет очистку хранилища
от избыточных данных.  
(Переопределяет
[CardInfoStorageObject.Clean()](M_Tessa_Cards_CardInfoStorageObject_Clean.htm))  
---|---  
[CleanCollectionAndSetNullIfEmpty](M_Tessa_Platform_Storage_StorageObject_CleanCollectionAndSetNullIfEmpty.htm)|
Очищает коллекцию, найденную по ключу key, после чего устанавливает null на
место коллекции, если она стала пустой.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[ClearCache](M_Tessa_Platform_Storage_StorageObject_ClearCache.htm)|  Очищает
внутренний кэш декораторов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[Clone](M_Tessa_Cards_CardStoreRequest_Clone.htm)|  Выполняет глубокое
клонирование хранилища объекта и возвращает созданный строго типизированный
декоратор для хранилища.  
[ContainsKey](M_Tessa_Platform_Storage_StorageObject_ContainsKey.htm)|
Возвращает признак того, что элемент с заданным ключом содержится в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[EnsureCacheResolved](M_Tessa_Cards_CardStoreRequest_EnsureCacheResolved.htm)|
Инициализирует объект-обёртку для всех значений, в т.ч. для вложенных
объектов. Рекомендуется выполнять при создании заполненного объекта перед
асинхронным обращением к его вложенным объектам.  
(Переопределяет
[CardInfoStorageObject.EnsureCacheResolved()](M_Tessa_Cards_CardInfoStorageObject_EnsureCacheResolved.htm))  
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
[FromPlainJsonWithRepairAsync](M_Tessa_Cards_CardStoreRequest_FromPlainJsonWithRepairAsync.htm)|
Устанавливает содержимое запроса в соответствии с данными, десериализованными
из текстового JSON. Типы произвольных данных
[Info](P_Tessa_Platform_Storage_InfoStorageObject_Info.htm) для карточки,
файлов и заданий могут быть искажены, т.к. информация об их структуре
неизвестна объекту. В JSON все типы запроса десериализуются как
[String](https://learn.microsoft.com/dotnet/api/system.string),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Int64](https://learn.microsoft.com/dotnet/api/system.int64) и
[Double](https://learn.microsoft.com/dotnet/api/system.double). Возвращает
текущий запрос для цепочки вызовов. Рассмотрите использование метода
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением полной информации по типам, которую можно будет
восстановить в методе
[FromTypedJson(String)](M_Tessa_Cards_CardStoreRequest_FromTypedJson.htm).  
[FromTypedJson](M_Tessa_Cards_CardStoreRequest_FromTypedJson.htm)|
Устанавливает содержимое запроса в соответствии с данными, десериализованными
из текстового JSON с сохранением типов. Используйте метод
[ToTypedJson(Boolean)](M_Tessa_Platform_Storage_StorageObject_ToTypedJson.htm)
для сериализации с сохранением типов. Для десериализации других объектов, у
которых нет метода FromTypedJson (например, request/response), используйте
метод
[DeserializeFromTypedJson(String)](M_Tessa_Platform_Storage_StorageHelper_DeserializeFromTypedJson.htm),
записав полученную структуру в объект obj.SetStorage(storage).  
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
[Init](M_Tessa_Platform_Storage_StorageObject_Init.htm)|  Инициализирует
значение объекта с заданным ключом, если он отсутствовал в хранилище.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[InitNotNull](M_Tessa_Platform_Storage_StorageObject_InitNotNull.htm)|
Инициализирует значение объекта с заданным ключом, если он отсутствовал в
хранилище или был равен null, посредством фабрики объектов.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
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
[RemoveSystemInfo](M_Tessa_Cards_CardInfoStorageObject_RemoveSystemInfo.htm)|
Удаляет системную информацию, которая может располагаться в любом месте в
хранилище текущего объекта и может быть найдена по ключам с префиксом
[SystemKeyPrefix](F_Tessa_Cards_CardHelper_SystemKeyPrefix.htm).
Внимание! После выполнения метода из карточки исчезнут важные сведения, такие
как информация об изменённых полях или о состоянии строк коллекционных и
древовидных секций.
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[RemoveUserInfo](M_Tessa_Cards_CardInfoStorageObject_RemoveUserInfo.htm)|
Удаляет пользовательскую информацию, которая может располагаться в любом месте
в хранилище текущего объекта и может быть найдена по ключам с префиксом
[UserKeyPrefix](F_Tessa_Cards_CardHelper_UserKeyPrefix.htm).  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
[RepairStorageAsync](M_Tessa_Cards_CardStoreRequest_RepairStorageAsync.htm)|
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
[TryGetCard](M_Tessa_Cards_CardStoreRequest_TryGetCard.htm)|  Возвращает
карточку или null, если карточка не была задана.  
[TryGetDictionary<T>](M_Tessa_Platform_Storage_StorageObject_TryGetDictionary__1.htm)|
Возвращает строго типизированное значение объекта Dictionary<string, object>
из хранилища по заданному ключу или default(T), если объект по заданному ключу
не найден.  
(Унаследован от [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm))  
[TryGetFileMapping](M_Tessa_Cards_CardStoreRequest_TryGetFileMapping.htm)|
Возвращает маппинг для контента сохраняемых файлов или null, если маппинг ещё
не был задан. Значение актуально задавать при сохранении карточки с контентом
файлов, которые являются виртуальными, т.е. принадлежат другой карточке.  
[TryGetInfo](M_Tessa_Cards_CardInfoStorageObject_TryGetInfo.htm)|  Возвращает
дополнительную пользовательскую информацию по текущему объекту или null, если
информация ещё не была задана.  
(Унаследован от
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm))  
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
[ValidateInternal](M_Tessa_Cards_CardStoreRequest_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[CardInfoStorageObject.ValidateInternal(IValidationResultBuilder)](M_Tessa_Cards_CardInfoStorageObject_ValidateInternal.htm))  
##  __Поля
[AffectVersionKey](F_Tessa_Cards_CardStoreRequest_AffectVersionKey.htm)|  
---|---  
[CardKey](F_Tessa_Cards_CardStoreRequest_CardKey.htm)|  
[DoesNotAffectVersionKey](F_Tessa_Cards_CardStoreRequest_DoesNotAffectVersionKey.htm)|  
[FileMappingKey](F_Tessa_Cards_CardStoreRequest_FileMappingKey.htm)|  
[ForceReleaseLockKey](F_Tessa_Cards_CardStoreRequest_ForceReleaseLockKey.htm)|  
[ForceTransactionKey](F_Tessa_Cards_CardStoreRequest_ForceTransactionKey.htm)|  
[SystemMethodKey](F_Tessa_Cards_CardStoreRequest_SystemMethodKey.htm)|  
## __Методы расширения
[AddKrProcessClientCommands](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_AddKrProcessClientCommands.htm)|
Добавляет в указанное хранилище список клиентских команд.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
---|---  
[AreButtonsIgnored](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_AreButtonsIgnored.htm)|
Получает из заданного хранилища значение флага показывающего, что при загрузке
карточки не надо добавлять в ответ информацию по тайлам вторичных процессов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[ConsiderHiddenStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_ConsiderHiddenStages.htm)|
Возвращает значение, показывающее, что в карточку должны быть загружены
скрытые этапы маршрута.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[ConsiderSkippedStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_ConsiderSkippedStages.htm)|
Возвращает значение из заданного хранилища, показывающее, требуется ли
отображать пропущенные этапы.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[DontHideStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_DontHideStages_1.htm)|
Добавляет в указанное хранилище значение, показывающее, необходимо ли
загружать в карточку скрытые этапы маршрута или нет.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[GetADFSAuthenticationResponse](M_Tessa_Cards_CardRequestExtensions_GetADFSAuthenticationResponse.htm)|
Возвращает сериализованную в XML информацию в виде строки, которая получена
при автоматическом создании сотрудника средствами ADFS, или null, если не
выполняется автоматическое создание сотрудника.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[GetForbidStoringHistory](M_Tessa_Cards_CardRequestExtensions_GetForbidStoringHistory_4.htm)|
Возвращает запрет на сохранение данных о сохраняемой карточке в историю
действий с карточкой.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[GetHasRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetHasRecalcChanges.htm)|
Возвращает значение, показывающее, что после пересчёта были изменения в
маршруте или нет. Информация добавляется только при выставленном флаге
[HasChangesToInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_InfoAboutChanges.htm).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetIgnorePermissionsWarning](M_Tessa_Cards_CardRequestExtensions_GetIgnorePermissionsWarning.htm)|
Возвращает признак того, что при сохранении карточки могут быть не указаны
токены безопасности, поэтому не следует показывать соответствующее
предупреждение. Если признак не был установлен, то возвращается false.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[GetInfoAboutChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetInfoAboutChanges_1.htm)|
Возвращает режим вывода информации об изменениях в маршруте после пересчёта
или значение по умолчанию для типа, если хранилище его не содержало.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetKrProcessClientCommands](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessClientCommands_1.htm)|
Возвращает из указанного хранилища список клиентских команд или значение по
умолчанию для типа, если оно их не содержало.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetKrProcessInstance](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessInstance.htm)|
Возвращает информацию об экземпляре процесса из указанного хранилища.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetKrProcessLaunchResult](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessLaunchResult.htm)|
Возвращает объект содержащий результат запуска процесса или значение по
умолчанию для типа, если указанный объект его не содержит.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetLocalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetNoLockingMainCard](M_Tessa_Cards_CardRequestExtensions_GetNoLockingMainCard_1.htm)|
Возвращает признак того, что не следует выполнять блокировку основной карточки
при создании или изменении сателлита.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[GetRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetRecalcChanges.htm)|
Возвращает информацию о различиях в маршруте до и после пересчёта.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetRecalcFlag](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetRecalcFlag_1.htm)|
Возвращает значение, показывающее, должен ли быть выполнен пересчёт маршрута
или нет.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[GetStartingSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStartingSecondaryProcess.htm)|
Возвращает из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[IgnoreButtons](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_IgnoreButtons.htm)|
Устанавливает значение, показывающее, что при загрузке карточки не надо
добавлять в ответ информацию по тайлам вторичных процессов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[IgnoreKrSatellite](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_IgnoreKrSatellite.htm)|
Устанавливает значение, показывающее, что при загрузке карточки не надо
загружать и обрабатывать информацию содержащуюся в основном сателлите
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
карточки.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IsADFSAuthenticationResponseExists](M_Tessa_Cards_CardRequestExtensions_IsADFSAuthenticationResponseExists.htm)|
Возвращает признак того, что в заданном запросе автоматически создаётся
сотрудник при входе в ADFS, т.е. при успешной авторизации по ADFS для
сотрудника, отсутствующего в Tessa, создаётся и заполняется карточка.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[IsKrSatelliteIgnored](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_IsKrSatelliteIgnored.htm)|
Возвращает значение, показывающее, что при загрузке карточки не надо загружать
и обрабатывать информацию содержащуюся в основном сателлите
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
карточки.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[RemoveLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveLocalTiles.htm)|
Удаляет из заданного хранилища информацию по локальным тайлам маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[RemoveSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveSecondaryProcess.htm)|
Удаляет из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса добавленную
[SetStartingSecondaryProcess(CardInfoStorageObject,
StartingSecondaryProcessInfo)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingSecondaryProcess.htm).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[RemoveStartingProcessTaskGroupRowID](M_Tessa_Cards_Workflow_WorkflowExtensions_RemoveStartingProcessTaskGroupRowID.htm)|
Удаляет идентификатор группы в истории заданий для первого задания бизнес-
процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).
Это определяет, что будет использована группа по умолчанию.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SetAddToRolesIDList](M_Tessa_Cards_CardRequestExtensions_SetAddToRolesIDList.htm)|
Устанавливает список идентификаторов ролей, в которые должен быть добавлен
создаваемый сотрудник в запросе на создание (первое сохранение) карточки
сотрудника CardStoreRequest. Если при включении сотрудника в одну из ролей
возникнет ошибка, то она будет добавлена как предупреждение, и включение в
другие роли, а также сохранение завершатся успешно.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetADFSAuthenticationResponse](M_Tessa_Cards_CardRequestExtensions_SetADFSAuthenticationResponse.htm)|
Устанавливает сериализованную в XML информацию в виде строки, которая получена
при автоматическом создании сотрудника средствами ADFS, или null, если
информацию требуется удалить.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetDigest](M_Tessa_Cards_CardRequestExtensions_SetDigest_1.htm)|
Устанавливает Digest для сохранения в историю действий с карточкой.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetForbidFileStoreChanging](M_Tessa_Cards_CardRequestExtensions_SetForbidFileStoreChanging.htm)|
Устанавливает признак того, что для файлов сохраняемой карточки запрещено
изменять местоположение контента при сохранении.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetForbidStoringHistory](M_Tessa_Cards_CardRequestExtensions_SetForbidStoringHistory_4.htm)|
Устанавливает запрет на сохранение данных о сохраняемой карточке в историю
действий с карточкой. Вызов метода в клиентских расширениях запрещён, это
приведёт к ошибке
[RequestFromClientCheckFailed](F_Tessa_Cards_CardValidationKeys_RequestFromClientCheckFailed.htm).  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetForceTaskPanel](M_Tessa_Cards_CardRequestExtensions_SetForceTaskPanel.htm)|  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetHasRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetHasRecalcChanges.htm)|
Задаёт значение, показывающее, что после пересчёта были изменения в маршруте
или нет. Информация добавляется только при выставленном флаге
[HasChangesToInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_InfoAboutChanges.htm).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetIgnorePermissionsWarning](M_Tessa_Cards_CardRequestExtensions_SetIgnorePermissionsWarning.htm)|
Устанавливает признак того, что при обработке карточки могут быть не указаны
токены безопасности, поэтому не следует показывать соответствующее
предупреждение.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetImportVersion](M_Tessa_Cards_CardRequestExtensions_SetImportVersion.htm)|
Устанавливает оригинальную версию импортируемой карточки, которую требуется
восстановить.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetInfoAboutChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetInfoAboutChanges_1.htm)|
Устанавливает в хранилище информацию о режиме информирования об изменениях в
маршруте после пересчёта.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetKrProcessInstance](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetKrProcessInstance_1.htm)|
Сохраняет в указанном объекте информация об экземпляре процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetKrProcessLaunchResult](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetKrProcessLaunchResult.htm)|
Сохраняет результаты запуска процесса в указанном хранилище.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetLocalTiles.htm)|
Сохраняет в указанном объекте коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetNoLockingMainCard](M_Tessa_Cards_CardRequestExtensions_SetNoLockingMainCard_1.htm)|
Устанавливает признак того, что не следует выполнять блокировку основной
карточки при создании или изменении сателлита.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetPluginType](M_Tessa_Cards_CardRequestExtensions_SetPluginType.htm)|
Устанавливает тип плагина при выполнении запроса к карточке из плагина
Chronos. Стандартные типы перечислены в
[CardPluginTypes](T_Tessa_Cards_CardPluginTypes.htm).  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetRecalcChanges.htm)|
Сохраняет в заданном хранилище информацию о различиях в маршруте до и после
пересчёта.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetRecalcFlag](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetRecalcFlag_1.htm)|
Задаёт значение, показывающее, что должен быть выполнен пересчёт маршрута.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetRepairSectionsFlag](M_Tessa_Cards_CardRequestExtensions_SetRepairSectionsFlag.htm)|
Устанавливает флаг, который указывает на то, что нужно починить (добавить)
строковые секции карточки в случае, если они отсутствуют в БД.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[SetStartingKrProcessParameters](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingKrProcessParameters_1.htm)|
Устанавливает параметры запускаемого процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetStartingProcessID](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessID.htm)|
Устанавливает идентификатор для запускаемого бизнес-процесса.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[SetStartingProcessName](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessName_1.htm)|
Устанавливает имя бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[SetStartingProcessNextTask](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessNextTask_1.htm)|
Устанавливает задание, которое будет использоваться при первом сохранении
сразу же после запуска процесса. Например, задание определяет секции
"постановки задачи", которые заполняются при отправке задач. Метод есть смысл
использовать только для тех процессов, которые его поддерживают.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[SetStartingProcessTaskGroupRowID](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessTaskGroupRowID.htm)|
Устанавливает идентификатор группы в истории заданий для первого задания
бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[SetStartingProcessTaskRowID](M_Tessa_Cards_Workflow_WorkflowExtensions_SetStartingProcessTaskRowID_1.htm)|
Устанавливает идентификатор первого задания бизнес-процесса, запускаемого
посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[SetStartingSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingSecondaryProcess.htm)|
Устанавливает информацию о процессе, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[SetWipeDeletedFlag](M_Tessa_Cards_CardRequestExtensions_SetWipeDeletedFlag.htm)|
Устанавливает флаг, который указывает на то, что нужно очищать удаленные в
корзину карточки, если они будут мешать импорту.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetAddToRolesIDList](M_Tessa_Cards_CardRequestExtensions_TryGetAddToRolesIDList.htm)|
Получает список идентификаторов ролей, в которые должен быть добавлен
создаваемый сотрудник, или null, аналогичный пустому списку.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetDigest](M_Tessa_Cards_CardRequestExtensions_TryGetDigest.htm)|
Возвращает Digest для сохранения в историю действий с карточкой или null, если
Digest не был установлен.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetForbidFileStoreChanging](M_Tessa_Cards_CardRequestExtensions_TryGetForbidFileStoreChanging.htm)|
Возвращает признак того, что для файлов сохраняемой карточки запрещено
изменять местоположение контента при сохранении.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetImportVersion](M_Tessa_Cards_CardRequestExtensions_TryGetImportVersion.htm)|
Возвращает оригинальную версию импортируемой карточки, которую требуется
восстановить.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetKrProcessClientCommands](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrProcessClientCommands.htm)|
Возвращает из указанного хранилища список клиентских команд или значение по
умолчанию для типа, если оно их не содержало.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetKrProcessInstance](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrProcessInstance.htm)|
Возвращает информацию об экземпляре процесса из указанного хранилища.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetKrProcessLaunchResult](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrProcessLaunchResult.htm)|
Возвращает объект, содержащий результат запуска процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetLocalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetPluginType](M_Tessa_Cards_CardRequestExtensions_TryGetPluginType.htm)|
Возвращает тип плагина, установленный при выполнении запроса к карточке из
плагина Chronos, или null, если запрос выполнен не из плагина или из
неизвестного плагина.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetRepairSectionsFlag](M_Tessa_Cards_CardRequestExtensions_TryGetRepairSectionsFlag.htm)|
Возвращает флаг, который указывает на то, что нужно починить (добавить)
строковые секции карточки в случае, если они отсутствуют в БД.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
[TryGetStartingKrProcessParameters](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStartingKrProcessParameters_1.htm)|
Возвращает параметры запускаемого процесса.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
[TryGetStartingProcessID](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessID.htm)|
Возвращает идентификатор бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm),  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[TryGetStartingProcessName](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessName.htm)|
Возвращает имя бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm),
или null, если бизнес-процесс не запускается.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[TryGetStartingProcessNextTask](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessNextTask.htm)|
Возвращает задание, которое будет использоваться при первом сохранении сразу
же после запуска процесса, или null, если такое задание не было установлено.
Например, задание определяет секции "постановки задачи", которые заполняются
при отправке задач. Метод есть смысл использовать только для тех процессов,
которые его поддерживают.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[TryGetStartingProcessTaskGroupRowID](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessTaskGroupRowID.htm)|
Метод запрашивает идентификатор группы в истории заданий для первого задания
бизнес-процесса, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).
Если метод вернул true, то в параметре groupRowID содержится идентификатор
группы, в которую добавляется запись в истории заданий (значение null
означает, что запись добавляется без группы, но не в группу по умолчанию).
Если метод вернул false, то запись добавляется в группу по умолчанию, которая
может отличаться от null.
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[TryGetStartingProcessTaskRowID](M_Tessa_Cards_Workflow_WorkflowExtensions_TryGetStartingProcessTaskRowID.htm)|
Возвращает идентификатор первого задания в бизнес-процессе, запускаемом
посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm),
или null, если бизнес-процесс не запускается или идентификатор определяется
самостоятельно в рамках процесса.  
(Определяется
[WorkflowExtensions](T_Tessa_Cards_Workflow_WorkflowExtensions.htm))  
[TryGetWipeDeletedFlag](M_Tessa_Cards_CardRequestExtensions_TryGetWipeDeletedFlag.htm)|
Возвращает флаг, который указывает на то, что нужно очищать удаленные в
корзину карточки, если они будут мешать импорту.  
(Определяется
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
