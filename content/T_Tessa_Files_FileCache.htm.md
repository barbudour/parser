# FileCache - класс
Кэш для контента файлов.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class FileCache : IFileCache
VB __Копировать
     Public MustInherit Class FileCache
    	Implements IFileCache
C++ __Копировать
     public ref class FileCache abstract : IFileCache
F# __Копировать
     [<AbstractClassAttribute>]
    type FileCache = 
        class
            interface IFileCache
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ FileCache
Derived
[Tessa.Files.FileLocalCache](T_Tessa_Files_FileLocalCache.htm)
Implements
    [IFileCache](T_Tessa_Files_IFileCache.htm)
##  __Конструкторы
[FileCache](M_Tessa_Files_FileCache__ctor.htm)| Инициализирует новый экземпляр
класса FileCache  
---|---  
##  __Свойства
[Options](P_Tessa_Files_FileCache_Options.htm)| Опции, которые дополнительно
поддерживает кэш файлов.  
---|---  
##  __Методы
[AllocateAsync](M_Tessa_Files_FileCache_AllocateAsync.htm)| Создаёт объект,
инкапсулирующий контент файла в кэше.  
---|---  
[ClearAsync](M_Tessa_Files_FileCache_ClearAsync.htm)| Очищает кэш, освобождая
все объекты, которые инкапсулируют контент файлов.  
[ClearCoreAsync](M_Tessa_Files_FileCache_ClearCoreAsync.htm)| Очищает кэш,
освобождая все объекты, которые инкапсулируют контент файлов.  
[CreateContentAsync](M_Tessa_Files_FileCache_CreateContentAsync.htm)| Создаёт
объект, инкапсулирующий контент файла.  
[DisposeDelayedContentAsync](M_Tessa_Files_FileCache_DisposeDelayedContentAsync.htm)|
Немедленно выполняет отложенное освобождение содержимого, если это требуется.  
[DisposeDelayedContentCoreAsync](M_Tessa_Files_FileCache_DisposeDelayedContentCoreAsync.htm)|
Немедленно выполняет отложенное освобождение содержимого, если это требуется.  
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
[HasPendingDelayedContentDisposalAsync](M_Tessa_Files_FileCache_HasPendingDelayedContentDisposalAsync.htm)|
Возвращает признак того, что кэш ожидает отложенное освобождение содержимого
хотя бы одного файла.  
[IsEmptyAsync](M_Tessa_Files_FileCache_IsEmptyAsync.htm)|  Признак того, что
кэш пустой, т.е. не содержит объектов, инкапсулирующих контент файлов.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NotifyDelayedContentDisposalPendingAsync](M_Tessa_Files_FileCache_NotifyDelayedContentDisposalPendingAsync.htm)|
Уведомляет кэш о необходимости выполнить отложенное освобождение содержимого
через некоторое время, если это требуется.  
[NotifyDelayedContentDisposalPendingCoreAsync](M_Tessa_Files_FileCache_NotifyDelayedContentDisposalPendingCoreAsync.htm)|
Уведомляет кэш о необходимости выполнить отложенное освобождение содержимого
через некоторое время, если это требуется.  
[RegisterForDisposalAsync](M_Tessa_Files_FileCache_RegisterForDisposalAsync.htm)|
Добавляет заданный объект контента к списку освобождаемых объектов при очистке
кэша (если кэш связан с карточкой - при закрытии или обновлении карточки).
Вызывайте метод для объектов, которые не созданы средствами этого же кэша.  
[RegisterForDisposalCoreAsync](M_Tessa_Files_FileCache_RegisterForDisposalCoreAsync.htm)|
Добавляет заданный объект контента к списку освобождаемых объектов при очистке
кэша (если кэш связан с карточкой - при закрытии или обновлении карточки).
Вызывайте метод для объектов, которые не созданы средствами этого же кэша.  
[ResetDelayedContentDisposalAsync](M_Tessa_Files_FileCache_ResetDelayedContentDisposalAsync.htm)|
Очищает информацию о необходимости выполнить отложенное освобождение
содержимого. Файлы, которые не были удалены и требуют отложенного
освобождения, останутся во временной папке (или в другом местоположении) и не
будут удалены.  
[ResetDelayedContentDisposalCoreAsync](M_Tessa_Files_FileCache_ResetDelayedContentDisposalCoreAsync.htm)|
Очищает информацию о необходимости выполнить отложенное освобождение
содержимого. Файлы, которые не были удалены и требуют отложенного
освобождения, останутся во временной папке (или в другом местоположении) и не
будут удалены.  
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
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
