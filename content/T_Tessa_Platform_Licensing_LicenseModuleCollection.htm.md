# LicenseModuleCollection - класс
Коллекция модулей, подключенных в лицензии
[ILicense](T_Tessa_Platform_Licensing_ILicense.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LicenseModuleCollection : ListStorage<LicenseModule>, 
    	ILicenseModuleCollection, IList<ILicenseModule>, ICollection<ILicenseModule>, 
    	IEnumerable<ILicenseModule>, IEnumerable, IReadOnlyList<ILicenseModule>, 
    	IReadOnlyCollection<ILicenseModule>
VB __Копировать
     Public NotInheritable Class LicenseModuleCollection
    	Inherits ListStorage(Of LicenseModule)
    	Implements ILicenseModuleCollection, IList(Of ILicenseModule), 
    	ICollection(Of ILicenseModule), IEnumerable(Of ILicenseModule), IEnumerable, 
    	IReadOnlyList(Of ILicenseModule), IReadOnlyCollection(Of ILicenseModule)
C++ __Копировать
     public ref class LicenseModuleCollection sealed : public ListStorage<LicenseModule^>, 
    	ILicenseModuleCollection, IList<ILicenseModule^>, ICollection<ILicenseModule^>, 
    	IEnumerable<ILicenseModule^>, IEnumerable, IReadOnlyList<ILicenseModule^>, 
    	IReadOnlyCollection<ILicenseModule^>
F# __Копировать
     [<SealedAttribute>]
    type LicenseModuleCollection = 
        class
            inherit ListStorage<LicenseModule>
            interface ILicenseModuleCollection
            interface IList<ILicenseModule>
            interface ICollection<ILicenseModule>
            interface IEnumerable<ILicenseModule>
            interface IEnumerable
            interface IReadOnlyList<ILicenseModule>
            interface IReadOnlyCollection<ILicenseModule>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[ListStorage](T_Tessa_Platform_Storage_ListStorage_1.htm)<[LicenseModule](T_Tessa_Platform_Licensing_LicenseModule.htm)> __ LicenseModuleCollection
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>, [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [ILicenseModuleCollection](T_Tessa_Platform_Licensing_ILicenseModuleCollection.htm)
##  __Конструкторы
[LicenseModuleCollection()](M_Tessa_Platform_Licensing_LicenseModuleCollection__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[LicenseModuleCollection(IList)](M_Tessa_Platform_Licensing_LicenseModuleCollection__ctor_1.htm)|
Создаёт экземпляр класса с указанием хранилища, декоратором для которого
является создаваемый объект.  
## __Свойства
[Count](P_Tessa_Platform_Storage_ListStorage_1_Count.htm)| Количество
элементов в коллекции.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
---|---  
[DefaultValueFactory](P_Tessa_Platform_Storage_ListStorage_1_DefaultValueFactory.htm)|
Фабрика для создания значений по умолчанию.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[Item[Guid]](P_Tessa_Platform_Licensing_LicenseModuleCollection_Item.htm)|
Возвращает модуль лицензии по его идентификатору.  
[Item[Int32]](P_Tessa_Platform_Storage_ListStorage_1_Item.htm)| Получает
элемент по отсчитываемому от нуля индексу.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
##  __Методы
[Add()](M_Tessa_Platform_Storage_ListStorage_1_Add.htm)|  Создаёт и добавляет
значение по умолчанию, причём в хранилище добавляется новый объект
List<object>.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
---|---  
[Add<TStorageProvider>(TStorageProvider)](M_Tessa_Platform_Storage_ListStorage_1_Add__1.htm)|
Добавляет объект, заполняемый из хранилища заданного объекта.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[AddItems<TStorageProvider>](M_Tessa_Platform_Storage_ListStorage_1_AddItems__1.htm)|
Добавляет объекты из заданного перечисления, причём каждый создаваемый объект
заполняется из хранилища заданного объекта.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[AddList<TStorageProvider>](M_Tessa_Platform_Storage_ListStorage_1_AddList__1.htm)|
Добавляет объект, заполняемый из коллекционного хранилища заданного объекта.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[AddValue](M_Tessa_Platform_Storage_ListStorage_1_AddValue.htm)|  Добавляет
элемент в конец списка как значение типа T. Метод рекомендуется использовать
для скалярных типов, например: ListStorage<Guid>.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[AsReadOnly](M_Tessa_Platform_Licensing_LicenseModuleCollection_AsReadOnly.htm)|
Возвращает доступную только для чтения обёртку для текущего состояния текущего
объекта. При изменении текущего объекта возвращённая обёртка не изменяется.  
[AsSerializable](M_Tessa_Platform_Licensing_LicenseModuleCollection_AsSerializable.htm)|
Возвращает обёртку для текущего объекта, которая может быть сериализована
средствами XML.  
[Clear](M_Tessa_Platform_Storage_ListStorage_1_Clear.htm)| Удаляет все
элементы коллекции.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[Clone](M_Tessa_Platform_Licensing_LicenseModuleCollection_Clone.htm)|
Выполняет глубокое клонирование хранилища объекта и возвращает созданный
строго типизированный декоратор для хранилища.  
[Contains(Guid)](M_Tessa_Platform_Licensing_LicenseModuleCollection_Contains.htm)|
Возвращает признак того, что в лицензию включён модуль с заданным
идентификатором.  
[Contains(T)](M_Tessa_Platform_Storage_ListStorage_1_Contains.htm)| Возвращает
признак того, что заданный элемент содержится в коллекции.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[CopyTo](M_Tessa_Platform_Storage_ListStorage_1_CopyTo.htm)| Копирует элементы
коллекции в массив, начиная с заданного отсчитываемого от нуля индекса.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[EnsureCacheResolved](M_Tessa_Platform_Storage_ListStorage_1_EnsureCacheResolved.htm)|
Инициализирует объект-обёртку для всех значений, в т.ч. для вложенных
объектов. Рекомендуется выполнять при создании заполненного объекта перед
асинхронным обращением к его вложенным объектам.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
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
[GetEnumerator](M_Tessa_Platform_Storage_ListStorage_1_GetEnumerator.htm)|
Возвращает итератор по элементам коллекции.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetStorage](M_Tessa_Platform_Storage_ListStorage_1_GetStorage.htm)|
Возвращает хранилище IList<object>, декоратором для которого является текущий
объект.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValidationName](M_Tessa_Platform_Validation_ValidationObject_GetValidationName.htm)|
Возвращает строку, определяющую имя объекта, или null, если имя объекта ещё
неизвестно или объект не содержит имени.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[IndexOf](M_Tessa_Platform_Storage_ListStorage_1_IndexOf.htm)| Возвращает
отсчитываемый от нуля индекс заданного элемента в коллекции.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[Insert(Int32)](M_Tessa_Platform_Storage_ListStorage_1_Insert.htm)|  Создаёт и
добавляет значение по умолчанию по заданному индексу, причём в хранилище
добавляется новый объект List<object>.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[Insert<TStorageProvider>(Int32,
TStorageProvider)](M_Tessa_Platform_Storage_ListStorage_1_Insert__1.htm)|
Добавляет объект по заданному индексу, заполняемый из хранилища заданного
объекта.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[InsertList<TStorageProvider>](M_Tessa_Platform_Storage_ListStorage_1_InsertList__1.htm)|
Добавляет объект по заданному индексу, заполняемый из коллекционного хранилища
заданного объекта.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[InsertValue](M_Tessa_Platform_Storage_ListStorage_1_InsertValue.htm)|
Вставляет элемент в заданную позицию как значение типа T. Метод рекомендуется
использовать для скалярных типов, например: ListStorage<Guid>.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[IsValid](M_Tessa_Platform_Validation_ValidationObject_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnCachedItemRemoved](M_Tessa_Platform_Storage_ListStorage_1_OnCachedItemRemoved.htm)|
Вызывается при удалении заданного элемента. Элемент должен быть добавлен в кэш
декораторов, чтобы событие произошло.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[OnCollectionCleared](M_Tessa_Platform_Storage_ListStorage_1_OnCollectionCleared.htm)|
Вызывается при удалении всех элементов из хранилища.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[OnItemAdded](M_Tessa_Platform_Storage_ListStorage_1_OnItemAdded.htm)|
Вызывается при добавлении заданного элемента в указанную позицию.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[OnUncachedItemRemoved](M_Tessa_Platform_Storage_ListStorage_1_OnUncachedItemRemoved.htm)|
Вызывается при удалении заданного объекта из хранилища. Элемент не должен быть
добавлен в кэш декораторов, чтобы событие произошло.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[Remove](M_Tessa_Platform_Storage_ListStorage_1_Remove.htm)| Удаляет заданный
элемент из коллекции.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[RemoveAll](M_Tessa_Platform_Storage_ListStorage_1_RemoveAll.htm)|  Удаляет
все эдементы списка, подходящие под заданную функцию предиката. Возвращает
количество удалённых элементов.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[RemoveAt](M_Tessa_Platform_Storage_ListStorage_1_RemoveAt.htm)| Удаляет
элемент в заданной позиции.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
[Set](M_Tessa_Platform_Licensing_LicenseModuleCollection_Set.htm)|  Заполняет
свойства текущего объекта из заданного объекта.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Platform_Licensing_LicenseModuleCollection_TryGet.htm)|
Возвращает модуль лицензии по его идентификатору или null, если
соответствующий модуль отсутствует.  
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[ValidateInternal](M_Tessa_Platform_Validation_ValidationObject_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
##  __События
[ItemChanged](E_Tessa_Platform_Storage_ListStorage_1_ItemChanged.htm)|
Элемент был добавлен или удалён, причём валидация уже была выполнена. Перед
обращением к элементу в аргументах события следует проверять его наличие.  
(Унаследован от [ListStorage<T>](T_Tessa_Platform_Storage_ListStorage_1.htm))  
---|---  
##  __Методы расширения
[AddRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<ILicenseModule>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<ILicenseModule>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<ILicenseModule>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<ILicenseModule>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<ILicenseModule, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[HasEnterpriseOrContains](M_Tessa_Platform_Licensing_LicensingExtensions_HasEnterpriseOrContains.htm)|
Возвращает признак того, что коллекция содержит модуль лицензии с указанным
идентификатором moduleID или что лицензия является Enterprise-редакцией, в
соответствии с которой модуль должен быть добавлен автоматически.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
[IndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[LastIndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[LastIndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1_1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ILicenseModule,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ILicenseModule,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<ILicenseModule>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<ILicenseModule>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveAll<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<ILicenseModule>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<ILicenseModule, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToLicenseModuleCollection](M_Tessa_Platform_Licensing_LicensingExtensions_ToLicenseModuleCollection.htm)|
Преобразует тип объекта
[ILicenseModuleCollection](T_Tessa_Platform_Licensing_ILicenseModuleCollection.htm)
в LicenseModuleCollection или создаёт новый объект LicenseModuleCollection,
свойства которого получены из заданного объекта.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
[ToObservableCollection<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<ILicenseModule>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<ILicenseModule>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
