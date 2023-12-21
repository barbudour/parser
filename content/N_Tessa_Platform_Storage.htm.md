# Tessa.Platform.Storage - пространство имён
Вспомогательные классы для работы с хранилищем, т.е. с сериализуемой хэш-
таблицей Dictionary<string, object>.
##  __Классы
[DefaultConstructorStorageValueFactory<TKey,
TValue>](T_Tessa_Platform_Storage_DefaultConstructorStorageValueFactory_2.htm)|
Фабрика, создающая объекты посредством конструктора по умолчанию, которые
используются в качестве значений в строго типизированных декораторах для
коллекций пар ключ / значение.  
---|---  
[DefaultStorageValueFactory<TKey,
TValue>](T_Tessa_Platform_Storage_DefaultStorageValueFactory_2.htm)|  Фабрика
по умолчанию, создающая объекты посредством вызова default(TValue), которые
используются в качестве значений в строго типизированных декораторах для
коллекций пар ключ / значение.  
[DictionaryStorage<TKey,
TValue>](T_Tessa_Platform_Storage_DictionaryStorage_2.htm)|  Базовый класс,
являющийся строго типизированным декоратором для хранилища IDictionary<string,
object>.  
[DictionaryStorageValueFactory<TKey,
TValue>](T_Tessa_Platform_Storage_DictionaryStorageValueFactory_2.htm)|
Фабрика для создания объектов, являющихся декораторами для Dictionary<string,
object> и используемых в качестве значений в строго типизированных декораторах
для коллекций пар ключ / значение.  
[DynamicStorageAccessor](T_Tessa_Platform_Storage_DynamicStorageAccessor.htm)|
Содержит фабрику для создания объектов
[DynamicStorageAccessor<TStorage>](T_Tessa_Platform_Storage_DynamicStorageAccessor_1.htm),
осуществляющих доступ к хранилищу пар ключ / значение через позднее
связывание.  
[DynamicStorageAccessor<TStorage>](T_Tessa_Platform_Storage_DynamicStorageAccessor_1.htm)|
Объект, осуществляющий доступ к хранилищу пар ключ / значение через позднее
связывание.  
[DynamicStorageAccessorOptions](T_Tessa_Platform_Storage_DynamicStorageAccessorOptions.htm)|
Настройки, определяющие поведение класса
[DynamicStorageAccessor<TStorage>](T_Tessa_Platform_Storage_DynamicStorageAccessor_1.htm).  
[DynamicValueAccessor](T_Tessa_Platform_Storage_DynamicValueAccessor.htm)|
Базовый объект, осуществляющий доступ к членам объекта-значения и навигацию по
дереву связанных объектов через позднее связывание.  
[GuidDictionaryStorage<T>](T_Tessa_Platform_Storage_GuidDictionaryStorage_1.htm)|
Класс, являющийся строго типизированным декоратором с ключом
[Guid](https://learn.microsoft.com/dotnet/api/system.guid) для хранилища
IDictionary<string, object>.  
[InfoStorageObject](T_Tessa_Platform_Storage_InfoStorageObject.htm)|  Базовый
класс для объектов, являющихся декораторами для хранилища, с поддержкой
дополнительной пользовательской информации.  
[ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm)|  Класс,
являющийся строго типизированным декоратором для хранилища List<object>.  
[ListStorageComparer](T_Tessa_Platform_Storage_ListStorageComparer.htm)|  
[ListStorageCompressor](T_Tessa_Platform_Storage_ListStorageCompressor.htm)|
Выполняет упаковку или распаковку коллекции ICollection<object> хэш-таблиц
IDictionary<string, object>, содержащих один и тот же набор ключей.
В качестве параметра targetKey методам [Compress(IDictionary<String, Object>,
String)](M_Tessa_Platform_Storage_ListStorageCompressor_Compress.htm) и
[Decompress(IDictionary<String, Object>,
String)](M_Tessa_Platform_Storage_ListStorageCompressor_Decompress.htm)
передаётся ключ, по которому искомая коллекция может быть найдена в хранилище.  
[ListStorageItemEventArgs<T>](T_Tessa_Platform_Storage_ListStorageItemEventArgs_1.htm)|
Аргументы события, происходящего при изменении коллекции
[ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm).  
[ListStorageSynchronizer](T_Tessa_Platform_Storage_ListStorageSynchronizer.htm)|
Вспомогательные методы для синхронизации списков
[ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm), со списками
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1).  
[ListStorageSynchronizer<TSource,
TTarget>](T_Tessa_Platform_Storage_ListStorageSynchronizer_2.htm)|  Объект,
выполняющий синхронизацию списка
[ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm) с одним или
несколькими списками
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1).  
[ListStorageSynchronizer<TSource,
TTarget>.TargetItemEventArgs](T_Tessa_Platform_Storage_ListStorageSynchronizer_2_TargetItemEventArgs.htm)|
Аргументы события, содержащие ссылку на объект, для которого произошло
событие.  
[ListStorageValueFactory<TKey,
TValue>](T_Tessa_Platform_Storage_ListStorageValueFactory_2.htm)|  Фабрика для
создания объектов, являющихся декораторами для List<object> и используемых в
качестве значений в строго типизированных декораторах для коллекций пар ключ /
значение.  
[SerializableObject](T_Tessa_Platform_Storage_SerializableObject.htm)|
Объект, сериализуемый средствами
[TessaSerializer](T_Tessa_Platform_Json_TessaSerializer.htm),
[DataContractSerializer](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.datacontractserializer),
[XmlSerializer](https://learn.microsoft.com/dotnet/api/system.xml.serialization.xmlserializer)
или
[BinaryFormatter](https://learn.microsoft.com/dotnet/api/system.runtime.serialization.formatters.binary.binaryformatter).  
[SerializableObjectComparer](T_Tessa_Platform_Storage_SerializableObjectComparer.htm)|
Сравнивает данные сериализуемых объектов.  
[StorageBoxingManager](T_Tessa_Platform_Storage_StorageBoxingManager.htm)|
Вспомогательные методы для объектов
[IStorageBoxingManager<T>](T_Tessa_Platform_Storage_IStorageBoxingManager_1.htm),
управляющих упаковкой объектов в хранилище и распаковкой объектов из него.  
[StorageContentMapping](T_Tessa_Platform_Storage_StorageContentMapping.htm)|
Представляет опции сериализации отдельно взятого выгружаемого контента для
storage объекта.  
[StorageDefaultBoxingManager<T>](T_Tessa_Platform_Storage_StorageDefaultBoxingManager_1.htm)|
Объект, выполняющий упаковку и распаковку объектов в хранилище по умолчанию.  
[StorageEnumBoxingManager<T>](T_Tessa_Platform_Storage_StorageEnumBoxingManager_1.htm)|
Объект, выполняющий упаковку и распаковку объектов-перечислений в хранилище.  
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm)|  Методы-
расширения для пространства имён Tessa.Platform.Storage.  
[StorageHelper](T_Tessa_Platform_Storage_StorageHelper.htm)|  Хэлперы для
взаимодействия с хранилищем.  
[StorageLinearGradientBrush](T_Tessa_Platform_Storage_StorageLinearGradientBrush.htm)|
Кисть линейного градиента, сериализуемая в объектах
[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm). Формат хранения
аналогичен значению LinearGradientBrush в WPF.  
[StorageMapping](T_Tessa_Platform_Storage_StorageMapping.htm)|  Опции
сериализации для подобъекта в storage.  
[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm)|
Класс, являющийся строго типизированным декоратором для хранилища
IDictionary<string, object> и имеющий заранее определённый набор строго
типизированных свойств.
Класс устанавливает, что значения по умолчанию этих свойств не должны
содержаться в хранилище, а свойства с вложенными элементами вида
IDictionary<string, object> или
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
должны создаваться автоматически при первом доступе.  
[StorageObjectComparer](T_Tessa_Platform_Storage_StorageObjectComparer.htm)|
Выполняет полное сравнение хранилищ IDictionary<string, object> для объектов
[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm).  
[StorageObjectStateProvider](T_Tessa_Platform_Storage_StorageObjectStateProvider.htm)|
Предоставляет информацию о наличии изменений в значениях объектов хранилища
IDictionary<string, object>. Объект сохраняет служебную информацию в объект
хранилища, располагающийся по заданному в конструкторе ключу.  
[StoragePathEqualityComparer](T_Tessa_Platform_Storage_StoragePathEqualityComparer.htm)|
Comparer по внутреннему пути в storage для отдельно взятого выгружаемого
контента.  
[StoragePathItem](T_Tessa_Platform_Storage_StoragePathItem.htm)|  Элемент пути
хранилища.  
[StoragePathItemComparer](T_Tessa_Platform_Storage_StoragePathItemComparer.htm)|
Компарер для объектов
[IStoragePathItem](T_Tessa_Platform_Storage_IStoragePathItem.htm).  
[StoragePathParser](T_Tessa_Platform_Storage_StoragePathParser.htm)|  Объект,
выполняющий синтаксический анализ строкового представления пути в storage-
объекте.  
[StoragePathParserException](T_Tessa_Platform_Storage_StoragePathParserException.htm)|
Представляет ошибку, возникающую при парсинге пути для хранилища.  
[StoragePathResolver](T_Tessa_Platform_Storage_StoragePathResolver.htm)|
Объект, обеспечивающий выполнение действий с элементами storage-объекта.  
[StoragePathResolverException](T_Tessa_Platform_Storage_StoragePathResolverException.htm)|
Представляет ошибку, возникающую при получении объектов из storage хранилища.  
[StoragePathValueInfo](T_Tessa_Platform_Storage_StoragePathValueInfo.htm)|
Класс предоставляет информацию о пути внутри storage и значении,
расположенному по данному пути.  
[StoragePathValueInfoComparer](T_Tessa_Platform_Storage_StoragePathValueInfoComparer.htm)|
Компарер для объектов
[StoragePathValueInfo](T_Tessa_Platform_Storage_StoragePathValueInfo.htm).  
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm)|
Объект, сериализуемый в хранилище Dictionary<string, object>.  
[StorageSerializationOptions](T_Tessa_Platform_Storage_StorageSerializationOptions.htm)|
Представляет опции сериализации выгружаемого во внешние источники контента из
storage.  
[StorageSerializer](T_Tessa_Platform_Storage_StorageSerializer.htm)|  Объект,
предоставляющий методы для сериализации и десериализации карточек с учетом
контента, выгружаемого во внешние файлы.  
[StorageValuesKeeper](T_Tessa_Platform_Storage_StorageValuesKeeper.htm)|
Позволяет запоминать и восстанавливать значения из хранилища (storage) по
заданным путям.  
[StringDictionaryStorage<T>](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)|
Класс, являющийся строго типизированным декоратором с ключом
[String](https://learn.microsoft.com/dotnet/api/system.string) для хранилища
IDictionary<string, object>.  
## __Структуры
[DynamicValueAccessor.PathItem](T_Tessa_Platform_Storage_DynamicValueAccessor_PathItem.htm)|
Информация о запрошенном пользователем элементе.  
---|---  
[StorageColor](T_Tessa_Platform_Storage_StorageColor.htm)|  Цвет,
сериализуемый в объектах
[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm).  
[StorageGradientStop](T_Tessa_Platform_Storage_StorageGradientStop.htm)|
Точка градиентного останова, используемая в градиентных кистях и сериализуемая
в объектах [StorageObject](T_Tessa_Platform_Storage_StorageObject.htm). Формат
хранения аналогичен значению GradientStop в WPF.  
[StoragePoint](T_Tessa_Platform_Storage_StoragePoint.htm)|  Точка,
сериализуемая в объектах
[StorageObject](T_Tessa_Platform_Storage_StorageObject.htm).  
## __Интерфейсы
[IDynamicValueAccessorOptions](T_Tessa_Platform_Storage_IDynamicValueAccessorOptions.htm)|
Настройки, определяющие поведение класса
[DynamicValueAccessor](T_Tessa_Platform_Storage_DynamicValueAccessor.htm).  
---|---  
[IListItemContainer<T>](T_Tessa_Platform_Storage_IListItemContainer_1.htm)|
Объект, являющийся контейнером для списка элементов.  
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)|
Объект, сериализуемый средствами
[TessaSerializer](T_Tessa_Platform_Json_TessaSerializer.htm).  
[IStorageBoxingManager<T>](T_Tessa_Platform_Storage_IStorageBoxingManager_1.htm)|
Объект, управляющий упаковкой объектов в хранилище и распаковкой объектов из
него. Для получения экземпляра объекта рекомендуется использовать метод
[Get<T>()](M_Tessa_Platform_Storage_StorageBoxingManager_Get__1.htm).  
[IStorageCachePolicyProvider](T_Tessa_Platform_Storage_IStorageCachePolicyProvider.htm)|
Поставщик управления политикой кэша объектов-обёрток для хранилища.  
[IStorageCleanable](T_Tessa_Platform_Storage_IStorageCleanable.htm)|
Поддерживает очистку хранилища от избыточных данных.  
[IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)|
Выполняет упаковку и распаковку данных хранилища.  
[IStorageContentMapping](T_Tessa_Platform_Storage_IStorageContentMapping.htm)|
Представляет опции сериализации отдельно взятого выгружаемого контента для
storage объекта.  
[IStorageDictionaryProvider](T_Tessa_Platform_Storage_IStorageDictionaryProvider.htm)|
Предоставляет доступ к хранилищу IDictionary<string, object>, декоратором для
которого является текущий объект.  
[IStorageListProvider](T_Tessa_Platform_Storage_IStorageListProvider.htm)|
Предоставляет доступ к хранилищу IList<object>, декоратором для которого
является текущий объект.  
[IStorageMapping](T_Tessa_Platform_Storage_IStorageMapping.htm)|  Опции
сериализации для подобъекта в storage.  
[IStorageNotificationReceiver](T_Tessa_Platform_Storage_IStorageNotificationReceiver.htm)|
Объект, получающий уведомления об изменениях в его хранилище.  
[IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm)|
Предоставляет доступ к хранилищу Dictionary<string, object>, декоратором для
которого является текущий объект.  
[IStorageObjectStateProvider](T_Tessa_Platform_Storage_IStorageObjectStateProvider.htm)|
Предоставляет информацию о наличии изменений в значениях объектов хранилища.  
[IStoragePathItem](T_Tessa_Platform_Storage_IStoragePathItem.htm)|  Элемент
пути хранилища.  
[IStoragePathParser](T_Tessa_Platform_Storage_IStoragePathParser.htm)|
Объект, выполняющий синтаксический анализ строкового представления пути в
storage-объекте.  
[IStoragePathResolver](T_Tessa_Platform_Storage_IStoragePathResolver.htm)|
Объект, обеспечивающий выполнение действий с элементами storage-объекта.  
[IStorageProvider](T_Tessa_Platform_Storage_IStorageProvider.htm)|
Предоставляет доступ к хранилищу, декоратором для которого является текущий
объект.  
[IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)|
Объект, сериализуемый в хранилище Dictionary<string, object>.  
[IStorageSerializationOptions](T_Tessa_Platform_Storage_IStorageSerializationOptions.htm)|
Представляет опции сериализации выгружаемого во внешние источники контента из
storage.  
[IStorageSerializer](T_Tessa_Platform_Storage_IStorageSerializer.htm)|
Объект, предоставляющий методы для сериализации и десериализации карточек с
учетом контента, выгружаемого во внешние файлы.  
[IStorageValueFactory<TKey,
TValue>](T_Tessa_Platform_Storage_IStorageValueFactory_2.htm)|  Фабрика для
создания объектов, используемых в качестве значений в строго типизированных
декораторах для коллекций пар ключ / значение.  
[IStorageValuesKeeper](T_Tessa_Platform_Storage_IStorageValuesKeeper.htm)|
Позволяет запоминать и восстанавливать значения из хранилища (storage) по
заданным путям.  
[ITypedSerializable](T_Tessa_Platform_Storage_ITypedSerializable.htm)|
Объект, сериализуемый в словарь-хранилище, где для указание типа объекта
служит отдельное поле TypeName.  
## __Перечисления
[DynamicValueAccessor.PathItemType](T_Tessa_Platform_Storage_DynamicValueAccessor_PathItemType.htm)|
Способ, которым пользователь запросил элемент.  
---|---  
[ListStorageAction](T_Tessa_Platform_Storage_ListStorageAction.htm)|
Действие, производённое с элементами коллекции
[ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm), о которых
сообщает событие.  
[StoragePathItemType](T_Tessa_Platform_Storage_StoragePathItemType.htm)|
Перечисление типов элемента пути.  
[StoragePathResolveOptions](T_Tessa_Platform_Storage_StoragePathResolveOptions.htm)|
Перечисление параметров получения значения из storage-объекта.
