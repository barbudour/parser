# ISubmittingQueueViewModel - интерфейс
##  __Definition
 **Пространство имён:** [Tessa.UI.Differences](N_Tessa_UI_Differences.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISubmittingQueueViewModel : IViewModelCollection<ISubmittingQueueItemViewModel>, 
    	IViewModel, INotifyPropertyChanged, IEnumerable<ISubmittingQueueItemViewModel>, IEnumerable, 
    	INotifyCollectionChanged
VB __Копировать
     Public Interface ISubmittingQueueViewModel
    	Inherits IViewModelCollection(Of ISubmittingQueueItemViewModel), IViewModel, INotifyPropertyChanged, 
    	IEnumerable(Of ISubmittingQueueItemViewModel), IEnumerable, INotifyCollectionChanged
C++ __Копировать
     public interface class ISubmittingQueueViewModel : IViewModelCollection<ISubmittingQueueItemViewModel^>, 
    	IViewModel, INotifyPropertyChanged, IEnumerable<ISubmittingQueueItemViewModel^>, IEnumerable, 
    	INotifyCollectionChanged
F# __Копировать
     type ISubmittingQueueViewModel = 
        interface
            interface IViewModelCollection<ISubmittingQueueItemViewModel>
            interface IViewModel
            interface INotifyPropertyChanged
            interface IEnumerable<ISubmittingQueueItemViewModel>
            interface IEnumerable
            interface INotifyCollectionChanged
        end
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ISubmittingQueueItemViewModel](T_Tessa_UI_Differences_ISubmittingQueueItemViewModel.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IViewModel](T_Tessa_UI_IViewModel.htm), [IViewModelCollection](T_Tessa_UI_IViewModelCollection_1.htm)<[ISubmittingQueueItemViewModel](T_Tessa_UI_Differences_ISubmittingQueueItemViewModel.htm)>
##  __Свойства
[CancelCommand](P_Tessa_UI_Differences_ISubmittingQueueViewModel_CancelCommand.htm)|  
---|---  
[Count](P_Tessa_UI_IViewModelCollection_1_Count.htm)|  
(Унаследован от
[IViewModelCollection<T>](T_Tessa_UI_IViewModelCollection_1.htm))  
[Exception](P_Tessa_UI_Differences_ISubmittingQueueViewModel_Exception.htm)|  
[FaultedItem](P_Tessa_UI_Differences_ISubmittingQueueViewModel_FaultedItem.htm)|  
[Item](P_Tessa_UI_IViewModelCollection_1_Item.htm)|  
(Унаследован от
[IViewModelCollection<T>](T_Tessa_UI_IViewModelCollection_1.htm))  
[Model](P_Tessa_UI_IViewModelCollection_1_Model.htm)|  
(Унаследован от
[IViewModelCollection<T>](T_Tessa_UI_IViewModelCollection_1.htm))  
[RefreshAndSubmitCommand](P_Tessa_UI_Differences_ISubmittingQueueViewModel_RefreshAndSubmitCommand.htm)|  
[RefreshCommand](P_Tessa_UI_Differences_ISubmittingQueueViewModel_RefreshCommand.htm)|  
[State](P_Tessa_UI_Differences_ISubmittingQueueViewModel_State.htm)|  
[SubmitCommand](P_Tessa_UI_Differences_ISubmittingQueueViewModel_SubmitCommand.htm)|  
[SubmittedItemCount](P_Tessa_UI_Differences_ISubmittingQueueViewModel_SubmittedItemCount.htm)|  
## __Методы
[Cancel](M_Tessa_UI_Differences_ISubmittingQueueViewModel_Cancel.htm)|  
---|---  
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1.getenumerator#system-
collections-generic-ienumerable-1-getenumerator)| Returns an enumerator that
iterates through the collection.  
(Унаследован от
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ISubmittingQueueItemViewModel](T_Tessa_UI_Differences_ISubmittingQueueItemViewModel.htm)>)  
[RefreshAndSubmitAsync](M_Tessa_UI_Differences_ISubmittingQueueViewModel_RefreshAndSubmitAsync.htm)|  
[RefreshAsync](M_Tessa_UI_Differences_ISubmittingQueueViewModel_RefreshAsync.htm)|  
[SubmitAsync](M_Tessa_UI_Differences_ISubmittingQueueViewModel_SubmitAsync.htm)|  
## __События
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged.collectionchanged)|
Occurs when the collection changes.  
(Унаследован от
[INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged))  
---|---  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
##  __Методы расширения
[AsArray<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
---|---  
[ConvertToListDictionaries<ISubmittingQueueItemViewModel>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<ISubmittingQueueItemViewModel>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<ISubmittingQueueItemViewModel, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ISubmittingQueueItemViewModel,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ISubmittingQueueItemViewModel,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<ISubmittingQueueItemViewModel>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<ISubmittingQueueItemViewModel>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<ISubmittingQueueItemViewModel>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToDictionaryAsync<ISubmittingQueueItemViewModel, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI.Differences - пространство имён](N_Tessa_UI_Differences.htm)
