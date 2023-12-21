# Tessa.Platform.Collections - пространство имён
Коллекции (такие как WeakDictionary) и связанные с ними хэлперы.
##  __Классы
[CollectionConverter](T_Tessa_Platform_Collections_CollectionConverter.htm)|  
---|---  
[ConcurrentContainer<TKey,
TValue>](T_Tessa_Platform_Collections_ConcurrentContainer_2.htm)|
Потокобезопасный контейнер для коллекции пар ключ / значение, удобная в
случае, если чтение данных производится гораздо чаще, чем их изменение, причём
чтение производится как правило уже после изменений.  
[ControllableItemEventArgs<TItem>](T_Tessa_Platform_Collections_ControllableItemEventArgs_1.htm)|
Аргументы события по действию с проверяемым элементом коллекции
[IControllableCollection<TItem>](T_Tessa_Platform_Collections_IControllableCollection_1.htm).
Действие может быть отменено при установке признака
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel) равным true.  
[EmptyHolder<T>](T_Tessa_Platform_Collections_EmptyHolder_1.htm)|  Содержит
кэш значений для массивов и коллекций, доступных только для чтения.  
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm)|
Предоставляет статические методы расширения для
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
[Extensions](T_Tessa_Platform_Collections_Extensions.htm)|  Методы-расширения
для пространства имён Tessa.Platform.Collections.  
[HashSet<TKey, TValue>](T_Tessa_Platform_Collections_HashSet_2.htm)|  Хэш
коллекция, сочетающая преимущества [IDictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)
и
[ISet<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset-1).
При этом ключ строится на основе экземпляра [!:TValue].  
[LimitedPool<T>](T_Tessa_Platform_Collections_LimitedPool_1.htm)|  Пул
объектов, имеющих ограниченное время жизни.  
[LimitedPoolExpirationTokenSource](T_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource.htm)|
Объект, по которому токены определяют признак того, что время жизни объектов в
пуле истекло. В момент вызова
[Dispose()](M_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource_Dispose.htm)
все токены
[Token](P_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource_Token.htm)
будут считаться истёкшими по времени жизни.  
[LimitedPoolItem<T>](T_Tessa_Platform_Collections_LimitedPoolItem_1.htm)|
Объект в пуле
[ILimitedPool<T>](T_Tessa_Platform_Collections_ILimitedPool_1.htm), время
жизни которого ограничено.  
[LookupContainer<TKey,
TValue>](T_Tessa_Platform_Collections_LookupContainer_2.htm)|  Контейнер для
значений, доступных по неуникальным ключам.  
[NamedObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_NamedObservableCollection_2.htm)|
Коллекция именованных объектов, для которой доступны уведомление об изменениях
и клонирование.  
[ObjectPool<T>](T_Tessa_Platform_Collections_ObjectPool_1.htm)|  Пул повторно
используемых объектов.  
[ObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollection_2.htm)|
Коллекция объектов, для которой доступны уведомление об изменениях и
клонирование.  
[ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm)|
Коллекция объектов, для которой доступны уведомление об изменениях и
клонирование, а также идентификация по неуникальному ключу.  
[ReadOnlyCollectionWrapper<T>](T_Tessa_Platform_Collections_ReadOnlyCollectionWrapper_1.htm)|
Обёртка для коллекции
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1),
доступная только для чтения.  
[ReadOnlyDictionaryWrapper<TKey,
TValue>](T_Tessa_Platform_Collections_ReadOnlyDictionaryWrapper_2.htm)|
Обертка для коллекции ключ-значение [IDictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)
доступная только для чтения  
[ReadOnlyNotificationCollection<T>](T_Tessa_Platform_Collections_ReadOnlyNotificationCollection_1.htm)|
Доступная только для чтения обёртка для коллекции, открыто поддерживающая
событие
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged.collectionchanged).  
[ReferenceEqualityComparer<T>](T_Tessa_Platform_Collections_ReferenceEqualityComparer_1.htm)|
Сравнивает объекты на равенство ссылок. Методы [Equals(T,
T)](M_Tessa_Platform_Collections_ReferenceEqualityComparer_1_Equals.htm) и
[GetHashCode(T)](M_Tessa_Platform_Collections_ReferenceEqualityComparer_1_GetHashCode.htm)
компаратора игнорируют любые определённые в объектах способы сравнения и
вычисления хеш-кода.  
[SealableList<T>](T_Tessa_Platform_Collections_SealableList_1.htm)|  Список,
поддерживающий защиту от изменений.  
[SealableObjectList<T>](T_Tessa_Platform_Collections_SealableObjectList_1.htm)|
Список, поддерживающий защиту от изменений как для себя, так и для
содержащихся в нём объектов. Не может содержать ссылки null. При удалении
элементов производит удаление только по точному совпадению ссылок удаляемых
элементов.  
[SealableObjectObservableCollection<T>](T_Tessa_Platform_Collections_SealableObjectObservableCollection_1.htm)|
Коллекция, поддерживающая защиту от изменений и уведомления об изменении.
Вложенные в коллекцию объекты также защищаются от изменений, а их значения
никогда не равны null.  
[SealableObservableCollection<T>](T_Tessa_Platform_Collections_SealableObservableCollection_1.htm)|
Коллекция, поддерживающая защиту от изменений и уведомления об изменении.  
[SuspendableObservableCollection<T>](T_Tessa_Platform_Collections_SuspendableObservableCollection_1.htm)|
Коллекция объектов, для которой доступна возможность подавить уведомления по
событиям
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)
и
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged.collectionchanged)
вызовом
[SuspendNotifications()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendNotifications.htm).  
[WeakDictionary<TKey,
TValue>](T_Tessa_Platform_Collections_WeakDictionary_2.htm)|  
## __Структуры
[HashSet<TKey,
TValue>.Enumerator](T_Tessa_Platform_Collections_HashSet_2_Enumerator.htm)|
Реализация энумератора.  
---|---  
[LimitedPoolExpirationToken](T_Tessa_Platform_Collections_LimitedPoolExpirationToken.htm)|
Токен истечения времени жизни объекта в пуле
[LimitedPoolItem<T>](T_Tessa_Platform_Collections_LimitedPoolItem_1.htm).  
[SuspendableObservableCollection<T>.SuspendChangesScope](T_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendChangesScope.htm)|  
## __Интерфейсы
[IControllableCollection<TItem>](T_Tessa_Platform_Collections_IControllableCollection_1.htm)|
Коллекция объектов, для которой опционально контролируется добавление и
удаление.  
---|---  
[ILimitedPool<T>](T_Tessa_Platform_Collections_ILimitedPool_1.htm)|  Пул
объектов, имеющих ограниченное время жизни.  
[ILimitedPoolItem<T>](T_Tessa_Platform_Collections_ILimitedPoolItem_1.htm)|
Объект в пуле
[ILimitedPool<T>](T_Tessa_Platform_Collections_ILimitedPool_1.htm), время
жизни которого ограничено.  
[ILookupContainer<TKey,
TValue>](T_Tessa_Platform_Collections_ILookupContainer_2.htm)|  Контейнер для
значений, доступных по неуникальным ключам. Интерфейс позволяет получать и
удалять значения, но не добавлять их.  
[INamedCollection<T>](T_Tessa_Platform_Collections_INamedCollection_1.htm)|
Коллекция, хранящая именованные объекты  
[INamedItem](T_Tessa_Platform_Collections_INamedItem.htm)|  Именованный
элемент коллекции.  
[INamedObject](T_Tessa_Platform_Collections_INamedObject.htm)|  Интерфейс
именованного объекта  
[INamedObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_INamedObservableCollection_2.htm)|
Коллекция именованных объектов, для которой доступны уведомление об изменениях
и клонирование.  
[IObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_IObservableCollection_2.htm)|
Коллекция объектов, для которой доступны уведомление об изменениях и
клонирование.  
[IObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_IObservableCollectionLookup_3.htm)|
Коллекция объектов, для которой доступны уведомление об изменениях и
клонирование, а также идентификация по неуникальному ключу.  
[ISuspendableObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_ISuspendableObservableCollection_2.htm)|
Коллекция объектов, для которой доступны уведомление об изменениях и
клонирование, а также предотвращение уведомлений об изменениях.  
## __Делегаты
[ControllableItemEventHandler<TItem>](T_Tessa_Platform_Collections_ControllableItemEventHandler_1.htm)|
Обработчик события по действию с проверяемым элементом коллекции
[IControllableCollection<TItem>](T_Tessa_Platform_Collections_IControllableCollection_1.htm).  
---|---  
## __Перечисления
[ControllableItemAction](T_Tessa_Platform_Collections_ControllableItemAction.htm)|
Действие, выполняемое с проверяемым элементом коллекции
[IControllableCollection<TItem>](T_Tessa_Platform_Collections_IControllableCollection_1.htm).  
---|---
