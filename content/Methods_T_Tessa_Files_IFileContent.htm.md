# IFileContent - методы
##  __Методы
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
## __Методы расширения
[ResolveRoot](M_Tessa_Files_FileExtensions_ResolveRoot.htm)|  Возвращает
корневой объект содержимого по свойствам
[Parent](P_Tessa_Files_IFileContent_Parent.htm). Возвращает текущий объект
content, если у него отсутствует родитель
[Parent](P_Tessa_Files_IFileContent_Parent.htm).  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
---|---  
[SetRemoteFromPathAsync](M_Tessa_Files_FileExtensions_SetRemoteFromPathAsync.htm)|
Устанавливает содержимое [IFileContent](T_Tessa_Files_IFileContent.htm) по
физическому файлу, расположенному по заданному пути. Метод доступен и для
локального, и для нелокального (remote) содержимого.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
##  __См. также
#### Ссылки
[IFileContent - ](T_Tessa_Files_IFileContent.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
