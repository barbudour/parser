# FileContent - методы
##  __Методы
[CheckDisposed](M_Tessa_Files_FileContent_CheckDisposed.htm)|  Выбрасывает
исключение [ObjectDisposedException], если ресурсы текущего объекта были
освобождены.  
---|---  
[CheckSealed](M_Tessa_Files_FileContent_CheckSealed.htm)|  Выбрасывает
исключение [Tessa.Platform.ObjectSealedException], если объект был защищён от
изменений.  
[DisposeAsync()](M_Tessa_Files_FileContent_DisposeAsync.htm)| Освобождает
ресурсы, занимаемые объектом.  
[DisposeAsync(Boolean)](M_Tessa_Files_FileContent_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
[EnsureLocalUpdatedAsync](M_Tessa_Files_FileContent_EnsureLocalUpdatedAsync.htm)|
Удостоверяет, что файл будет загружен локально и доступен по пути
[IFileContent.GetLocalFilePath], если файл является локальным
[IFileContent.IsLocal]. Если файл не локальный, то метод не выполняет
действий.  
[EnterLockAsync](M_Tessa_Files_FileContent_EnterLockAsync.htm)|  Выполняет
вход в блок, в пределах которого нет других обращений к контенту файла.
Вызовите метод в блоке using(await
content.EnterLockAsync().ConfigureAwait(false)).  
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
[GetAsync](M_Tessa_Files_FileContent_GetAsync.htm)|  Открывает и возвращает
поток с контентом файла. Если контент файла отсутствует, то вызывает
исключение [System.InvalidOperationException]. Поэтому перед получением
контента можно обратиться к свойству [IFileContent.HasData].  
[GetContentFromFilePathFuncAsync](M_Tessa_Files_FileContent_GetContentFromFilePathFuncAsync.htm)|
Возвращает функцию, которая получает контент файла по заданному пути. Функцию
можно использовать при создании контента
[RemoteFileContent](T_Tessa_Files_RemoteFileContent.htm).  
[GetCoreAsync](M_Tessa_Files_FileContent_GetCoreAsync.htm)|  Возвращает поток
с содержимым файла. Если файл не был загружен, то может быть выброшено
исключение.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLocalFilePath](M_Tessa_Files_FileContent_GetLocalFilePath.htm)|
Возвращает локальный путь к контенту файла, если контент доступен локально.
Если контент не доступен локально, то вызывает исключение
[System.InvalidOperationException]. Поэтому перед вызовом метода можно
обратиться к свойству [IFileContent.IsLocal].  
[GetLocalFilePathCore](M_Tessa_Files_FileContent_GetLocalFilePathCore.htm)|
Возвращает путь к файлу с локальным контентом, даже если он ещё не был
загружен, или null, если контент не представлен локальным файлом.  
[GetSizeFromFilePathFuncAsync](M_Tessa_Files_FileContent_GetSizeFromFilePathFuncAsync.htm)|
Возвращает функцию, которая получает размер файла по заданному пути. Функцию
можно использовать при создании контента
[RemoteFileContent](T_Tessa_Files_RemoteFileContent.htm).  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_Files_FileContent_InitializeAsync.htm)| Выполняет
асинхронную инициализацию объекта.  
[InvalidateAsync](M_Tessa_Files_FileContent_InvalidateAsync.htm)|  Удаляет
локально загруженный контент, переводя его в начальное состояние. Следующий
раз при получении контента он будет заново загружен.  
[InvalidateCoreAsync](M_Tessa_Files_FileContent_InvalidateCoreAsync.htm)|
Сбрасывает информацию о контенте файла. Например, очищает дату изменения
файла. Если контент не является локальным, то может не выполнять действий.  
[IsModifiedAsync](M_Tessa_Files_FileContent_IsModifiedAsync.htm)|  Возвращает
признак того, что контент файла на диске был изменён с момента его установки
методом [IFileContent.Set]. Для защищённых от изменений объектов метод всегда
возвращает false.  
[IsModifiedCoreAsync](M_Tessa_Files_FileContent_IsModifiedCoreAsync.htm)|
Возвращает признак того, что локальный контент был изменён. Например, был
изменён файл на диске по дате изменения. При изменении контента может быть
обновлён его размер, а также он может быть, например, помечен как изменённый в
структуре карточки.  
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
[PrepareContentLocationCoreAsync](M_Tessa_Files_FileContent_PrepareContentLocationCoreAsync.htm)|
Подготавливает местоположение контента перед его записью или перемещением в
это местоположение. Например, создаёт папку на диске, если контент представлен
файлом на диске.  
[RemoveContentSafeCoreAsync](M_Tessa_Files_FileContent_RemoveContentSafeCoreAsync.htm)|
Метод удаляет локальный контент, если он был создан. Если контент не является
локальным, то метод не должен выполнять действий. Метод не должен выбрасывать
исключений, даже критичных.  
[RenameAsync](M_Tessa_Files_FileContent_RenameAsync.htm)|  Переименовывает
файл, в который записывается контент. Если файл ещё не существует, то он будет
назван по-другому в момент создания. Метод гарантированно сработает только в
том случае, если контент является локальным, т.е. свойство
[IFileContent.IsLocal] возвращает true.  
[RenameCoreAsync](M_Tessa_Files_FileContent_RenameCoreAsync.htm)|
Переименовывает имя контента в соответствии с новым именем файла. Если контент
представлен локальным файлом на диске, то метод должен переименовать этот
файл. Если контент не является локальным, то метод может не выполнять
действий.  
[Seal](M_Tessa_Files_FileContent_Seal.htm)| Защищает объект от изменений.  
[SetAsync](M_Tessa_Files_FileContent_SetAsync.htm)| Открывает и возвращает
поток, выполняющий перезапись контента файла.  
[SetCoreAsync](M_Tessa_Files_FileContent_SetCoreAsync.htm)|  Устанавливает
содержимое файла. Если контент запрещено изменять, то может быть выброшено
исключение.  
[SetLocalAsync](M_Tessa_Files_FileContent_SetLocalAsync.htm)| Устанавливает
контент локального файла по заданному пути.  
[SetLocalCoreAsync](M_Tessa_Files_FileContent_SetLocalCoreAsync.htm)|
Устанавливает локальное содержимое файла, представленное в виде файла на
диске, по заданному методу, который получает в параметре путь к файлу на диске
и может его создать или изменить некоторым способом. Если содержимое файла не
является локальным, то может быть выброшено исключение.  
[SetRemoteAsync](M_Tessa_Files_FileContent_SetRemoteAsync.htm)|  Устанавливает
содержимое файла, представленное заданными методами. Если контент запрещено
изменять, то может быть выброшено исключение. Метод доступен как для локальных
файлов, так и для нелокальных (remote), в т.ч. для файлов большого размера.  
[SetRemoteCoreAsync](M_Tessa_Files_FileContent_SetRemoteCoreAsync.htm)|
Устанавливает содержимое файла, представленное заданными методами. Если
контент запрещено изменять, то может быть выброшено исключение. Метод доступен
как для локальных файлов, так и для нелокальных (remote), в т.ч. для файлов
большого размера.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateLocalContentFromParentCoreAsync](M_Tessa_Files_FileContent_UpdateLocalContentFromParentCoreAsync.htm)|
Обновляет локальный контент на основании контента родительского объекта. При
вызове этого метода гарантируется, что у текущего контента есть родительский
контент, в котором присутствуют загруженные данные. Если контент не локальный,
то метод может не выполнять действий, но не должен выбрасывать исключений.  
[UpdateModifiedCoreAsync](M_Tessa_Files_FileContent_UpdateModifiedCoreAsync.htm)|
Обновляет информацию, на основании которой можно определить, изменялся ли
контент. Например, сохраняет время изменения файла, чтобы его можно было
сравнить со временем изменения в любой другой момент.  
[UpdateSizeAsync](M_Tessa_Files_FileContent_UpdateSizeAsync.htm)|  Обновляет
свойство с размером контента [IFileContent.Size] для загруженных файлов.  
[UpdateSizeCoreAsync](M_Tessa_Files_FileContent_UpdateSizeCoreAsync.htm)|
Обновляет размер локального контента. Возвращает true, если размер был
обновлён.  
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
[ResolveRoot](M_Tessa_Files_FileExtensions_ResolveRoot.htm)|  Возвращает
корневой объект содержимого по свойствам
[Parent](P_Tessa_Files_IFileContent_Parent.htm). Возвращает текущий объект
content, если у него отсутствует родитель
[Parent](P_Tessa_Files_IFileContent_Parent.htm).  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SetRemoteFromPathAsync](M_Tessa_Files_FileExtensions_SetRemoteFromPathAsync.htm)|
Устанавливает содержимое [IFileContent](T_Tessa_Files_IFileContent.htm) по
физическому файлу, расположенному по заданному пути. Метод доступен и для
локального, и для нелокального (remote) содержимого.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
##  __См. также
#### Ссылки
[FileContent - ](T_Tessa_Files_FileContent.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
