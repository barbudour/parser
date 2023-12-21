# RemoteFileContent - методы
##  __Методы
[CheckDisposed](M_Tessa_Files_FileContent_CheckDisposed.htm)|  Выбрасывает
исключение [ObjectDisposedException], если ресурсы текущего объекта были
освобождены.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
---|---  
[CheckSealed](M_Tessa_Files_FileContent_CheckSealed.htm)|  Выбрасывает
исключение [Tessa.Platform.ObjectSealedException], если объект был защищён от
изменений.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[DisposeAsync()](M_Tessa_Files_FileContent_DisposeAsync.htm)| Освобождает
ресурсы, занимаемые объектом.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[DisposeAsync(Boolean)](M_Tessa_Files_FileContent_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[EnsureLocalUpdatedAsync](M_Tessa_Files_FileContent_EnsureLocalUpdatedAsync.htm)|
Удостоверяет, что файл будет загружен локально и доступен по пути
[IFileContent.GetLocalFilePath], если файл является локальным
[IFileContent.IsLocal]. Если файл не локальный, то метод не выполняет
действий.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[EnterLockAsync](M_Tessa_Files_FileContent_EnterLockAsync.htm)|  Выполняет
вход в блок, в пределах которого нет других обращений к контенту файла.
Вызовите метод в блоке using(await
content.EnterLockAsync().ConfigureAwait(false)).  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
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
[FromContentAsync](M_Tessa_Files_RemoteFileContent_FromContentAsync.htm)|
Создаёт объект контента файла, содержимое и размер которого определяются по
заданному объекту контента content.  
[FromFilePathAsync](M_Tessa_Files_RemoteFileContent_FromFilePathAsync.htm)|
Создаёт объект контента файла, который соответствует заданному файлу,
доступному по полному пути на диске filePath.  
[FromStreamAndSizeAsync](M_Tessa_Files_RemoteFileContent_FromStreamAndSizeAsync.htm)|
Создаёт объект контента файла, который может быть получен по заданному функции
getContentFuncAsync и имеет фиксированный (заранее вычисленный) размер. Если
размер не является фиксированным, то следует использовать конструктор
[RemoteFileContent](T_Tessa_Files_RemoteFileContent.htm)/  
[GetAsync](M_Tessa_Files_FileContent_GetAsync.htm)|  Открывает и возвращает
поток с контентом файла. Если контент файла отсутствует, то вызывает
исключение [System.InvalidOperationException]. Поэтому перед получением
контента можно обратиться к свойству [IFileContent.HasData].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[GetCoreAsync](M_Tessa_Files_RemoteFileContent_GetCoreAsync.htm)|  Возвращает
поток с содержимым файла. Если файл не был загружен, то может быть выброшено
исключение.  
(Переопределяет
[FileContent.GetCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_GetCoreAsync.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLocalFilePath](M_Tessa_Files_FileContent_GetLocalFilePath.htm)|
Возвращает локальный путь к контенту файла, если контент доступен локально.
Если контент не доступен локально, то вызывает исключение
[System.InvalidOperationException]. Поэтому перед вызовом метода можно
обратиться к свойству [IFileContent.IsLocal].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[GetLocalFilePathCore](M_Tessa_Files_RemoteFileContent_GetLocalFilePathCore.htm)|
Возвращает путь к файлу с локальным контентом, даже если он ещё не был
загружен, или null, если контент не представлен локальным файлом.  
(Переопределяет
[FileContent.GetLocalFilePathCore()](M_Tessa_Files_FileContent_GetLocalFilePathCore.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_Files_FileContent_InitializeAsync.htm)| Выполняет
асинхронную инициализацию объекта.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[InvalidateAsync](M_Tessa_Files_FileContent_InvalidateAsync.htm)|  Удаляет
локально загруженный контент, переводя его в начальное состояние. Следующий
раз при получении контента он будет заново загружен.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[InvalidateCoreAsync](M_Tessa_Files_RemoteFileContent_InvalidateCoreAsync.htm)|
Сбрасывает информацию о контенте файла. Например, очищает дату изменения
файла. Если контент не является локальным, то может не выполнять действий.  
(Переопределяет
[FileContent.InvalidateCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_InvalidateCoreAsync.htm))  
[IsModifiedAsync](M_Tessa_Files_FileContent_IsModifiedAsync.htm)|  Возвращает
признак того, что контент файла на диске был изменён с момента его установки
методом [IFileContent.Set]. Для защищённых от изменений объектов метод всегда
возвращает false.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[IsModifiedCoreAsync](M_Tessa_Files_RemoteFileContent_IsModifiedCoreAsync.htm)|
Возвращает признак того, что локальный контент был изменён. Например, был
изменён файл на диске по дате изменения. При изменении контента может быть
обновлён его размер, а также он может быть, например, помечен как изменённый в
структуре карточки.  
(Переопределяет
[FileContent.IsModifiedCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_IsModifiedCoreAsync.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[PrepareContentLocationCoreAsync](M_Tessa_Files_RemoteFileContent_PrepareContentLocationCoreAsync.htm)|
Подготавливает местоположение контента перед его записью или перемещением в
это местоположение. Например, создаёт папку на диске, если контент представлен
файлом на диске.  
(Переопределяет
[FileContent.PrepareContentLocationCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_PrepareContentLocationCoreAsync.htm))  
[RemoveContentSafeCoreAsync](M_Tessa_Files_RemoteFileContent_RemoveContentSafeCoreAsync.htm)|
Метод удаляет локальный контент, если он был создан. Если контент не является
локальным, то метод не должен выполнять действий. Метод не должен выбрасывать
исключений, даже критичных.  
(Переопределяет
[FileContent.RemoveContentSafeCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_RemoveContentSafeCoreAsync.htm))  
[RenameAsync](M_Tessa_Files_FileContent_RenameAsync.htm)|  Переименовывает
файл, в который записывается контент. Если файл ещё не существует, то он будет
назван по-другому в момент создания. Метод гарантированно сработает только в
том случае, если контент является локальным, т.е. свойство
[IFileContent.IsLocal] возвращает true.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[RenameCoreAsync](M_Tessa_Files_RemoteFileContent_RenameCoreAsync.htm)|
Переименовывает имя контента в соответствии с новым именем файла. Если контент
представлен локальным файлом на диске, то метод должен переименовать этот
файл. Если контент не является локальным, то метод может не выполнять
действий.  
(Переопределяет [FileContent.RenameCoreAsync(String,
CancellationToken)](M_Tessa_Files_FileContent_RenameCoreAsync.htm))  
[Seal](M_Tessa_Files_FileContent_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[SetAsync](M_Tessa_Files_FileContent_SetAsync.htm)| Открывает и возвращает
поток, выполняющий перезапись контента файла.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[SetCoreAsync](M_Tessa_Files_RemoteFileContent_SetCoreAsync.htm)|
Устанавливает содержимое файла. Если контент запрещено изменять, то может быть
выброшено исключение.  
(Переопределяет [FileContent.SetCoreAsync(Stream,
CancellationToken)](M_Tessa_Files_FileContent_SetCoreAsync.htm))  
[SetLocalAsync](M_Tessa_Files_FileContent_SetLocalAsync.htm)| Устанавливает
контент локального файла по заданному пути.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[SetLocalCoreAsync](M_Tessa_Files_RemoteFileContent_SetLocalCoreAsync.htm)|
Устанавливает локальное содержимое файла, представленное в виде файла на
диске, по заданному методу, который получает в параметре путь к файлу на диске
и может его создать или изменить некоторым способом. Если содержимое файла не
является локальным, то может быть выброшено исключение.  
(Переопределяет [FileContent.SetLocalCoreAsync(Func<String, CancellationToken,
ValueTask>,
CancellationToken)](M_Tessa_Files_FileContent_SetLocalCoreAsync.htm))  
[SetRemoteAsync](M_Tessa_Files_FileContent_SetRemoteAsync.htm)|  Устанавливает
содержимое файла, представленное заданными методами. Если контент запрещено
изменять, то может быть выброшено исключение. Метод доступен как для локальных
файлов, так и для нелокальных (remote), в т.ч. для файлов большого размера.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[SetRemoteCoreAsync](M_Tessa_Files_RemoteFileContent_SetRemoteCoreAsync.htm)|
Устанавливает содержимое файла, представленное заданными методами. Если
контент запрещено изменять, то может быть выброшено исключение. Метод доступен
как для локальных файлов, так и для нелокальных (remote), в т.ч. для файлов
большого размера.  
(Переопределяет [FileContent.SetRemoteCoreAsync(Func<CancellationToken,
ValueTask<Stream>>, Func<CancellationToken, ValueTask<Int64>>,
CancellationToken)](M_Tessa_Files_FileContent_SetRemoteCoreAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateLocalContentFromParentCoreAsync](M_Tessa_Files_RemoteFileContent_UpdateLocalContentFromParentCoreAsync.htm)|
Обновляет локальный контент на основании контента родительского объекта. При
вызове этого метода гарантируется, что у текущего контента есть родительский
контент, в котором присутствуют загруженные данные. Если контент не локальный,
то метод может не выполнять действий, но не должен выбрасывать исключений.  
(Переопределяет
[FileContent.UpdateLocalContentFromParentCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_UpdateLocalContentFromParentCoreAsync.htm))  
[UpdateModifiedCoreAsync](M_Tessa_Files_RemoteFileContent_UpdateModifiedCoreAsync.htm)|
Обновляет информацию, на основании которой можно определить, изменялся ли
контент. Например, сохраняет время изменения файла, чтобы его можно было
сравнить со временем изменения в любой другой момент.  
(Переопределяет
[FileContent.UpdateModifiedCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_UpdateModifiedCoreAsync.htm))  
[UpdateSizeAsync](M_Tessa_Files_FileContent_UpdateSizeAsync.htm)|  Обновляет
свойство с размером контента [IFileContent.Size] для загруженных файлов.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[UpdateSizeCoreAsync](M_Tessa_Files_RemoteFileContent_UpdateSizeCoreAsync.htm)|
Обновляет размер локального контента. Возвращает true, если размер был
обновлён.  
(Переопределяет
[FileContent.UpdateSizeCoreAsync(CancellationToken)](M_Tessa_Files_FileContent_UpdateSizeCoreAsync.htm))  
##  __Методы расширения
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
[RemoteFileContent - ](T_Tessa_Files_RemoteFileContent.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
