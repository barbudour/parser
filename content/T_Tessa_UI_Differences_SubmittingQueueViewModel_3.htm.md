# SubmittingQueueViewModel<TItemModel, TItemViewModel, TObjectModel> \- класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Differences](N_Tessa_UI_Differences.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SubmittingQueueViewModel<TItemModel, TItemViewModel, TObjectModel> : ViewModelCollection<TItemModel, TItemViewModel>, 
    	ISubmittingQueueViewModel, IViewModelCollection<ISubmittingQueueItemViewModel>, IViewModel, INotifyPropertyChanged, 
    	IEnumerable<ISubmittingQueueItemViewModel>, IEnumerable, INotifyCollectionChanged
    where TItemModel : SubmittingQueueItem<TObjectModel>
    where TItemViewModel : SubmittingQueueItemViewModel<TItemModel, TObjectModel>
VB __Копировать
     Public MustInherit Class SubmittingQueueViewModel(Of TItemModel As SubmittingQueueItem(Of TObjectModel), TItemViewModel As SubmittingQueueItemViewModel(Of TItemModel, TObjectModel), TObjectModel)
    	Inherits ViewModelCollection(Of TItemModel, TItemViewModel)
    	Implements ISubmittingQueueViewModel, IViewModelCollection(Of ISubmittingQueueItemViewModel), 
    	IViewModel, INotifyPropertyChanged, IEnumerable(Of ISubmittingQueueItemViewModel), IEnumerable, 
    	INotifyCollectionChanged
C++ __Копировать
    generic<typename TItemModel, typename TItemViewModel, typename TObjectModel>
    where TItemModel : SubmittingQueueItem<TObjectModel>
    where TItemViewModel : SubmittingQueueItemViewModel<TItemModel, TObjectModel>
    public ref class SubmittingQueueViewModel abstract : public ViewModelCollection<TItemModel, TItemViewModel>, 
    	ISubmittingQueueViewModel, IViewModelCollection<ISubmittingQueueItemViewModel^>, IViewModel, INotifyPropertyChanged, 
    	IEnumerable<ISubmittingQueueItemViewModel^>, IEnumerable, INotifyCollectionChanged
F# __Копировать
     [<AbstractClassAttribute>]
    type SubmittingQueueViewModel<'TItemModel, 'TItemViewModel, 'TObjectModel when 'TItemModel : SubmittingQueueItem<'TObjectModel> when 'TItemViewModel : SubmittingQueueItemViewModel<'TItemModel, 'TObjectModel>> = 
        class
            inherit ViewModelCollection<'TItemModel, 'TItemViewModel>
            interface ISubmittingQueueViewModel
            interface IViewModelCollection<ISubmittingQueueItemViewModel>
            interface IViewModel
            interface INotifyPropertyChanged
            interface IEnumerable<ISubmittingQueueItemViewModel>
            interface IEnumerable
            interface INotifyCollectionChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ViewModelCollection](T_Tessa_UI_ViewModelCollection_2.htm)<TItemModel, TItemViewModel> __ SubmittingQueueViewModel<TItemModel, TItemViewModel, TObjectModel>
