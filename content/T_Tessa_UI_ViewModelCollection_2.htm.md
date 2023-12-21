# ViewModelCollection<TItemModel, TItemViewModel> \- класс
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ViewModelCollection<TItemModel, TItemViewModel> : IList<TItemViewModel>, 
    	ICollection<TItemViewModel>, IEnumerable<TItemViewModel>, IEnumerable, 
    	IList, ICollection, IReadOnlyList<TItemViewModel>, IReadOnlyCollection<TItemViewModel>, 
    	IViewModelCollection<TItemViewModel>, IViewModel, INotifyPropertyChanged, INotifyCollectionChanged, 
    	IWeakEventListener
    where TItemModel : class
    where TItemViewModel : class, IViewModel
VB __Копировать
     Public MustInherit Class ViewModelCollection(Of TItemModel As Class, TItemViewModel As {Class, IViewModel})
    	Implements IList(Of TItemViewModel), ICollection(Of TItemViewModel), 
    	IEnumerable(Of TItemViewModel), IEnumerable, IList, ICollection, 
    	IReadOnlyList(Of TItemViewModel), IReadOnlyCollection(Of TItemViewModel), 
    	IViewModelCollection(Of TItemViewModel), IViewModel, INotifyPropertyChanged, INotifyCollectionChanged, 
    	IWeakEventListener
C++ __Копировать
    generic<typename TItemModel, typename TItemViewModel>
    where TItemModel : ref class
    where TItemViewModel : ref class, IViewModel
    public ref class ViewModelCollection abstract : IList<TItemViewModel>, 
    	ICollection<TItemViewModel>, IEnumerable<TItemViewModel>, IEnumerable, 
    	IList, ICollection, IReadOnlyList<TItemViewModel>, IReadOnlyCollection<TItemViewModel>, 
    	IViewModelCollection<TItemViewModel>, IViewModel, INotifyPropertyChanged, INotifyCollectionChanged, 
    	IWeakEventListener
