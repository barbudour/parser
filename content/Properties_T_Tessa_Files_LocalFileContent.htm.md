# LocalFileContent - свойства
##  __Свойства
[Cancellation](P_Tessa_Files_FileContent_Cancellation.htm)|  Объект, который
может использоваться для отмены асинхронных операций с содержимым файла, если
оно поддерживает отмену. На текущий момент это доступно для загрузки
содержимого версии файла.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
---|---  
[HasCurrentContentData](P_Tessa_Files_FileContent_HasCurrentContentData.htm)|
Признак, который определяет доступность текущего контента для получения,
например, по наличию файла в локальной папке. Свойство
[HasData](P_Tessa_Files_FileContent_HasData.htm) определяет доступность как
текущего контента, так и родительского. Связь родительский-дочерний актуально
для последней версии файла.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[HasData](P_Tessa_Files_FileContent_HasData.htm)|  Возвращает признак того,
что контент файла был установлен методом [IFileContent.Set].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[IsBoundToFileSource](P_Tessa_Files_LocalFileContent_IsBoundToFileSource.htm)|
Признак того, что контент был создан источником файлов, а не передан снаружи,
поэтому для оптимизации обращения к содержимому можно использовать источник
файлов. Обычно актуально для Remote-контента.  
(Переопределяет
[FileContent.IsBoundToFileSource](P_Tessa_Files_FileContent_IsBoundToFileSource.htm))  
[IsDirty](P_Tessa_Files_FileContent_IsDirty.htm)|  Признак того, что контент
мог быть изменён. Следует установить значение равным true перед открытием
контента на редактирование во внешней программе. Определить точно, был ли
изменён контент, можно, вызвав метод [IFileContent.IsModified].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[IsDisposed](P_Tessa_Files_FileContent_IsDisposed.htm)| Признак того, что
контент был освобождён и объект нельзя использовать.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[IsLocal](P_Tessa_Files_LocalFileContent_IsLocal.htm)|  Признак того, что
контент является локальным, т.е. к нему можно получить локальный путь
посредством метода [IFileContent.GetLocalFilePath].  
(Переопределяет [FileContent.IsLocal](P_Tessa_Files_FileContent_IsLocal.htm))  
[IsSealed](P_Tessa_Files_FileContent_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[Parent](P_Tessa_Files_FileContent_Parent.htm)|  Родительский контент или
null, если родительский контент отсутствует. Если производится запрос текущего
контента, и он не был установлен, то он сначала локально копируется из
родительского, если тот существует, а затем считывается локально.  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[RequestInfo](P_Tessa_Files_FileContent_RequestInfo.htm)|  Дополнительная
пользовательская информация, передаваемая в запросы к серверу, которые
относятся к загрузке содержимого файла или версии, которые сохраняются в
текущем объекте. Рекомендуется, чтобы все данные были сериализуемых типов (в
соответствии с типовой BSON-сериализацией в системе). Такие данные могут
перезаписать данные из [IFileObject.RequestInfo].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[Size](P_Tessa_Files_FileContent_Size.htm)|  Размер контента файла в байтах
или 0, если контент ещё не был загружен. Проверить, был ли загружен контент,
можно, обратившись к свойству [IFileContent.HasData].  
(Унаследован от [FileContent](T_Tessa_Files_FileContent.htm))  
[Uri](P_Tessa_Files_LocalFileContent_Uri.htm)|  Ссылка к контенту файла,
который может быть доступен как локально (на диске), так и удалённо (сетевой
ресурс). Значение может быть равно null, если контент недоступен по ссылке.  
(Переопределяет [FileContent.Uri](P_Tessa_Files_FileContent_Uri.htm))  
##  __См. также
#### Ссылки
[LocalFileContent - ](T_Tessa_Files_LocalFileContent.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
