# CardFileManager - методы
##  __Методы
[CreateContainerAsync](M_Tessa_Cards_CardFileManager_CreateContainerAsync.htm)|
Создаёт контейнер с информацией по заданной карточке и по её файлам.  
---|---  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[PrepareForStoreAsync](M_Tessa_Cards_CardFileManager_PrepareForStoreAsync.htm)|
Подготавливает карточку из текущего контейнера и контент её файлов к
сохранению. Возвращает объект запрос на сохранение карточки.  
[StoreAsync](M_Tessa_Cards_CardFileManager_StoreAsync.htm)|  Сохраняет
карточку из текущего контейнера и контент её файлов, при этом позволяет
асинхронно отслеживать её состояние. В процессе сохранения карточка в
контейнере и её файлы не изменяются, поэтому метод безопасно вызывать
повторно.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[CreateContainerRemoteAsync](M_Tessa_Cards_CardExtensions_CreateContainerRemoteAsync.htm)|
Создаёт контейнер с информацией по заданной карточке и по её файлам. Все файлы
создаются с Remote-содержимым, при загрузке и замене которого не используется
временная папка. Операции с такими файлами будут выполняться быстрее, но при
условии надо быть уверенными, что содержимое файлов, работа с которыми
выполняется, умещается в памяти. Возможные ошибки при загрузке файлов из
карточки игнорируются. В этом случае к созданном контейнере не будет добавлено
файлов, хотя файлы присутствуют в карточке.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[CardFileManager - ](T_Tessa_Cards_CardFileManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
