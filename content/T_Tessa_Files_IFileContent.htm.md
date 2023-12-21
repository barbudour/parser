# IFileContent - интерфейс
Контент файла.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileContent : INotifyPropertyChanged, 
    	IAsyncDisposable, IAsyncInitializable, ISealable
VB __Копировать
     Public Interface IFileContent
    	Inherits INotifyPropertyChanged, IAsyncDisposable, IAsyncInitializable, ISealable
C++ __Копировать
     public interface class IFileContent : INotifyPropertyChanged, 
    	IAsyncDisposable, IAsyncInitializable, ISealable
F# __Копировать
     type IFileContent = 
        interface
            interface INotifyPropertyChanged
            interface IAsyncDisposable
            interface IAsyncInitializable
            interface ISealable
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[Cancellation](P_Tessa_Files_IFileContent_Cancellation.htm)|  Объект, который
может использоваться для отмены асинхронных операций с содержимым файла, если
оно поддерживает отмену. На текущий момент это доступно для загрузки
содержимого версии файла.  
---|---  
[HasData](P_Tessa_Files_IFileContent_HasData.htm)|  Возвращает признак того,
что контент файла был установлен методом [IFileContent.Set].  
[IsBoundToFileSource](P_Tessa_Files_IFileContent_IsBoundToFileSource.htm)|
Признак того, что контент был создан источником файлов, а не передан снаружи,
поэтому для оптимизации обращения к содержимому можно использовать источник
файлов. Обычно актуально для Remote-контента.  
[IsDirty](P_Tessa_Files_IFileContent_IsDirty.htm)|  Признак того, что контент
мог быть изменён. Следует установить значение равным true перед открытием
контента на редактирование во внешней программе. Определить точно, был ли
изменён контент, можно, вызвав метод [IFileContent.IsModified].  
[IsDisposed](P_Tessa_Files_IFileContent_IsDisposed.htm)| Признак того, что
контент был освобождён и объект нельзя использовать.  
[IsLocal](P_Tessa_Files_IFileContent_IsLocal.htm)|  Признак того, что контент
является локальным, т.е. к нему можно получить локальный путь посредством
метода [IFileContent.GetLocalFilePath].  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Parent](P_Tessa_Files_IFileContent_Parent.htm)|  Родительский контент или
null, если родительский контент отсутствует. Если производится запрос текущего
контента, и он не был установлен, то он сначала локально копируется из
родительского, если тот существует, а затем считывается локально.  
[RequestInfo](P_Tessa_Files_IFileContent_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запросы к серверу, которые
относятся к загрузке содержимого файла или версии, которые сохраняются в
текущем объекте. Рекомендуется, чтобы все данные были сериализуемых типов (в
соответствии с типовой BSON-сериализацией в системе). Такие данные могут
перезаписать данные из [IFileObject.RequestInfo].  
[Size](P_Tessa_Files_IFileContent_Size.htm)|  Размер контента файла в байтах
или 0, если контент ещё не был загружен. Проверить, был ли загружен контент,
можно, обратившись к свойству [IFileContent.HasData].  
[Uri](P_Tessa_Files_IFileContent_Uri.htm)|  Ссылка к контенту файла, который
может быть доступен как локально (на диске), так и удалённо (сетевой ресурс).
Значение может быть равно null, если контент недоступен по ссылке.  
## __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[EnsureLocalUpdatedAsync](M_Tessa_Files_IFileContent_EnsureLocalUpdatedAsync.htm)|
Удостоверяет, что файл будет загружен локально и доступен по пути
[IFileContent.GetLocalFilePath], если файл является локальным
[IFileContent.IsLocal]. Если файл не локальный, то метод не выполняет
действий.  
[EnterLockAsync](M_Tessa_Files_IFileContent_EnterLockAsync.htm)|  Выполняет
вход в блок, в пределах которого нет других обращений к контенту файла.
Вызовите метод в блоке using(await
content.EnterLockAsync().ConfigureAwait(false)).  
[GetAsync](M_Tessa_Files_IFileContent_GetAsync.htm)|  Открывает и возвращает
поток с контентом файла. Если контент файла отсутствует, то вызывает
исключение [System.InvalidOperationException]. Поэтому перед получением
контента можно обратиться к свойству [IFileContent.HasData].  
[GetLocalFilePath](M_Tessa_Files_IFileContent_GetLocalFilePath.htm)|
Возвращает локальный путь к контенту файла, если контент доступен локально.
Если контент не доступен локально, то вызывает исключение
[System.InvalidOperationException]. Поэтому перед вызовом метода можно
обратиться к свойству [IFileContent.IsLocal].  
[InitializeAsync](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm)|
Выполняет асинхронную инициализацию объекта.  
(Унаследован от
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm))  
[InvalidateAsync](M_Tessa_Files_IFileContent_InvalidateAsync.htm)|  Удаляет
локально загруженный контент, переводя его в начальное состояние. Следующий
раз при получении контента он будет заново загружен.  
[IsModifiedAsync](M_Tessa_Files_IFileContent_IsModifiedAsync.htm)|  Возвращает
признак того, что контент файла на диске был изменён с момента его установки
методом [IFileContent.Set]. Для защищённых от изменений объектов метод всегда
возвращает false.  
[RenameAsync](M_Tessa_Files_IFileContent_RenameAsync.htm)|  Переименовывает
файл, в который записывается контент. Если файл ещё не существует, то он будет
назван по-другому в момент создания. Метод гарантированно сработает только в
том случае, если контент является локальным, т.е. свойство
[IFileContent.IsLocal] возвращает true.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[SetAsync](M_Tessa_Files_IFileContent_SetAsync.htm)| Открывает и возвращает
поток, выполняющий перезапись контента файла.  
[SetLocalAsync](M_Tessa_Files_IFileContent_SetLocalAsync.htm)| Устанавливает
контент локального файла по заданному пути.  
[SetRemoteAsync](M_Tessa_Files_IFileContent_SetRemoteAsync.htm)|
Устанавливает содержимое файла, представленное заданными методами. Если
контент запрещено изменять, то может быть выброшено исключение. Метод доступен
как для локальных файлов, так и для нелокальных (remote), в т.ч. для файлов
большого размера.  
[UpdateSizeAsync](M_Tessa_Files_IFileContent_UpdateSizeAsync.htm)|  Обновляет
свойство с размером контента [IFileContent.Size] для загруженных файлов.  
## __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __Методы расширения
[ResolveRoot](M_Tessa_Files_FileExtensions_ResolveRoot.htm)|  Возвращает
корневой объект содержимого по свойствам
[Parent](P_Tessa_Files_IFileContent_Parent.htm). Возвращает текущий объект
content, если у него отсутствует родитель
[Parent](P_Tessa_Files_IFileContent_Parent.htm).  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
---|---  
[SetRemoteFromPathAsync](M_Tessa_Files_FileExtensions_SetRemoteFromPathAsync.htm)|
Устанавливает содержимое IFileContent по физическому файлу, расположенному по
заданному пути. Метод доступен и для локального, и для нелокального (remote)
содержимого.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
