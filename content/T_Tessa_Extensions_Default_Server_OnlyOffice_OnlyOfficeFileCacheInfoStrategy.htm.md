# OnlyOfficeFileCacheInfoStrategy - класс
Объект, управляющий информацией по файлу в кэше.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.OnlyOffice](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class OnlyOfficeFileCacheInfoStrategy : IOnlyOfficeFileCacheInfoStrategy
VB __Копировать
     Public NotInheritable Class OnlyOfficeFileCacheInfoStrategy
    	Implements IOnlyOfficeFileCacheInfoStrategy
C++ __Копировать
     public ref class OnlyOfficeFileCacheInfoStrategy sealed : IOnlyOfficeFileCacheInfoStrategy
F# __Копировать
     [<SealedAttribute>]
    type OnlyOfficeFileCacheInfoStrategy = 
        class
            interface IOnlyOfficeFileCacheInfoStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ OnlyOfficeFileCacheInfoStrategy
Implements
    [IOnlyOfficeFileCacheInfoStrategy](T_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfoStrategy.htm)
##  __Конструкторы
[OnlyOfficeFileCacheInfoStrategy](M_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfoStrategy__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[CleanCacheInfoAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfoStrategy_CleanCacheInfoAsync.htm)|
Очищает кэш от информации по файлам, доступ к содержимому которых выполнялся
раньше заданной даты. Не удаляет сами файлы, для этого также вызовите
[CleanCacheAsync(Nullable<DateTime>,
CancellationToken)](M_Tessa_FileConverters_IFileConverterCache_CleanCacheAsync.htm).  
---|---  
[DeleteAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfoStrategy_DeleteAsync.htm)|
Удаляет информацию о файле из кэша.  
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
[InsertAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfoStrategy_InsertAsync.htm)|
Добавляет указанную информацию о файле в кэш.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetInfoAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfoStrategy_TryGetInfoAsync.htm)|
Возвращает информацию по файлу в кэше или null, если файл не найден по
указанному идентификатору.  
[UpdateInfoAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfoStrategy_UpdateInfoAsync.htm)|
Обновляет информацию по файлу в кэше. Выбрасывает исключение, если файл не
найден по указанному идентификатору.  
[UpdateInfoOnEditorOpenedAsync](M_Tessa_Extensions_Default_Server_OnlyOffice_OnlyOfficeFileCacheInfoStrategy_UpdateInfoOnEditorOpenedAsync.htm)|
Устанавливает флаг "Редактор был открыт"
[EditorWasOpen](P_Tessa_Extensions_Default_Server_OnlyOffice_IOnlyOfficeFileCacheInfo_EditorWasOpen.htm)
для файла в кэше. Выбрасывает исключение, если файл не найден по указанному
идентификатору.  
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
[Tessa.Extensions.Default.Server.OnlyOffice - пространство
имён](N_Tessa_Extensions_Default_Server_OnlyOffice.htm)