Derived
[Tessa.UI.Localization.Differences.LocalizationSubmittingQueueViewModel](T_Tessa_UI_Localization_Differences_LocalizationSubmittingQueueViewModel.htm)
[Tessa.UI.Scheme.Differences.SchemeSubmittingQueueViewModel](T_Tessa_UI_Scheme_Differences_SchemeSubmittingQueueViewModel.htm)
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ISubmittingQueueItemViewModel](T_Tessa_UI_Differences_ISubmittingQueueItemViewModel.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ISubmittingQueueViewModel](T_Tessa_UI_Differences_ISubmittingQueueViewModel.htm), [IViewModel](T_Tessa_UI_IViewModel.htm), [IViewModelCollection](T_Tessa_UI_IViewModelCollection_1.htm)<[ISubmittingQueueItemViewModel](T_Tessa_UI_Differences_ISubmittingQueueItemViewModel.htm)>
#### Параметры типа
TItemModel
TItemViewModel
TObjectModel
##  __Конструкторы
[SubmittingQueueViewModel<TItemModel, TItemViewModel,
TObjectModel>(SubmittingQueue<TObjectModel, TItemModel>,
ViewModelScope)](M_Tessa_UI_Differences_SubmittingQueueViewModel_3__ctor.htm)|
Инициализирует новый экземпляр класса SubmittingQueueViewModel<TItemModel,
TItemViewModel, TObjectModel>  
---|---  
[SubmittingQueueViewModel<TItemModel, TItemViewModel,
TObjectModel>(SubmittingQueue<TObjectModel, TItemModel>, ViewModelScope,
Boolean)](M_Tessa_UI_Differences_SubmittingQueueViewModel_3__ctor_1.htm)|
Инициализирует новый экземпляр класса SubmittingQueueViewModel<TItemModel,
TItemViewModel, TObjectModel>  
##  __Свойства
[CancelCommand](P_Tessa_UI_Differences_SubmittingQueueViewModel_3_CancelCommand.htm)|  
---|---  
[Count](P_Tessa_UI_ViewModelCollection_2_Count.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Exception](P_Tessa_UI_Differences_SubmittingQueueViewModel_3_Exception.htm)|  
[FaultedItem](P_Tessa_UI_Differences_SubmittingQueueViewModel_3_FaultedItem.htm)|  
[IsInitialized](P_Tessa_UI_ViewModelCollection_2_IsInitialized.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[IsReadOnly](P_Tessa_UI_ViewModelCollection_2_IsReadOnly.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Item](P_Tessa_UI_ViewModelCollection_2_Item.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Items](P_Tessa_UI_ViewModelCollection_2_Items.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Model](P_Tessa_UI_Differences_SubmittingQueueViewModel_3_Model.htm)|  
[ParentViewModel](P_Tessa_UI_ViewModelCollection_2_ParentViewModel.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[RefreshAndSubmitCommand](P_Tessa_UI_Differences_SubmittingQueueViewModel_3_RefreshAndSubmitCommand.htm)|  
[RefreshCommand](P_Tessa_UI_Differences_SubmittingQueueViewModel_3_RefreshCommand.htm)|  
[Scope](P_Tessa_UI_ViewModelCollection_2_Scope.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[State](P_Tessa_UI_Differences_SubmittingQueueViewModel_3_State.htm)|  
[SubmitCommand](P_Tessa_UI_Differences_SubmittingQueueViewModel_3_SubmitCommand.htm)|  
[SubmittedItemCount](P_Tessa_UI_Differences_SubmittingQueueViewModel_3_SubmittedItemCount.htm)|  
## __Методы
[Add](M_Tessa_UI_ViewModelCollection_2_Add.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
---|---  
[Cancel](M_Tessa_UI_Differences_SubmittingQueueViewModel_3_Cancel.htm)|  
[Clear](M_Tessa_UI_ViewModelCollection_2_Clear.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[ClearItems](M_Tessa_UI_ViewModelCollection_2_ClearItems.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Contains](M_Tessa_UI_ViewModelCollection_2_Contains.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[CopyTo](M_Tessa_UI_ViewModelCollection_2_CopyTo.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[CreateRefreshManager](M_Tessa_UI_Differences_SubmittingQueueViewModel_3_CreateRefreshManager.htm)|  
[CreateSubmitManager](M_Tessa_UI_Differences_SubmittingQueueViewModel_3_CreateSubmitManager.htm)|  
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
[GetEnumerator](M_Tessa_UI_ViewModelCollection_2_GetEnumerator.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetItemModel](M_Tessa_UI_ViewModelCollection_2_GetItemModel.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetItemModelCore](M_Tessa_UI_ViewModelCollection_2_GetItemModelCore.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetItemViewModel](M_Tessa_UI_ViewModelCollection_2_GetItemViewModel.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetItemViewModelCore](M_Tessa_UI_ViewModelCollection_2_GetItemViewModelCore.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IndexOf](M_Tessa_UI_ViewModelCollection_2_IndexOf.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Initialize](M_Tessa_UI_ViewModelCollection_2_Initialize.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[Insert](M_Tessa_UI_ViewModelCollection_2_Insert.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[InsertItem](M_Tessa_UI_ViewModelCollection_2_InsertItem.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Move](M_Tessa_UI_ViewModelCollection_2_Move.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[MoveItem](M_Tessa_UI_ViewModelCollection_2_MoveItem.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnCollectionChanged](M_Tessa_UI_ViewModelCollection_2_OnCollectionChanged.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnPropertyChanged(String)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnPropertyChangedAsync(String)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnReceiveWeakEvent](M_Tessa_UI_ViewModelCollection_2_OnReceiveWeakEvent.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnSourceItemInserted](M_Tessa_UI_ViewModelCollection_2_OnSourceItemInserted.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnSourceItemMoved](M_Tessa_UI_ViewModelCollection_2_OnSourceItemMoved.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnSourceItemRemoved](M_Tessa_UI_ViewModelCollection_2_OnSourceItemRemoved.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnSourceItemReplaced](M_Tessa_UI_ViewModelCollection_2_OnSourceItemReplaced.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[OnSourceItemsResetted](M_Tessa_UI_ViewModelCollection_2_OnSourceItemsResetted.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[RefreshAndSubmitAsync](M_Tessa_UI_Differences_SubmittingQueueViewModel_3_RefreshAndSubmitAsync.htm)|  
[RefreshAsync](M_Tessa_UI_Differences_SubmittingQueueViewModel_3_RefreshAsync.htm)|  
[Remove](M_Tessa_UI_ViewModelCollection_2_Remove.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[RemoveAt](M_Tessa_UI_ViewModelCollection_2_RemoveAt.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[RemoveItem](M_Tessa_UI_ViewModelCollection_2_RemoveItem.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[ReplaceItem](M_Tessa_UI_ViewModelCollection_2_ReplaceItem.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
[SubmitAsync](M_Tessa_UI_Differences_SubmittingQueueViewModel_3_SubmitAsync.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CollectionChanged](E_Tessa_UI_ViewModelCollection_2_CollectionChanged.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
---|---  
[PropertyChanged](E_Tessa_UI_ViewModelCollection_2_PropertyChanged.htm)|  
(Унаследован от [ViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_ViewModelCollection_2.htm))  
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
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<ISubmittingQueueItemViewModel>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
