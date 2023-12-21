# CardMetadataBuilderBase.MetadataContainer - класс
Контейнер, в котором собирается информацию о секциях и колонках, необходимых
для построения объекта [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)
в методе [BuildAsync(CardTypeCollection, ISchemeService,
CancellationToken)](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_BuildAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected sealed class MetadataContainer : IEnumerable<KeyValuePair<Guid, CardMetadataBuilderBase.SectionContainerInfo>>, 
    	IEnumerable
VB __Копировать
     Protected NotInheritable Class MetadataContainer
    	Implements IEnumerable(Of KeyValuePair(Of Guid, CardMetadataBuilderBase.SectionContainerInfo)), 
    	IEnumerable
C++ __Копировать
     protected ref class MetadataContainer sealed : IEnumerable<KeyValuePair<Guid, CardMetadataBuilderBase.SectionContainerInfo^>>, 
    	IEnumerable
F# __Копировать
     [<SealedAttribute>]
    type MetadataContainer = 
        class
            interface IEnumerable<KeyValuePair<Guid, CardMetadataBuilderBase.SectionContainerInfo>>
            interface IEnumerable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMetadataBuilderBase.MetadataContainer
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [CardMetadataBuilderBase.SectionContainerInfo](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_SectionContainerInfo.htm)>>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
##  __Конструкторы
[CardMetadataBuilderBase.MetadataContainer](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer__ctor.htm)|
Создаёт экземпляр класса с указанием максимально допустимого числа типов
карточек, информацию о которых может содержать одна колонка.  
---|---  
## __Свойства
[Count](P_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer_Count.htm)|
Количество секций, информацию о которых содержит контейнер.  
---|---  
[DelayedSchemeCheckCardTypeIDSet](P_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer_DelayedSchemeCheckCardTypeIDSet.htm)|
Идентификаторы типов карточек, проверка схемы для которых выполняется после
выполнения всех расширений на метаинформацию.  
[Sections](P_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer_Sections.htm)|  
## __Методы
[AddComplexColumn](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer_AddComplexColumn.htm)|
Добавляет информацию о комплексной колонке.  
---|---  
[AddPhysicalColumn](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer_AddPhysicalColumn.htm)|
Добавляет информацию о физической колонке.  
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
[GetEnumerator](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer_GetEnumerator.htm)|
Returns an enumerator that iterates through a collection.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetOrAddSectionInfo](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer_GetOrAddSectionInfo.htm)|
Возвращает собранную информацию по секции с заданным идентификатором, если
информация по секции с таким идентификатором не найдена, то создает ее.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[AsArray<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
---|---  
[ForEach<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
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
[OrderByDependencies<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<KeyValuePair<Guid,
CardMetadataBuilderBase.SectionContainerInfo>>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
