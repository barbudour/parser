# IValidationResultBuilder - интерфейс
Объект, выполняющий построение результата валидации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IValidationResultBuilder : IReadOnlyList<IValidationResultItem>, 
    	IEnumerable<IValidationResultItem>, IEnumerable, IReadOnlyCollection<IValidationResultItem>, 
    	IFormattable
VB __Копировать
     Public Interface IValidationResultBuilder
    	Inherits IReadOnlyList(Of IValidationResultItem), IEnumerable(Of IValidationResultItem), 
    	IEnumerable, IReadOnlyCollection(Of IValidationResultItem), IFormattable
C++ __Копировать
     public interface class IValidationResultBuilder : IReadOnlyList<IValidationResultItem^>, 
    	IEnumerable<IValidationResultItem^>, IEnumerable, IReadOnlyCollection<IValidationResultItem^>, 
    	IFormattable
F# __Копировать
     type IValidationResultBuilder = 
        interface
            interface IReadOnlyList<IValidationResultItem>
            interface IEnumerable<IValidationResultItem>
            interface IEnumerable
            interface IReadOnlyCollection<IValidationResultItem>
            interface IFormattable
        end
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>, [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IFormattable](https://learn.microsoft.com/dotnet/api/system.iformattable)
##  __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1.count#system-
collections-generic-ireadonlycollection-1-count)| Gets the number of elements
in the collection.  
(Унаследован от
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>)  
---|---  
[Item](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1.item#system-
collections-generic-ireadonlylist-1-item\(system-int32\))| Gets the element at
the specified index in the read-only list.  
(Унаследован от
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>)  
##  __Методы
[Add(IValidationResultBuilder)](M_Tessa_Platform_Validation_IValidationResultBuilder_Add.htm)|
Добавляет сообщения валидации, которые были добавлены в заданный объект,
выполняющий построение результата валидации.  
---|---  
[Add(IValidationResultItem)](M_Tessa_Platform_Validation_IValidationResultBuilder_Add_1.htm)|
Добавляет копию указанного сообщения валидации.  
[Add(ValidationResult)](M_Tessa_Platform_Validation_IValidationResultBuilder_Add_3.htm)|
Добавляет сообщения о валидации, заданные в указанном результате валидации.  
[Add(ValidationKey, ValidationResultType, String, String, String, String,
String)](M_Tessa_Platform_Validation_IValidationResultBuilder_Add_2.htm)|
Добавляет информационное сообщение с указанным текстом.  
[Build](M_Tessa_Platform_Validation_IValidationResultBuilder_Build.htm)|
Выполняет построение объекта, содержащего результат валидации.  
[Clear](M_Tessa_Platform_Validation_IValidationResultBuilder_Clear.htm)|
Удаляет все сообщения валидации.  
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1.getenumerator#system-
collections-generic-ienumerable-1-getenumerator)| Returns an enumerator that
iterates through the collection.  
(Унаследован от
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IValidationResultItem](T_Tessa_Platform_Validation_IValidationResultItem.htm)>)  
[HasData](M_Tessa_Platform_Validation_IValidationResultBuilder_HasData.htm)|
Возвращает признак того, что объект содержит сообщения валидации.  
[IsSuccessful](M_Tessa_Platform_Validation_IValidationResultBuilder_IsSuccessful.htm)|
Возвращает признак того, что результат валидации при его построении будет
успешным.  
[Remove](M_Tessa_Platform_Validation_IValidationResultBuilder_Remove.htm)|
Удаляет заданное сообщение валидации. Возвращает признак того, что сообщение
было найдено и удалено.  
[RemoveAll(String)](M_Tessa_Platform_Validation_IValidationResultBuilder_RemoveAll.htm)|
Удаляет все сообщения валидации, которые добавлены с заданным сообщением.
Возвращает количество удалённых сообщений.  
[RemoveAll(ValidationKey)](M_Tessa_Platform_Validation_IValidationResultBuilder_RemoveAll_1.htm)|
Удаляет все сообщения валидации, которые добавлены с заданным ключом.
Возвращает количество удалённых сообщений.  
[RemoveAt](M_Tessa_Platform_Validation_IValidationResultBuilder_RemoveAt.htm)|
Удаляет сообщение валидации с заданным индексом.  
[ToString(ValidationLevel)](M_Tessa_Platform_Validation_IValidationResultBuilder_ToString.htm)|
Возвращает текстовое представление для сообщений валидации с указанным режимом
вывода.  
[ToString(String,
IFormatProvider)](https://learn.microsoft.com/dotnet/api/system.iformattable.tostring#system-
iformattable-tostring\(system-string-system-iformatprovider\))| Formats the
value of the current instance using the specified format.  
(Унаследован от
[IFormattable](https://learn.microsoft.com/dotnet/api/system.iformattable))  
##  __Методы расширения
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
[IndexOf<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IValidationResultItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
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
