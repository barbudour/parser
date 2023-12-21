# FileSourceGrouping - класс
Группировка по источнику файла.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.ExternalFiles](N_Tessa_Extensions_Default_Client_ExternalFiles.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FileSourceGrouping : FileGrouping
VB __Копировать
     Public NotInheritable Class FileSourceGrouping
    	Inherits FileGrouping
C++ __Копировать
     public ref class FileSourceGrouping sealed : public FileGrouping
F# __Копировать
     [<SealedAttribute>]
    type FileSourceGrouping = 
        class
            inherit FileGrouping
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[ViewModel](T_Tessa_UI_ViewModel_1.htm)<[EmptyModel](T_Tessa_UI_EmptyModel.htm)> __[FileControlObject](T_Tessa_UI_Files_FileControlObject.htm) __[FileGrouping](T_Tessa_UI_Files_FileGrouping.htm) __ FileSourceGrouping
##  __Заметки
Класс-наследник может переопределить поведение класса, например, установить
сортировку по умолчанию для данной группировки.
## __Конструкторы
[FileSourceGrouping](M_Tessa_Extensions_Default_Client_ExternalFiles_FileSourceGrouping__ctor.htm)|
Инициализирует новый экземпляр класса FileSourceGrouping  
---|---  
##  __Свойства
[Caption](P_Tessa_UI_Files_FileControlObject_Caption.htm)| Отображаемое имя
объекта.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
---|---  
[IsCollapsed](P_Tessa_UI_Files_FileControlObject_IsCollapsed.htm)| Признак
того, что объект скрыт от пользователя и может быть выбран только из кода.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[Model](P_Tessa_UI_ViewModel_1_Model.htm)|  Модель для текущей модели
представления.  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[Name](P_Tessa_UI_Files_FileControlObject_Name.htm)| Имя объекта, по которому
объект можно идентифицировать в коллекциях.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[Scope](P_Tessa_UI_ViewModel_1_Scope.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
##  __Методы
[Attach](M_Tessa_UI_Files_FileControlObject_Attach.htm)| Добавляет поведение,
свойственное для текущего объекта, для заданной модели представления файла.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
---|---  
[Detach](M_Tessa_UI_Files_FileControlObject_Detach.htm)| Удаляет поведение,
свойственное для текущего объекта, для заданной модели представления файла.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[Equals(IFileControlObject)](M_Tessa_UI_Files_FileControlObject_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[Equals(Object)](M_Tessa_UI_Files_FileControlObject_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FinalizeAsync](M_Tessa_UI_Files_FileControlObject_FinalizeAsync.htm)|
Финализирует текущий объект для заданного элемента управления файлами. Обычно
выполняется код очистки и возврата элемента управления к исходному состоянию.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[FinalizeCoreAsync](M_Tessa_UI_Files_FileControlObject_FinalizeCoreAsync.htm)|
Финализирует текущий объект для заданного элемента управления файлами. Обычно
выполняется код очистки и возврата элемента управления к исходному состоянию.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[GetGroupInfo](M_Tessa_UI_Files_FileGrouping_GetGroupInfo.htm)|  Возвращает
структуру, которая описывает информацию по группе для заданной модели
представления файла, по которой выполняется группировка. Структура
определяется идентификатор группы, отображаемое название и строку для
сортировки.  
(Унаследован от [FileGrouping](T_Tessa_UI_Files_FileGrouping.htm))  
[GetGroupInfoCore](M_Tessa_Extensions_Default_Client_ExternalFiles_FileSourceGrouping_GetGroupInfoCore.htm)|  
(Переопределяет
[FileGrouping.GetGroupInfoCore(IFileViewModel)](M_Tessa_UI_Files_FileGrouping_GetGroupInfoCore.htm))  
[GetHashCode](M_Tessa_UI_Files_FileControlObject_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_UI_Files_FileControlObject_InitializeAsync.htm)|
Инициализирует текущий объект для заданного элемента управления файлами.
Обычно выполняется код, подготавливающий элемент управления к работе с
объектом.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[InitializeCoreAsync](M_Tessa_UI_Files_FileControlObject_InitializeCoreAsync.htm)|
Инициализирует текущий объект для заданного элемента управления файлами.
Обычно выполняется код, подготавливающий элемент управления к работе с
объектом.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NotifyAdded](M_Tessa_UI_Files_FileControlObject_NotifyAdded.htm)|  Вызов
этого метода уведомляет объект о том, что в коллекцию был добавлен элемент
item. Коллекцию можно получить из свойства [IFileViewModel.Collection].  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[NotifyRemoved](M_Tessa_UI_Files_FileControlObject_NotifyRemoved.htm)|  Вызов
этого метода уведомляет объект о том, что из коллекции был удалён элемент
item. Коллекцию можно получить из свойства [IFileViewModel.Collection].  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[OnModelPropertyChanged](M_Tessa_UI_ViewModel_1_OnModelPropertyChanged.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_UI_NotificationUIObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnReceiveWeakEvent](M_Tessa_UI_ViewModel_1_OnReceiveWeakEvent.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[StartListening](M_Tessa_UI_Files_FileControlObject_StartListening.htm)|
Запускает наблюдение за свойствами моделей представления файлов, содержащихся
в коллекции.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[StopListening](M_Tessa_UI_Files_FileControlObject_StopListening.htm)|
Останавливает наблюдение за свойствами моделей представления файлов,
содержащихся в коллекции.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[SuggestUpdate](M_Tessa_UI_Files_FileControlObject_SuggestUpdate.htm)|
Выполняет принудительное уведомление подписчиков события
[IFileViewModelListener.UpdateSuggested].  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
[ToString](M_Tessa_UI_Files_FileControlObject_ToString.htm)| Возвращает
строковое представление объекта.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
[UpdateSuggested](E_Tessa_UI_Files_FileControlObject_UpdateSuggested.htm)|
Событие, происходящее при изменении наблюдаемых свойств у моделей или моделей
представления файлов.  
(Унаследован от [FileControlObject](T_Tessa_UI_Files_FileControlObject.htm))  
##  __Поля
[CardSourceGroupName](F_Tessa_Extensions_Default_Client_ExternalFiles_FileSourceGrouping_CardSourceGroupName.htm)|  
---|---  
[ExternalSourceGroupName](F_Tessa_Extensions_Default_Client_ExternalFiles_FileSourceGrouping_ExternalSourceGroupName.htm)|  
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
[Tessa.Extensions.Default.Client.ExternalFiles - пространство
имён](N_Tessa_Extensions_Default_Client_ExternalFiles.htm)
