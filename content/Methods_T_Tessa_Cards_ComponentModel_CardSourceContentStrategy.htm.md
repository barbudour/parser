# CardSourceContentStrategy - методы
##  __Методы
[CleanCardAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_CleanCardAsync.htm)|
Очищает место, отведённое для контента файлов, принадлежащих карточке. Метод
вызывается перед удалением карточки.  
---|---  
[CleanFileAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_CleanFileAsync.htm)|
Очищает место, отведённое для контента файла. Метод вызывается перед удалением
файла.  
[CopyAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_CopyAsync.htm)|
Выполняет копирование контента из исходного местоположения в целевое. Если
исходное и целевое местоположения совпадут, то метод завершится с ошибкой и
вернёт false.  
[CreateDefault](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_CreateDefault.htm)|
Создаёт экземпляр класса
[CardSourceContentStrategy](T_Tessa_Cards_ComponentModel_CardSourceContentStrategy.htm)
с параметрами по умолчанию при создании без контейнера Unity.  
[DeleteAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_DeleteAsync.htm)|
Удаляет контент версии файла.  
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
[GetAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_GetAsync.htm)|
Загружает контент версии файла.  
[GetContentStrategy](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_GetContentStrategy.htm)|
Возвращает стратегию для взаимодействия с указанным местоположением контента
файлов.  
[GetContentStrategyAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_GetContentStrategyAsync.htm)|
Возвращает стратегию для взаимодействия с указанным местоположением контента
файлов.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSizeAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_GetSizeAsync.htm)|
Возвращает длину контента версии файла в байтах.  
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
[MoveAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_MoveAsync.htm)|
Перемещает контент файла (но не записи по файлу) из исходного местоположения
sourceContext в целевое местоположение targetContext. При этом файл может
перемещаться между карточками и между разными файловыми хранилищами (если
текущая стратегия поддерживает разные хранилища). Если исходное и целевое
местоположения совпадают, то метод не выполняет действий и возвращает true.  
[MoveFileAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_MoveFileAsync.htm)|
Перемещает контент файла sourceFileID (но не записи по файлу) из карточки с
идентификатором sourceCardID в файл targetFileID в карточку с идентификатором
targetCardID. Содержимое не может быть перемещено между разными хранилищами
посредством этого метода, для этого долежн быть создан файл, в который
копируется содержимое исходного файла.  
[MoveFilesAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_MoveFilesAsync.htm)|
Перемещает контент файлов из карточки с идентификатором sourceCardID в
карточку с идентификатором targetCardID. При этом записи в секции по файлам не
перемещаются между карточками, для этого используйте методы
[Tessa.Cards.ComponentModel.ICardStoreStrategy.MoveFiles] или
[Tessa.Cards.ComponentModel.ICardStoreStrategy.MoveFilesAndSetTask].
Содержимое не может быть перемещено между разными хранилищами посредством
этого метода, для этого долежн быть создан файл, в который копируется
содержимое исходного файла.  
[StoreAsync](M_Tessa_Cards_ComponentModel_CardSourceContentStrategy_StoreAsync.htm)|
Сохраняет контент версии файла.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[CardSourceContentStrategy -
](T_Tessa_Cards_ComponentModel_CardSourceContentStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
