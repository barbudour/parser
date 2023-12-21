# CardFileSourceSettings - класс
Потокобезопасный кэш настроек по всем местоположениям контентов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardFileSourceSettings : ICardFileSourceSettings, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class CardFileSourceSettings
    	Implements ICardFileSourceSettings, IDisposable
C++ __Копировать
     public ref class CardFileSourceSettings sealed : ICardFileSourceSettings, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type CardFileSourceSettings = 
        class
            interface ICardFileSourceSettings
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardFileSourceSettings
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm)
##  __Конструкторы
[CardFileSourceSettings(ICardFileSourceOverrideProvider,
IUnityDisposableContainer)](M_Tessa_Cards_CardFileSourceSettings__ctor_1.htm)|
Создаёт экземпляр класса без указания местоположений контентов.  
---|---  
[CardFileSourceSettings(IEnumerable<ICardFileSource>, ICardFileSource,
ICardFileSourceOverrideProvider,
IUnityDisposableContainer)](M_Tessa_Cards_CardFileSourceSettings__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей для получения значений
вручную.  
## __Свойства
[Empty](P_Tessa_Cards_CardFileSourceSettings_Empty.htm)|  Объект настроек,
который не содержит информации по местоположениям контента файлов.  
---|---  
## __Методы
[CreateDefault](M_Tessa_Cards_CardFileSourceSettings_CreateDefault.htm)|
Создаёт настройки с местоположением контента файлов для файловой системы и
базы данных по умолчанию.  
---|---  
[Dispose](M_Tessa_Cards_CardFileSourceSettings_Dispose.htm)| Освобождает
ресурсы, занимаемые объектом.  
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
[GetAllAsync](M_Tessa_Cards_CardFileSourceSettings_GetAllAsync.htm)| Все
доступные местоположения.  
[GetAsync](M_Tessa_Cards_CardFileSourceSettings_GetAsync.htm)|  Возвращает
информацию по местоположению файлов для заданного типа местоположения.
Возвращённый объект гарантированно не равен null. Если информации по
местоположению не найдено, то выбрасывается исключение
[System.Collections.Generic.KeyNotFoundException].  
[GetDefaultAsync](M_Tessa_Cards_CardFileSourceSettings_GetDefaultAsync.htm)|
Местоположение по умолчанию. Может быть равно null только в том случае, если в
системе не зарегистрировано ни одного местоположения.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLargeFileSizeAsync](M_Tessa_Cards_CardFileSourceSettings_GetLargeFileSizeAsync.htm)|
Начальный размер файла в байтах, который считается большим файлом, поэтому для
него может быть доступна особая обработка на клиенте, или null, если файлы
любого размера не считаются большими. Свойство может использоваться на клиенте
и на сервере.  
[GetMaxFileSizeAsync](M_Tessa_Cards_CardFileSourceSettings_GetMaxFileSizeAsync.htm)|
Максимальный размер файла в байтах, для которого разрешена загрузка в систему,
или null, если ограничения по размеру отсутствует. Свойство может
использоваться на клиенте и на сервере.  
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
[SetCachingSourceAsync](M_Tessa_Cards_CardFileSourceSettings_SetCachingSourceAsync.htm)|
Устанавливает источник получения настроек по местоположению файлов.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetAsync](M_Tessa_Cards_CardFileSourceSettings_TryGetAsync.htm)|
Возвращает информацию по местоположению файлов для заданного типа
местоположения или null, если в системе не задано информации для заданного
типа.  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