F# __Копировать
     [<AbstractClassAttribute>]
    type ViewModelCollection<'TItemModel, 'TItemViewModel when 'TItemModel : not struct when 'TItemViewModel : not struct and IViewModel> = 
        class
            interface IList<'TItemViewModel>
            interface ICollection<'TItemViewModel>
            interface IEnumerable<'TItemViewModel>
            interface IEnumerable
            interface IList
            interface ICollection
            interface IReadOnlyList<'TItemViewModel>
            interface IReadOnlyCollection<'TItemViewModel>
            interface IViewModelCollection<'TItemViewModel>
            interface IViewModel
            interface INotifyPropertyChanged
            interface INotifyCollectionChanged
            interface IWeakEventListener
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewModelCollection<TItemModel, TItemViewModel>
Derived
[Tessa.UI.Cards.Types.CardTypeObjectViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_Cards_Types_CardTypeObjectViewModelCollection_2.htm)
[Tessa.UI.Controls.GridColumnViewModelCollection](T_Tessa_UI_Controls_GridColumnViewModelCollection.htm)
[Tessa.UI.Controls.ItemsControlViewModel<TItemModel,
TItemViewModel>.ItemCollection](T_Tessa_UI_Controls_ItemsControlViewModel_2_ItemCollection.htm)
[Tessa.UI.Differences.SubmittingQueueViewModel<TItemModel, TItemViewModel,
TObjectModel>](T_Tessa_UI_Differences_SubmittingQueueViewModel_3.htm)
[Tessa.UI.EditableViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_EditableViewModelCollection_2.htm)
[Tessa.UI.Files.FileViewModelCollection](T_Tessa_UI_Files_FileViewModelCollection.htm)
[Tessa.UI.PartionableViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_PartionableViewModelCollection_2.htm)
[Tessa.UI.SelectableViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_SelectableViewModelCollection_2.htm)
[Tessa.UI.SortableViewModelCollection<TItemModel,
TItemViewModel>](T_Tessa_UI_SortableViewModelCollection_2.htm)
Подробнее __Less __
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItemViewModel>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<TItemViewModel>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<TItemViewModel>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<TItemViewModel>, [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<TItemViewModel>, [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.icollection), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IWeakEventListener](https://learn.microsoft.com/dotnet/api/system.windows.iweakeventlistener), [IViewModel](T_Tessa_UI_IViewModel.htm), [IViewModelCollection](T_Tessa_UI_IViewModelCollection_1.htm)<TItemViewModel>
#### Параметры типа
TItemModel
TItemViewModel
##  __Конструкторы
[ViewModelCollection<TItemModel,
TItemViewModel>(ViewModelCollection<TItemModel,
TItemViewModel>)](M_Tessa_UI_ViewModelCollection_2__ctor_2.htm)|
Инициализирует новый экземпляр класса ViewModelCollection<TItemModel,
TItemViewModel>  
---|---  
[ViewModelCollection<TItemModel, TItemViewModel>(IList<TItemModel>,
ViewModelScope)](M_Tessa_UI_ViewModelCollection_2__ctor.htm)| Инициализирует
новый экземпляр класса ViewModelCollection<TItemModel, TItemViewModel>  
[ViewModelCollection<TItemModel,
TItemViewModel>(ViewModelCollection<TItemModel, TItemViewModel>,
Boolean)](M_Tessa_UI_ViewModelCollection_2__ctor_3.htm)| Инициализирует новый
экземпляр класса ViewModelCollection<TItemModel, TItemViewModel>  
[ViewModelCollection<TItemModel, TItemViewModel>(IList<TItemModel>,
ViewModelScope, Boolean)](M_Tessa_UI_ViewModelCollection_2__ctor_1.htm)|
Инициализирует новый экземпляр класса ViewModelCollection<TItemModel,
TItemViewModel>  
##  __Свойства
[Count](P_Tessa_UI_ViewModelCollection_2_Count.htm)|  
---|---  
[IsInitialized](P_Tessa_UI_ViewModelCollection_2_IsInitialized.htm)|  
[IsReadOnly](P_Tessa_UI_ViewModelCollection_2_IsReadOnly.htm)|  
[Item](P_Tessa_UI_ViewModelCollection_2_Item.htm)|  
[Items](P_Tessa_UI_ViewModelCollection_2_Items.htm)|  
[Model](P_Tessa_UI_ViewModelCollection_2_Model.htm)|  
[ParentViewModel](P_Tessa_UI_ViewModelCollection_2_ParentViewModel.htm)|  
[Scope](P_Tessa_UI_ViewModelCollection_2_Scope.htm)|  
## __Методы
[Add](M_Tessa_UI_ViewModelCollection_2_Add.htm)|  
---|---  
[Clear](M_Tessa_UI_ViewModelCollection_2_Clear.htm)|  
[ClearItems](M_Tessa_UI_ViewModelCollection_2_ClearItems.htm)|  
[Contains](M_Tessa_UI_ViewModelCollection_2_Contains.htm)|  
[CopyTo](M_Tessa_UI_ViewModelCollection_2_CopyTo.htm)|  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetItemModel](M_Tessa_UI_ViewModelCollection_2_GetItemModel.htm)|  
[GetItemModelCore](M_Tessa_UI_ViewModelCollection_2_GetItemModelCore.htm)|  
[GetItemViewModel](M_Tessa_UI_ViewModelCollection_2_GetItemViewModel.htm)|  
[GetItemViewModelCore](M_Tessa_UI_ViewModelCollection_2_GetItemViewModelCore.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IndexOf](M_Tessa_UI_ViewModelCollection_2_IndexOf.htm)|  
[Initialize](M_Tessa_UI_ViewModelCollection_2_Initialize.htm)|  
[Insert](M_Tessa_UI_ViewModelCollection_2_Insert.htm)|  
[InsertItem](M_Tessa_UI_ViewModelCollection_2_InsertItem.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Move](M_Tessa_UI_ViewModelCollection_2_Move.htm)|  
[MoveItem](M_Tessa_UI_ViewModelCollection_2_MoveItem.htm)|  
[OnCollectionChanged](M_Tessa_UI_ViewModelCollection_2_OnCollectionChanged.htm)|  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
[OnPropertyChanged(String)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
[OnPropertyChangedAsync(PropertyChangedEventArgs)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
[OnPropertyChangedAsync(String)](M_Tessa_UI_ViewModelCollection_2_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
[OnReceiveWeakEvent](M_Tessa_UI_ViewModelCollection_2_OnReceiveWeakEvent.htm)|  
[OnSourceItemInserted](M_Tessa_UI_ViewModelCollection_2_OnSourceItemInserted.htm)|  
[OnSourceItemMoved](M_Tessa_UI_ViewModelCollection_2_OnSourceItemMoved.htm)|  
[OnSourceItemRemoved](M_Tessa_UI_ViewModelCollection_2_OnSourceItemRemoved.htm)|  
[OnSourceItemReplaced](M_Tessa_UI_ViewModelCollection_2_OnSourceItemReplaced.htm)|  
[OnSourceItemsResetted](M_Tessa_UI_ViewModelCollection_2_OnSourceItemsResetted.htm)|  
[Remove](M_Tessa_UI_ViewModelCollection_2_Remove.htm)|  
[RemoveAt](M_Tessa_UI_ViewModelCollection_2_RemoveAt.htm)|  
[RemoveItem](M_Tessa_UI_ViewModelCollection_2_RemoveItem.htm)|  
[ReplaceItem](M_Tessa_UI_ViewModelCollection_2_ReplaceItem.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CollectionChanged](E_Tessa_UI_ViewModelCollection_2_CollectionChanged.htm)|  
---|---  
[PropertyChanged](E_Tessa_UI_ViewModelCollection_2_PropertyChanged.htm)|  
## __Методы расширения
[AddRange<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AddRangeForList](M_Tessa_Platform_Collections_Extensions_AddRangeForList.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<TItemViewModel>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<TItemViewModel>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<TItemViewModel>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<TItemViewModel>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<TItemViewModel, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRangeForList](M_Tessa_Platform_Collections_Extensions_InsertRangeForList.htm)|
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
[LastIndexOf<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[LastIndexOf<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1_1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TItemViewModel,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TItemViewModel,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<TItemViewModel>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<TItemViewModel>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveAll<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveAllForList](M_Tessa_Platform_Collections_Extensions_RemoveAllForList.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<TItemViewModel>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<TItemViewModel, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<TItemViewModel>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<TItemViewModel>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<TItemViewModel>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
